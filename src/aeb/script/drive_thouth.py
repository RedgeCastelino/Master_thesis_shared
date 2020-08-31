#!/usr/bin/env python
import rospy
import message_filters
import numpy as np
import math
import time

# import ROS messages
from object_list.msg import ObjectsList
from osi3_bridge.msg import TrafficUpdateMovingObject
from vehicle_control.msg import Trajectory

# import class with aeb parameters
from ClassAeb import Aeb
from ClassAeb import Features

global initial_time
initial_time = 0
global is_1step
is_1step= True


aeb_data=Aeb()


def aeb_funtion():

    # Node initialization
    rospy.init_node('aeb', anonymous=False)  # Start node
    #rate = rospy.Rate(rospy.get_param("freq") )  # Define the node frequency 100hz

    #Define the Publisher with time stamp combination based on ROS time
    ego_sub = message_filters.Subscriber("/ego_data", TrafficUpdateMovingObject)
    objs_sub = message_filters.Subscriber("/sensor0/obj_list_egoframe", ObjectsList)
    ts = message_filters.ApproximateTimeSynchronizer([ego_sub, objs_sub], 3,3)
    ts.registerCallback(callback)
    rospy.spin()  # Make sure that every time a message is received the callback will be called again

def callback(ego, obj_list):

    ## Define initial Time because the controller cannot manage the high time values from ROS

    global initial_time
    global is_1step
    global aeb_data


    aeb_data.last_status = aeb_data.status
    if is_1step:
        is_1step = False
        initial_time = ego.header.stamp.secs + ego.header.stamp.nsecs * 1e-9
        aeb_data.yaw = ego.object.orientation.yaw

    # Find the Target
    near_obj = find_target(obj_list)

    ## Initialization variables
    #aeb_data = Aeb()                     # Object which contain all AEB Parameters
    egovx = ego.object.velocity.x        # Ego velocity
    Traj = Trajectory()                  # Trajectory message
    Traj.header.stamp = rospy.Time.now() # Include actual time on the stamp
    Traj.reftime=initial_time                         ## Include the initial time on the trajectory message

    ## Considering just longitudinal movement the yaw of the car keeps always the same
    Traj.yaw = np.full((aeb_data.amount_data), aeb_data.yaw)

    ## Fullfil Trajectory time with header time + steps
    Timenow = np.full(aeb_data.amount_data, (ego.header.stamp.secs+ego.header.stamp.nsecs*1e-9-initial_time)) # Vector with the actual time
    Traj.time = aeb_data.timesteparray + Timenow

    #print(ego.object.position.x )
    ## Calculate AEB
    if near_obj == 9999:
        [aeb_data,reldist] = calculate_aeb(egovx, obj_list.obj_list[near_obj],aeb_data)
    ## Definition of actual condition
        if aeb_data.offset >= abs(reldist) and obj_list.obj_list[near_obj].geometric.vx <=0.5:
            #print ("Stop")
            aeb_data.status = 3
            vel_aux = np.full(aeb_data.amount_data + 1, 0)
        elif aeb_data.offset >= abs(reldist) and obj_list.obj_list[near_obj].geometric.vx > 0.5:
            #print ("Following")
            aeb_data.status = 4
            vel_aux = np.full(aeb_data.amount_data+1,obj_list.obj_list[near_obj].geometric.vx)
        elif (abs(aeb_data.ttc) < aeb_data.stoptime.stage3) and (aeb_data.ttc < 0):
            #print("Stage 3 is on")
            aeb_data.status = 3
            #vel_aux = np.full(aeb_data.amount_data + 1, 0)
            vel_aux = velocity_calculation(egovx,aeb_data.acc.stage3,aeb_data.time_step,aeb_data.amount_data)
        elif (abs(aeb_data.ttc) < aeb_data.stoptime.stage2) and (aeb_data.ttc < 0):
            #print("Stage 2 is on")
            aeb_data.status = 2
            vel_aux = velocity_calculation(egovx,aeb_data.acc.stage2,aeb_data.time_step,aeb_data.amount_data)
        elif (abs(aeb_data.ttc) < aeb_data.stoptime.stage1) and (aeb_data.ttc < 0):
            #print("Stage 1 is on")
            aeb_data.status = 1
            vel_aux = velocity_calculation(egovx,aeb_data.acc.stage1,aeb_data.time_step,aeb_data.amount_data)
        elif (abs(aeb_data.ttc) < aeb_data.stoptime.fw) and (aeb_data.ttc < 0):
            aeb_data.status = 5
            #print("FW is on")
            vel_aux = np.full(aeb_data.amount_data+1, aeb_data.des_vel)
        else:
            #print("AEB is off")
            aeb_data.status = 0
            ## keep the expected velocity
            vel_aux = np.full(aeb_data.amount_data + 1, aeb_data.des_vel)

        #print ("TTC ", aeb_data.ttc)
        #print("relative distance ", reldist)
        #print("relative velocity ", obj_list.obj_list[near_obj].geometric.vx - egovx)
    elif ego.object.position.x > 240:
        #print("End of the Test")
        vel_aux = np.full(aeb_data.amount_data + 1, 0)
        aeb_data.status = 3
    else:
        #print("AEB is off")
        aeb_data.status = 0
        ## keep the expected velocity
        vel_aux = np.full(aeb_data.amount_data + 1, aeb_data.des_vel)

    #if aeb_data.status == 3 and aeb_data.last_status == 3:
    #    egox = np.full(aeb_data.amount_data, aeb_data.x)
    #    egoy = np.full(aeb_data.amount_data, aeb_data.y)
    #    print ('Full brake')
    #elif aeb_data.status == 3:
    #    aeb_data.x = ego.object.position.x
    #    aeb_data.y = ego.object.position.y
    #    egox = np.full(aeb_data.amount_data, ego.object.position.x)
    #    egoy = np.full(aeb_data.amount_data, ego.object.position.y)
    #else:
    #    egox = np.full(aeb_data.amount_data, ego.object.position.x)
    #    egoy = np.full(aeb_data.amount_data, ego.object.position.y)


    egox = np.full(aeb_data.amount_data, ego.object.position.x)
    egoy = np.full(aeb_data.amount_data, ego.object.position.y)


    Traj = position_calculation(aeb_data, vel_aux, Traj,egox,egoy,egovx)
    Traj.v = vel_aux[0:aeb_data.amount_data]
    #return Traj
    pub = rospy.Publisher('trajectory', Trajectory, queue_size=10,latch=True)
    pub.publish(Traj)
    #rate = rospy.Rate(25)  # Define the node frequency 100hz
    #rate.sleep()

