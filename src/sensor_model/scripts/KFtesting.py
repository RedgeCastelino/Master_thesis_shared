#!/usr/bin/env python
import numpy as np
import rospy
import math
import message_filters
import time
## Import Funtions
from rotate import rotate
from scipy.spatial import distance
## Import Objects
from ClassKF import KF , rotatedata
from ClassSens import Sens , Ego
from std_msgs.msg import Float64
# import all necessary ROS messages

from object_list.msg import ObjectList, ObjectsList
from osi3_bridge.msg import GroundTruthMovingObjects, TrafficUpdateMovingObject

deviationsum = 0
deviation = 0
count = 0
deviationy  = 0
deviationsumy = 0
distanc = 0
distsum = 0
deviationsumvx =0
deviationsumvy =0

def sensor_rotate():
    # Node initialization
    #print('ran')
    rospy.init_node('KFtesting', anonymous=False)  # Start node
    rate = rospy.Rate(rospy.get_param("freq"))
    # subscribe to sensor data and ego data with time synchronization
    objs1 = message_filters.Subscriber('/sensor0/obj_list_egoframe', ObjectsList)
    objsI = message_filters.Subscriber('/sensor5/obj_list_egoframe', ObjectsList)

    #ts = message_filters.ApproximateTimeSynchronizer([objs1, objsI],30,0.003)
    ts = message_filters.TimeSynchronizer([objs1, objsI], 10)
    ts.registerCallback(callback)

    rospy.spin()

def callback(objs1,objsI):
    global deviationsum
    global deviation
    global count
    global deviationy
    global deviationsumy
    global oldtime
    global distanc
    global distsum
    global deviationsumvx
    global deviationsumvy


    if count == 0:
        oldtime = objsI.header.stamp.to_sec()

    newtime = objsI.header.stamp.to_sec()
    print("length", len(objsI.obj_list))
    time_elapsed = (float(newtime) - float(oldtime))/1000000000

    deviation = objsI.obj_list[0].geometric.x - objs1.obj_list[0].geometric.x

    deviationsum += np.square(deviation)
    count += 1
    avg_deviation = np.sqrt(deviationsum/count)

    deviationy = objsI.obj_list[0].geometric.y - objs1.obj_list[0].geometric.y
    deviationsumy += np.square(deviationy)
    avg_deviationy = np.sqrt(deviationsumy / count)

    deviationvx = objsI.obj_list[0].geometric.vx - objs1.obj_list[0].geometric.vx
    # print('deviation',deviation )
    deviationsumvx += np.square(deviationvx)
    avg_deviationvx = np.sqrt(deviationsumvx / count)

    deviationvy = objsI.obj_list[0].geometric.vy - objs1.obj_list[0].geometric.vy
    # print('deviation',deviation )
    deviationsumvy += np.square(deviationvy)
    avg_deviationvy = np.sqrt(deviationsumvy / count)

    print('time:',time_elapsed,'x:', avg_deviation,'y:',avg_deviationy,'vx:',avg_deviationvx,'vy:',avg_deviationvy)
    distsum += distanc
    avg_dist = distsum/count




    pub = rospy.Publisher('abc', Float64, queue_size=10, latch=True)
    pub.publish(avg_deviation)
if __name__ == '__main__':
    sensor_rotate()