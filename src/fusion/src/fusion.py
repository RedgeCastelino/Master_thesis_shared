#!/usr/bin/env python

import numpy as np
import rospy
import math
import message_filters
import tf
from object_list.msg import ObjectList, ObjectsList
from osi3_bridge.msg import GroundTruthMovingObjects, TrafficUpdateMovingObject


# import function
#import ClassAssociate
#from ObjectAssociation import feature_select
#import Objects
from scipy.spatial import distance
from Association import *
from fusion_function import *
from ClassExistance_Objects import * 
from ClassFusion import *
main_data = fusion()


globaltrack = ObjectsList()
count=0
egoveh = Ego()
prev_time = 0   # time stamp of prev message
current_time = 0 # time stamp of current message



def sensor_fusion():

    rospy.init_node('sensor_fusion', anonymous=False)  # Start node

    #rate = rospy.Rate(rospy.get_param("freq"))  # Define the node frequency 100hz
    #subscribe to sensor data (add additional sensors here
    sensor1 = message_filters.Subscriber("/sensor0/obj_list_egoframe", ObjectsList)
    sensor2 = message_filters.Subscriber("/sensor1/obj_list_egoframe", ObjectsList)



    ego_data = message_filters.Subscriber('/ego_data', TrafficUpdateMovingObject)

    #add all sensors to time synchronizer
    #ts = message_filters.ApproximateTimeSynchronizer([sensor1,sensor2,ego_data], 10,0.1)
    ts = message_filters.TimeSynchronizer([sensor1, sensor2, ego_data], 30)
    #ts = message_filters.TimeSynchronizer([sensor1, ego_data], 10)
    ts.registerCallback(callback)

    rospy.spin()  # spin() simply keeps python from exiting until this node is stopped

#def callback(sensor1,sensor2,ego_data):
def callback(sensor1,sensor2,ego_data):
    global count
    global main_data
    global prev_time
    global current_time
    tic = rospy.Time.now()
    #print('time',rospy.Time.now())
    main_data.sensorslist = []
    print('callback started')
    #print('sensor12',sensor1.header.stamp.nsecs)
    count= count +1

    main_data.sensorslist.append(sensor1)
    main_data.sensorslist.append(sensor2)

    main_data.egoveh.vel.x = ego_data.object.velocity.x
    main_data.egoveh.vel.y = ego_data.object.velocity.y
    main_data.egoveh.acc.x = ego_data.object.acceleration.x
    main_data.egoveh.acc.y = ego_data.object.acceleration.y

    if count == 0:
        main_data.egoveh.neworientation = ego_data.object.orientation.yaw
        count += 1
        main_data.egoveh.testyaw = main_data.egoveh.neworientation
        main_data.egoveh.newyaw = 0
        prev_time = ego_data.header.stamp.to_sec()
        current_time = ego_data.header.stamp.to_sec()
        #ego_veh.
    else:
        main_data.egoveh.oldorientation = main_data.egoveh.neworientation
        main_data.egoveh.neworientation = ego_data.object.orientation.yaw
        main_data.egoveh.newyaw = main_data.egoveh.oldorientation - main_data.egoveh.neworientation
        prev_time = current_time
        current_time = ego_data.header.stamp.to_sec()

        main_data.egoveh.t = current_time-prev_time
        main_data.egoveh.yawrate =  main_data.egoveh.newyaw/ main_data.egoveh.t


        #print('time interval',(nt-ot))
        #print('process time',((rospy.Time.now()).to_sec()-nt))

    if len(main_data.globaltrack.obj_list) == 0:
        #print('RAN')
        main_data.globaltrack = main_data.sensorslist[0]
        a = 0
        for i, obj in enumerate(main_data.globaltrack.obj_list):
            obj.obj_id = int(a)
            obj.sensors_fused = [main_data.sensorslist[0].sensor_property.sensor_id]
            a += 1
            Sensor_obj = SensorObject(obj,main_data.sensorslist[0].sensor_property)
            Sensor_obj.set_existance_probability_mass_factors()
            Sensor_obj.set_classification_mass_factors()
            obj.classification_mass = Sensor_obj.list_classification_mass_factor

    #print('fusion runs')
    main_data.fuse()

    #print(main_data.AssignmentList)
    #print(len(main_data.globaltrack.obj_list))
    #main_data.evaluate_time
    main_data.sensorlist_previous = main_data.sensorslist
    #print(len(main_data.globaltrack.obj_list))
    #main_data.fuse()
    pub = rospy.Publisher('fused_data', ObjectsList, queue_size=10,latch=True)
    toc = rospy.Time.now()
    time = toc.to_sec() - tic.to_sec()
    print('fusion time', time)
    print("test")
    pub.publish(main_data.globaltrack)





