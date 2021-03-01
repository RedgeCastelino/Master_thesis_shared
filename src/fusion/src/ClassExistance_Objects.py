import numpy as np
import rospy
import math
import message_filters
from scipy.spatial import distance
from scipy.stats import chi2
from scipy.linalg import sqrtm
from object_list.msg import ObjectList, ObjectsList
from osi3_bridge.msg import GroundTruthMovingObjects, TrafficUpdateMovingObject
import sys
# import function
#from rotate import rotate
#from scipy.spatial import distance

class GlobalObject:
    def __init__(self,obj):
        self.object_id = obj.obj_id
        #self.dimension_vector = copy.deepcopy(object.dimension_vector)
        self.existance_probability = obj.prop_existence
        self.persistance_probability = obj.prop_persistance
        #self.classification_vector = copy.deepcopy(object.classification_vector)
        #self.probability_object_moved = copy.deepcopy(object.probability_object_moved)
        #self.feature_vector = copy.deepcopy(object.feature_vector)

        self.mass_existance = None
        self.mass_nonexistance = None
        self.mass_uncertainity = None
        self.list_existance_mass_factor = None
        self.fused_probability_existance = None
        self.fused_probability_nonexistance = None
        self.global_predicted_mass_existance = None
        self.global_predicted_mass_nonexistance = None
        self.global_predicted_mass_uncertainity = None
        self.global_predicted_masslist = None

        self.mass_car = obj.classification_mass[0]
        self.mass_truck = obj.classification_mass[1]
        self.mass_motorcycle = obj.classification_mass[2]
        self.mass_bicycle = obj.classification_mass[3]
        self.mass_pedestrian = obj.classification_mass[4]
        self.mass_stationary = obj.classification_mass[5]
        self.mass_vehicle = obj.classification_mass[6]
        self.mass_vru = obj.classification_mass[7]
        self.mass_traffic = obj.classification_mass[8]
        self.mass_vehicle_stationary = obj.classification_mass[9]
        self.mass_vru_stationary = obj.classification_mass[10]
        self.mass_ignorance = obj.classification_mass[11]
        self.list_classification_mass_factor = obj.classification_mass

    def existance_mass_prediction(self , prediction_weight):
        """
        Method to predict the existence mass factors for existence probability.

        :param prediction_weight: Defined in the fusion configuration.
        """
        global_object_mass_existance = float(self.mass_existance)
        global_object_mass_nonexistance = float(self.mass_nonexistance)
        global_object_mass_uncertainity = float(self.mass_uncertainity)
        prediction_weight = float(prediction_weight)

        self.global_predicted_mass_existance = ((1 - prediction_weight) * global_object_mass_existance)
        self.global_predicted_mass_nonexistance = ((1 - prediction_weight) * global_object_mass_nonexistance)
        self.global_predicted_mass_uncertainity = ((global_object_mass_uncertainity) + (prediction_weight * (global_object_mass_existance + global_object_mass_nonexistance)))
        self.global_predicted_masslist = [self.global_predicted_mass_existance , self.global_predicted_mass_nonexistance , self.global_predicted_mass_uncertainity]


    def set_existance_probability_mass_factors(self, sensor_trust):

        """
        Method to set the new existence probability mass factors after fusion.

        :param sensor:
        """


        self.mass_existance = (self.persistance_probability * float(sensor_trust) * self.existance_probability)
        self.mass_nonexistance = (self.persistance_probability * float(sensor_trust) * (1 - self.existance_probability))
        self.mass_uncertainity = (1 - (float(self.mass_existance) + float(self.mass_nonexistance)))

        self.list_existance_mass_factor = [self.mass_existance, self.mass_nonexistance, self.mass_uncertainity]




