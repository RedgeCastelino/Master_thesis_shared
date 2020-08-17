#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):

    hello_str = data.data
    pub = rospy.Publisher('reply', String, queue_size=10)
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    return data.data
    
def listener():

    rospy.init_node('replier', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    rospy.Subscriber("chatter", String, callback)
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    # rospy.init_node('listener', anonymous=True)
    # spin() simply keeps python from exiting until this node is stopped

    rospy.spin()

if __name__ == '__main__':
    listener()
