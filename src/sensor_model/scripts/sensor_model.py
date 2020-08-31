#!/usr/bin/env python
import numpy as np
import rospy
import math
import message_filters
import matplotlib.pyplot as plt

# import all necessary ROS messages
from object_list.msg import ObjectList, ObjectsList
from osi3_bridge.msg import GroundTruthMovingObjects, TrafficUpdateMovingObject

# import function
from rotate import rotate

# import class
from ClassSens import Sens
from ClassSens import Features

c=0
count =0
yawcount=0
classification = {
    # id: Obj_list type   OSI type
    0 : "other",          #unknown
    1 : "other",         #other
    2 : "car",            #car
    3 : "pedestrian",     #pedestrian
    4 : "other",          #animal
    5 : "truck",          #truck
    6 : "other",          #trailer
    7 : "motorcycle",     #motorbike
    8 : "bicycle",        #bicycle
    9 : "truck",          #bus
    10 : "other",         #tram
    11 : "other",         #train
    12 : "other",         #wheelchair
}
counter = 0
def sensor_model():
    # Node initialization
    rospy.init_node('sensor_model_ideal', anonymous=False)  # Start node
    rate = rospy.Rate(rospy.get_param("freq"))  # Define the node frequency 100hz
    rospy.Subscriber("/osi3_moving_obj", GroundTruthMovingObjects, callback)
    rospy.spin()  # spin() simply keeps python from exiting until this node is stopped

def sensor_model_ego():
    rospy.init_node('sensor_model_ideal', anonymous=False)  # Start node
    # Subscriber the data in callback function
    ego_data = message_filters.Subscriber("/ego_data", TrafficUpdateMovingObject)
    osi_objs = message_filters.Subscriber("/osi3_moving_obj", GroundTruthMovingObjects)
    ts = message_filters.ApproximateTimeSynchronizer([ego_data, osi_objs], 10, 10)
    # ts = message_filters.TimeSynchronizer([ego_data, objs_list], 10)
    ts.registerCallback(callback2)
    rospy.spin()  # spin() simply keeps python from exiting until this node is stopped

def callback2(ego_data,osi_objs):
    global ego_dataCOPY
    ego_dataCOPY = ego_data
    callback(osi_objs)


def callback(osi_objs):
    global ntime
    global otime

    # Separate EGO and objects data
    [ego,osi_objs_noego] = find_ego(osi_objs)

    # copy the time from received osi GT message
    header = osi_objs.header
    ntime = osi_objs.header.stamp.nsecs

    # Return object list with objects inside the field of view with position origin on the sensor origin and rotation
    data_process(ego,osi_objs_noego,header)

    # Update the time
    otime=ntime

def find_ego (osi_objs):
    global ego_dataCOPY
    # find the smaller id number inside the list
    ID=osi_objs.objects[0].id
    IDpos=0
    for i in range(len(osi_objs.objects)):
        if osi_objs.objects[i].id < ID:   # take into account that the EGO is the first spawn Object
            ID = osi_objs.objects[i].id
            IDpos = i

    #Assign the object with smaller ID to EGO
    if rospy.get_param("matlab") == 0:
        ego = osi_objs.objects[IDpos]

    else:
        ego = ego_dataCOPY.object
    # Assign all other ID's to the obj_list

    osi_objs_noego = [x for x in osi_objs.objects if not x.id == ID]


    return [ego, osi_objs_noego]


