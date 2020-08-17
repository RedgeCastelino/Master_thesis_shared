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

global initial_time
initial_time = 0
global is_1step
is_1step= True

def aeb():

    # Node initialization
    rospy.init_node('aeb', anonymous=False)  # Start node
    rate = rospy.Rate(100)  # Define the node frequency 100hz
    #Define the Publisher
    final_time = 10
    ### time_step = rospy.get_param("time_step")  # 200   ## Time step in seconds##
    time_step = 0.01#0.04  # s
    amount_data = int(final_time / time_step)

     #Time stamp combination
    ego_sub = message_filters.Subscriber("/ego_data", TrafficUpdateMovingObject)
    objs_sub = message_filters.Subscriber("/sensor0/obj_list_egoframe", ObjectsList)
    ts = message_filters.ApproximateTimeSynchronizer([ego_sub, objs_sub], 50,50)
    ts.registerCallback(callback)
    rospy.spin()  # spin() simply keeps python from exiting until this node is stopped

def callback(ego, obj_list):

    global initial_time
    global is_1step
    if is_1step:
        is_1step = False
        initial_time = ego.header.stamp.secs + ego.header.stamp.nsecs * 1e-9

    near_obj = find_target(obj_list)
    aeb_data = Aeb()
    egovx = ego.object.velocity.x
    Traj = Trajectory()
    Traj.header.stamp = rospy.Time.now()
    Traj.reftime=initial_time
    des_vel = 11.11111111
    ### final_time = rospy.get_param("final_time")  # 2 s   ## amount of future time which data is sent to the controller####
    final_time = 10
    ### time_step = rospy.get_param("time_step")  # 200   ## Time step in seconds##
    time_step = 0.01 #s


    amount_data = int(final_time/time_step)
    ## Considering just longitudinal movement
    Traj.yaw = np.full((amount_data), ego.object.orientation.yaw)


    ## Fullfil Trajectory time with header time + steps
    Timesteparray = np.linspace(time_step, final_time, num=amount_data)
    Timenow = np.full(amount_data, (ego.header.stamp.secs+ego.header.stamp.nsecs*1e-9-initial_time))
    Traj.time = Timesteparray + Timenow
    #Traj.time = Timesteparray

    #print(obj_list.obj_list[near_obj].geometric.vx)
    ## Calculate AEB
    if near_obj != 9999:
        [aeb,reldist] = calculate_aeb(egovx, obj_list.obj_list[near_obj])
    ## Definition of actual condition
        if (abs(aeb.ttc) < aeb.stoptime.stage3) and (aeb.ttc < 0):
            print("Stage 3 is on")
            vel_aux = velocity_calculation(egovx,aeb_data.acc.stage3,time_step,amount_data)
        elif (abs(aeb.ttc) < aeb.stoptime.stage2) and (aeb.ttc < 0):
            print("Stage 2 is on")
            vel_aux = velocity_calculation(egovx,aeb_data.acc.stage2,time_step,amount_data)
        elif (abs(aeb.ttc) < aeb.stoptime.stage1) and (aeb.ttc < 0):
            print("Stage 1 is on")
            vel_aux = velocity_calculation(egovx,aeb_data.acc.stage1,time_step,amount_data)
        elif (abs(aeb.ttc) < aeb.stoptime.fw) and (aeb.ttc < 0):
            print("FW is on")
            vel_aux = np.full(amount_data+1, des_vel)
        
        #if (abs(aeb.ttc) < aeb.stoptime.fw) and (aeb.ttc < 0):
         #   print ("Stop")
          #  vel_aux = np.full(amount_data+1,0)

        elif aeb.offset >= abs(reldist): #and obj_list.obj_list[near_obj].geometric.vx-egovx <=0.5:
            print ("Stop")
            vel_aux = np.full(amount_data + 1,0)
            #print ("Following")
            #vel_aux = np.full(amount_data+1,obj_list.obj_list[near_obj].geometric.vx)

        #if ego.header.seq >300:
            #print('AEB is on')
            #vel_aux = np.full(amount_data+1,0)

        else:
            print("AEB is off")
            ## keep the expected velocity
            vel_aux = np.full(amount_data + 1, des_vel)

        #print ("TTC ", aeb.ttc)
        #print("relative distance ", reldist)
        #print("relative velocity ", obj_list.obj_list[near_obj].geometric.vx - egovx)
    else:
        print("AEB is off")
        ## keep the expected velocity
        vel_aux = np.full(amount_data + 1, des_vel)

    egox = np.full(amount_data, ego.object.position.x)
    egoy = np.full(amount_data, ego.object.position.y)
    Traj = position_calculation(time_step, vel_aux, Traj,egox,egoy)
    Traj.v = vel_aux[0:amount_data]
    #return Traj
    pub = rospy.Publisher('trajectory', Trajectory, queue_size=10,latch=True)
    pub.publish(Traj)
    #rate = rospy.Rate(25)  # Define the node frequency 100hz
    #rate.sleep()

def position_calculation(step, vel, Traj, egox,egoy):
    pos = np.zeros(len(vel)-1)
    for i in range (1,len(vel)-1):
        pos[i] = pos[i-1] + (vel[i]+vel[i+1]) * 0.5 * step

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
    lat_rang = rospy.get_param("lat_rang") #1.5   ## Lateral range of evaluation [m]
    near_x = 9999
    near_obj = 9999
    for i in range(len(obj_list.obj_list)):
        if abs(obj_list.obj_list[i].geometric.y) < lat_rang:  ################# Lateral range of evaluation
            if obj_list.obj_list[i].geometric.x < near_x:
                near_x = obj_list.obj_list[i].geometric.x
                near_obj = i
    return near_obj

def calculate_aeb (egovx,obj):
    aeb=Aeb()
    rel_velx = obj.geometric.vx - egovx
    reldist = obj.geometric.x - abs(obj.dimension.length * math.cos(obj.geometric.yaw)) - abs(obj.dimension.width * math.sin(obj.geometric.yaw))
    #print(reldist)
    #ttc = distance - offset / relative velocity
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

if __name__ == '__main__':
    aeb()
