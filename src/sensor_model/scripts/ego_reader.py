#!/usr/bin/env python

import rospy
import math

from osi3_bridge.msg import GroundTruthMovingObjects, TrafficUpdateMovingObject
from rotate import rotate


def vehicle_reader():
    # Node initialization
    rospy.init_node('ego_reader', anonymous=False)  # Start node
    rospy.Subscriber("/osi3_moving_obj", GroundTruthMovingObjects, callback)
    rospy.spin()  # spin() simply keeps python from exiting until this node is stopped

def callback(osi_objs):
    ego_data = find_ego(osi_objs)
    header =  osi_objs.header
    public_ego(ego_data,header)


def find_ego(osi_objs):
    global ego_dataCOPY
    # find the smaller id number inside the list
    ID = osi_objs.objects[0].id
    IDpos = 0
    for i in range(len(osi_objs.objects)):
        if osi_objs.objects[i].id < ID:  # take into account that the EGO is the first spawn Object
            ID = osi_objs.objects[i].id
            IDpos = i

    # Assign the object with smaller ID to EGO
    ego = osi_objs.objects[IDpos]
    # Assign all other ID's to the obj_list
    #osi_objs_noego = [x for x in osi_objs.objects if not x.id == ID]

    return ego


def public_ego(ego,header):
    global egoyaw #ego orientation in map frame (dont forget redge and maikol)

    ego_data = TrafficUpdateMovingObject()
    ego_data.header.stamp = header.stamp
    ego_data.header.frame_id = "EGO"

    #ego_data to have ego parameters in ego frame (example velocity of ego  in x and y directions of ego / longitudinal and lateral velocity)
    ego_data.object = ego
    [ego_data.object.velocity.x, ego_data.object.velocity.y] = rotate(ego.velocity.x,ego.velocity.y,-ego.orientation.yaw)
    [ego_data.object.acceleration.x, ego_data.object.acceleration.y] = rotate(ego.acceleration.x,ego.acceleration.y,-ego.orientation.yaw)
    egoyaw= ego.orientation.yaw
    pub = rospy.Publisher('ego_data', TrafficUpdateMovingObject, queue_size=10)
    pub.publish(ego_data)

if __name__ == '__main__':
    vehicle_reader()