class SensorObject:
    def __init__(self,obj,property):
        self.ids = obj.obj_id
        self.sensor_trust = property.trust_existance
        self.existance_probability = obj.prop_existence
        self.persistance_probability = obj.prop_persistance
        self.classification_vector = [obj.classification.car, obj.classification.truck, obj.classification.motorcycle, obj.classification.bicycle, obj.classification.pedestrian, obj.classification.stacionary, obj.classification.other]

        if (np.sqrt(np.square(obj.geometric.vx) + np.square(obj.geometric.vy)) > 0  and np.sqrt(np.square(obj.geometric.vx) + np.square(obj.geometric.vy)) < 1):

            self.probability_object_moved = 0.3
        elif np.sqrt(np.square(obj.geometric.vx) + np.square(obj.geometric.vy)) > 1:
            self.probabiliry_object_moved = 0.6
        else:
            self.probabiliry_object_moved = 0.01

        self.feature_vector = None
        self.sensor = property
        #self.sensor = None

        #self.state_vector_EGOFOR = None
        self.mass_existance = None
        self.mass_nonexistance = None
        self.mass_uncertainity = None
        self.list_existance_mass_factor = None

        self.mass_car = None
        self.mass_truck = None
        self.mass_motorcycle = None
        self.mass_bicycle = None
        self.mass_pedestrian = None
        self.mass_stationary = None
        self.mass_vehicle = None
        self.mass_vru = None
        self.mass_traffic = None
        self.mass_vehicle_stationary = None
        self.mass_vru_stationary = None
        self.mass_ignorance = None
        self.list_classification_mass_factor = None


    def set_existance_probability_mass_factors(self):
        """
        Calculate the exitence probability mass factors for the sensor object using the existence vector.

        """


        self.mass_existance = (float(self.persistance_probability) * float(self.sensor_trust) * float(
            self.existance_probability))
        self.mass_nonexistance = (float(self.persistance_probability) * float(self.sensor_trust) * float(
            (1 - self.existance_probability)))
        self.mass_uncertainity = (1 - (float(self.mass_existance) + float(self.mass_nonexistance)))

        self.list_existance_mass_factor = [self.mass_existance, self.mass_nonexistance, self.mass_uncertainity]

    def set_classification_mass_factors(self):
        """
        Claculate the classification probability mass factors for the sensor object using the classification vector.
        """
        object_probability_car = self.classification_vector[0]
        object_probability_truck = self.classification_vector[1]
        object_probability_motorcycle = self.classification_vector[2]
        object_probability_bicycle = self.classification_vector[3]
        object_probability_pedestrian = self.classification_vector[4]
        object_probability_stationary = self.classification_vector[5]
        object_probability_other = self.classification_vector[6]
        object_moved = 0.5#self.probability_object_moved    #Need to determine

        self.mass_car = float(self.sensor.trust_car) * float(object_probability_car)
        self.mass_truck = float(self.sensor.trust_truck) * float(object_probability_truck)
        self.mass_motorcycle = float(self.sensor.trust_motorcycle) * float(object_probability_motorcycle)
        self.mass_bicycle = float(self.sensor.trust_bicycle) * float(object_probability_bicycle)
        self.mass_pedestrian = float(self.sensor.trust_pedestrian) * float(object_probability_pedestrian)
        self.mass_stationary = float(self.sensor.trust_stationary) * float(object_probability_stationary)

        mass_sum = float(self.mass_car) + float(self.mass_truck) + float(self.mass_motorcycle) + float(self.mass_bicycle) + float(self.mass_pedestrian)

        object_probability_vehicle = (float(self.mass_car) + float(self.mass_truck) + float(self.mass_motorcycle)) / (mass_sum)
        object_probability_vru = (float(self.mass_bicycle) + float(self.mass_pedestrian)) / (mass_sum)

        self.mass_vehicle = (float(object_moved)) * (float(object_probability_vehicle)) * (
                    ((1 - float(self.sensor.trust_car)) * float(object_probability_car)) + (
                        (1 - float(self.sensor.trust_truck)) * float(object_probability_truck)) + (
                                (1 - float(self.sensor.trust_motorcycle)) * float(object_probability_motorcycle)))
        self.mass_vru = (float(object_moved)) * (float(object_probability_vru)) * (
                    ((1 - float(self.sensor.trust_bicycle)) * float(object_probability_bicycle)) + (
                        (1 - float(self.sensor.trust_pedestrian)) * float(object_probability_pedestrian)))
        self.mass_traffic = ((float(object_moved)) * (float(object_probability_vru)) * (
                    ((1 - float(self.sensor.trust_car)) * float(object_probability_car)) + (
                        (1 - float(self.sensor.trust_truck)) * float(object_probability_truck)) + (
                                (1 - float(self.sensor.trust_motorcycle)) * float(object_probability_motorcycle)))) + (
                                        (float(object_moved)) * (float(object_probability_vehicle)) * (
                                            ((1 - float(self.sensor.trust_bicycle)) * float(object_probability_bicycle)) + (
                                                (1 - float(self.sensor.trust_pedestrian)) * float(object_probability_pedestrian))))

        self.mass_vehicle_stationary = (1 - float(object_moved)) * (float(object_probability_vehicle)) * (
                    ((1 - float(self.sensor.trust_car)) * float(object_probability_car)) + (
                        (1 - float(self.sensor.trust_truck)) * float(object_probability_truck)) + (
                                (1 - float(self.sensor.trust_motorcycle)) * float(object_probability_motorcycle)))
        self.mass_vru_stationary = (1 - float(object_moved)) * (float(object_probability_vru)) * (
                    ((1 - float(self.sensor.trust_bicycle)) * float(object_probability_bicycle)) + (
                        (1 - float(self.sensor.trust_pedestrian)) * float(object_probability_pedestrian)))

        self.mass_ignorance = (1 - (
                    self.mass_car + self.mass_truck + self.mass_motorcycle + self.mass_bicycle + self.mass_pedestrian + self.mass_stationary + self.mass_vehicle + self.mass_vru + self.mass_traffic + self.mass_vehicle_stationary + self.mass_vru_stationary))

        self.list_classification_mass_factor = [self.mass_car, self.mass_truck, self.mass_motorcycle, self.mass_bicycle,
                                                self.mass_pedestrian, self.mass_stationary, self.mass_vehicle,
                                                self.mass_vru, self.mass_traffic, self.mass_vehicle_stationary,
                                                self.mass_vru_stationary, self.mass_ignorance]



