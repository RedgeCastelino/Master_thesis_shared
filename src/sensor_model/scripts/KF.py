#!/usr/bin/env python
import numpy as np
import rospy
import math
from ClassKF import KF
# import all necessary ROS messages
from object_list.msg import ObjectList, ObjectsList
from osi3_bridge.msg import GroundTruthMovingObjects, TrafficUpdateMovingObject

KFlist=[]
countlist=[]
count = 0
counter =0

for i in range(1000):
    a = KF()
    KFlist.append(a)
    #countlist.append(0)



def sensor_model():
    # Node initialization
    rospy.init_node('KF', anonymous=False)  # Start node
    rate = rospy.Rate(100)  # Define the node frequency 1hz

    # Subscriber the data in callback function
    rospy.Subscriber("obj_list_egoframe", ObjectsList, callback)
    #rospy.Subscriber("obj_list_egoframe", ObjectsList, callback)

    rospy.spin()  # spin() simply keeps python from exiting until this node is stopped


def callback(objs_list):
    global KF
    global count
    global counter
    global oldtime
    global newtime

    #print(objs_list)
    '''for i in objs_list.object_list:
    a=KF
    if counter = 0
        newtime = float(str(objs_list.header.stamp))
        oldtime = newtime
        t= 1
        count+=1
    else:
        newtime = float(str(objs_list.header.stamp))
        t= newtime-oldtime
        oldtime = newtime'''
    for i,a in enumerate(objs_list.obj_list):
        x = KFlist[a.obj_id]
        #print(x)
        if x.track == 0:

            x.track = 1
            x.newtime= float(str(objs_list.header.stamp))
            x.oldtime=  x.newtime
            t = 1


            x.a = np.array([[1,t,t*t/2,0,0,0],[0,1,t,0,0,0],[0,0,1,0,0,0],[0,0,0,1,t,t*t/2],[0,0,0,0,1,t],[0,0,0,0,0,1]])
            #x.xnn = np.array([[a.geometric.x], [a.geometric.vx], [a.geometric.ax], [a.geometric.y],[a.geometric.vy],[a.geometric.ay]])
            x.g = np.array([[t*t*t/6,0],[t*t/2,0],[t,0],[0,t*t*t/6],[0,t*t/2],[0,t]])
            #KF[a.obj_id]=x
        else:
            x.newtime = float(str(objs_list.header.stamp))
            t = x.newtime-x.oldtime
            if t >= 1.5:
                x=KF()
                x.track = 1
                x.newtime= float(str(objs_list.header.stamp))

                t = 1
                x.a = np.array([[1,t,t*t/2,0,0,0],[0,1,t,0,0,0],[0,0,1,0,0,0],[0,0,0,1,t,t*t/2],[0,0,0,0,1,t],[0,0,0,0,0,1]])

                x.g = np.array([[t*t*t/6,0],[t*t/2,0],[t,0],[0,t*t*t/6],[0,t*t/2],[0,t]])
                #KF[a.obj_id]=x

            x.oldtime=  x.newtime

            x.yn = np.array([[a.geometric.x], [a.geometric.y]]) # column vector

            #Kalman equations
            x.xn_nm1 =x.a.dot(x.xnn) #column vector
            #print(type(x.g))

            x.pn_nm1 = (x.a.dot(x.pnn)).dot(x.a.transpose()) +(x.g.dot(x.c_s)).dot(x.g.transpose())
            x.gamma_n = x.yn -x.c.dot(x.xn_nm1)
            x.s_n = (x.c.dot(x.pn_nm1)).dot(x.c.transpose()) + x.c_m
            x.k_n = (x.pn_nm1.dot(x.c.transpose())).dot(np.linalg.inv(x.s_n))
            x.xnn = x.xn_nm1 + x.k_n.dot(x.gamma_n)
            I = np.zeros((6,6),int)
            np.fill_diagonal(I,1)
            x.pnn = (I - x.k_n.dot(x.c)).dot(x.pn_nm1)
            KFlist[a.obj_id]=x
            a.geometric.x = x.xnn[0]
            a.geometric.vx = x.xnn[1]
            a.geometric.ax = x.xnn[2]
            a.geometric.y = x.xnn[3]
            a.geometric.vy = x.xnn[4]
            a.geometric.ay = x.xnn[5]
    pub = rospy.Publisher('afterKF', ObjectsList, queue_size=10)
    pub.publish(objs_list)
    print(objs_list)

    #x.a = [[1,t,t*t/2,0,0,0],[0,1,t,0,0,0],[0,0,1,0,0,0],[0,0,0,1,t,t*t/2],[0,0,0,0,1,t],[0,0,0,0,0,1]]
    #x.xnn
    #KF.append(x)

    print (objs_list)



if __name__ == '__main__':
    sensor_model()
