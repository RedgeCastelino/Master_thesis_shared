#!/usr/bin/env python
import numpy as np
import rospy
import math
import message_filters

## Import Funtions
from rotate import rotate

## Import Objects
from ClassKF import KF , rotatedata,Prob
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
prob_tracker = []
for i in range(1000):
    a = KF()
    b=rotatedata()
    KFlist.append(a)
    rotateinfo.append(b)
    oldKFlist.append(a)
    c=Prob()
    prob_tracker.append(c)
def sensor_rotate():
    # Node initialization

    rospy.init_node('sensor2ego', anonymous=False)  # Start node
    rospy.Rate(rospy.get_param("freq"))

    # subscribe to sensor data and ego data with time synchronization
    ego_data = message_filters.Subscriber('/ego_data', TrafficUpdateMovingObject) #maikol pls confirm msg name from matlab function
    objs_list = message_filters.Subscriber('objs_list', ObjectsList)
    #ts = message_filters.ApproximateTimeSynchronizer([ego_data, objs_list],10,0.1)
    ts = message_filters.TimeSynchronizer([ego_data, objs_list], 30)
    ts.registerCallback(callback)

    rospy.spin()

def callback(ego_data,objs_list):
    global egoveh # object containing ego parameters
    global egocount
    global time # Time step
    tic = rospy.Time.now()
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

    #Apply kalman filter to sensor data if not an ideal sensorori
    if rospy.get_param("sensortype") != 5:
        #apply kalman filter function
        filtered_objs_list = kalman(objs_list)
        filtered_objs_list = calculate_probability(filtered_objs_list)
        # rotate objects list from sensor to ego frame
        new_objs_list = vector_rotate(filtered_objs_list)
    else:

        # rotate objects list from sensor to ego frame
        new_objs_list = vector_rotate(objs_list)
        for i, a in enumerate(objs_list.obj_list):
            #change relative to absolute velocities
            a.geometric.vx += egoveh.vel.x
            a.geometric.vy += egoveh.vel.y
            a.geometric.ax += egoveh.acc.x
            a.geometric.ay += egoveh.acc.y
    #for i , obj in enumerate(objs_list.obj_list):
    #    if np.sqrt(np.square(obj.geometric.vx) + np.square(obj.geometric.vy)) > (rospy.get_param('posxerr')*2*rospy.get_param('freq')):
    #        obj.prop_mov = 70

    toc = rospy.Time.now()
    time = toc.to_sec() - tic.to_sec()
    print('Sensor to EGO time', time)
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
        new = objs_list.header.stamp.to_sec()
        time = 0.1
        count1 +=1
    else:
        old = new
        new = objs_list.header.stamp.to_sec()
        time = float((new-old))

    sens = Sens()

    for i, a in enumerate(objs_list.obj_list):
        objs_list.header.frame_id = "EGOframe"
        a.time = objs_list.header.stamp.to_sec()

        ## Change the sensor position/velocity/acc origin from sensor to ego
        [a.geometric.x, a.geometric.y] = rotate(a.geometric.x, a.geometric.y, sens.rot.yaw)
        [a.geometric.vx, a.geometric.vy] = rotate(a.geometric.vx, a.geometric.vy, sens.rot.yaw)
        [a.geometric.ax, a.geometric.ay] = rotate(a.geometric.ax, a.geometric.ay, sens.rot.yaw)
        a.geometric.x = a.geometric.x + sens.pos.x
        a.geometric.y = a.geometric.y + sens.pos.y
        a.geometric.yaw += sens.rot.yaw #confirm + or -
    return objs_list



