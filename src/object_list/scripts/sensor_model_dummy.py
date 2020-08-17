#!/usr/bin/env python
# license removed for brevityi

import rospy #permit to use python 
import numpy as np
from object_list.msg import ObjectsList
from object_list.msg import ObjectList

def sensor_model_dummy():

   pub = rospy.Publisher('camera_obj', ObjectsList, queue_size=100) #
   rospy.init_node('camera',anonymous=False)  # Initiate the node camera and anonymous true permitt openinig this node a lot of times including numbers in the end of the node name  
   rate=rospy.Rate(1)  #1 hz

   while not rospy.is_shutdown():

        b=ObjectsList()
        a1=ObjectList()
        a1.geometric.x = 1
        a1.geometric.y = 1
        
        a2=ObjectList()
        a2.geometric.x = 2
        a2.geometric.y = 2
        
        b.header.stamp = rospy.Time.now()
        b.header.frame_id = "sensor_model_dummy"
        b.obj_list = np.append(a1,a2)
	rospy.loginfo(b)
        pub.publish(b)
        rate.sleep()

if __name__ == '__main__':
    try:
        sensor_model_dummy()
    except rospy.ROSInterruptException:
        pass