'''
def sensor_fusion():

    rospy.init_node('sensor_fusion', anonymous=False)  # Start node
    #rate = rospy.Rate(rospy.get_param("freq"))  # Define the node frequency 100hz
    #subscribe to sensor data (add additional sensors here
    ego_data = rospy.Subscriber('/ego_data', TrafficUpdateMovingObject, ego_callback)
    sensor1 = rospy.Subscriber("/sensor0/obj_list_egoframe", ObjectsList,sensor_callback)
    sensor2 = rospy.Subscriber("/sensor1/obj_list_egoframe", ObjectsList,sensor_callback)



    #ego_data = rospy.Subscriber('/ego_data', TrafficUpdateMovingObject,ego_callback)

    #add all sensors to time synchronizer
    #ts = message_filters.ApproximateTimeSynchronizer([sensor1,sensor2,ego_data], 10,0.1)
    #ts = message_filters.TimeSynchronizer([sensor1, sensor2, ego_data], 10)
    #ts.registerCallback(callback)
    rospy.spin()  # spin() simply keeps python from exiting until this node is stopped
def ego_callback(ego_data):
    global count
    global main_data
    main_data.egoveh.vel.x = ego_data.object.velocity.x
    main_data.egoveh.vel.y = ego_data.object.velocity.y
    main_data.egoveh.acc.x = ego_data.object.acceleration.x
    main_data.egoveh.acc.y = ego_data.object.acceleration.y  # (obj.geometric.y + obj.geometric.vy * t  * obj.geometric.ay *t*t/2) *np.sin(egoveh.newyaw)

    if count == 0:
        main_data.egoveh.neworientation = ego_data.object.orientation.yaw
        count += 1
        main_data.egoveh.testyaw = main_data.egoveh.neworientation
        main_data.egoveh.newyaw = 0
    else:
        main_data.egoveh.oldorientation = main_data.egoveh.neworientation
        main_data.egoveh.neworientation = ego_data.object.orientation.yaw
        main_data.egoveh.newyaw = 0  # main_data.egoveh.oldorientation - main_data.egoveh.neworientation

def sensor_callback(sensor):
    global main_data
    main_data.sensorslist = []
    main_data.sensorslist.append(sensor)
    main_data.associate()

    # print(main_data.AssignmentList)
    # print(len(main_data.globaltrack.obj_list))
    # main_data.evaluate_time
    main_data.sensorlist_previous = main_data.sensorslist
    # print(len(main_data.globaltrack.obj_list))
    # main_data.fuse()
    pub = rospy.Publisher('fused_data', ObjectsList, queue_size=10, latch=True)
    pub.publish(main_data.globaltrack)
    #ego = tf.TransformBroadcaster()
    #ego.sendTransform((ego_data.object.position.x, ego_data.object.position.y, 0),
    #                  tf.transformations.quaternion_from_euler(0, 0, ego_data.object.orientation.yaw), rospy.Time.now(),
    #                  "ego", "map")
'''

if __name__ == '__main__':
    sensor_fusion()





