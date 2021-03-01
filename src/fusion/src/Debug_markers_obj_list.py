#!/usr/bin/env python
import roslib; roslib.load_manifest('visualization_marker_tutorials')
import rospy
from std_msgs.msg import String
from object_list.msg import ObjectsList
from object_list.msg import ObjectList

from geometry_msgs.msg import Quaternion
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
import rospy
import math
import tf
import message_filters

OFFSET_CAR_X = -2.3 # distance to front
car_ego_x = 0
car_ego_y = 0
data_alt = 0
topic = 'visualization_marker_array'
publisher = rospy.Publisher(topic, MarkerArray,queue_size=10)
rospy.init_node('Objekt_Visualization')
br = tf.TransformBroadcaster()

#define each color to the specific class, input value ist the name(string) from the classifciation
def evaluateColor(Class): 
    class_List = {
	"car": [1,0,0,1],
	"truck":[0,1,0,1],
	"motorcycle": [0,0,1,1],
	"bicycle": [1,1,0,1],
	"pedestrian": [1,0,1,3],
	"stacionary": [0,1,1,3],
	"other":[1,1,1,2]   
    }
    return class_List.get(Class)
    
 
def evaluateClassification(objectClass):
    
    temp_prop = 0
    result = ""
    #tmp includes all Attributes of the message Classification
    tmp = [a for a in dir(objectClass) if not a.startswith('__') and not a.startswith('_') and not callable(getattr(objectClass,a))]
    

    for i in range(len(tmp)):
        if(getattr(objectClass, tmp[i]) > temp_prop ):
            temp_prop = getattr(objectClass, tmp[i])
            result = tmp[i]
    return (result) # return value is the name of the class whith the highest probability
            
    


def evaluateObject(objectData):
    marker = Marker()
    #r, g, b, typ = evaluateColor(evaluateClassification(objectData.classification))
    marker.header.frame_id = "/ego"
    
    marker.type = 1
    
    marker.action = marker.ADD
    marker.scale.x = objectData.dimension.length
    marker.scale.y = objectData.dimension.width
    
    marker.scale.z = 2.0
    marker.color.a = 1.0
   
    marker.color.r = 1.0
    marker.color.g = 0.0
    marker.color.b = 0.0

    marker.pose.orientation = Quaternion(*tf.transformations.quaternion_from_euler(0,0,objectData.geometric.yaw))
    #marker.pose.orientation.w = 1
    #print(marker.pose.orientation)
    marker.pose.position.x = objectData.geometric.x
    marker.pose.position.y = objectData.geometric.y
    marker.pose.position.z = 1.0
    marker.lifetime = rospy.Duration(0.1)
    return marker

def evaluateObjectID(objectData):
    marker = Marker()

    marker.header.frame_id = "/world"
    marker.id = i
    marker.type = typ

    marker.action = marker.ADD
    marker.scale.x = objectData.dimension.lenght
    marker.scale.y = objectData.dimension.width

    marker.scale.z = 2.0
    marker.color.a = 1.0

    marker.color.r = 1.0
    marker.color.g = 0.0
    marker.color.b = 0.0

    marker.pose.orientation.w = 1.0
    marker.pose.position.x = data.position.x
    marker.pose.position.y = data.position.y
    marker.pose.position.z = 1.0
    marker.lifetime = rospy.Duration(0.1)
    marker.text = "ID:" + str(objectData.obj_id)
    return marker


def callback_simulation(data):

    global car_ego_x
    global car_ego_y
    target_marker_publisher = rospy.Publisher('/target_marker', Marker, queue_size=10)
    

    markerArray = MarkerArray()

    #print('marker')
    for i,obj in enumerate(data.obj_list):
        #markerObj = evaluateObject(data.obj_list[i])
        #markerID = evaluateObjectID(data.obj_list[i])
        #markerID.id = i*2+1
        #markerObj.publishCube()
        #markerArray.markers.append(markerObj)
        #markerArray.markers.append(markerID)
        marker = Marker()
        marker.header.frame_id = "/map"
        marker.id = obj.obj_id
        marker.lifetime = rospy.Duration(3)
        marker.type = marker.CUBE
        marker.action = marker.ADD
        marker.scale.x = obj.dimension.length
        marker.scale.y = obj.dimension.width
        marker.scale.z = 3
        marker.color.a = 1.0
        marker.color.r = 1.0
        marker.color.g = 1.0
        marker.color.b = 0.0
        """if color == "red":
            marker.color.r = 1.0
        elif color == "green":
            marker.color.g = 1.0
        elif color == "blue":target_marker_publisher
            marker.color.b = 1.0
        elif color == "yellow":
            marker.color.r = 1.0
            marker.color.g = 1.0
        elif color == "majenta":
            marker.color.g = 1.0
            marker.color.b = 1.0
        elif color == "cyan":
            marker.color.r = 1.0
            marker.color.b = 1.0
        """
        marker.pose.orientation.w = 1.0
        #pt = behaviour_planner.projector.forward(
         #   GPSPoint(float(rospy.get_param("late")), float(rospy.get_param("lone"))))
        marker.pose.position.x = obj.geometric.x
        marker.pose.position.y = obj.geometric.y
        marker.pose.position.z = 0
        target_marker_publisher.publish(marker)
        #print(marker)
    
    #rospy.loginfo(markerArray)
    #publisher.publishCube(markerArray)


