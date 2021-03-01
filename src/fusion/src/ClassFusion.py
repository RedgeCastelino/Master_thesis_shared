

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

from scipy.spatial import distance
from Association import *
from fusion_function import *
from ClassExistance_Objects import * 

global now
global existance


class fusion:
    def __init__(self):
        self.egoveh = Ego() #consists of updated ego parameters

        self.globaltrack = ObjectsList() #Objects list of fused sensor data/ Global track

        self.globaltrack_predicted= ObjectsList() #global track predicted to current time

        self.sensorslist = []  # list of sensor objectlists
        self.sensorlist_previous = [] # list of sensor objectlists from previous update
        self.sensorslist_predicted = [] # list of sensor objectlists predicted to current time


        self.CostMatrixA = None
        self.CostMatrixB = None
        self.CostMatrix = None
        self.AssociationMatrix = None
        self.ThresholdMatrix = None
        self.AssignmentMatrix = None
        self.AssignmentList = []
        self.tolerance = 1   #tolerance for auction algorithm
        self.breakr = 0 #param to break from auction algorithm if auction algorithm takes too long taking too long
        
    def auction_algorithm(self):
        
        starttime = rospy.get_rostime().to_sec()

        """
        Method to perform auction algorithm for optimal assignment of sensor level objects and global level objects.
        """
        #now = rospy.Time.now()
        cost_matrix = self.CostMatrix
        tolerance = self.tolerance
        dimension_cost_matrix = cost_matrix.shape
        bid_price_list = [0] * dimension_cost_matrix[1]
        assignment_matrix_list = [-9999] * dimension_cost_matrix[0]
        bid_price = np.array([bid_price_list])
        assignment_matrix = np.array([assignment_matrix_list])

        assignment_complete = 0
        print('starting Assignment ')
        while assignment_complete == 0:
            if -9999 in assignment_matrix:
                not_assigned_object_index = np.where(assignment_matrix == -9999)
                sensor_object_index = not_assigned_object_index[1][0]

                sensor_object_benifit = cost_matrix[sensor_object_index] - bid_price
                maximum_value_index = np.argmax(sensor_object_benifit[0])

                if maximum_value_index in assignment_matrix:
                    already_assigned_object_index = np.where(assignment_matrix == maximum_value_index)[1][0]
                    assignment_matrix[0][sensor_object_index] = maximum_value_index
                    assignment_matrix[0][already_assigned_object_index] = -9999

                    first_best = np.partition(sensor_object_benifit[0].flatten(), -2)[-1]
                    second_best = np.partition(sensor_object_benifit[0].flatten(), -2)[-2]
                    object_new_bidprice = (
                                float(bid_price[0][sensor_object_index]) + (float(first_best) - float(second_best)) + float((tolerance)))
                   #print(object_new_bidprice)
                    try:
                        bid_price[0][sensor_object_index] = object_new_bidprice
                    except:
                        bid_price[0][sensor_object_index] =sys.maxsize
                else:
                    assignment_matrix[0][sensor_object_index] = maximum_value_index
                endtime = rospy.get_rostime().to_sec()
                time = endtime - starttime
                if time > 1.5:
                    self.breakr = 1
                    break


            else:
                assignment_complete = 1
        return (assignment_matrix)
    
    def fuse(self):

        self.AssignmentList = []
        
        global now
        now = rospy.Time.now()


        for m,sensor in enumerate(self.sensorslist):
            
            self.AssociationMatrix = np.zeros((len(sensor.obj_list), len(
                self.globaltrack.obj_list)))  # intialize Association matrix (M*N) M - objs in sensor track, N - objs in global track
            self.CostMatrixA = np.zeros((len(sensor.obj_list), len(
                self.globaltrack.obj_list)))  # intialize Cost matrixA (M*N) M - objs in sensor track, N - objs in global track
            self.ThresholdMatrix = np.zeros((len(sensor.obj_list), len(
                self.globaltrack.obj_list)))  # intialize Threshold matrixA (M*N) M - objs in sensor track, N - objs in global track
            threshold = chi2.ppf(0.95, 6)  # select threshold from chi distribution usinf 2 degrees of freedom

            self.CostMatrixB = np.zeros((len(sensor.obj_list), len(sensor.obj_list)))  # intialize Cost matrixB (M*M) M - objs in sensor track
            np.fill_diagonal(self.CostMatrixB, threshold)
            
            for c,globalobj  in enumerate(self.globaltrack.obj_list):
            
                for i, sensorobj in enumerate(sensor.obj_list):

                    [scenario,globalxf,globalyf,sensorxf,sensoryf,geometric] = feature_select(globalobj, sensorobj)

                    global_association_state = np.array([[globalobj.geometric.x],[globalobj.geometric.y]])
                    sensor_association_state = np.array([[sensorobj.geometric.x], [sensorobj.geometric.y]])

                    global_covariance = np.array ([[globalobj.covariance[0],globalobj.covariance[3]],[globalobj.covariance[18],globalobj.covariance[21]]])
                    sensor_covariance = np.array([[sensorobj.covariance[0], sensorobj.covariance[3]],[sensorobj.covariance[18], sensorobj.covariance[21]]])

                    maha_distance,threshold = statistical_distance(sensor_association_state, global_association_state, sensor_covariance, global_covariance)

                    # Maha distance - mahalanobis distance
                    if maha_distance > threshold:
                        
                        maha_distance = 9999

                    self.AssociationMatrix[i,c] = maha_distance
                    self.ThresholdMatrix[i,c] = threshold
                    self.CostMatrixB[i,i] = threshold
            
            sensorobjs,globalobjs = np.shape(self.AssociationMatrix)
            for i in range(sensorobjs):
                for j in range(globalobjs):
                    if self.AssociationMatrix[i,j] == 9999:
                        self.CostMatrixA[i, j] = 0
                    else:
                        self.CostMatrixA[i,j] =  2*self.ThresholdMatrix[i,j] - self.AssociationMatrix[i,j]


            self.CostMatrix = np.concatenate((self.CostMatrixA, self.CostMatrixB), axis=1)
            self.AssignmentMatrix = fusion.auction_algorithm(self)[0]
            if self.breakr == 1:
                self.breakr = 0
                continue
            
            self.AssignmentList.append(self.AssignmentMatrix)
            for l, asign in enumerate(self.AssignmentMatrix):
                try:
                    sensor.obj_list[l].obj_id = self.globaltrack.obj_list[asign].obj_id

                except:

                    sensor.obj_list[l].obj_id = self.globaltrack.obj_list[-1].obj_id +1

        self.globaltrack_predicted = temp_alignment(self.globaltrack, self.egoveh)
        

        self.sensorslist_predicted = self.sensorslist
        
        for m, predicted_sensor in enumerate(self.sensorslist_predicted): # iterate every sensor in sensors list

            
            if len(predicted_sensor.obj_list) == 0:
                continue
            global_ids = [i.obj_id for i in self.globaltrack_predicted.obj_list] # list of global object ids
            try:
                prev_obj_ids = [j.obj_id for j in self.sensorlist_previous[m].obj_list]
            except:
                prev_obj_ids = []
            for n, predict_obj in enumerate(predicted_sensor.obj_list):
                sensor_trust = predicted_sensor.sensor_property.trust_existance #get parameter from launch file
                property = predicted_sensor.sensor_property

                if predict_obj.obj_id in global_ids and  predict_obj.obj_id in prev_obj_ids: 
                    #FUSION IF BOTH GLOBAL AND PREVIOUS SENSOR TRACK HAVE OBJECT ID // SENSOR OBJECT ALREADY EXIST IN GLOBAL TRACK AND PREVIOUS SENSOR TRACK
                    l = global_ids.index(predict_obj.obj_id)
                    glob_pred_obj = self.globaltrack_predicted.obj_list[global_ids.index(predict_obj.obj_id)]
                    prev_obj = self.sensorlist_previous[m].obj_list[prev_obj_ids.index(predict_obj.obj_id)]
                    prev_obj_aligned = temp_alignment_obj(prev_obj, self.egoveh,
                                                          self.sensorlist_previous[m].sensor_property,self.sensorlist_previous[m])

                    Sensor_obj = SensorObject(predict_obj, property)
                    Sensor_obj.set_existance_probability_mass_factors()
                    Sensor_obj.set_classification_mass_factors()


                    Global_obj = GlobalObject(glob_pred_obj)
                    Global_obj.set_existance_probability_mass_factors(sensor_trust)
                    Global_obj.existance_mass_prediction(0.01)



                    existance_fusion = ExistanceFusion(Sensor_obj,Global_obj)
                    existance_fusion.existance_fusion_object_assosiated()
                    #fused_existance = existance_fusion.fused_probability_existance
                    classification_fusion = ClassificationFusion(Sensor_obj,Global_obj)
                    classification_fusion.classification_fusion()


                    # FUSION IF NOT 1ST UPDATE OF THIS PARTICULAR SENSOR IN GLOBAL TRACK
                    if self.sensorlist_previous[m].sensor_property.sensor_id in glob_pred_obj.sensors_fused:





                        [global_state, global_covariance] = information_matrix_fusion(glob_pred_obj,
                                                                                      prev_obj_aligned,
                                                                                      predict_obj,
                                                                                      predicted_sensor.sensor_property.sensor_id)

                    # FUSION IF  1ST UPDATE OF THIS PARTICULAR SENSOR IN GLOBAL TRACK
                    else:
                        [global_state, global_covariance] = cross_covarience_recurssion_fusion(glob_pred_obj, predict_obj)


                    self.globaltrack.obj_list[l].prop_existence = existance_fusion.fused_probability_existance
                    self.globaltrack.obj_list[l].prop_persistance = predict_obj.prop_persistance

                    fused_classification_massfactors_list = [classification_fusion.fused_mass_factor_car,
                                                             classification_fusion.fused_mass_factor_truck,
                                                             classification_fusion.fused_mass_factor_motorcycle,
                                                             classification_fusion.fused_mass_factor_bicycle,
                                                             classification_fusion.fused_mass_factor_pedestrian,
                                                             classification_fusion.fused_mass_factor_stationary,
                                                             classification_fusion.fused_mass_factor_vehicle,
                                                             classification_fusion.fused_mass_factor_vru,
                                                             classification_fusion.fused_mass_factor_traffic,
                                                             classification_fusion.fused_mass_factor_statvehicle,
                                                             classification_fusion.fused_mass_factor_statvru,
                                                             classification_fusion.fused_mass_factor_ignorance]

                    self.globaltrack.obj_list[l].classification_mass = fused_classification_massfactors_list
                    self.globaltrack.obj_list[l].classification.car = classification_fusion.fused_probability_car
                    self.globaltrack.obj_list[l].classification.truck = classification_fusion.fused_probability_truck
                    self.globaltrack.obj_list[l].classification.motorcycle = classification_fusion.fused_probability_motorcycle
                    self.globaltrack.obj_list[l].classification.bicycle= classification_fusion.fused_probability_bicycle
                    self.globaltrack.obj_list[l].classification.pedestrian = classification_fusion.fused_probability_pedestrian
                    self.globaltrack.obj_list[l].classification.stacionary = classification_fusion.fused_probability_stationary
                    self.globaltrack.obj_list[l].classification.car = classification_fusion.fused_probability_car
                    self.globaltrack.obj_list[l].classification.other = classification_fusion.fused_probability_other


                    self.globaltrack.obj_list[l].geometric.x = float(global_state[0])
                    self.globaltrack.obj_list[l].geometric.vx = float(global_state[1])
                    self.globaltrack.obj_list[l].geometric.ax = float(global_state[2])
                    self.globaltrack.obj_list[l].geometric.y = float(global_state[3])
                    self.globaltrack.obj_list[l].geometric.vy = float(global_state[4])
                    self.globaltrack.obj_list[l].geometric.ay = float(global_state[5])
                    self.globaltrack.obj_list[l].covariance = global_covariance.flatten()







                    try:
                        self.globaltrack.obj_list[l].time = predicted_sensor.header.stamp.to_sec()
                    except:
                        self.globaltrack.obj_list[l].time = (rospy.Time.now()).to_sec()
                    latesttime = self.globaltrack.obj_list[l].time
                    
                    #Update sensor id in global track (to check in next iteration)
                    if predicted_sensor.sensor_property.sensor_id not in self.globaltrack.obj_list[l].sensors_fused:
                        self.globaltrack.obj_list[l].sensors_fused.append(predicted_sensor.sensor_property.sensor_id)
                
                
                # FUSION IF OBJECT EXIST IN GLOBAL TRACK BUT NOT IN PREVIOUS SENSOR TRACK if 1st update from sensor
                elif predict_obj.obj_id in global_ids and predict_obj.obj_id not in prev_obj_ids:  
                    print("Update 1st from sensor")

                    l = global_ids.index(predict_obj.obj_id)

                    glob_pred_obj = self.globaltrack_predicted.obj_list[l]

                    [global_state, global_covariance] = cross_covarience_recurssion_fusion(glob_pred_obj,
                                                                                           predict_obj)

                    Sensor_obj = SensorObject(predict_obj, property)
                    Sensor_obj.set_existance_probability_mass_factors()
                    Sensor_obj.set_classification_mass_factors()

                    Global_obj = GlobalObject(glob_pred_obj)
                    Global_obj.set_existance_probability_mass_factors(sensor_trust)
                    Global_obj.existance_mass_prediction(0.01)

                    existance_fusion = ExistanceFusion(Sensor_obj, Global_obj)
                    existance_fusion.existance_fusion_object_assosiated()
                    # fused_existance = existance_fusion.fused_probability_existance
                    classification_fusion = ClassificationFusion(Sensor_obj, Global_obj)
                    classification_fusion.classification_fusion()

                    existance_fusion = ExistanceFusion(Sensor_obj, Global_obj)
                    existance_fusion.existance_fusion_object_assosiated()

                    self.globaltrack.obj_list[l].prop_existence = existance_fusion.fused_probability_existance
                    self.globaltrack.obj_list[l].prop_persistance = predict_obj.prop_persistance

                    fused_classification_massfactors_list = [classification_fusion.fused_mass_factor_car,
                                                             classification_fusion.fused_mass_factor_truck,
                                                             classification_fusion.fused_mass_factor_motorcycle,
                                                             classification_fusion.fused_mass_factor_bicycle,
                                                             classification_fusion.fused_mass_factor_pedestrian,
                                                             classification_fusion.fused_mass_factor_stationary,
                                                             classification_fusion.fused_mass_factor_vehicle,
                                                             classification_fusion.fused_mass_factor_vru,
                                                             classification_fusion.fused_mass_factor_traffic,
                                                             classification_fusion.fused_mass_factor_statvehicle,
                                                             classification_fusion.fused_mass_factor_statvru,
                                                             classification_fusion.fused_mass_factor_ignorance]

                    self.globaltrack.obj_list[l].classification_mass = fused_classification_massfactors_list
                    self.globaltrack.obj_list[l].classification.car = classification_fusion.fused_probability_car
                    self.globaltrack.obj_list[l].classification.truck = classification_fusion.fused_probability_truck
                    self.globaltrack.obj_list[
                        l].classification.motorcycle = classification_fusion.fused_probability_motorcycle
                    self.globaltrack.obj_list[
                        l].classification.bicycle = classification_fusion.fused_probability_bicycle
                    self.globaltrack.obj_list[
                        l].classification.pedestrian = classification_fusion.fused_probability_pedestrian
                    self.globaltrack.obj_list[
                        l].classification.stacionary = classification_fusion.fused_probability_stationary
                    self.globaltrack.obj_list[l].classification.car = classification_fusion.fused_probability_car
                    self.globaltrack.obj_list[l].classification.other = classification_fusion.fused_probability_other


                    self.globaltrack.obj_list[l].geometric.x = float(global_state[0])
                    self.globaltrack.obj_list[l].geometric.vx = float(global_state[1])
                    self.globaltrack.obj_list[l].geometric.ax = float(global_state[2])
                    self.globaltrack.obj_list[l].geometric.y = float(global_state[3])
                    self.globaltrack.obj_list[l].geometric.vy = float(global_state[4])
                    self.globaltrack.obj_list[l].geometric.ay = float(global_state[5])
                    self.globaltrack.obj_list[l].covariance = global_covariance.flatten()
                    try:
                        self.globaltrack.obj_list[l].time = predicted_sensor.header.stamp.to_sec()
                    except:
                        self.globaltrack.obj_list[l].time = (rospy.Time.now()).to_sec()
                    latesttime = self.globaltrack.obj_list[l].time
                    if predicted_sensor.sensor_property.sensor_id not in self.globaltrack.obj_list[l].sensors_fused:
                        self.globaltrack.obj_list[l].sensors_fused.append(predicted_sensor.sensor_property.sensor_id)
                    #print('latesttime is ', latesttime)







                #FUSION IF NEW OBJECT  FROM SENSOR (AS PER ASSOCIATION) 
                elif predict_obj.obj_id not in global_ids: 
                    print("new obj")
                    predict_obj.obj_id = self.globaltrack.obj_list[-1].obj_id +1
                    Sensor_obj = SensorObject(predict_obj, property)
                    Sensor_obj.set_existance_probability_mass_factors()
                    Sensor_obj.set_classification_mass_factors()




                    self.sensorslist[m].obj_list[n].obj_id = predict_obj.obj_id
                    self.globaltrack.obj_list.append(predict_obj)
                    self.globaltrack.obj_list[-1].sensors_fused = []

                    self.globaltrack.obj_list[-1].classification_mass = Sensor_obj.list_classification_mass_factor

                    if predicted_sensor.sensor_property.sensor_id not in self.globaltrack.obj_list[-1].sensors_fused:
                        self.globaltrack.obj_list[-1].sensors_fused.append(predicted_sensor.sensor_property.sensor_id)
                    try:
                        self.globaltrack.obj_list[-1].time = predicted_sensor.header.stamp.to_sec()
                    except:
                        self.globaltrack.obj_list[-1].time =(rospy.Time.now()).to_sec()

        self.globaltrack = evaluate_time(self.globaltrack)
        #self.globaltrack.header.stamp = self.sensorslist[0].header.stamp
        try:
            self.globaltrack.header.stamp = rospy.Time.from_sec(latesttime)
        except:
            self.globaltrack.header.stamp = rospy.Time.now()

        #print('length is ', len(self.globaltrack.obj_list))
        self.sensorlist_previous = self.sensorslist

