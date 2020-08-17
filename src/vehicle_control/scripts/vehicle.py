#!/usr/bin/env python
import rospy
import message_filters
import matlab.engine
import math
import rospkg
import numpy as np
from rotate import rotate

global old_time
global old_pos


# import ROS messages
from vehicle_control.msg import Trajectory
from osi3_bridge.msg import GroundTruthMovingObjects, TrafficUpdateMovingObject

def vehicle():

    global ego_data
    global eng
    global pub

    pub = rospy.Publisher('ego_data', TrafficUpdateMovingObject, queue_size=10,latch=True)

    #veh_pub = rospy.Publisher('ego_data', TrafficUpdateMovingObject, queue_size=10)

    print('Initializing MATLAB')
    eng = matlab.engine.start_matlab()
    #Define Matlab path
    rospack = rospkg.RosPack()
    eng.cd(rospack.get_path('vehicle_control')+'/scripts')
    print('MATLAB Initialized')

    #Initiate ROS node
    rospy.init_node('simulated_vehicle', anonymous=False)  # Start node
    rate = rospy.Rate(25)  # Define the node frequency 100hz

    # Receive car position from simulation Osi3 GT
    # Publish car position

    print('Calibrating EGO position, Please do not move the EGO nor the Digital Twin')
    #while not subscriber_connected:
    #    num_connections = veh_pub.get_num_connections()
    #    gt_msg = rospy.wait_for_message("/osi3_moving_obj", GroundTruthMovingObjects, timeout=10)
    #    ego_data = calibration(gt_msg)

    #    if num_connections > 1:
    #        subscriber_connected = True
    #        print('EGO calibration complete')

    gt_msg = rospy.wait_for_message("/osi3_moving_obj", GroundTruthMovingObjects, timeout=10)
    ego_data = calibration(gt_msg)
    ego_data.object.orientation.yaw=0.0  ##########################
    pub.publish(ego_data)
    print('EGO calibration complete')
#        veh_pub.publish(ego_data)
#        rate.sleep()

    # Subscribe trajectory and use ego_data as arg --> output new car position

    #while not rospy.is_shutdown():
    #    rospy.Subscriber("/trajectory", Trajectory, callback)
    #    pub = rospy.Publisher('ego_data', TrafficUpdateMovingObject, queue_size=10)
    #    pub.publish(ego_data)
    #    rate.sleep() #keeps python from exiting until this node is stopped
    #pub.publish(ego_data)
    rospy.Subscriber("/trajectory", Trajectory, callback)
    rospy.spin() #keeps python from exiting until this node is stopped



