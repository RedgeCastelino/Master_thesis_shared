#include <thread>
#include <mutex>

#include <ros/ros.h>
#include <osi3_bridge/GroundTruthMovingObjects.h>
#include <osi_version.pb.h>
#include <osi_groundtruth.pb.h>
#include <osi_protocol_header.h>
extern "C" {
    #include <udp.h>
}

#define MAX_BUFFER_SIZE 65535   // UDP Buffer
#define DEFAULT_UDP_PORT 22222
#define DEFAULT_LOOP_RATE 22222

void collector(osi3_bridge::GroundTruthMovingObjects &msg, std::mutex &msg_mutex, int port)
{
    SOCKET udp_sock;
    static osi3::InterfaceVersion currentInterfaceVersion = osi3::InterfaceVersion::descriptor()->file()->options().GetExtension(osi3::current_interface_version);
    void *network_buffer = new uint8_t[MAX_BUFFER_SIZE];
    
    if(!udp_init(&udp_sock))
    {
        ROS_FATAL("UDP Init");
        google::protobuf::ShutdownProtobufLibrary();
        delete [] (uint8_t *)network_buffer;
        return;
    }
    if(!udp_bind(&udp_sock, port))
    {
        ROS_FATAL("UDP Bind");
        udp_close(&udp_sock);
        google::protobuf::ShutdownProtobufLibrary();
        delete [] (uint8_t *)network_buffer;
        return;
    }
    
    while(ros::ok())
    {
        size_t cur_size = MAX_BUFFER_SIZE;
        if(!udp_recv(&udp_sock, (uint8_t *)network_buffer, &cur_size, NULL, NULL))
        {
            ROS_FATAL("UDP Recv");
            break;
        }
        
        if(osiph_check_magic_id(network_buffer) && osiph_check_protocol_version(network_buffer) &&
           osiph_get_osi_version_major(network_buffer) == currentInterfaceVersion.version_major() &&
           osiph_get_osi_version_minor(network_buffer) == currentInterfaceVersion.version_minor() &&
           osiph_get_osi_version_patch(network_buffer) == currentInterfaceVersion.version_patch() &&
           osiph_get_payload_size(network_buffer) == cur_size - osiph_get_header_size())
        {
            if(osiph_get_payload_type(network_buffer) == osi_GroundTruth)
            {
                osi3::GroundTruth osi_in;
                osi3_bridge::GroundTruthMovingObjects ros_in;
                std::string payload((char *)osiph_get_payload(network_buffer),
                                    osiph_get_payload_size(network_buffer));
                osi_in.ParseFromString(payload);
                
                if(osi_in.has_timestamp() && 
                   osi_in.timestamp().has_seconds() &&
                   osi_in.timestamp().has_nanos())
                {
                    ros_in.header.stamp = ros::Time(osi_in.timestamp().seconds(),
                                                    osi_in.timestamp().nanos());
                }
                else
                {
                    ros_in.header.stamp = ros::Time();
                }
                
                if(osi_in.moving_object_size() > 0)
                {
                    ros_in.objects.resize(osi_in.moving_object_size());
                }
                
                for(int obj_cnt = 0; obj_cnt < osi_in.moving_object_size(); ++obj_cnt)
                {
                    ros_in.objects[obj_cnt].id = osi_in.moving_object(obj_cnt).id().value();
                    
                    ros_in.objects[obj_cnt].dimension.length = osi_in.moving_object(obj_cnt).base().dimension().length();
                    ros_in.objects[obj_cnt].dimension.width = osi_in.moving_object(obj_cnt).base().dimension().width();
                    ros_in.objects[obj_cnt].dimension.height = osi_in.moving_object(obj_cnt).base().dimension().height();
 
                    ros_in.objects[obj_cnt].position.x = osi_in.moving_object(obj_cnt).base().position().x();
                    ros_in.objects[obj_cnt].position.y = osi_in.moving_object(obj_cnt).base().position().y();
                    ros_in.objects[obj_cnt].position.z = osi_in.moving_object(obj_cnt).base().position().z();
                    
                    ros_in.objects[obj_cnt].orientation.roll = osi_in.moving_object(obj_cnt).base().orientation().roll();
                    ros_in.objects[obj_cnt].orientation.roll = osi_in.moving_object(obj_cnt).base().orientation().pitch();
                    ros_in.objects[obj_cnt].orientation.roll = osi_in.moving_object(obj_cnt).base().orientation().yaw();
                    
                    ros_in.objects[obj_cnt].velocity.x = osi_in.moving_object(obj_cnt).base().velocity().x();
                    ros_in.objects[obj_cnt].velocity.y = osi_in.moving_object(obj_cnt).base().velocity().y();
                    ros_in.objects[obj_cnt].velocity.z = osi_in.moving_object(obj_cnt).base().velocity().z();
                    
                    ros_in.objects[obj_cnt].acceleration.x = osi_in.moving_object(obj_cnt).base().acceleration().x();
                    ros_in.objects[obj_cnt].acceleration.y = osi_in.moving_object(obj_cnt).base().acceleration().y();
                    ros_in.objects[obj_cnt].acceleration.z = osi_in.moving_object(obj_cnt).base().acceleration().z();
                    
                    switch(osi_in.moving_object(obj_cnt).type())
                    {
                        case osi3::MovingObject_Type_TYPE_UNKNOWN:
                            ros_in.objects[obj_cnt].type = osi3_bridge::MovingObject::TYPE_UNKNOWN;
                            break;
                        case osi3::MovingObject_Type_TYPE_OTHER:
                            ros_in.objects[obj_cnt].type = osi3_bridge::MovingObject::TYPE_OTHER;
                            break;
                        case osi3::MovingObject_Type_TYPE_PEDESTRIAN:
                            ros_in.objects[obj_cnt].type = osi3_bridge::MovingObject::TYPE_PEDESTRIAN;
                            break;
                        case osi3::MovingObject_Type_TYPE_ANIMAL:
                            ros_in.objects[obj_cnt].type = osi3_bridge::MovingObject::TYPE_ANIMAL;
                            break;
                        case osi3::MovingObject_Type_TYPE_VEHICLE:
                            switch(osi_in.moving_object(obj_cnt).vehicle_classification().type())
                            {
                                case osi3::MovingObject_VehicleClassification_Type_TYPE_UNKNOWN:
                                    ros_in.objects[obj_cnt].type = osi3_bridge::MovingObject::TYPE_UNKNOWN;
                                    break;
                                case osi3::MovingObject_VehicleClassification_Type_TYPE_OTHER:
                                    ros_in.objects[obj_cnt].type = osi3_bridge::MovingObject::TYPE_OTHER;
                                    break;
                                case osi3::MovingObject_VehicleClassification_Type_TYPE_SMALL_CAR:
                                case osi3::MovingObject_VehicleClassification_Type_TYPE_COMPACT_CAR:
                                case osi3::MovingObject_VehicleClassification_Type_TYPE_MEDIUM_CAR:
                                case osi3::MovingObject_VehicleClassification_Type_TYPE_LUXURY_CAR:
                                    ros_in.objects[obj_cnt].type = osi3_bridge::MovingObject::TYPE_CAR;
                                    break;
                                case osi3::MovingObject_VehicleClassification_Type_TYPE_DELIVERY_VAN:
                                case osi3::MovingObject_VehicleClassification_Type_TYPE_HEAVY_TRUCK:
                                case osi3::MovingObject_VehicleClassification_Type_TYPE_SEMITRAILER:
                                    ros_in.objects[obj_cnt].type = osi3_bridge::MovingObject::TYPE_TRUCK;
                                    break;
                                case osi3::MovingObject_VehicleClassification_Type_TYPE_TRAILER:
                                    ros_in.objects[obj_cnt].type = osi3_bridge::MovingObject::TYPE_TRAILER;
                                    break;
                                case osi3::MovingObject_VehicleClassification_Type_TYPE_MOTORBIKE:
                                    ros_in.objects[obj_cnt].type = osi3_bridge::MovingObject::TYPE_MOTORBIKE;
                                    break;
                                case osi3::MovingObject_VehicleClassification_Type_TYPE_BICYCLE:
                                    ros_in.objects[obj_cnt].type = osi3_bridge::MovingObject::TYPE_BICYCLE;
                                    break;
                                case osi3::MovingObject_VehicleClassification_Type_TYPE_BUS:
                                    ros_in.objects[obj_cnt].type = osi3_bridge::MovingObject::TYPE_BUS;
                                    break;
                                case osi3::MovingObject_VehicleClassification_Type_TYPE_TRAM:
                                    ros_in.objects[obj_cnt].type = osi3_bridge::MovingObject::TYPE_TRAM;
                                    break;
                                case osi3::MovingObject_VehicleClassification_Type_TYPE_TRAIN:
                                    ros_in.objects[obj_cnt].type = osi3_bridge::MovingObject::TYPE_TRAIN;
                                    break;
                                case osi3::MovingObject_VehicleClassification_Type_TYPE_WHEELCHAIR:
                                    ros_in.objects[obj_cnt].type = osi3_bridge::MovingObject::TYPE_WHEELCHAIR;
                                    break;
                                default:
                                    ros_in.objects[obj_cnt].type = osi3_bridge::MovingObject::TYPE_UNKNOWN;
                                    break;
                            }
                            break;
                        default:
                            ros_in.objects[obj_cnt].type = osi3_bridge::MovingObject::TYPE_UNKNOWN;
                            break;
                    }
                    msg_mutex.lock();
                    msg = ros_in;
                    msg_mutex.unlock();
                    ROS_INFO("Neue UDP Nachricht");
                }
            }
            else
            {
                // TODO: Was macht man mit anderen Payload Types
                ROS_WARN("Falscher Type");
            }
        }
        else
        {
            // TODO: Was machet man mit anderen Paketen?
            ROS_WARN("Falsches Paket");
        }
    }
    
    udp_close(&udp_sock);
    google::protobuf::ShutdownProtobufLibrary();
    delete [] (uint8_t *)network_buffer;
}

int main(int argc, char **argv)
{
    GOOGLE_PROTOBUF_VERIFY_VERSION;
    uint32_t i = 0;
    int param_port;
    int param_loop_rate;
    
    ros::init(argc, argv, "osi3_bridge_publisher");
    ros::NodeHandle n;
    ros::Publisher osi3_pub = n.advertise<osi3_bridge::GroundTruthMovingObjects>("from_osi3", 10);
    n.param("loop_rate", param_loop_rate, DEFAULT_LOOP_RATE);
    n.param("listen_port", param_port, DEFAULT_UDP_PORT);
    ros::Rate loop_rate(param_loop_rate);
    
    osi3_bridge::GroundTruthMovingObjects msg;
    std::mutex msg_mutex;
    std::thread t1(collector, std::ref(msg), std::ref(msg_mutex), param_port);
    
    
    while(ros::ok())
    {
        if(msg.objects.size() > 0)
        {
            msg_mutex.lock();
            msg.header.seq = i++;
            osi3_pub.publish(msg);
            msg_mutex.unlock();
            
            ROS_INFO("ROS Publish: %lf", msg.objects[0].position.x);
        }
        
        loop_rate.sleep();
    }
    
    t1.join();
    
    return 0;
}

