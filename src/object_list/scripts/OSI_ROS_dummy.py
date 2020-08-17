#!/usr/bin/env python

import rospy #permit to use python 
import numpy as np
#from std_msgs.msg import String # permit use the message String from std_msgs
from osi3_bridge.msg import MovingObject
from osi3_bridge.msg import GroundTruthMovingObjects


def OSI_ROS_dummy():
   pub = rospy.Publisher('osi3_moving_obj_dummy', GroundTruthMovingObjects, queue_size=10) #
   rospy.init_node('osi3_dummy',anonymous=False)  # Initiate the node camera and anonymous true permitt openig this node a lot of time including number in the end of the node name  
   rate=rospy.Rate(100)  #100 hz

   while not rospy.is_shutdown():
        

	b=GroundTruthMovingObjects()

        a1=MovingObject()
        a1.position.x = 1
        a1.position.y = 1
        a1.id = 1
     
        a2=MovingObject()
        a2.id = 2
        a2.position.x = 2
        a2.position.y = 2
        a2.type=2

        a3=MovingObject()
        a3.id = 3
        a3.position.x = 0
        a3.position.y = 0
        a3.type=3


        b.header.stamp = rospy.Time.now()
        b.header.frame_id = "sensor_model_dummy"
        b.objects = np.append(a1,a2)
        b.objects = np.append(b.objects,a3)

        #rospy.loginfo(b)
        pub.publish(b)
        rate.sleep()


if __name__ == '__main__':
    try:
        OSI_ROS_dummy()
    except rospy.ROSInterruptException:
        pass