def position_calculation(aeb_data, vel, Traj, egox,egoy,egovx):
    pos = np.zeros(len(vel)-1)
    if aeb_data.status == 3:
        vel_aux = velocity_calculation(egovx, 9.0, aeb_data.time_step, aeb_data.amount_data)
        for i in range (1,len(vel_aux)-1):
            pos[i] = pos[i - 1] + (vel_aux[i] + vel_aux[i + 1]) * 0.5 * aeb_data.time_step
    else:
        for i in range (1,len(vel)-1):
            pos[i] = pos[i-1] + (vel[i]+vel[i+1]) * 0.5 * aeb_data.time_step

    Traj.x = egox+pos*math.cos(Traj.yaw[0])
    Traj.y = egoy+pos*math.sin(Traj.yaw[0])
    #Traj.x = pos*math.cos(Traj.yaw[0])
    #Traj.y = pos*math.sin(Traj.yaw[0])

    return(Traj)


def velocity_calculation(egovx,acc,step,amount_data):
    v=egovx
    i=0
    vel = np.zeros(amount_data+1)
    while v >= 0 and (i) <= amount_data:
        vel[i] = v
        v = v - acc * step
        i = i+1
    return(vel)


def find_target(obj_list):

    near_x = 9999
    near_obj = 9999
    for i in range(len(obj_list.obj_list)):

        ### calculate near x and near y from each object###
        near_feature_x = calculate_x_y(obj_list.obj_list[i])
        if near_feature_x < near_x:
            near_x = near_feature_x
            near_obj = i
    return near_obj

def calculate_aeb (egovx,obj,aeb):
    rel_velx = obj.geometric.vx - egovx
    reldist = obj.geometric.x # - abs(obj.dimension.length * math.cos(obj.geometric.yaw)) - abs(obj.dimension.width * math.sin(obj.geometric.yaw))
    #reldist = calculate_rel_dist(obj)
    ##ttc   =         (distance - offset) / relative velocity * Signal of relative velocity
    aeb.ttc = safe_div(reldist-aeb.offset, abs(rel_velx)) * safe_div(rel_velx, abs(rel_velx))
    aeb.stoptime.fw = egovx/aeb.acc.fw + aeb.react.driver
    aeb.stoptime.stage1 = egovx / aeb.acc.stage1 + aeb.react.system
    aeb.stoptime.stage2 = egovx / aeb.acc.stage2 + aeb.react.system
    aeb.stoptime.stage3 = egovx / aeb.acc.stage3 + aeb.react.system

    return [aeb,reldist]

def safe_div(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 9999


def calculate_x_y(obj):

    x = Features()  # Import a class with all features as float 0.0
    y = Features()

    # Calculate the features
    tg_wl = math.atan(obj.dimension.width / obj.dimension.length)
    hip_wl = 0.5 * math.sqrt(obj.dimension.width ** 2 + obj.dimension.length ** 2)
    beta = obj.geometric.yaw - tg_wl
    psi = obj.geometric.yaw + tg_wl

    x.FL = obj.geometric.x + hip_wl * math.cos(psi)
    y.FL = obj.geometric.y - hip_wl * math.sin(psi)
    x.FR = obj.geometric.x + hip_wl * math.cos(beta)
    y.FR = obj.geometric.y - hip_wl * math.sin(beta)
    x.RR = obj.geometric.x - hip_wl * math.cos(-psi)
    y.RR = obj.geometric.y - hip_wl * math.sin(-psi)
    x.RL = obj.geometric.x - hip_wl * math.cos(-beta)
    y.RL = obj.geometric.y - hip_wl * math.sin(-beta)
    x.FM = (x.FR + x.FL) / 2
    y.FM = (y.FR + y.FL) / 2
    x.ML = (x.RL + x.FL) / 2
    y.ML = (y.RL + y.FL) / 2
    x.MR = (x.RR + x.FR) / 2
    y.MR = (y.RR + y.FR) / 2
    x.RM = (x.RR + x.RL) / 2
    y.RM = (y.RR + y.RL) / 2

    X = [x.FL, x.FM, x.FR, x.MR, x.RR, x.RM, x.RL, x.ML] # Vector of x position for the Features
    Y = [y.FL, y.FM, y.FR, y.MR, y.RR, y.RM, y.RL, y.ML] # Vector of y position for the Features

    ## Discover which Features are inside the lateral range of the AEB
    lat_rang = rospy.get_param("lat_rang")  # 1.5   ## Lateral range of evaluation [m]
    near_x=9999
    for i in range (8):
        if abs(Y[i]) < lat_rang:  ################# Lateral range of evaluation
            ### calculate near x inside desired y###
            if X[i] < near_x:
                near_x = X[i]
    return near_x

if __name__ == '__main__':
    aeb_funtion()