class ExistanceFusion:
    mass_factor_combination = [['e', 'n', 'e'],
                               ['n', 'ne', 'ne'],
                               ['e', 'ne', 'i']]


    def __init__(self,sensor_object,global_object):
        self.sensor_object = sensor_object # need to determine
        self.global_object = global_object # need to determine


        #self.time_difference = global_object.current_time - global_object.previous_time

        self.fused_mass_factor_existance = None
        self.fused_mass_factor_nonexistance = None
        self.fused_mass_factor_uncertainity = None

        self.fused_probability_existance = None
        self.fused_probability_nonexistance = None

    def existance_fusion_object_assosiated(self):
        """
        Method to perfrom the existence fusion between the sensor object and the global object if the objects are associated.

        :return: Assigns the class object with the fusion results.
        """
        sensor_existance_mass_factors = (self.sensor_object.list_existance_mass_factor) # need to determine
        global_existance_mass_factors = (self.global_object.global_predicted_masslist) # need to determine
        #print('inside fusion', sensor_existance_mass_factors, global_existance_mass_factors)
        #a = sensor_existance_mass_factors
        #b = global_existance_mass_factors
        #c = ExistanceFusion.mass_factor_combination

        self.fused_mass_factor_existance, self.fused_mass_factor_nonexistance, self.fused_mass_factor_uncertainity = self.get_fused_mass_factors()
        print("out of fused mass and in exist fuse associated")
        self.fused_probability_existance = ((self.fused_mass_factor_existance) + ((1 / 2) * (self.fused_mass_factor_uncertainity)))
        self.fused_probability_nonexistance = (1 - (self.fused_probability_existance))

    #def get_fused_mass_factors(sensor_existance_mass_factors, global_existance_mass_factors , mass_factor_combination):
    def get_fused_mass_factors(self):
        """
        Method to perfrom the fused mass factors.

        :param sensor_existance_mass_factors:
        :param global_existance_mass_factors:
        :param mass_factor_combination:

        :return: fused_mass_factor_existance, fused_mass_factor_nonexistance, fused_mass_factor_uncertainity
        """
        sensor_existance_mass_factors = (self.sensor_object.list_existance_mass_factor)  # need to determine
        global_existance_mass_factors = (self.global_object.global_predicted_masslist)  # need to determine
        # print('inside fusion', sensor_existance_mass_factors, global_existance_mass_factors)
        mass_factor_combination = ExistanceFusion.mass_factor_combination
        sum_intersection_existance = 0
        sum_intersection_nonexistance = 0
        sum_intersection_uncertainity = 0
        sum_intersection_null = 0

        for row in range(len(sensor_existance_mass_factors)):
            for column in range(len(global_existance_mass_factors)):
                if mass_factor_combination[row][column] == 'e':
                    sum_intersection_existance = sum_intersection_existance + (
                                sensor_existance_mass_factors[row] * global_existance_mass_factors[column])

                elif mass_factor_combination[row][column] == 'n':
                    sum_intersection_null = sum_intersection_null + (
                                sensor_existance_mass_factors[row] * global_existance_mass_factors[column])

                elif mass_factor_combination[row][column] == 'ne':
                    sum_intersection_nonexistance = sum_intersection_nonexistance + (
                                sensor_existance_mass_factors[row] * global_existance_mass_factors[column])

                elif mass_factor_combination[row][column] == 'i':
                    sum_intersection_uncertainity = sum_intersection_uncertainity + (
                                sensor_existance_mass_factors[row] * global_existance_mass_factors[column])

        print('inside DST combination')
        #print('mass factor combination', mass_factor_combination)
        #print('sum of elements', sum_intersection_existance, sum_intersection_nonexistance,sum_intersection_null,sum_intersection_uncertainity)
        fused_mass_factor_existance = ((sum_intersection_existance) / (1 - (sum_intersection_null)))
        fused_mass_factor_nonexistance = ((sum_intersection_nonexistance) / (1 - (sum_intersection_null)))
        fused_mass_factor_uncertainity = ((sum_intersection_uncertainity) / (1 - (sum_intersection_null)))

        return (fused_mass_factor_existance, fused_mass_factor_nonexistance, fused_mass_factor_uncertainity)