def kalman(objs_list):
    global KF # kalman filter class object
    global oldtime
    global newtime
    global egoveh # object containing ego parameters
    global oldob # old objects list
    global xnm1 # current state vector x[n|n-1] estimate given all previous measurements (n = time instance)

    yaw = egoveh.newyaw
    #yaw = 0
    if rospy.get_param("sensortype") == 1:
        #For Camera
        for i,a in enumerate(objs_list.obj_list):
            x = KFlist[a.obj_id]

            if x.track == 0: ## Element of Class KF and Work Similar to a counter
                x.track = 1
                x.newtime= objs_list.header.stamp.to_sec()
                x.oldtime=  x.newtime
                t = 0.1

                #kinematic model #trying const yaw rate model
                x.a = np.array([[np.cos(yaw),t*np.cos(yaw),t*t*np.cos(yaw)/2,np.sin(yaw),t*np.sin(yaw),t*t*np.sin(yaw)/2],[0,np.cos(yaw),t*np.cos(yaw),0,np.sin(yaw),t*np.sin(yaw)],[0,0,np.cos(yaw),0,0,np.sin(yaw)],[-np.sin(yaw),-t*np.sin(yaw),-t*t*np.sin(yaw)/2,np.cos(yaw),t*np.cos(yaw),t*t*np.cos(yaw)/2],[0,-np.sin(yaw),-t*np.sin(yaw),0,np.cos(yaw),t*np.cos(yaw)],[0,0,-np.sin(yaw),0,0,np.cos(yaw)]])
                x.b = np.array([[-t*np.cos(yaw),-t*t*np.cos(yaw)/2,-t*np.sin(yaw),-t*t*np.sin(yaw)/2],[0,0,0,0],[0,0,0,0],[t*np.sin(yaw),t*t*np.sin(yaw),-t*np.cos(yaw),-t*t*np.cos(yaw)],[0,0,0,0],[0,0,0,0]])
                #state vector estimate givel all measurememnts including preent measurement
                x.xnn = np.array([[a.geometric.x], [a.geometric.vx], [a.geometric.ax], [a.geometric.y],[a.geometric.vy],[a.geometric.ay]])
                #error model #trying const yaw rate model
                x.g = np.array([[t * t * t * np.cos(yaw) / 6, -t * t * t * np.cos(yaw) / 6, t * t * t * np.sin(yaw) / 6,
                                 -t * t * t * np.sin(yaw) / 6],
                                [t * t * np.cos(yaw) / 2, 0, t * t * np.sin(yaw) / 2, 0],
                                [t * np.cos(yaw), 0, t * np.sin(yaw), 0],
                                [-t * t * t * np.sin(yaw) / 6, t * t * t * np.sin(yaw) / 6,
                                 -t * t * t * np.cos(yaw) / 6, -t * t * t * np.cos(yaw) / 6],
                                [-t * t * np.sin(yaw) / 2, 0, t * t * np.cos(yaw) / 2, 0],
                                [-t * np.sin(yaw), 0, t * np.cos(yaw), 0]])
                x.u = np.array([[egoveh.vel.x], [egoveh.acc.x],[egoveh.vel.y],[egoveh.acc.y]])
            else:
                x.newtime = objs_list.header.stamp.to_sec()
                t = x.newtime-x.oldtime
                if t >= 1.5:
                    x=KF()
                    x.track = 1
                    x.newtime= objs_list.header.stamp.to_sec()
                    t=0.1
                    x.a = np.array([[np.cos(yaw),t*np.cos(yaw),t*t*np.cos(yaw)/2,np.sin(yaw),t*np.sin(yaw),t*t*np.sin(yaw)/2],[0,np.cos(yaw),t*np.cos(yaw),0,np.sin(yaw),t*np.sin(yaw)],[0,0,np.cos(yaw),0,0,np.sin(yaw)],[-np.sin(yaw),-t*np.sin(yaw),-t*t*np.sin(yaw)/2,np.cos(yaw),t*np.cos(yaw),t*t*np.cos(yaw)/2],[0,-np.sin(yaw),-t*np.sin(yaw),0,np.cos(yaw),t*np.cos(yaw)],[0,0,-np.sin(yaw),0,0,np.cos(yaw)]])
                    x.b = np.array(
                        [[-t * np.cos(yaw), -t * t * np.cos(yaw) / 2, -t * np.sin(yaw), -t * t * np.sin(yaw) / 2],
                         [0, 0, 0, 0], [0, 0, 0, 0],
                         [t * np.sin(yaw), t * t * np.sin(yaw), -t * np.cos(yaw), -t * t * np.cos(yaw)], [0, 0, 0, 0],
                         [0, 0, 0, 0]])
                    x.xnn = np.array(
                        [[a.geometric.x], [a.geometric.vx], [a.geometric.ax], [a.geometric.y], [a.geometric.vy],
                         [a.geometric.ay]])
                    x.g = np.array([[t*t*t*np.cos(yaw)/6,-t*t*t*np.cos(yaw)/6,t*t*t*np.sin(yaw)/6,-t*t*t*np.sin(yaw)/6],[t*t*np.cos(yaw)/2,0,t*t*np.sin(yaw)/2,0],[t*np.cos(yaw),0,t*np.sin(yaw),0],[-t*t*t*np.sin(yaw)/6,t*t*t*np.sin(yaw)/6,-t*t*t*np.cos(yaw)/6,-t*t*t*np.cos(yaw)/6],[-t*t*np.sin(yaw)/2,0,t*t*np.cos(yaw)/2,0],[-t*np.sin(yaw),0,t*np.cos(yaw),0]])

                x.a = np.array([[np.cos(yaw),t*np.cos(yaw),t*t*np.cos(yaw)/2,np.sin(yaw),t*np.sin(yaw),t*t*np.sin(yaw)/2],[0,np.cos(yaw),t*np.cos(yaw),0,np.sin(yaw),t*np.sin(yaw)],[0,0,np.cos(yaw),0,0,np.sin(yaw)],[-np.sin(yaw),-t*np.sin(yaw),-t*t*np.sin(yaw)/2,np.cos(yaw),t*np.cos(yaw),t*t*np.cos(yaw)/2],[0,-np.sin(yaw),-t*np.sin(yaw),0,np.cos(yaw),t*np.cos(yaw)],[0,0,-np.sin(yaw),0,0,np.cos(yaw)]])
                x.b = np.array(
                    [[-t * np.cos(yaw), -t * t * np.cos(yaw) / 2, -t * np.sin(yaw), -t * t * np.sin(yaw) / 2],
                     [0, 0, 0, 0], [0, 0, 0, 0],
                     [t * np.sin(yaw), t * t * np.sin(yaw), -t * np.cos(yaw), -t * t * np.cos(yaw)], [0, 0, 0, 0],
                     [0, 0, 0, 0]])
                x.g = np.array([[t*t*t*np.cos(yaw)/6,-t*t*t*np.cos(yaw)/6,t*t*t*np.sin(yaw)/6,-t*t*t*np.sin(yaw)/6],
                                [t*t*np.cos(yaw)/2,0,t*t*np.sin(yaw)/2,0],
                                [t*np.cos(yaw),0,t*np.sin(yaw),0],
                                [-t*t*t*np.sin(yaw)/6,t*t*t*np.sin(yaw)/6,-t*t*t*np.cos(yaw)/6,-t*t*t*np.cos(yaw)/6],
                                [-t*t*np.sin(yaw)/2,0,t*t*np.cos(yaw)/2,0],
                                [-t*np.sin(yaw),0,t*np.cos(yaw),0]])
                x.u = np.array([[egoveh.vel.x], [egoveh.acc.x], [egoveh.vel.y], [egoveh.acc.y]])
                x.oldtime =  x.newtime
                
            x.yn = np.array([[a.geometric.x], [a.geometric.y]]) # column vector
            noise = rospy.get_param("processnoise")
            if abs(yaw) > 0.1:
                #x.c_s[0,0] = 100000000000
                
                #x.c_s[2,2]=100000000000
                noise = 10000000000
                x.a = np.array([[np.cos(yaw),0,0,np.sin(yaw),0,0],[0,np.cos(yaw),0,0,np.sin(yaw),0],[0,0,np.cos(yaw),0,0,np.sin(yaw)],[-np.sin(yaw),0,0,np.cos(yaw),0,0],[0,-np.sin(yaw),0,0,np.cos(yaw),0],[0,0,-np.sin(yaw),0,0,np.cos(yaw)]])
                x.b = np.array(
                    [[-t * np.cos(yaw), -t * t * np.cos(yaw) / 2, -t * np.sin(yaw), -t * t * np.sin(yaw) / 2],
                     [0, 0, 0, 0], [0, 0, 0, 0],
                     [t * np.sin(yaw), t * t * np.sin(yaw), -t * np.cos(yaw), -t * t * np.cos(yaw)], [0, 0, 0, 0],
                     [0, 0, 0, 0]])
                id1 = np.zeros((6,6))
                np.fill_diagonal(id1,noise)
            print('noise',noise)
            #else:
            #    x.c_s[0,0] = rospy.get_param("processnoise")
            #    x.c_s[2, 2] = rospy.get_param("processnoise")
            x.xn_nm1 =x.a.dot(x.xnn) + x.b.dot(x.u) #column vector
            #print(x.g)
            if abs(yaw) > 0.1:
                x.pn_nm1 = (x.a.dot(x.pnn)).dot(x.a.transpose()) + id1 #+(x.g.dot(x.c_s)).dot(x.g.transpose())
            else: 
                x.pn_nm1 = (x.a.dot(x.pnn)).dot(x.a.transpose()) +(x.g.dot(x.c_s)).dot(x.g.transpose())
            x.gamma_n = x.yn -x.c.dot(x.xn_nm1) - x.d.dot(x.u)
            x.s_n = (x.c.dot(x.pn_nm1)).dot(x.c.transpose()) + x.c_m
            x.k_n = (x.pn_nm1.dot(x.c.transpose())).dot(np.linalg.inv(x.s_n))
            x.xnn = x.xn_nm1 + x.k_n.dot(x.gamma_n)
            #print( x.pn_nm1 )
            #print("YAW",yaw)
            #print('X', 'Measured :',x.yn[0],'Predicted :' ,x.xn_nm1[0], 'state',x.xnn[0])
            #print('Y', 'Measured :',x.yn[1],'Predicted :' ,x.xn_nm1[1],'state',x.xnn[1])
                
            I = np.zeros((6,6),int)
            np.fill_diagonal(I,1)
            x.pnn = (I - x.k_n.dot(x.c)).dot(x.pn_nm1)
            KFlist[a.obj_id]=x
            a.geometric.x = float(x.xnn[0])
            a.geometric.vx = float(x.xnn[1])
            a.geometric.ax = float(x.xnn[2])
            a.geometric.y = float(x.xnn[3])
            a.geometric.vy = float(x.xnn[4])
            a.geometric.ay = float(x.xnn[5])
            a.covariance = x.pnn.flatten()
            #print(rospy.get_param(sensortype))

        oldob = objs_list
        return(objs_list)

    elif rospy.get_param("sensortype") == 0:
    #FOR RADAR
        for i, a in enumerate(objs_list.obj_list):
            #convert relative velocities/acceleration to absolute as input for kalman filter
            #a.geometric.vx += egoveh.vel.x
            #a.geometric.vy += egoveh.vel.y
            #a.geometric.ax += egoveh.acc.x
            #a.geometric.ay += egoveh.acc.y

            x = KFlist[a.obj_id]

            if x.track == 0:

                x.track = 1
                x.newtime = objs_list.header.stamp.to_sec()
                x.oldtime = x.newtime
                t = 0.1
                #yaw = 0
                x.a = np.array([[np.cos(yaw),t*np.cos(yaw),t*t*np.cos(yaw)/2,np.sin(yaw),t*np.sin(yaw),t*t*np.sin(yaw)/2],[0,np.cos(yaw),t*np.cos(yaw),0,np.sin(yaw),t*np.sin(yaw)],[0,0,np.cos(yaw),0,0,np.sin(yaw)],[-np.sin(yaw),-t*np.sin(yaw),-t*t*np.sin(yaw)/2,np.cos(yaw),t*np.cos(yaw),t*t*np.cos(yaw)/2],[0,-np.sin(yaw),-t*np.sin(yaw),0,np.cos(yaw),t*np.cos(yaw)],[0,0,-np.sin(yaw),0,0,np.cos(yaw)]])
                x.b = np.array(
                    [[-t * np.cos(yaw), -t * t * np.cos(yaw) / 2, -t * np.sin(yaw), -t * t * np.sin(yaw) / 2],
                     [0, 0, 0, 0], [0, 0, 0, 0],
                     [t * np.sin(yaw), t * t * np.sin(yaw), -t * np.cos(yaw), -t * t * np.cos(yaw)], [0, 0, 0, 0],
                     [0, 0, 0, 0]])
                x.xnn = np.array([[a.geometric.x], [a.geometric.vx], [a.geometric.ax], [a.geometric.y], [a.geometric.vy],
                                  [a.geometric.ay]])
                x.g = np.array([[t*t*t*np.cos(yaw)/6,-t*t*t*np.cos(yaw)/6,t*t*t*np.sin(yaw)/6,-t*t*t*np.sin(yaw)/6],[t*t*np.cos(yaw)/2,0,t*t*np.sin(yaw)/2,0],[t*np.cos(yaw),0,t*np.sin(yaw),0],[-t*t*t*np.sin(yaw)/6,t*t*t*np.sin(yaw)/6,-t*t*t*np.cos(yaw)/6,-t*t*t*np.cos(yaw)/6],[-t*t*np.sin(yaw)/2,0,t*t*np.cos(yaw)/2,0],[-t*np.sin(yaw),0,t*np.cos(yaw),0]])
                x.u = np.array([[egoveh.vel.x], [egoveh.acc.x], [egoveh.vel.y], [egoveh.acc.y]])

            else:
                x.newtime = objs_list.header.stamp.to_sec()
                t = x.newtime - x.oldtime
                if t >= 1.5:
                    x = KF()
                    x.track = 1
                    x.newtime = objs_list.header.stamp.to_sec()
                    t = 0.1
                    x.a = np.array([[np.cos(yaw),t*np.cos(yaw),t*t*np.cos(yaw)/2,np.sin(yaw),t*np.sin(yaw),t*t*np.sin(yaw)/2],[0,np.cos(yaw),t*np.cos(yaw),0,np.sin(yaw),t*np.sin(yaw)],[0,0,np.cos(yaw),0,0,np.sin(yaw)],[-np.sin(yaw),-t*np.sin(yaw),-t*t*np.sin(yaw)/2,np.cos(yaw),t*np.cos(yaw),t*t*np.cos(yaw)/2],[0,-np.sin(yaw),-t*np.sin(yaw),0,np.cos(yaw),t*np.cos(yaw)],[0,0,-np.sin(yaw),0,0,np.cos(yaw)]])
                    x.b = np.array(
                        [[-t * np.cos(yaw), -t * t * np.cos(yaw) / 2, -t * np.sin(yaw), -t * t * np.sin(yaw) / 2],
                         [0, 0, 0, 0], [0, 0, 0, 0],
                         [t * np.sin(yaw), t * t * np.sin(yaw), -t * np.cos(yaw), -t * t * np.cos(yaw)], [0, 0, 0, 0],
                         [0, 0, 0, 0]])
                    x.xnn = np.array(
                        [[a.geometric.x], [a.geometric.vx], [a.geometric.ax], [a.geometric.y], [a.geometric.vy],
                         [a.geometric.ay]])
                    x.g = np.array([[t*t*t*np.cos(yaw)/6,-t*t*t*np.cos(yaw)/6,t*t*t*np.sin(yaw)/6,-t*t*t*np.sin(yaw)/6],[t*t*np.cos(yaw)/2,0,t*t*np.sin(yaw)/2,0],[t*np.cos(yaw),0,t*np.sin(yaw),0],[-t*t*t*np.sin(yaw)/6,t*t*t*np.sin(yaw)/6,-t*t*t*np.cos(yaw)/6,-t*t*t*np.cos(yaw)/6],[-t*t*np.sin(yaw)/2,0,t*t*np.cos(yaw)/2,0],[-t*np.sin(yaw),0,t*np.cos(yaw),0]])
                    x.u = np.array([[egoveh.vel.x], [egoveh.acc.x], [egoveh.vel.y], [egoveh.acc.y]])
                x.a = np.array([[np.cos(yaw),t*np.cos(yaw),t*t*np.cos(yaw)/2,np.sin(yaw),t*np.sin(yaw),t*t*np.sin(yaw)/2],[0,np.cos(yaw),t*np.cos(yaw),0,np.sin(yaw),t*np.sin(yaw)],[0,0,np.cos(yaw),0,0,np.sin(yaw)],[-np.sin(yaw),-t*np.sin(yaw),-t*t*np.sin(yaw)/2,np.cos(yaw),t*np.cos(yaw),t*t*np.cos(yaw)/2],[0,-np.sin(yaw),-t*np.sin(yaw),0,np.cos(yaw),t*np.cos(yaw)],[0,0,-np.sin(yaw),0,0,np.cos(yaw)]])
                x.b = np.array(
                    [[-t * np.cos(yaw), -t * t * np.cos(yaw) / 2, -t * np.sin(yaw), -t * t * np.sin(yaw) / 2],
                     [0, 0, 0, 0], [0, 0, 0, 0],
                     [t * np.sin(yaw), t * t * np.sin(yaw), -t * np.cos(yaw), -t * t * np.cos(yaw)], [0, 0, 0, 0],
                     [0, 0, 0, 0]])
                # x.g = np.array([[0, 0], [0, 0], [t, 0], [0, 0], [0, 0], [0, 0]])
                x.g = np.array([[t*t*t*np.cos(yaw)/6,-t*t*t*np.cos(yaw)/6,t*t*t*np.sin(yaw)/6,-t*t*t*np.sin(yaw)/6],[t*t*np.cos(yaw)/2,0,t*t*np.sin(yaw)/2,0],[t*np.cos(yaw),0,t*np.sin(yaw),0],[-t*t*t*np.sin(yaw)/6,t*t*t*np.sin(yaw)/6,-t*t*t*np.cos(yaw)/6,-t*t*t*np.cos(yaw)/6],[-t*t*np.sin(yaw)/2,0,t*t*np.cos(yaw)/2,0],[-t*np.sin(yaw),0,t*np.cos(yaw),0]])
                x.u = np.array([[egoveh.vel.x], [egoveh.acc.x], [egoveh.vel.y], [egoveh.acc.y]])
                x.oldtime = x.newtime
            #print('time2',t)
            x.yn = np.array([[a.geometric.x],[a.geometric.vx], [a.geometric.y],[a.geometric.vy]])  # column vector

            x.xn_nm1 = x.a.dot(x.xnn)   + x.b.dot(x.u) #column vector

            x.pn_nm1 = (x.a.dot(x.pnn)).dot(x.a.transpose()) + (x.g.dot(x.c_s)).dot(x.g.transpose())
            x.gamma_n = x.yn - x.c.dot(x.xn_nm1) - x.d.dot(x.u)
            x.s_n = (x.c.dot(x.pn_nm1)).dot(x.c.transpose()) + x.c_m

            x.k_n = (x.pn_nm1.dot(x.c.transpose())).dot(np.linalg.inv(x.s_n))
            x.xnn = x.xn_nm1 + x.k_n.dot(x.gamma_n)


            I = np.zeros((6, 6), int)
            np.fill_diagonal(I, 1)
            x.pnn = (I - x.k_n.dot(x.c)).dot(x.pn_nm1)

            KFlist[a.obj_id] = x
            a.geometric.x = float(x.xnn[0])
            a.geometric.vx = float(x.xnn[1])
            a.geometric.ax = float(x.xnn[2])
            a.geometric.y = float(x.xnn[3])
            a.geometric.vy = float(x.xnn[4])
            a.geometric.ay = float(x.xnn[5])
            a.covariance = x.pnn.flatten()



            #print(a.obj_id, (a.covariance[0]+a.covariance[18]))
        #   oldob = objs_list
        #print('time2', t)
        return (objs_list)

