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
from rotate import rotate



class boss:
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
        self.breakr = 0



    def associate(self):
        '''method that performs association of objects from sensor list to objects from global track '''
        ''' Output is an Association matrix (vector) that indicates which object of the sensor object list needs to be fused with which object from the global object list'''
        #print('assciate runs')
        self.AssignmentList = []
        global fused_track

        if len(self.globaltrack.obj_list) == 0:
            self.globaltrack = self.sensorslist[0]
            a=0
            for i, obj in enumerate(self.globaltrack.obj_list):

                obj.obj_id = int(a)
                obj.sensors_fused= [self.sensorslist[0].sensor_property.sensor_id]
                a+=1

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

                    #[scenario,globalxf,globalyf,sensorxf,sensoryf,geometric] = feature_select(globalobj, sensorobj)
                    #print('GLOBAL ID',globalobj.obj_id)
                   # print('SENSOR ID',sensorobj.obj_id)
                    #maha_distance,threshold  = StateAssociation(scenario,globalxf,globalyf,sensorxf,sensoryf,globalobj,sensorobj,sigma2omegax,sigma2omegay,geometric)
                    #global_association_state = np.array([[globalobj.geometric.x],[globalobj.geometric.y]])
                    global_association_state = np.array([[globalobj.geometric.x],[globalobj.geometric.vx],[globalobj.geometric.ax],[globalobj.geometric.y],[globalobj.geometric.vy],[globalobj.geometric.ay]])

                    #sensor_association_state = np.array([[sensorobj.geometric.x],[sensorobj.geometric.y]])
                    sensor_association_state = np.array([[sensorobj.geometric.x],[sensorobj.geometric.vx],[sensorobj.geometric.ax],[sensorobj.geometric.y],[sensorobj.geometric.vy],[sensorobj.geometric.ay]])
                    #globalobjcovariance = globalobj.covariance.flatten()
                    #sensorobj.covariance = sensorobj.covariance.flatten()
                    #print(globalobj.covariance)
                    #print(sensorobj.covariance)
                    #global_covariance = np.array ([[globalobj.covariance[0],globalobj.covariance[3]],[globalobj.covariance[18],globalobj.covariance[21]]])
                    #sensor_covariance = np.array([[sensorobj.covariance[0], sensorobj.covariance[3]],
                     #                             [sensorobj.covariance[18], sensorobj.covariance[21]]])
                    global_covariance = np.reshape(globalobj.covariance,(6,6))
                    sensor_covariance = np.reshape(sensorobj.covariance,(6,6))

                    maha_distance,threshold = get_statistical_distance(sensor_association_state , global_association_state , sensor_covariance , global_covariance )
                    #maha_distance = distance.euclidean((globalobj.geometric.x,globalobj.geometric.y),(sensorobj.geometric.x,sensorobj.geometric.y))


                    # Maha distance - mahalanobis distance
                    if maha_distance > threshold:
                        #print('maha',maha_distance,'thresh',threshold)
                        maha_distance = 9999

                    self.AssociationMatrix[i,c] = maha_distance
                    self.ThresholdMatrix[i,c] = threshold
                    self.CostMatrixB[i,i] = threshold
            print('associate matrix')
            #print(np.shape(self.AssociationMatrix))
            print(self.AssociationMatrix)
            sensorobjs,globalobjs = np.shape(self.AssociationMatrix)
            for i in range(sensorobjs):
                for j in range(globalobjs):
                    if self.AssociationMatrix[i,j] == 9999:
                        self.CostMatrixA[i, j] = 0
                    else:
                        self.CostMatrixA[i,j] =  2*self.ThresholdMatrix[i,j] - self.AssociationMatrix[i,j]

            self.CostMatrix = np.concatenate((self.CostMatrixA, self.CostMatrixB), axis=1)
            self.AssignmentMatrix = boss.auction_algorithm(self)[0]
            if self.breakr == 1:
                self.breakr = 0
                continue
            print('ASSISGNE',self.AssignmentMatrix)

        self.globaltrack_predicted = temp_alignment(self.globaltrack, self.egoveh)






def evaluate_time(globaltrack,sensor):

    time_stamp = rospy.Time.now()
    time_elapsed =  float(time_stamp.to_sec())


    for i,obj in enumerate(globaltrack.obj_list):
        ids = [j.obj_id for j in  sensor.obj_list]
        time = time_elapsed - float(obj.time)

        if time > 0.2:
            #print('this happened')
            globaltrack.obj_list.remove(obj)