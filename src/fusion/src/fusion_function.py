# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 09:30:05 2020

@author: Redge
"""

import numpy as np
import rospy
import math
import message_filters
import tf
from object_list.msg import ObjectList, ObjectsList
from osi3_bridge.msg import GroundTruthMovingObjects, TrafficUpdateMovingObject

from scipy.spatial import distance as di
from scipy.stats import chi2
from scipy.linalg import sqrtm
from object_list.msg import ObjectList, ObjectsList
from osi3_bridge.msg import GroundTruthMovingObjects, TrafficUpdateMovingObject

# import function
#import ClassAssociate
#from ObjectAssociation import feature_select


def temp_alignment(track,egoveh):
    "function to perform temporal alignment/prediction of objects_list"
    "Returns objects list with state vector predicted to current time"
    #global now
    now = rospy.Time.now()

    for i, obj in enumerate(track.obj_list):

        t = float(now.to_sec()) - float(obj.time)
        
        if obj.geometric.ax <= 0.5:
            obj.geometric.ax = 0
        if obj.geometric.ay <= 10.5:
            obj.geometric.ay = 0
        yaw = egoveh.yawrate * t
        
        
        state = np.array([[float(obj.geometric.x)], [float(obj.geometric.vx)], [float(obj.geometric.ax)], [float(obj.geometric.y)], [float(obj.geometric.vy)],[float(obj.geometric.ay)]])

        a = np.array([[np.cos(yaw), t * np.cos(yaw), 0 * t * t * np.cos(yaw) / 2, np.sin(yaw), t * np.sin(yaw),
                       0 * t * t * np.sin(yaw) / 2],
                      [0, np.cos(yaw), 0 * t * np.cos(yaw), 0, np.sin(yaw), 0 * t * np.sin(yaw)],
                      [0, 0, np.cos(yaw), 0, 0, np.sin(yaw)],
                      [-np.sin(yaw), -t * np.sin(yaw), 0 * -t * t * np.sin(yaw) / 2, np.cos(yaw), t * np.cos(yaw),
                       0 * t * t * np.cos(yaw) / 2],
                      [0, -np.sin(yaw), -t * np.sin(yaw), 0, np.cos(yaw), t * np.cos(yaw)],
                      [0, 0, -np.sin(yaw), 0, 0, np.cos(yaw)]])
        u = np.array([[egoveh.vel.x], [egoveh.acc.x], [egoveh.vel.y], [egoveh.acc.y]])
        b = np.array(
            [[-t * np.cos(yaw), 0 * -t * t * np.cos(yaw) / 2, -t * np.sin(yaw), 0 * -t * t * np.sin(yaw) / 2],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [t * np.sin(yaw), 0 * t * t * np.sin(yaw), -t * np.cos(yaw), 0 * -t * t * np.cos(yaw)],
             [0, 0, 0, 0],
             [0, 0, 0, 0]])
        g = np.array([[t * t * t * np.cos(yaw) / 6, -t * t * t * np.cos(yaw) / 6, t * t * t * np.sin(yaw) / 6,
                       -t * t * t * np.sin(yaw) / 6], [t * t * np.cos(yaw) / 2, 0, t * t * np.sin(yaw) / 2, 0],
                      [t * np.cos(yaw), 0, t * np.sin(yaw), 0],
                      [-t * t * t * np.sin(yaw) / 6, t * t * t * np.sin(yaw) / 6, -t * t * t * np.cos(yaw) / 6,
                       -t * t * t * np.cos(yaw) / 6], [-t * t * np.sin(yaw) / 2, 0, t * t * np.cos(yaw) / 2, 0],
                      [-t * np.sin(yaw), 0, t * np.cos(yaw), 0]])

        eta_s = np.array([[10],[0],[10] ,[0]])
        id = np.zeros((6, 6))
        np.fill_diagonal(id, rospy.get_param("fusion_process_noise")) # rospy.get_param("Fusion_process_noise")
        covariance = np.reshape(obj.covariance,(6,6))
        predicted_state = a.dot(state) + b.dot(u)
        predicted_covariance = (a.dot(covariance)).dot(a.transpose())+ id #+g.dot(eta_s)#+(g.dot(c_s)).dot(g.transpose()) #
        obj.covariance = predicted_covariance.flatten()
        obj.geometric.x = float(predicted_state[0])
        obj.geometric.vx = float(predicted_state[1])
        obj.geometric.ax = float(predicted_state[2])

        obj.geometric.y = float(predicted_state[3])
        obj.geometric.vy = float(predicted_state[4])
        obj.geometric.ay = float(predicted_state[5])


    return track

def temp_alignment_obj(ob,egoveh,sensor_property,objs_list):
    "function to perform temporal alignment/prediction of single object from objects_list"
    "Returns object with state vector predicted to current time"
    
    #global now
    now = rospy.Time.now()
    obj = ob
    t = float(now.to_sec()) - float(objs_list.header.stamp.to_sec())
 
    if obj.geometric.ax <= 0.5:
        obj.geometric.ax = 0
    if obj.geometric.ay <= 0.5:
        obj.geometric.ay = 0


    yaw = egoveh.newyaw

    state = np.array([[float(obj.geometric.x)], [float(obj.geometric.vx)], [float(obj.geometric.ax)], [float(obj.geometric.y)], [float(obj.geometric.vy)],[float(obj.geometric.ay)]])


    a = np.array([[np.cos(yaw), t * np.cos(yaw), t * t * np.cos(yaw) / 2, np.sin(yaw), t * np.sin(yaw),
                    t * t * np.sin(yaw) / 2],
                  [0, np.cos(yaw),  t * np.cos(yaw), 0, np.sin(yaw),  t * np.sin(yaw)],
                  [0, 0, np.cos(yaw), 0, 0, np.sin(yaw)],
                  [-np.sin(yaw), -t * np.sin(yaw), -t * t * np.sin(yaw) / 2, np.cos(yaw), t * np.cos(yaw),
                    t * t * np.cos(yaw) / 2],
                  [0, -np.sin(yaw), -t * np.sin(yaw), 0, np.cos(yaw), t * np.cos(yaw)],
                  [0, 0, -np.sin(yaw), 0, 0, np.cos(yaw)]])
    u = np.array([[egoveh.vel.x], [egoveh.acc.x], [egoveh.vel.y], [egoveh.acc.y]])

    b = np.array(
        [[-t * np.cos(yaw),  -t * t * np.cos(yaw) / 2, -t * np.sin(yaw),  -t * t * np.sin(yaw) / 2],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [t * np.sin(yaw),  t * t * np.sin(yaw), -t * np.cos(yaw),  -t * t * np.cos(yaw)],
         [0, 0, 0, 0],
         [0, 0, 0, 0]])

    g  = np.array([[t*t*t*np.cos(yaw)/6,-t*t*t*np.cos(yaw)/6,t*t*t*np.sin(yaw)/6,-t*t*t*np.sin(yaw)/6],
                   [t*t*np.cos(yaw)/2,0,t*t*np.sin(yaw)/2,0],
                   [t*np.cos(yaw),0,t*np.sin(yaw),0],
                   [-t*t*t*np.sin(yaw)/6,t*t*t*np.sin(yaw)/6,-t*t*t*np.cos(yaw)/6,-t*t*t*np.cos(yaw)/6],
                   [-t*t*np.sin(yaw)/2,0,t*t*np.cos(yaw)/2,0],
                   [-t*np.sin(yaw),0,t*np.cos(yaw),0]])

    c_s =np.array([[0.1, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0.1, 0] ,[0, 0,  0,0]])

    covariance = np.reshape(obj.covariance,(6,6))
    predicted_state = a.dot(state) + b.dot(u)

    id = np.zeros((6, 6))
    np.fill_diagonal(id, rospy.get_param("fusion_process_noise"))
    predicted_covariance = (a.dot(covariance)).dot(a.transpose()) + id 
    obj.covariance = predicted_covariance.flatten()
    obj.geometric.x = float(predicted_state[0])
    obj.geometric.vx = float(predicted_state[1])
    obj.geometric.ax = float(predicted_state[2])
    obj.geometric.y = float(predicted_state[3])
    obj.geometric.vy = float(predicted_state[4])

    obj.geometric.ay = float(predicted_state[5])

    return(obj)

def information_matrix_fusion(glob_pred_obj,prev_obj_aligned,predict_obj,sensor_id):
    """
    Function to perfrom the Information matrix fusion.

    """
    

    global_state_matrix = np.array([[float(glob_pred_obj.geometric.x)], [float(glob_pred_obj.geometric.vx)],
                                         [float(glob_pred_obj.geometric.ax)], [float(glob_pred_obj.geometric.y)],
                                         [float(glob_pred_obj.geometric.vy)], [float(glob_pred_obj.geometric.ay)]])

    global_cvarience_matrix = np.reshape(glob_pred_obj.covariance, (6, 6)) #+ id

    sensor_state_matrix = np.array([[float(predict_obj.geometric.x)], [float(predict_obj.geometric.vx)],
                                         [float(predict_obj.geometric.ax)],
                                         [float(predict_obj.geometric.y)], [float(predict_obj.geometric.vy)],
                                         [float(predict_obj.geometric.ay)]])
    sensor_covarience_matrix = np.reshape(predict_obj.covariance, (6, 6))

    previous_sensor_state_matrix = np.array(
                                        [[float(prev_obj_aligned.geometric.x)], [float(prev_obj_aligned.geometric.vx)],
                                         [float(prev_obj_aligned.geometric.ax)], [float(prev_obj_aligned.geometric.y)],
                                         [float(prev_obj_aligned.geometric.vy)], [float(prev_obj_aligned.geometric.ay)]])
    previous_sensor_covarience_matrix = np.reshape(prev_obj_aligned.covariance, (6, 6))

    glob_pred_obj_inv = np.linalg.inv(global_cvarience_matrix)

    sensor_covarience_matrix_inv = np.linalg.inv(sensor_covarience_matrix)


    previous_sensor_covarience_matrix_inv = np.linalg.pinv(previous_sensor_covarience_matrix)

    inverse_fused_covarience_matrix = (np.linalg.pinv(global_cvarience_matrix)) + ((np.linalg.pinv(sensor_covarience_matrix)) )#- (previous_sensor_covarience_matrix_inv))
    fused_covarience_matrix = np.linalg.pinv(inverse_fused_covarience_matrix)

    fused_state_matrix = fused_covarience_matrix.dot((glob_pred_obj_inv.dot(global_state_matrix)) + (sensor_covarience_matrix_inv.dot(sensor_state_matrix))-previous_sensor_covarience_matrix_inv.dot(previous_sensor_state_matrix))

    return [fused_state_matrix, fused_covarience_matrix]



def cross_covarience_recurssion_fusion(glob_pred_obj,predict_obj):
    "Function to perform cross covariance recursion fusion on object list "
    
    
    
    global_state_matrix = np.array([[float(glob_pred_obj.geometric.x)], [float(glob_pred_obj.geometric.vx)],
                                   [float(glob_pred_obj.geometric.ax)], [float(glob_pred_obj.geometric.y)],
                                   [float(glob_pred_obj.geometric.vy)], [float(glob_pred_obj.geometric.ay)]])
    global_cvarience_matrix = np.reshape(glob_pred_obj.covariance, (6, 6))

    sensor_state_matrix = np.array([[float(predict_obj.geometric.x)], [float(predict_obj.geometric.vx)],
                                    [float(predict_obj.geometric.ax)],
                                    [float(predict_obj.geometric.y)], [float(predict_obj.geometric.vy)],
                                    [float(predict_obj.geometric.ay)]])
    sensor_covarience_matrix = np.reshape(predict_obj.covariance, (6, 6))

    global_covariance_inv = np.linalg.pinv(global_cvarience_matrix)
    sensor_covariance_inv = np.linalg.pinv(sensor_covarience_matrix)


    inverse_fused_covarience_matrix = global_covariance_inv + sensor_covariance_inv
    fused_covarience_matrix = np.linalg.pinv(inverse_fused_covarience_matrix)

    fused_state_matrix = fused_covarience_matrix.dot(
        (global_covariance_inv.dot(global_state_matrix)) + (sensor_covariance_inv.dot(sensor_state_matrix)))

    
    return [fused_state_matrix, fused_covarience_matrix]

def evaluate_time(globaltrack):
    "Function to perform Object management."
    "Existance is penalized if object not updated for more than 0.5secs " 
    
    "Global object is deleted if object Existance falls below threshold existance" 
    time_stamp = rospy.Time.now()
    time_elapsed =  float(time_stamp.to_sec())


    for i,obj in enumerate(globaltrack.obj_list):

        time = time_elapsed - float(obj.time)
        #print('time',time)

        if time > 0.5:
            obj.prop_existence -= 0.05
            print('lengt',len(globaltrack.obj_list))
            print(obj.prop_existence,time)
        if obj.prop_existence < rospy.get_param("threshold_exist"):

            print('deleting',obj.prop_existence)
            globaltrack.obj_list.remove(obj)


    return(globaltrack)
    
def rotate (x,y,angle):
    "function to perform roatation of coordinate frame"
    rotx = x * math.cos(angle) - y * math.sin(angle)
    roty = x * math.sin(angle) + y * math.cos(angle)

    return [rotx,roty]
