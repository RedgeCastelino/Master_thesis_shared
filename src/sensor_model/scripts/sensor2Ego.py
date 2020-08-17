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

count1 = 0 # TO CALCULATE TIME - Objectlist related
egocount=0 # counter to calculate ego yawrate
time =0

KFlist=[] # List of all objects KF (Every object in OL "Object_managment")
rotateinfo=[] # List of all objects rotatedata (Every object in OL "Object_managment")

egoveh = Ego()


#create a list o update kalman parameters
oldKFlist=[]
for i in range(1000):
    a = KF()
    b=rotatedata()
    KFlist.append(a)
    rotateinfo.append(b)
    oldKFlist.append(a)

def sensor_rotate():
    # Node initialization
    rospy.init_node('sensor2ego', anonymous=False)  # Start node
    rate = rospy.Rate(100)
    # subscribe to sensor data and ego data with time synchronization
    ego_data = message_filters.Subscriber('/ego_data', TrafficUpdateMovingObject)
    objs_list = message_filters.Subscriber('objs_list', ObjectsList)
    ts = message_filters.ApproximateTimeSynchronizer([ego_data, objs_list], 20, 20)
    #ts = message_filters.TimeSynchronizer([ego_data, objs_list], 10)
    ts.registerCallback(callback)

    rospy.spin()

def callback(ego_data,objs_list):
    global egoveh # object containing ego parameters
    global egocount
    global time # Time step

    # provide ego data parameters to global variable ego_veh
    egoveh.vel.x = ego_data.object.velocity.x
    egoveh.vel.y = ego_data.object.velocity.y
    egoveh.acc.x = ego_data.object.acceleration.x
    egoveh.acc.y = ego_data.object.acceleration.y
        # calculate ego yaw (how much the car has rotated since last measurement in egoveh.newyaw)
    if egocount == 0 :
        egoveh.neworientation = ego_data.object.orientation.yaw
        egocount+=1
        egoveh.testyaw = egoveh.neworientation
        egoveh.newyaw = 0
    else:
        egoveh.oldorientation =  egoveh.neworientation
        egoveh.neworientation = ego_data.object.orientation.yaw
        egoveh.newyaw = egoveh.oldorientation-egoveh.neworientation


    ## Start the ROS publisher
    pub=rospy.Publisher('obj_list_egoframe', ObjectsList, queue_size=10,latch=True)

    #Apply kalman filter to sensor data if not an ideal sensor
    if rospy.get_param("sensortype") != 5:
        #apply kalman filter function
        filtered_objs_list = kalman(objs_list)
        # rotate objects list from sensor to ego frame
        new_objs_list = vector_rotate(filtered_objs_list)
    else:

        # rotate objects list from sensor to ego frame
        new_objs_list = vector_rotate(objs_list)
    pub.publish(new_objs_list)

def vector_rotate(objs_list):
    #rotate objects list from sensor to ego frame
    global egoveh # object containing ego parameters
    global new #current objects list time
    global old # previous object list time
    global time # time step
    global count1 #count for time step calculation
    #global count
    global old_objs #previous objects list

    #calculate time
    if count1 ==0:
        new = float(str(objs_list.header.stamp.nsecs))
        time = 0.1
        count1 +=1
    else:
        old = new
        new = float(str(objs_list.header.stamp.nsecs))
        time = float(str((new-old)))/1000000000 #nsecs to secs

    sens = Sens()

    for i, a in enumerate(objs_list.obj_list):
        objs_list.header.frame_id = "EGOframe"

        ## Change the sensor position/velocity/acc origin from sensor to ego
        [a.geometric.x, a.geometric.y] = rotate(a.geometric.x, a.geometric.y, sens.rot.yaw)
        [a.geometric.vx, a.geometric.vy] = rotate(a.geometric.vx, a.geometric.vy, sens.rot.yaw)
        [a.geometric.ax, a.geometric.ay] = rotate(a.geometric.ax, a.geometric.ay, sens.rot.yaw)
        a.geometric.x = a.geometric.x + sens.pos.x
        a.geometric.y = a.geometric.y + sens.pos.y
    return objs_list