def callback_simulation2(data):
    global car_ego_x
    global car_ego_y
    target_marker_publisher2 = rospy.Publisher('/target_marker2', Marker, queue_size=10)

    markerArray = MarkerArray()

    # print('marker')
    for i, obj in enumerate(data.obj_list):
        # markerObj = evaluateObject(data.obj_list[i])
        # markerID = evaluateObjectID(data.obj_list[i])
        # markerID.id = i*2+1
        # markerObj.publishCube()
        # markerArray.markers.append(markerObj)
        # markerArray.markers.append(markerID)
        marker = Marker()
        marker.header.frame_id = "/map"
        marker.id = obj.obj_id
        marker.lifetime = rospy.Duration(3)
        marker.type = marker.CUBE
        marker.action = marker.ADD
        marker.scale.x = obj.dimension.length
        marker.scale.y = obj.dimension.width
        marker.scale.z = 3
        marker.color.a = 1.0
        marker.color.r = 1.0
        marker.color.g = 0.0
        marker.color.b = 0.0
        """if color == "red":
            marker.color.r = 1.0
        elif color == "green":
            marker.color.g = 1.0
        elif color == "blue":target_marker_publisher
            marker.color.b = 1.0
        elif color == "yellow":
            marker.color.r = 1.0
            marker.color.g = 1.0
        elif color == "majenta":
            marker.color.g = 1.0
            marker.color.b = 1.0
        elif color == "cyan":
            marker.color.r = 1.0
            marker.color.b = 1.0
        """
        marker.pose.orientation.w = 1.0
        # pt = behaviour_planner.projector.forward(
        #   GPSPoint(float(rospy.get_param("late")), float(rospy.get_param("lone"))))
        marker.pose.position.x = obj.geometric.x
        marker.pose.position.y = obj.geometric.y
        marker.pose.position.z = 0
        target_marker_publisher2.publish(marker)
        # print(marker)

    # rospy.loginfo(markerArray)
    # publisher.publishCube(markerArray)
def callback_simulation3(data):
    global car_ego_x
    global car_ego_y
    target_marker_publisher2 = rospy.Publisher('/target_marker3', Marker, queue_size=10)

    markerArray = MarkerArray()

    # print('marker')
    for i, obj in enumerate(data.obj_list):
        # markerObj = evaluateObject(data.obj_list[i])
        # markerID = evaluateObjectID(data.obj_list[i])
        # markerID.id = i*2+1
        # markerObj.publishCube()
        # markerArray.markers.append(markerObj)
        # markerArray.markers.append(markerID)
        marker = Marker()
        marker.header.frame_id = "/map"
        marker.id = obj.obj_id
        marker.lifetime = rospy.Duration(3)
        marker.type = marker.CUBE
        marker.action = marker.ADD
        marker.scale.x = obj.dimension.length
        marker.scale.y = obj.dimension.width
        marker.scale.z = 3
        marker.color.a = 1.0
        marker.color.r = 0.0
        marker.color.g = 0.0
        marker.color.b = 1.0
        """if color == "red":
            marker.color.r = 1.0
        elif color == "green":
            marker.color.g = 1.0
        elif color == "blue":target_marker_publisher
            marker.color.b = 1.0
        elif color == "yellow":
            marker.color.r = 1.0
            marker.color.g = 1.0
        elif color == "majenta":
            marker.color.g = 1.0
            marker.color.b = 1.0
        elif color == "cyan":
            marker.color.r = 1.0
            marker.color.b = 1.0
        """
        marker.pose.orientation.w = 1.0
        # pt = behaviour_planner.projector.forward(
        #   GPSPoint(float(rospy.get_param("late")), float(rospy.get_param("lone"))))
        marker.pose.position.x = obj.geometric.x
        marker.pose.position.y = obj.geometric.y
        marker.pose.position.z = 0
        target_marker_publisher2.publish(marker)
def callback_egovehicle(data):
    global car_ego_x
    global car_ego_y

    car_ego_x = data.object.position.x
    car_ego_y = data.object.position.y

    br.sendTransform((car_ego_x,car_ego_y,0),tf.transformations.quaternion_from_euler(data.object.orientation.roll,data.object.orientation.pitch,data.object.orientation.yaw),rospy.Time.now(),"chassis","base_link")
def callback3(fused_data, fused_data2, fused_data3):
    print('RUN')
    callback_simulation(fused_data)
    callback_simulation2(fused_data2)
    callback_simulation3(fused_data3)

#def callback32(fused_data,fused_data2,fused_data3):



def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    

    #rospy.Subscriber("chatter", String, callback)
    #rospy.Subscriber('/sensor0/afterKF', ObjectsList, callback_simulation)
    #fused_data = rospy.Subscriber('/sensor0/obj_list_egoframe', ObjectsList, callback_simulation)
    #fused_data2 = rospy.Subscriber('/sensor1/obj_list_egoframe', ObjectsList, callback_simulation2)
    #fused_data3 = rospy.Subscriber('/fused_data', ObjectsList, callback_simulation3)
    fused_data = message_filters.Subscriber('/sensor0/obj_list_egoframe', ObjectsList )
    fused_data2 = message_filters.Subscriber('/sensor1/obj_list_egoframe', ObjectsList )
    fused_data3 = message_filters.Subscriber('/fused_data', ObjectsList)
    #fused_data = message_filters.Subscriber('/sensor0/obj_list_egoframe', ObjectsList)
    #fused_data2 = message_filters.Subscriber('/sensor1/obj_list_egoframe', ObjectsList)
    #fused_data3= message_filters.Subscriber('/fused_data', ObjectsList)
    ts = message_filters.ApproximateTimeSynchronizer([fused_data, fused_data2, fused_data3], 10,1)
    ts.registerCallback(callback3)


    #print(fused_data)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