def calculate_probability(objs_list):

    global KFlist
    global prob_tracker
    for i,obj in enumerate(objs_list.obj_list):
         # Calculate/Model Probabilitys
         # persistance_probability based on range
        #tracker = prob_tracker[obj.id]
        sensor_range = rospy.get_param('senrange')
        obj_range = np.sqrt(np.square(obj.geometric.x) + np.square(obj.geometric.y))
        #print("obj_range",obj_range)
        max_persistance_range = rospy.get_param('range_max_persistance')  # parameterize
        range_max_persistance = max_persistance_range * sensor_range

         # birth probability

        birth_probability = rospy.get_param('birth_existance')  # parameterize
        detection_probability =rospy.get_param('detection_probability')
        clutter_probability =rospy.get_param('clutter_probability')



        alpha = 2
        max_persistance = rospy.get_param('max_persistance')  # parameterize
        range_min_persistance = 0.1  # m
        if obj_range < range_min_persistance:
            peristance_probability_range = 0
            #print("below_min")
        elif obj_range > sensor_range:
            peristance_probability_range = 0
            #print("obj_range",obj_range)
            #print("beyond max")
        elif obj_range < sensor_range and obj_range > range_max_persistance:
            #print("intermide")
            peristance_probability_range = max_persistance * math.exp((math.log(alpha, 10) * (obj_range-sensor_range)) / (sensor_range-sensor_range*(1-max_persistance_range)))

        else:
            peristance_probability_range = max_persistance

        if KFlist[obj.obj_id].track2 == 0:
            probability_existance = birth_probability
            probability_nonexistance = birth_probability
            KFlist[obj.obj_id].track2 = 1
            #print("!!!!")
        else:
            prev_existance = prob_tracker[obj.obj_id].existance
            prev_noneexistance = prob_tracker[obj.obj_id].nonexistance
            predicted_existance = prob_tracker[obj.obj_id].persistance * prev_existance + birth_probability * prev_noneexistance
            predicted_non_existance = (1-prob_tracker[obj.obj_id].persistance) * prev_existance + (1-birth_probability) * prev_noneexistance
            print("predicted_existance",predicted_existance, predicted_non_existance)
            eta = 1/(detection_probability * predicted_existance + predicted_non_existance * clutter_probability)
            print ("eta",eta)

            probability_existance = eta * detection_probability * predicted_existance
            probability_nonexistance = eta * clutter_probability * predicted_non_existance
            if probability_existance > rospy.get_param('max_existance'):
                probability_existance = rospy.get_param('max_existance')
            if probability_nonexistance > rospy.get_param('max_existance'):
                probability_nonexistance = rospy.get_param('max_existance')
            #print(probability_existance)
            #print("______")
            print ( "final existance",probability_existance, probability_nonexistance)

        obj.prop_existence = probability_existance
        obj.prop_nonexistence = probability_nonexistance
        prob_tracker[obj.obj_id].existance = probability_existance
        prob_tracker[obj.obj_id].nonexistance = probability_nonexistance
        prob_tracker[obj.obj_id].persistance = peristance_probability_range
        #print("persitance",peristance_probability_range)
        obj.prop_persistance = peristance_probability_range

    return objs_list











    














if __name__ == '__main__':
    sensor_rotate()