def data_process (ego,osi_objs_noego,header):

    # Import all sensor parameter from Sensor class <-- Parameter are changeable in Ros launch File
    sens = Sens()

    global count    # Counter for iniciating yawrate calculation = 0
    global counter  # Counter for intitiating old osi data
    global osi_old  #
    global ntime
    global otime

    global yawrate

    if counter == 0:
        osi_old = osi_objs_noego
        counter += 1

    if count == 0:
        yawrate = 0

    objs_list = ObjectsList()
    objs_list.header.stamp = header.stamp
    objs_list.header.frame_id = "Sensor"

    for i in range (len(osi_objs_noego)):

        # Rotate and Translate the object position from map to ego
        osi_objs_noego[i].position.x = osi_objs_noego[i].position.x - ego.position.x
        osi_objs_noego[i].position.y = osi_objs_noego[i].position.y - ego.position.y
        [osi_objs_noego[i].position.x, osi_objs_noego[i].position.y] = rotate(osi_objs_noego[i].position.x, osi_objs_noego[i].position.y, -ego.orientation.yaw)

        # Rotate and Translate the object position from ego to sensor
        osi_objs_noego[i].position.x = osi_objs_noego[i].position.x - sens.pos.x
        osi_objs_noego[i].position.y = osi_objs_noego[i].position.y - sens.pos.y
        [osi_objs_noego[i].position.x, osi_objs_noego[i].position.y] = rotate(osi_objs_noego[i].position.x,osi_objs_noego[i].position.y, -sens.rot.yaw)

        # Calculate the object orientation from map to sensor
        osi_objs_noego[i].orientation.yaw -= (ego.orientation.yaw + sens.rot.yaw)

        # Keep the angles are between -pi and pi
        if osi_objs_noego[i].orientation.yaw < -math.pi:
            osi_objs_noego[i].orientation.yaw += 2*math.pi
        elif osi_objs_noego[i].orientation.yaw > math.pi:
            osi_objs_noego[i].orientation.yaw -= 2*math.pi

        # changed to absolute , real sensor should add ego velocity and give overground velocity/objs of objects
        # Rotate and Translate the object velocity from map to sensor (Relative Velocity)
        osi_objs_noego[i].velocity.x = osi_objs_noego[i].velocity.x - ego.velocity.x
        osi_objs_noego[i].velocity.y = osi_objs_noego[i].velocity.y - ego.velocity.y
        [osi_objs_noego[i].velocity.x, osi_objs_noego[i].velocity.y] = rotate(osi_objs_noego[i].velocity.x,osi_objs_noego[i].velocity.y, -(ego.orientation.yaw + sens.rot.yaw))

        # Transpose the object acceleration from map to sensor.
        osi_objs_noego[i].acceleration.x = osi_objs_noego[i].acceleration.x - ego.acceleration.x
        osi_objs_noego[i].acceleration.y = osi_objs_noego[i].acceleration.y - ego.acceleration.y
        [osi_objs_noego[i].acceleration.x, osi_objs_noego[i].acceleration.y] = rotate(osi_objs_noego[i].acceleration.x,osi_objs_noego[i].acceleration.y, -(ego.orientation.yaw + sens.rot.yaw))

        # Calculate features
        [features,features_check] = calculate_features(osi_objs_noego[i],sens)


        # If one of the features is inside the field of view it calculates the error and fullfil the Aeberhard Object List
        if features_check == 1: # Just entities inside FOV

            ## Include statistical errors on
            osi_objs_noego[i] = include_sens_error (osi_objs_noego[i])
            ## Initialize the Object list
            obj_list= ObjectList()

            ## fullfil object list
            obj_list.geometric.x = osi_objs_noego[i].position.x #relative
            obj_list.geometric.y = osi_objs_noego[i].position.y #relative
            obj_list.geometric.vx = osi_objs_noego[i].velocity.x #relative
            obj_list.geometric.vy = osi_objs_noego[i].velocity.y #relative
            obj_list.geometric.ax = osi_objs_noego[i].acceleration.x #relative
            obj_list.geometric.ay = osi_objs_noego[i].acceleration.y #relative
            obj_list.geometric.yaw = osi_objs_noego[i].orientation.yaw #- (ego.orientation.yaw +sens.rot.yaw)

            obj_list.obj_id=osi_objs_noego[i].id

            ## Necessary to include errors
            obj_list.dimension.length = osi_objs_noego[i].dimension.length
            obj_list.dimension.width = osi_objs_noego[i].dimension.width
            obj_list.features = features

            ## Necessary to include errors
            if classification[osi_objs_noego[i].type] == "car":
                obj_list.classification.car = 1
                obj_list.prop_mov = 1
            elif classification[osi_objs_noego[i].type] ==  "truck":
                obj_list.classification.truck = 1
                obj_list.prop_mov = 1
            elif classification[osi_objs_noego[i].type] == "motorcycle":
                obj_list.classification.motorcycle = 1
                obj_list.prop_mov = 1
            elif classification[osi_objs_noego[i].type] == "bicycle":
                obj_list.classification.bicycle = 1
            elif classification[osi_objs_noego[i].type] == "pedestrian":
                obj_list.classification.pedestrian = 1
            elif classification[osi_objs_noego[i].type] == "stacionary":
                obj_list.classification.stacionary = 1
            elif classification[osi_objs_noego[i].type] == "other":
                obj_list.classification.other = 1

            if count != 0:
                t = float(str(ntime)) - float(str(otime))
                t = t / 1000000000.0
                obj_list.geometric.yawrate = (osi_objs_noego[i].orientation.yaw - osi_old[i].orientation.yaw) / t
            else:
                obj_list.geometric.yawrate = 0
            #obj_list.geometric.yaw -= egoyaw
            objs_list.obj_list.append(obj_list)

    count=1