def kalman(objs_list):
    global KF # kalman filter class object
    global oldtime
    global newtime
    global egoveh # object containing ego parameters
    global oldob # old objects list
    global xnm1 # current state vector x[n|n-1] estimate given all previous measurements (n = time instance)


    if rospy.get_param("sensortype") == 1:
        #For Camera
        for i,a in enumerate(objs_list.obj_list):
            x = KFlist[a.obj_id]

            if x.track == 0: ## Element of Class KF and Work Similar to a counter
                x.track = 1
                x.newtime= float(str(objs_list.header.stamp.nsecs))/1000000000
                x.oldtime=  x.newtime
                t = 0.1
                #kinematic model
                x.a = np.array([[1,t,t*t/2,0,0,0],[0,1,t,0,0,0],[0,0,1,0,0,0],[0,0,0,1,t,t*t/2],[0,0,0,0,1,t],[0,0,0,0,0,1]])
                #state vector estimate givel all measurememnts including preent measurement
                x.xnn = np.array([[a.geometric.x], [a.geometric.vx], [a.geometric.ax], [a.geometric.y],[a.geometric.vy],[a.geometric.ay]])
                #error model
                x.g = np.array([[t*t*t/6,0],[t*t/2,0],[t,0],[0,t*t*t/6],[0,t*t/2],[0,t]])

            else:
                x.newtime = float(str(objs_list.header.stamp.nsecs))/1000000000
                t = x.newtime-x.oldtime
                if t >= 1.5:
                    x=KF()
                    x.track = 1
                    x.newtime= float(str(objs_list.header.stamp))
                    t=0.1
                    x.a = np.array(
                        [[1, t, t * t / 2, 0, 0, 0], [0, 1, t, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, t, t * t / 2],
                         [0, 0, 0, 0, 1, t], [0, 0, 0, 0, 0, 1]])
                    x.xnn = np.array(
                        [[a.geometric.x], [a.geometric.vx], [a.geometric.ax], [a.geometric.y], [a.geometric.vy],
                         [a.geometric.ay]])
                    x.g = np.array([[t * t * t / 6, 0], [t * t / 2, 0], [t, 0], [0, t * t * t / 6], [0, t * t / 2], [0, t]])

                x.a = np.array([[1,t,t*t/2,0,0,0],[0,1,t,0,0,0],[0,0,1,0,0,0],[0,0,0,1,t,t*t/2],[0,0,0,0,1,t],[0,0,0,0,0,1]])
                x.g = np.array([[t*t*t/6,0],[t*t/2,0],[t,0],[0,t*t*t/6],[0,t*t/2],[0,t]])
                x.oldtime =  x.newtime

            x.yn = np.array([[a.geometric.x], [a.geometric.y]]) # column vector

            x.xn_nm1 =x.a.dot(x.xnn) #+ x.b.dot(x.u) #column vector

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
            a.covariance = x.pnn.flatten()
        oldob = objs_list
        return(objs_list)

    elif rospy.get_param("sensortype") == 0:
    #FOR RADAR
        for i, a in enumerate(objs_list.obj_list):


            x = KFlist[a.obj_id]

            if x.track == 0:

                x.track = 1
                x.newtime = float(str(objs_list.header.stamp.nsecs)) / 1000000000
                x.oldtime = x.newtime
                t = 0.1

                x.a = np.array(
                    [[1, t, t * t / 2, 0, 0, 0], [0, 1, t, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, t, t * t / 2],
                     [0, 0, 0, 0, 1, t], [0, 0, 0, 0, 0, 1]])
                x.xnn = np.array([[a.geometric.x], [a.geometric.vx], [a.geometric.ax], [a.geometric.y], [a.geometric.vy],
                                  [a.geometric.ay]])
                x.g = np.array([[t * t * t / 6, 0], [t * t / 2, 0], [t, 0], [0, t * t * t / 6], [0, t * t / 2], [0, t]])

            else:
                x.newtime = float(str(objs_list.header.stamp.nsecs)) / 1000000000
                t = x.newtime - x.oldtime
                if t >= 1.5:
                    x = KF()
                    x.track = 1
                    x.newtime = float(str(objs_list.header.stamp))
                    t = 0.1
                    x.a = np.array(
                        [[1, t, t * t / 2, 0, 0, 0], [0, 1, t, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, t, t * t / 2],
                         [0, 0, 0, 0, 1, t], [0, 0, 0, 0, 0, 1]])
                    x.xnn = np.array(
                        [[a.geometric.x], [a.geometric.vx], [a.geometric.ax], [a.geometric.y], [a.geometric.vy],
                         [a.geometric.ay]])
                    x.g = np.array([[t * t * t / 6, 0], [t * t / 2, 0], [t, 0], [0, t * t * t / 6], [0, t * t / 2], [0, t]])

                x.a = np.array(
                    [[1, t, t * t / 2, 0, 0, 0], [0, 1, t, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, t, t * t / 2],
                     [0, 0, 0, 0, 1, t], [0, 0, 0, 0, 0, 1]])
                # x.g = np.array([[0, 0], [0, 0], [t, 0], [0, 0], [0, 0], [0, 0]])
                x.g = np.array([[t * t * t / 6, 0], [t * t / 2, 0], [t, 0], [0, t * t * t / 6], [0, t * t / 2], [0, t]])

                x.oldtime = x.newtime

            x.yn = np.array([[a.geometric.x], [a.geometric.y],[a.geometric.vx],[a.geometric.vy]])  # column vector

            x.xn_nm1 = x.a.dot(x.xnn)  # + x.b.dot(x.u) #column vector

            x.pn_nm1 = (x.a.dot(x.pnn)).dot(x.a.transpose()) + (x.g.dot(x.c_s)).dot(x.g.transpose())
            x.gamma_n = x.yn - x.c.dot(x.xn_nm1)
            x.s_n = (x.c.dot(x.pn_nm1)).dot(x.c.transpose()) + x.c_m

            x.k_n = (x.pn_nm1.dot(x.c.transpose())).dot(np.linalg.inv(x.s_n))
            x.xnn = x.xn_nm1 + x.k_n.dot(x.gamma_n)



            I = np.zeros((6, 6), int)
            np.fill_diagonal(I, 1)
            x.pnn = (I - x.k_n.dot(x.c)).dot(x.pn_nm1)

            KFlist[a.obj_id] = x
            a.geometric.x = x.xnn[0]
            a.geometric.vx = x.xnn[1]
            a.geometric.ax = x.xnn[2]
            a.geometric.y = x.xnn[3]
            a.geometric.vy = x.xnn[4]
            a.geometric.ay = x.xnn[5]
            a.covariance = x.pnn.flatten()

        # print(x.track)
        oldob = objs_list
        return (objs_list)

if __name__ == '__main__':
    sensor_rotate()
