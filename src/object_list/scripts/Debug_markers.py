#!/usr/bin/env python
import roslib; roslib.load_manifest('visualization_marker_tutorials')
import rospy
from std_msgs.msg import String
from osi3_bridge.msg import GroundTruthMovingObjects
from geometry_msgs.msg import Quaternion

from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
import rospy
import math
import tf

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
    marker.header.frame_id = "/world"
    
    marker.type = 1
    
    marker.action = marker.ADD
    marker.scale.x = objectData.dimension.length
    marker.scale.y = objectData.dimension.width
    
    marker.scale.z = 2.0
    marker.color.a = 1.0
   
    marker.color.r = 1.0
    marker.color.g = 0.0
    marker.color.b = 0.0

    marker.pose.orientation = Quaternion(*tf.transformations.quaternion_from_euler(0,0,objectData.orientation.yaw))
    #marker.pose.orientation.w = 1
    print(marker.pose.orientation)
    marker.pose.position.x = objectData.position.x
    marker.pose.position.y = objectData.position.y
    marker.pose.position.z = 1.0
    marker.lifetime = rospy.Duration(0.1)
    return marker

def evaluateObjectID(objectData):
    marker = Marker()

    marker.header.frame_id = "/world"

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
    
    

    markerArray = MarkerArray()


    for i in range(len(data.objects)):
        markerObj = evaluateObject(data.objects[i])
        markerObj.id = i*2
        
        #markerID = evaluateObjectID(data.obj_list[i])
        
        #markerID.id = i*2+1
        markerArray.markers.append(markerObj)
        #markerArray.markers.append(markerID)

    
    #rospy.loginfo(markerArray)
    publisher.publish(markerArray)
    
   
def callback_egovehicle(data):
    global car_ego_x
    global car_ego_y

    car_ego_x = data.object.position.x
    car_ego_y = data.object.position.y

    br.sendTransform((car_ego_x,car_ego_y,0),tf.transformations.quaternion_from_euler(data.object.orientation.roll,data.object.orientation.pitch,data.object.orientation.yaw),rospy.Time.now(),"chassis","base_link")

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    

    #rospy.Subscriber("chatter", String, callback)
    #rospy.Subscriber('/sensor0/afterKF', ObjectsList, callback_simulation)
    rospy.Subscriber('/osi3_moving_obj', GroundTruthMovingObjects, callback_simulation)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