# Publish the object list
    pub = rospy.Publisher("objs_list", ObjectsList, queue_size=10,latch=True)
    pub.publish(objs_list)
    osi_old = osi_objs_noego
    public_ego(ego,header)
    return

def public_ego(ego,header):
    global egoyaw #ego orientation in map frame (dont forget redge and maikol)

    ego_data = TrafficUpdateMovingObject()
    ego_data.header.stamp = header.stamp
    ego_data.header.frame_id = "EGO"

    #ego_data to have ego parameters in ego frame (example velocity of ego  in x and y directions of ego / longitudinal and lateral velocity)
    ego_data.object = ego
    [ego_data.object.velocity.x, ego_data.object.velocity.y] = rotate(ego.velocity.x,ego.velocity.y,-ego.orientation.yaw)
    [ego_data.object.acceleration.x, ego_data.object.acceleration.y] = rotate(ego.acceleration.x,ego.acceleration.y,-ego.orientation.yaw)
    egoyaw= ego.orientation.yaw

    if rospy.get_param("matlab") == 0:
    #print(ego_data)
        pub = rospy.Publisher('ego_data', TrafficUpdateMovingObject, queue_size=10)
        pub.publish(ego_data)



def include_sens_error (new):
    global osi_old

    # FOR CAMERA OR LIDAR
    if rospy.get_param("sensortype") == 1:
       #import standard deviation of errors from parameters
        std_rx = rospy.get_param("posxerr")
        std_ry = rospy.get_param("posyerr")

       # generate erros in posx and posy with normal distribution
        posx_error = np.random.normal(loc=0.0, scale = std_rx )
        posy_error = np.random.normal(loc=0.0, scale = std_ry )

        # add errors to postion
        new.position.x += posx_error
        new.position.y += posy_error
       #set velocity and accln to 0 since camera/lidar does not give velocity or accelration
        new.velocity.x = 0
        new.velocity.y = 0
        new.acceleration.x = 0
        new.acceleration.y = 0


    elif rospy.get_param("sensortype") == 0:
    # FOR RADAR

        x= (new.position.y)/(new.position.x)
        #determine azimuth angle
        azi=np.arctan2(new.position.y,new.position.x)
        range=np.sqrt(np.square(new.position.x)+np.square(new.position.y))
        #import range and azi error from paramters
        std_range = rospy.get_param("rangerr")

        std_azi = rospy.get_param("azierr")

        #add errors with normal distribution
        range_error = np.random.normal(loc=0.0, scale = std_range ) # generates error with normal distribution
        azi_error = np.random.normal(loc=0.0, scale = std_azi ) # generates error with normal distribution
        range += range_error
        azi += azi_error

        #import velocity error from paramters
        std_v=rospy.get_param("velerr")

        vel_err = np.random.normal(loc=0.0, scale = std_v ) # generates error with normal distribution
        # using velocity in x and y direction determin radial velocity
        v = np.sqrt(np.square(new.velocity.x)+np.square(new.velocity.y))
        #add errors to radial velocity
        v += vel_err

        #resolve range and velocity to positions and velocities in x and y direction
        new.position.x = range * np.cos(azi)
        new.position.y = range * np.sin(azi)
        #new.velocity.x = v * np.cos(azi)
        if new.velocity.y < 0:
            new.velocity.y = -abs(v * np.sin(azi))
        else:
            new.velocity.y = abs(v * np.sin(azi))
        if new.velocity.x <0 :
            new.velocity.x = -abs(v * np.cos(azi))
        else :
            new.velocity.x = abs(v * np.cos(azi))
        new.acceleration.x = 0
        new.acceleration.y = 0
    return new



