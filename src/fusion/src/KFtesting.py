#!/usr/bin/env python
import numpy as np
import rospy
import math
import message_filters

## Import Funtions
from rotate import rotate

## Import Objects
from ClassKF import KF , rotatedata
from ClassSens import Sens , Ego

# import all necessary ROS messages
from object_list.msg import ObjectList, ObjectsList
from osi3_bridge.msg import GroundTruthMovingObjects, TrafficUpdateMovingObject

deviationsum = 0
deviation = 0+
count = 0

def sensor_rotate():
    # Node initialization

    rospy.init_node('KFtesting', anonymous=False)  # Start node
    rate = rospy.Rate(rospy.get_param("freq"))
    # subscribe to sensor data and ego data with time synchronization
    objs1 = message_filters.Subscriber('/sensor0/obj_list_egoframe', ObjectsList)
    objsI = message_filters.Subscriber('/sensor5/obj_list_egoframe', ObjectsList)
    ts = message_filters.TimeSynchronizer([ego_data, objs_list],10)
    #ts = message_filters.TimeSynchronizer([ego_data, objs_list], 10)
    ts.registerCallback(callback)

    rospy.spin()

def callback(objs1,objsI):

    for i, obj in enumerate(objs1):
         for d, idealobj in enumerate(objsI):
            if idealobj.obj_id == obj.obj_id:
                deviation = idealobj.geometric.x - obj-geometric.x
                deviationsum += deviation
                deviationy = idealobj.geometric.y - obj-geometric.y
                deviationsumy += deviationy


                count += 1
                avg_deviation = deviationsum/count
                print(avg_deviation)

if __name__ == '__main__':
    sensor_rotate()