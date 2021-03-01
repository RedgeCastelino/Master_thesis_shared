# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 09:13:52 2020

@author: Redge
"""

import numpy as np
import rospy
import math

import message_filters
from scipy.spatial import distance as di
from scipy.stats import chi2
from scipy.linalg import sqrtm
from object_list.msg import ObjectList, ObjectsList
from osi3_bridge.msg import GroundTruthMovingObjects, TrafficUpdateMovingObject

import sys
# import function
#from rotate import rotate
from scipy.spatial import distance

class Features:
    def __init__(self):

        self.FL = 0.0
        self.FM = 0.0
        self.FR = 0.0
        self.MR = 0.0
        self.RR = 0.0
        self.RM = 0.0
        self.RL = 0.0
        self.ML = 0.0
class Pos:
    def __init__(self):
        self.y = 0  # m
        self.x = 0  # m

class Vel:
    def __init__(self):
        self.y = 0  # m/s
        self.x = 0  # m/s

class Acc:
    def __init__(self):
        self.y = 0  # m/s^2
        self.x = 0  # m/s^2
class Ego:
    def __init__(self):
        self.pos = Pos()
        self.pos.x = 0
        self.pos.y = 0
        self.vel = Vel()
        self.vel.x = 0
        self.vel.y = 0
        self.acc = Acc()
        self.acc.x = 0
        self.acc.y = 0
        self.neworientation = 0
        self.oldorientation = 0
        self.oldyaw = 0
        self.newyaw = 0
        self.yawrate = 0
        self.testyaw = 0
        self.testyawrate = 0
        self.t = 0

def feature_select(global_obj, sensor_obj):

    #glob_feat_x,glob_feat_y = calculate_x_y(global_obj)
    #sens_feat_x,sens_feat_y = calculate_x_y(sensor_obj)

    glob_feat_x, glob_feat_y = calculate_features(global_obj)
    sens_feat_x, sens_feat_y = calculate_features(sensor_obj)

    #scenario: 1 for common corner,2 for common side feature, 3 for features on common side, features unrelated
    if global_obj.features.FL == 1 and sensor_obj.features.FL == 1:
        scenario = 1
        globalxf = glob_feat_x.FL
        globalyf = glob_feat_y.FL
        sensorxf = sens_feat_x.FL
        sensoryf = sens_feat_y.FL
        geometric = [0,0]
    elif global_obj.features.FR == 1 and sensor_obj.features.FR == 1:
        scenario = 1
        globalxf = glob_feat_x.FR
        globalyf = glob_feat_y.FR
        sensorxf = sens_feat_x.FR
        sensoryf = sens_feat_y.FR
        geometric = [0,0]
    elif global_obj.features.RL == 1 and sensor_obj.features.RL == 1:
        scenario = 1
        globalxf = glob_feat_x.RL
        globalyf = glob_feat_y.RL
        sensorxf = sens_feat_x.RL
        sensoryf = sens_feat_y.RL
        geometric = [0,0]
    elif global_obj.features.RR == 1 and sensor_obj.features.RR == 1:
        scenario = 1
        globalxf = glob_feat_x.RR
        globalyf = glob_feat_y.RR
        sensorxf = sens_feat_x.RR
        sensoryf = sens_feat_y.RR
        geometric = [0,0]
    elif global_obj.features.FM == 1 and sensor_obj.features.FM == 1:
        scenario = 2
        if abs(global_obj.dimension.width - global_obj.dimension.width) <  (np.sqrt(global_obj.dimension.width_variance) + np.sqrt(sensor_obj.dimension.width_variance)):
            globalxf = glob_feat_x.FM
            globalyf = glob_feat_y.FM
            sensorxf = sens_feat_x.FM
            sensoryf = sens_feat_y.FM
            geometric = [0,0]

        else :
            globalxf = glob_feat_x.FM
            globalyf = glob_feat_y.FM
            sensorxf = sens_feat_x.FM
            sensoryf = sens_feat_y.FM
            geometric = [0,1]

    elif global_obj.features.RM == 1 and sensor_obj.features.RM == 1:
        scenario = 2
        if abs(global_obj.dimension.width - sensor_obj.dimension.width) < (
                np.sqrt(global_obj.dimension.width_variance) + np.sqrt(sensor_obj.dimension.width_variance)):
            globalxf = glob_feat_x.RM
            globalyf = glob_feat_y.RM
            sensorxf = sens_feat_x.RM
            sensoryf = sens_feat_y.RM
            geometric = [0, 0]

        else:
            globalxf = glob_feat_x.RM
            globalyf = glob_feat_y.RM
            sensorxf = sens_feat_x.RM
            sensoryf = sens_feat_y.RM
            geometric = [0,1]

    elif global_obj.features.ML == 1 and sensor_obj.features.ML == 1:
        scenario = 2
        if abs(global_obj.dimension.length - sensor_obj.dimension.length) < (
                np.sqrt(global_obj.dimension.length_variance) + np.sqrt(sensor_obj.dimension.length_variance)):
            globalxf = glob_feat_x.ML
            globalyf = glob_feat_y.ML
            sensorxf = sens_feat_x.ML
            sensoryf = sens_feat_y.ML
            geometric = [1,0]

        else:
            globalxf = glob_feat_x.ML
            globalyf = glob_feat_y.ML
            sensorxf = sens_feat_x.ML
            sensoryf = sens_feat_y.ML
            geometric = [1,0]
    elif global_obj.features.MR == 1 and sensor_obj.features.MR == 1:
        scenario = 2
        if abs(global_obj.dimension.length - sensor_obj.dimension.length) < (
                np.sqrt(global_obj.dimension.length_variance) + np.sqrt(sensor_obj.dimension.length_variance)):
            globalxf = glob_feat_x.MR
            globalyf = glob_feat_y.MR
            sensorxf = sens_feat_x.MR
            sensoryf = sens_feat_y.MR
            geometric = [0, 1]

        else:
            globalxf = glob_feat_x.MR
            globalyf = glob_feat_y.MR
            sensorxf = sens_feat_x.MR
            sensoryf = sens_feat_y.MR
            geometric = [0, 1]
    elif global_obj.features.FL == 1 and sensor_obj.features.FR == 1:
        scenario = 3
        globalxf = glob_feat_x.FL
        globalyf = glob_feat_y.FL
        sensorxf = sens_feat_x.FR
        sensoryf = sens_feat_y.FR
        geometric = [0, 1] # delete y elements since only x is common
    elif global_obj.features.FL == 1 and sensor_obj.features.RL == 1:
        scenario = 3
        globalxf = glob_feat_x.FL
        globalyf = glob_feat_y.FL
        sensorxf = sens_feat_x.RL
        sensoryf = sens_feat_y.RL
        geometric = [1, 0] # delete x elements since only y is common

    elif global_obj.features.FR == 1 and sensor_obj.features.FL == 1:
        scenario = 3
        globalxf = glob_feat_x.FR
        globalyf = glob_feat_y.FR
        sensorxf = sens_feat_x.FL
        sensoryf = sens_feat_y.FL
        geometric = [0,1] # delete y elements since only x is common
    elif global_obj.features.FR == 1 and sensor_obj.features.RR == 1:
        scenario = 3
        globalxf = glob_feat_x.FR
        globalyf = glob_feat_y.FR
        sensorxf = sens_feat_x.RR
        sensoryf = sens_feat_y.RR
        geometric = [1, 0] # delete x elements since only y is common
    elif global_obj.features.RR == 1 and sensor_obj.features.FR == 1:
        scenario = 3
        globalxf = glob_feat_x.RR
        globalyf = glob_feat_y.RR
        sensorxf = sens_feat_x.RR
        sensoryf = sens_feat_x.RR
        geometric = [1, 0]  # delete x elements since only y is common
    elif global_obj.features.RR == 1 and sensor_obj.features.RL == 1:
        scenario = 3
        globalxf = glob_feat_x.RR
        globalyf = glob_feat_y.RR
        sensorxf = sens_feat_x.RL
        sensoryf = sens_feat_y.RL
        geometric = [0, 1]  # delete y elements since only x is common
    elif global_obj.features.RL == 1 and sensor_obj.features.RR == 1:
        scenario = 3
        globalxf = glob_feat_x.RL
        globalyf = glob_feat_y.RL
        sensorxf = sens_feat_x.RR
        sensoryf = sens_feat_y.RR
        geometric = [0, 1]  # delete y elements since only x is common
    elif global_obj.features.RL == 1 and sensor_obj.features.FL == 1:
        scenario = 3
        globalxf = glob_feat_x.RL
        globalyf = glob_feat_y.RL
        sensorxf = sens_feat_x.FL
        sensoryf = sens_feat_y.FL
        geometric = [1, 0]  # delete x elements since only y is common
    else:
        scenario = 4
        #return all feature coordinates
        globalxf =  glob_feat_x
        globalyf = glob_feat_y
        sensorxf = sens_feat_x
        sensoryf = sens_feat_y
        geometric = [0, 0]

    return [scenario,globalxf,globalyf,sensorxf,sensoryf,geometric]

def calculate_features(obj):

    obj_list = ObjectList()
    features = obj_list.features  # import a all features as bool
    x = Features()  # Import a class with all features as float 0.0
    y = Features()
    # Version 1 do not include the verification of the hided features - Just take into account if it is inside the FOV

    # Calculate the features
    features_check = 0

    tg_wl = math.atan(obj.dimension.width / obj.dimension.length)
    hip_wl = 0.5 * math.sqrt(obj.dimension.width ** 2 + obj.dimension.length ** 2)
    beta = obj.geometric.yaw - tg_wl
    psi = obj.geometric.yaw + tg_wl

    x.FL = obj.geometric.x + hip_wl * math.cos(psi)
    y.FL = obj.geometric.y + hip_wl * math.sin(psi)

    #[features.FL, features_check] = evaluate_feature(x.FL, y.FL, sens, features_check)

    x.FR = obj.geometric.x + hip_wl * math.cos(beta)
    y.FR = obj.geometric.y + hip_wl * math.sin(beta)

    #[features.FR, features_check] = evaluate_feature(x.FR, y.FR, sens, features_check)

    x.RR = obj.geometric.x - hip_wl * math.cos(-psi)
    y.RR = obj.geometric.y - hip_wl * math.sin(psi)
   # [features.RR, features_check] = evaluate_feature(x.RR, y.RR, sens, features_check)

    x.RL = obj.geometric.x - hip_wl * math.cos(-beta)
    y.RL = obj.geometric.y - hip_wl * math.sin(beta)
   # [features.RL, features_check] = evaluate_feature(x.RL, y.RL, sens, features_check)

    x.FM = (x.FR + x.FL) / 2
    y.FM = (y.FR + y.FL) / 2
   # [features.FM, features_check] = evaluate_feature(x.FM, y.FM, sens, features_check)

    x.ML = (x.RL + x.FL) / 2
    y.ML = (y.RL + y.FL) / 2
   # [features.ML, features_check] = evaluate_feature(x.ML, y.ML, sens, features_check)

    x.MR = (x.RR + x.FR) / 2
    y.MR = (y.RR + y.FR) / 2
   # [features.MR, features_check] = evaluate_feature(x.MR, y.MR, sens, features_check)

    x.RM = (x.RR + x.RL) / 2
    y.RM = (y.RR + y.RL) / 2
   # [features.RM, features_check] = evaluate_feature(x.RM, y.RM, sens, features_check)

    #if more than two features are availabel
    X = np.asarray( [x.FL, x.FM, x.FR, x.MR, x.RR, x.RM, x.RL, x.ML]) # Vector of x position for the Features
    Y = np.asarray( [y.FL, y.FM, y.FR, y.MR, y.RR, y.RM, y.RL, y.ML]) # Vector of y position for the Features
    #FOV_features = np.asarray([features.FL, features.FM, features.FR, features.MR, features.RR, features.RM, features.RL, features.ML])  # Vector of y position for the Features
    #hidden_features = evaluate_hidden_features(X,Y)

    #features_list = FOV_features*hidden_features


    #[features.FL, features.FM, features.FR, features.MR, features.RR, features.RM, features.RL, features.ML] = features_list

    #plt.plot(y.RR, x.RR, 'g^', y.RL, x.RL, 'go', y.FR, x.FR, 'r^', y.FL, x.FL, 'ro', y.FM, x.FM, 'rs', y.ML, x.ML, 'bo', y.MR, x.MR, 'b^',  y.RM, x.RM, 'gs' )
    #plt.show()

    return x,y

def statistical_distance(sensor_association_state, global_association_state, sensor_covariance, global_covariance):
    """
    Fusion to calculate the statistical distance between the sensor object and global objects NOT based on feature points .
    calculated based on Central coordinates
    (FOR TESTING ONLY)

    """

    C = np.array([[1, 0], [0, 1]])
    c_m = np.array([[0.1, 0], [0, 0.1]])
    innov_cov = (C.dot(sensor_covariance)).dot(C.transpose()) + c_m
    distance = di.mahalanobis(sensor_association_state, global_association_state, innov_cov)
    threshold = chi2.ppf(0.95, len(sensor_association_state))
    return distance,threshold


def get_statistical_distance(scenario, globalxf, globalyf, sensorxf, sensoryf, geometric, sensor_covariance, global_covariance):
    #from scipy.spatial import distance
    """
    Fusion to calculate the statistical distance between the sensor object and global objects based on feature points .

    """

    C = np.array([[1, 0], [0, 1]])
    c_m = np.array([[0.1, 0], [0, 0.1]])
    innov_cov = (C.dot(sensor_covariance)).dot(C.transpose()) + c_m




    if scenario == 1:
        global_association_state = np.array([[globalxf],[globalyf]])
        sensor_association_state = np.array([[sensorxf],[sensoryf]])
        distance = distance.mahalanobis(sensor_association_state, global_association_state, innov_cov) #+ 2 * np.log(
            #np.sqrt(np.linalg.det(innov_cov)))
        threshold = chi2.ppf(0.05, len(sensor_association_state))
    elif scenario == 2:
        if geometric[0] == 0 and geometric[1] == 0:
            global_association_state = np.array([[globalxf], [globalyf]])
            sensor_association_state = np.array([[sensorxf],[sensoryf]])
        elif  geometric[0] == 1:
            global_association_state =  float(globalyf)
            sensor_association_state = float(sensoryf)
            sensor_covariance =sensor_covariance[1,1]
            global_covariance = global_covariance[1,1]
            innov_cov = sensor_covariance + 0.1
        elif geometric[1] == 1:
            global_association_state = float(globalxf)
            sensor_association_state = float(sensorxf)
            sensor_covariance = sensor_covariance[0, 0]
            global_covariance = global_covariance[0, 0]
            innov_cov = sensor_covariance + 0.1
        distance = distance.mahalanobis(sensor_association_state, global_association_state, innov_cov)# + 2 * np.log(
            #np.sqrt(np.linalg.det(innov_cov)))
        try:
            threshold = chi2.ppf(0.95, len(sensor_association_state))
        except:
            threshold = chi2.ppf(0.95, 2)
    elif scenario == 3:
        if geometric[0] == 1:
            global_association_state = float(globalyf)
            sensor_association_state = float(sensoryf)
            sensor_covariance = sensor_covariance[1, 1]
            global_covariance = global_covariance[1, 1]
            innov_cov = sensor_covariance + 0.1
        elif geometric[1] == 1:
            global_association_state = float(globalxf)
            sensor_association_state = float(sensorxf)
            sensor_covariance = sensor_covariance[0, 0]
            global_covariance = global_covariance[0, 0]
            innov_cov = sensor_covariance + 0.1
        distance = distance.mahalanobis(sensor_association_state, global_association_state, innov_cov) #+ 2 * np.log(np.sqrt(innov_cov))

        try:
            threshold = chi2.ppf(0.95, len(sensor_association_state))
        except:
            threshold = chi2.ppf(0.95, 1)
    else:
        #globalx = [globalxf.FL, globalxf.FM, globalxf.FR, globalxf.MR, globalxf.RR, globalxf.RM, globalxf.RL,globalxf.ML]  # Vector of x position for the Features / List of objects y(features)
        globalx = [globalxf.FL, globalxf.FM, globalxf.FR, globalxf.MR, globalxf.RR, globalxf.RM, globalxf.RL,globalxf.ML]  # Vector of x position for the Features / List of objects y(features)
        globaly = [globalyf.FL, globalyf.FM, globalyf.FR, globalyf.MR, globalyf.RR, globalyf.RM, globalyf.RL, globalyf.ML]  # Vector of y position for the Features

        sensorx = [sensorxf.FL, sensorxf.FM, sensorxf.FR, sensorxf.MR, sensorxf.RR, sensorxf.RM, sensorxf.RL,
                   sensorxf.ML]  # Vector of x position for the Features / List of objects y(features)
        sensory = [sensoryf.FL, sensoryf.FM, sensoryf.FR, sensoryf.MR, sensoryf.RR, sensoryf.RM, sensoryf.RL,
                   sensoryf.ML]
        distance = 9999999
        for i in range(len(globalx)):
            global_association_state = np.array([[globalx[i]], [globaly[i]]])
            sensor_association_state = np.array([[sensorx[i]], [sensory[i]]])
            innov_cov = (C.dot(sensor_covariance)).dot(C.transpose()) + c_m

            d = distance.mahalanobis(sensor_association_state, global_association_state, innov_cov) #+ 2 * np.log(
                #np.sqrt(np.linalg.det(innov_cov)))
            if d < distance:
                distance = d
                threshold = chi2.ppf(0.95, len(sensor_association_state))
    return(distance, threshold)