def calculate_features(obj,sens):

    obj_list = ObjectList()
    features = obj_list.features  # import a all features as bool
    x = Features()  # Import a class with all features as float 0.0
    y = Features()
    # Version 1 do not include the verification of the hided features - Just take into account if it is inside the FOV

    # Calculate the features
    features_check = 0

    tg_wl = math.atan(obj.dimension.width / obj.dimension.length)
    hip_wl = 0.5 * math.sqrt(obj.dimension.width ** 2 + obj.dimension.length ** 2)
    beta = obj.orientation.yaw - tg_wl
    psi = obj.orientation.yaw + tg_wl

    x.FL = obj.position.x + hip_wl * math.cos(psi)
    y.FL = obj.position.y - hip_wl * math.sin(psi)

    # x.FL = obj.position.x + obj.dimension.length * math.cos(obj.orientation.yaw) + obj.dimension.width * math.sin(obj.orientation.yaw)
    # y.FL = obj.position.y + obj.dimension.length * math.sin(obj.orientation.yaw) - obj.dimension.width * math.cos(obj.orientation.yaw)
    [features.FL, features_check] = evaluate_feature(x.FL, y.FL, sens, features_check)

    # x.FR = obj.position.x + obj.dimension.length * math.cos(obj.orientation.yaw) - obj.dimension.width * math.sin(obj.orientation.yaw)
    # y.FR = obj.position.y + obj.dimension.length * math.sin(obj.orientation.yaw) + obj.dimension.width * math.cos(obj.orientation.yaw)
    x.FR = obj.position.x + hip_wl * math.cos(beta)
    y.FR = obj.position.y - hip_wl * math.sin(beta)
    [features.FR, features_check] = evaluate_feature(x.FR, y.FR, sens, features_check)

    # x.RR = obj.position.x - obj.dimension.length * math.cos(obj.orientation.yaw) - obj.dimension.width * math.sin(obj.orientation.yaw)
    # y.RR = obj.position.y - obj.dimension.length * math.sin(obj.orientation.yaw) + obj.dimension.width * math.cos(obj.orientation.yaw)
    x.RR = obj.position.x - hip_wl * math.cos(-psi)
    y.RR = obj.position.y - hip_wl * math.sin(-psi)
    [features.RR, features_check] = evaluate_feature(x.RR, y.RR, sens, features_check)

    # x.RL = obj.position.x + obj.dimension.length * math.cos(obj.orientation.yaw) + obj.dimension.width * math.sin(obj.orientation.yaw)
    # y.RL = obj.position.y + obj.dimension.length * math.sin(obj.orientation.yaw) - obj.dimension.width * math.cos(obj.orientation.yaw)
    x.RL = obj.position.x - hip_wl * math.cos(-beta)
    y.RL = obj.position.y - hip_wl * math.sin(-beta)
    [features.RL, features_check] = evaluate_feature(x.RL, y.RL, sens, features_check)

    x.FM = (x.FR + x.FL) / 2
    y.FM = (y.FR + y.FL) / 2
    [features.FM, features_check] = evaluate_feature(x.FM, y.FM, sens, features_check)

    x.ML = (x.RL + x.FL) / 2
    y.ML = (y.RL + y.FL) / 2
    [features.ML, features_check] = evaluate_feature(x.ML, y.ML, sens, features_check)

    x.MR = (x.RR + x.FR) / 2
    y.MR = (y.RR + y.FR) / 2
    [features.MR, features_check] = evaluate_feature(x.MR, y.MR, sens, features_check)

    x.RM = (x.RR + x.RL) / 2
    y.RM = (y.RR + y.RL) / 2
    [features.RM, features_check] = evaluate_feature(x.RM, y.RM, sens, features_check)

    #plt.plot(y.RR, x.RR, 'g^', y.RL, x.RL, 'go', y.FR, x.FR, 'r^', y.FL, x.FL, 'ro', y.FM, x.FM, 'rs', y.ML, x.ML, 'bo', y.MR, x.MR, 'b^',  y.RM, x.RM, 'gs' )
    #plt.show()

    return [features, features_check]


def evaluate_feature (x,y,sens,check):

    # calculates object azimuth
    if x < 0:
        azimuth = math.pi - abs(math.atan(foo(y,x)))
    else:
        azimuth = abs(math.atan(foo(y,x)))

    # check if the object is inside the field of view of the sensor.
    if (math.sqrt(x**2 + y**2) <= sens.fov.r and azimuth <= sens.fov.angle/2):
        feature = 1
        check=1
    else:
        feature = 0

    return [feature,check]

def foo(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 0


if __name__ == '__main__':
    if rospy.get_param("matlab") == 0:
        sensor_model()
    else:
        sensor_model_ego()