def callback(traj):
    #ego_data=arg[0]
    #eng=arg[1]
    global ego_data
    global pub
    global eng
    global old_time
    global old_pos
    # ego_data has velocity in acceleration in ego_osi frame while ego has velocities and accelerations in Map frame

    rXtraj = matlab.double(tuple(traj.x))  # Trajectory x-points              (1xm) vector
    rYtraj = matlab.double(tuple(traj.y))  # Trajectory y-points              (1xm) vector
    PsiTraj = matlab.double(tuple(traj.yaw))  # Trajectory yaw angle          (1xm) vector
    tTraj = matlab.double(tuple(traj.time))  # Trajectory time_stamp          (1xm) vector
    vTraj = matlab.double(tuple(traj.v))  # Trajectory velocity               (1xm) vector

    #m=len(rXtraj)
    #tTraj = matlab.double(tuple(np.linspace(0, 2.0, num=m)))  # Trajectory time_stamp               ((1xm) vector)

    rX = ego_data.object.position.x  # current x - point of EGO                    (1x1) scalar
    rY = ego_data.object.position.y  # current y - point of EGO                    (1x1) scalar
    yaw = ego_data.object.orientation.yaw # current yaw angle of EGO  (1x1) scalar
    v = ego_data.object.velocity.x  # current velocity of EGO                      (1x1) scalar
    ax = ego_data.object.acceleration.x  # current acceleration in x of EGO        (1x1) scalar
    ay = ego_data.object.acceleration.y  # current acceleration in y of EGO        (1x1) scalar

    if v<=0.1:
        v=0.1



    res = eng.Vehicle(rXtraj, rYtraj, vTraj, PsiTraj, tTraj, rX, rY, yaw, v, ax, ay, nargout=6)  ### run Matlab Funtion
    #res = eng.Vehicle(rXtraj, rYtraj, vTraj, PsiTraj, tTraj, rX, rY, 0.0, v, ax, 0.0, nargout=6)  ### run Matlab Funtion

    if ego_data.header.seq == 1:
        old_time = ego_data.header.stamp.nsecs
        old_pos = res[0]
    time_step = (ego_data.header.stamp.nsecs-old_time)*1e-9
    print ("time step  ", time_step ,"        calculated velocity", safe_div((res[0]-old_pos),time_step), "velocity", res[2])#, "posx ", res[0], "     posy ",res[1], "   yaw  ",res[5], "     velocity x",res[2])
    #print (res)

    old_time = ego_data.header.stamp.nsecs
    old_pos = res[0]


    # Update ego_data with the output of the simulated vehicle
    ego_data.object.position.x = res[0]                     # Updated x - point of EGO m - Map Frame
    ego_data.object.position.y = res[1]                     # Updated y - point of EGO m - Map Frame
    #ego_data.object.orientation.yaw = res[5]    # Updated yaw angle of EGO rad
    ego_data.object.velocity.x = res[2]                     # Updated velocity x on EGO frame
    ego_data.object.velocity.y = 0.0                               # Lateral velocity of the EGO = 0 on EGO frame
    ego_data.object.acceleration.x = res[3]                      # Longitudinal acceleration on EGO frame
    ego_data.object.acceleration.y = res[4]                      # Lateral acc in EGO frame

    ego_data.header.stamp = rospy.Time.now()
    ego_osi = ego_data
    # Rotate from EGO to Map frame
    [ego_osi.object.velocity.x, ego_osi.object.velocity.y] = rotate(res[2],0,0)#-ego_osi.object.orientation.yaw)  # Lateral Velocity = 0   Updated velocity of EGO  m/s - Map Frame
    [ego_osi.object.acceleration.x, ego_osi.object.acceleration.y] = rotate(res[3],res[4],0)#-ego_osi.object.orientation.yaw) # Updated accel in y of EGO m/s2 Map Frame

    pub.publish(ego_data)
    ego_osi.header.frame_id="Map"
    osipub = rospy.Publisher('osi3_traffic_update', TrafficUpdateMovingObject, queue_size=10)
    osipub.publish(ego_osi)

    #print(ego_data)


def calibration(osi_objs):
    global ego_data
    # find the smaller id number inside the list
    ID=osi_objs.objects[0].id
    IDpos=0
    for i in range(len(osi_objs.objects)):
        if osi_objs.objects[i].id < ID:   # take into account that the EGO is the first spawn Object
            ID = osi_objs.objects[i].id
            IDpos = i

    #Assign the object with smaller ID to EGO
    ego_data = TrafficUpdateMovingObject()
    ego_data.object = osi_objs.objects[IDpos]
    ego_data.header.stamp = osi_objs.header.stamp
    ego_data.header.frame_id = "EGO"
    [ego_data.object.velocity.x, ego_data.object.velocity.y] = rotate(ego_data.object.velocity.x, ego_data.object.velocity.y,ego_data.object.orientation.yaw)
    [ego_data.object.acceleration.x, ego_data.object.acceleration.y] = rotate(ego_data.object.acceleration.x, ego_data.object.acceleration.y,ego_data.object.orientation.yaw)

    #pub = rospy.Publisher('ego_data', TrafficUpdateMovingObject, queue_size=10,latch=True)
    #veh_pub.publish(ego_data)
    return ego_data

def safe_div(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 0

if __name__ == '__main__':
    vehicle()