#def assign_Sensor_obj(obj,sensor_trust_probability):
#    sensor_obj = SensorObject()
#    sensor_obj.id = obj.obj_id
#    sensor_obj.existance_probability = obj.prop_existence
#    sensor_obj.persistance_probability =obj.prop_persistance
#    sensor_obj.sensor_trust = sensor_trust_probability

#    return sensor_obj

#def assign_Global_obj(obj):
#    global_obj = GlobalObject()
#    global_obj.global_object_id = obj.obj_id
#    global_obj.existance_probability = obj.prop_existence
#    global_obj.persistance_probability = obj.prop_persistance


#    return global_obj
class ClassificationFusion:
    """
    Class to perform classification fusion between the associated objects.

    Class Attributes:
    mass_factor_combination

    Class Methods:
    __init__
    classification_fusion
    """

    mass_factor_combination = [
        ['car', 'null', 'null', 'null', 'null', 'null', 'car', 'null', 'car', 'car', 'null', 'car'],
        ['null', 'truck', 'null', 'null', 'null', 'null', 'truck', 'null', 'truck', 'truck', 'null', 'truck'],
        ['null', 'null', 'moto', 'null', 'null', 'null', 'moto', 'null', 'moto', 'moto', 'null', 'moto'],
        ['null', 'null', 'null', 'bicycle', 'null', 'null', 'null', 'bicycle', 'bicycle', 'null', 'bicycle', 'bicycle'],
        ['null', 'null', 'null', 'null', 'ped', 'null', 'null', 'ped', 'ped', 'null', 'ped', 'ped'],
        ['null', 'null', 'null', 'null', 'null', 'stat', 'null', 'null', 'null', 'stat', 'stat', 'stat'],
        ['car', 'truck', 'moto', 'null', 'null', 'null', 'veh', 'null', 'veh', 'veh', 'null', 'veh'],
        ['null', 'null', 'null', 'bicycle', 'ped', 'null', 'null', 'vru', 'vru', 'null', 'vru', 'vru'],
        ['car', 'truck', 'moto', 'bicycle', 'ped', 'null', 'veh', 'vru', 'traffic', 'veh', 'vru', 'traffic'],
        ['car', 'truck', 'moto', 'null', 'null', 'stat', 'veh', 'null', 'veh', 'vehstat', 'stat', 'vehstat'],
        ['null', 'null', 'null', 'bicycle', 'ped', 'stat', 'null', 'vru', 'vru', 'stat', 'vrustat', 'vrustat'],
        ['car', 'truck', 'moto', 'bicycle', 'ped', 'stat', 'veh', 'vru', 'traffic', 'vehstat', 'vrustat', 'all']]

    def __init__(self, sensor_object, global_object):
        """
        Class object constructor

        :param sensor_object: Sensor objects involved in the classification fusion
        :param global_object: Global object involved in the classification fusion.
        """
        self.sensor_object = sensor_object
        self.global_object = global_object

        self.fused_mass_factor_car = None
        self.fused_mass_factor_truck = None
        self.fused_mass_factor_motorcycle = None
        self.fused_mass_factor_bicycle = None
        self.fused_mass_factor_pedestrian = None
        self.fused_mass_factor_stationary = None
        self.fused_mass_factor_vehicle = None
        self.fused_mass_factor_vru = None
        self. fused_mass_factor_traffic = None
        self. fused_mass_factor_statvehicle = None
        self.fused_mass_factor_statvru = None
        self. fused_mass_factor_ignorance = None

        self.fused_probability_car = None
        self.fused_probability_truck = None
        self.fused_probability_motorcycle = None
        self.fused_probability_bicycle = None
        self.fused_probability_pedestrian = None
        self.fused_probability_stationary = None
        self.fused_probability_other = None



    def classification_fusion(self):
        """
        Method to perfrom the classification fusion.
        Updates the clssification fusion results in the class object.

        """
        sensor_classification_mass_factors = (self.sensor_object.list_classification_mass_factor)
        global_classification_mass_factors = (self.global_object.list_classification_mass_factor)

        sum_intersection_car = 0
        sum_intersection_truck = 0
        sum_intersection_motorcycle = 0
        sum_intersection_bicycle = 0
        sum_intersection_pedestrian = 0
        sum_intersection_stationary = 0
        sum_intersection_vehicle = 0
        sum_intersection_vru = 0
        sum_intersection_traffic = 0
        sum_intersection_statvehicle = 0
        sum_intersection_statvru = 0
        sum_intersection_null = 0
        sum_intersection_all = 0
        for row in range(len(sensor_classification_mass_factors)):
            for column in range(len(global_classification_mass_factors)):
                if ClassificationFusion.mass_factor_combination[row][column] == 'car':
                    sum_intersection_car = sum_intersection_car + (
                                sensor_classification_mass_factors[row] * global_classification_mass_factors[column])

                elif ClassificationFusion.mass_factor_combination[row][column] == 'truck':
                    sum_intersection_truck = sum_intersection_truck + (
                                sensor_classification_mass_factors[row] * global_classification_mass_factors[column])

                elif ClassificationFusion.mass_factor_combination[row][column] == 'moto':
                    sum_intersection_motorcycle = sum_intersection_motorcycle + (
                                sensor_classification_mass_factors[row] * global_classification_mass_factors[column])

                elif ClassificationFusion.mass_factor_combination[row][column] == 'bicycle':
                    sum_intersection_bicycle = sum_intersection_bicycle + (
                                sensor_classification_mass_factors[row] * global_classification_mass_factors[column])

                elif ClassificationFusion.mass_factor_combination[row][column] == 'ped':
                    sum_intersection_pedestrian = sum_intersection_pedestrian + (
                                sensor_classification_mass_factors[row] * global_classification_mass_factors[column])

                elif ClassificationFusion.mass_factor_combination[row][column] == 'stat':
                    sum_intersection_stationary = sum_intersection_stationary + (
                                sensor_classification_mass_factors[row] * global_classification_mass_factors[column])

                elif ClassificationFusion.mass_factor_combination[row][column] == 'veh':
                    sum_intersection_vehicle = sum_intersection_vehicle + (
                                sensor_classification_mass_factors[row] * global_classification_mass_factors[column])

                elif ClassificationFusion.mass_factor_combination[row][column] == 'vru':
                    sum_intersection_vru = sum_intersection_vru + (
                                sensor_classification_mass_factors[row] * global_classification_mass_factors[column])

                elif ClassificationFusion.mass_factor_combination[row][column] == 'traffic':
                    sum_intersection_traffic = sum_intersection_traffic + (
                                sensor_classification_mass_factors[row] * global_classification_mass_factors[column])

                elif ClassificationFusion.mass_factor_combination[row][column] == 'vehstat':
                    sum_intersection_statvehicle = sum_intersection_statvehicle + (
                                sensor_classification_mass_factors[row] * global_classification_mass_factors[column])

                elif ClassificationFusion.mass_factor_combination[row][column] == 'vrustat':
                    sum_intersection_statvru = sum_intersection_statvru + (
                                sensor_classification_mass_factors[row] * global_classification_mass_factors[column])

                elif ClassificationFusion.mass_factor_combination[row][column] == 'all':
                    sum_intersection_all = sum_intersection_all + (
                                sensor_classification_mass_factors[row] * global_classification_mass_factors[column])

                elif ClassificationFusion.mass_factor_combination[row][column] == 'null':
                    sum_intersection_null = sum_intersection_null + (
                                sensor_classification_mass_factors[row] * global_classification_mass_factors[column])

        self.fused_mass_factor_car = (sum_intersection_car) / (1 - sum_intersection_null)
        self.fused_mass_factor_truck = (sum_intersection_truck) / (1 - sum_intersection_null)
        self.fused_mass_factor_motorcycle = (sum_intersection_motorcycle) / (1 - sum_intersection_null)
        self.fused_mass_factor_bicycle = (sum_intersection_bicycle) / (1 - sum_intersection_null)
        self.fused_mass_factor_pedestrian = (sum_intersection_pedestrian) / (1 - sum_intersection_null)
        self.fused_mass_factor_stationary = (sum_intersection_stationary) / (1 - sum_intersection_null)
        self.fused_mass_factor_vehicle = (sum_intersection_vehicle) / (1 - sum_intersection_null)
        self.fused_mass_factor_vru = (sum_intersection_vru) / (1 - sum_intersection_null)
        self.fused_mass_factor_traffic = (sum_intersection_traffic) / (1 - sum_intersection_null)
        self.fused_mass_factor_statvehicle = (sum_intersection_statvehicle) / (1 - sum_intersection_null)
        self.fused_mass_factor_statvru = (sum_intersection_statvru) / (1 - sum_intersection_null)
        self.fused_mass_factor_ignorance = (sum_intersection_all) / (1 - sum_intersection_null)

        self.fused_probability_car = (self.fused_mass_factor_car) + ((1 / 3) * self.fused_mass_factor_vehicle) + (
                    (1 / 5) * self.fused_mass_factor_traffic) + ((1 / 4) * self.fused_mass_factor_statvehicle)
        self.fused_probability_truck = (self.fused_mass_factor_truck) + ((1 / 3) * self.fused_mass_factor_vehicle) + (
                    (1 / 5) * self.fused_mass_factor_traffic) + ((1 / 4) * self.fused_mass_factor_statvehicle)
        self.fused_probability_motorcycle = (self.fused_mass_factor_motorcycle) + ((1 / 3) * self.fused_mass_factor_vehicle) + (
                    (1 / 5) * self.fused_mass_factor_traffic) + ((1 / 4) * self.fused_mass_factor_statvehicle)
        self.fused_probability_bicycle = (self.fused_mass_factor_bicycle) + ((1 / 2) * self.fused_mass_factor_vru) + (
                    (1 / 5) * self.fused_mass_factor_traffic) + ((1 / 3) * self.fused_mass_factor_statvru)
        self.fused_probability_pedestrian = (self.fused_mass_factor_pedestrian) + ((1 / 2) * self.fused_mass_factor_vru) + (
                    (1 / 5) * self.fused_mass_factor_traffic) + ((1 / 3) * self.fused_mass_factor_statvru)
        self.fused_probability_stationary = (self.fused_mass_factor_stationary) + (
                    (1 / 3) * self.fused_mass_factor_statvehicle) + ((1 / 3) * self.fused_mass_factor_statvru)
        self.fused_probability_other = 1 - (self.fused_probability_car + self.fused_probability_truck + self.fused_probability_motorcycle + self.fused_probability_bicycle + self.fused_probability_pedestrian + self.fused_probability_stationary)
