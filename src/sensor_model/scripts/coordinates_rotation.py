#!/usr/bin/env python
import rospy
from ClassSens import Sens

# import ROS messages
from object_list.msg import ObjectsList

# import class
from ClassSens import Sens


def coordinates_rotation():
    # Node initialization
    rospy.init_node('coord_rotation', anonymous=False)  # Start node
    rate = rospy.Rate(100)  # Define the node frequency 1hz

    # Subscriber the data in callback function
    rospy.Subscriber("obj_list", ObjectsList, callback)

    rospy.spin()  # spin() simply keeps python from exiting until this node is stopped

    def callback(obj_list):

        # Return object list with objects inside the field of view with position origin on the sensor origin and rotation

        obj_list_car_origin = rotate_transpose(obj_list,sens)

if __name__ == '__main__':
    coordinates_rotation()