#!/usr/bin/env python


import sys
import glob
import os


try:
    sys.path.append(glob.glob('/opt/carla-simulator/PythonAPI/carla/dist/carla-0.9.8-py2.7-linux-x86_64.egg')[0])

#    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
#        sys.version_info.major,
#        sys.version_info.minor,
#        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

# ==============================================================================
# -- add PythonAPI for release mode --------------------------------------------
# ==============================================================================
try:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/carla')
except IndexError:
    pass

import carla
import rospy
import numpy as np
import math

from osi3_bridge.msg import TrafficUpdateMovingObject



def CARLA_OSI_ROS():

    ## Connect with CARLA server
    client = carla.Client('localhost', 2000)  ### It starts the communication between server and client
    client.set_timeout(10.0)  # seconds       ### After 10 seconds without communication with CARLA server the script stops
    #client.set_timeout(10.0)  # seconds       ### After 10 seconds without communication with CARLA server the script stops
    world = client.get_world()
    global actor_list
    actor_list = world.get_actors()

    # Initiate ROS node
    rospy.init_node('CARLAOSI_update', anonymous=False)  # Start node
    rate = rospy.Rate(25)  # Define the node frequency 100hz
    rospy.Subscriber("/osi3_traffic_update", TrafficUpdateMovingObject, set_ego)
    rospy.spin()


def set_ego(ego):

    actor = actor_list.find(ego.object.id)
    actor.set_simulate_physics(enabled=False)
    location = carla.Location(x=ego.object.position.x, y=-ego.object.position.y, z=ego.object.position.z)
    velocity = carla.Vector3D(x=ego.object.velocity.x, y=-ego.object.velocity.y, z=ego.object.velocity.z)
    rotation = carla.Rotation(pitch=-ego.object.orientation.pitch*180/math.pi, yaw=-ego.object.orientation.yaw*180/math.pi, roll=ego.object.orientation.roll*180/math.pi)
    transform = carla.Transform(location,rotation)

    actor.set_transform(transform)
    actor.set_velocity(velocity)

    return

if __name__ == '__main__':
    try:
        CARLA_OSI_ROS()
    except rospy.ROSInterruptException:
        pass

