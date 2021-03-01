#!/usr/bin/env python
import numpy as np
import rospy
import math
import message_filters
import matplotlib.pyplot as plt
import tf
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

    rospy.init_node('sensor_model_ideal', anonymous=False)  # Start node

    # Subscriber the data in callback function
    ego_data = message_filters.Subscriber("/ego_data", TrafficUpdateMovingObject)
    osi_objs = message_filters.Subscriber("/osi3_moving_obj", GroundTruthMovingObjects)
    #ts = message_filters.ApproximateTimeSynchronizer([ego_data, osi_objs], 10, 0.1)
    ts = message_filters.TimeSynchronizer([ego_data, osi_objs], 3)
    ts.registerCallback(callback)

    rospy.spin()  # spin() simply keeps python from exiting until this node is stopped


def callback(ego,osi_objs):
    tic = rospy.Time.now()
    global ntime
    global otime

    fixed = tf.TransformBroadcaster()
    fixed.sendTransform((0,0,0),tf.transformations.quaternion_from_euler(0, 0, 1),rospy.Time.now(),"ego","map")





    #
    [osi_objs_noego] = find_ego(osi_objs)

    #else :
     #   ego = ego_dataCOPY
    # copy the time from received osi GT message
    header = osi_objs.header
    ntime = float(osi_objs.header.stamp.secs) + float(osi_objs.header.stamp.nsecs)/1000000000

    # Return object list with objects inside the field of view with position origin on the sensor origin and rotation
    data_process(ego.object,osi_objs_noego,header)
    toc = rospy.Time.now()
    time = toc.to_sec() - tic.to_sec()
    print('sensormodel time', time)
    # Update the time
    otime=ntime

def find_ego (osi_objs):

    # find the smaller id number inside the list
    ID=osi_objs.objects[0].id
    IDpos=0
    for i in range(len(osi_objs.objects)):
        if osi_objs.objects[i].id < ID:   # take into account that the EGO is the first spawn Object
            ID = osi_objs.objects[i].id
            IDpos = i


    # Assign all other ID's to the obj_list

    osi_objs_noego = [x for x in osi_objs.objects if not x.id == ID]


    return [osi_objs_noego]


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
    #Assign Sensor properties to topic
    objs_list.sensor_property.sensor_id = rospy.get_param("sensorID")
    objs_list.sensor_property.sensortype = rospy.get_param("sensortype")
    if rospy.get_param("sensortype") == 0:
        objs_list.sensor_property.posx_variance = float(rospy.get_param("rangerr"))/3
        objs_list.sensor_property.posy_variance = float(rospy.get_param("rangerr"))/3
        objs_list.sensor_property.trust_existance = float(rospy.get_param("trust_existance"))
        objs_list.sensor_property.trust_car = float(rospy.get_param("trust_car"))
        objs_list.sensor_property.trust_truck = float(rospy.get_param("trust_truck"))
        objs_list.sensor_property.trust_motorcycle = float(rospy.get_param("trust_motorcycle"))
        objs_list.sensor_property.trust_bicycle = float(rospy.get_param("trust_bicycle"))
        objs_list.sensor_property.trust_pedestrian = float(rospy.get_param("trust_pedestrian"))
        objs_list.sensor_property.trust_stationary = float(rospy.get_param("trust_stationary"))
        objs_list.sensor_property.trust_other = float(rospy.get_param("trust_other"))
    elif rospy.get_param("sensortype") != 5 :
        objs_list.sensor_property.posx_variance= float(rospy.get_param("posxerr"))/3
        #print(objs_list.sensor_property.posx_variance)
        objs_list.sensor_property.posy_variance = float(rospy.get_param("posyerr"))/3
        objs_list.sensor_property.trust_existance = float(rospy.get_param("trust_existance"))
        objs_list.sensor_property.trust_car = float(rospy.get_param("trust_car"))
        objs_list.sensor_property.trust_truck = float(rospy.get_param("trust_truck"))
        objs_list.sensor_property.trust_motorcycle = float(rospy.get_param("trust_motorcycle"))
        objs_list.sensor_property.trust_bicycle = float(rospy.get_param("trust_bicycle"))
        objs_list.sensor_property.trust_pedestrian = float(rospy.get_param("trust_pedestrian"))
        objs_list.sensor_property.trust_stationary = float(rospy.get_param("trust_stationary"))
        objs_list.sensor_property.trust_other = float(rospy.get_param("trust_other"))

    objs_list.sensor_property.velx_variance = float(rospy.get_param("velerr"))/3
    objs_list.sensor_property.vely_variance = float(rospy.get_param("velerr"))/3

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
        [osi_objs_noego[i].velocity.x, osi_objs_noego[i].velocity.y] = rotate(osi_objs_noego[i].velocity.x,
                                                                              osi_objs_noego[i].velocity.y,
                                                                              -(ego.orientation.yaw + sens.rot.yaw))

        osi_objs_noego[i].velocity.x = osi_objs_noego[i].velocity.x - ego.velocity.x
        osi_objs_noego[i].velocity.y = osi_objs_noego[i].velocity.y - ego.velocity.y

        # Transpose the object acceleration from map to sensor.
        [osi_objs_noego[i].acceleration.x, osi_objs_noego[i].acceleration.y] = rotate(osi_objs_noego[i].acceleration.x,
                                                                                      osi_objs_noego[i].acceleration.y,
                                                                                      -(ego.orientation.yaw + sens.rot.yaw))
        osi_objs_noego[i].acceleration.x = osi_objs_noego[i].acceleration.x - ego.acceleration.x
        osi_objs_noego[i].acceleration.y = osi_objs_noego[i].acceleration.y - ego.acceleration.y


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
            obj_list.dimension.length_variance = 0.2
            obj_list.dimension.width_variance = 0.2

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
                if t == 0 :
                    t = 1/(rospy.get_param('freq'))
                #t = t / 1000000000.0
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

'''
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
'''
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
    y.FL = obj.position.y + hip_wl * math.sin(psi)

    [features.FL, features_check] = evaluate_feature(x.FL, y.FL, sens, features_check)

    x.FR = obj.position.x + hip_wl * math.cos(beta)
    y.FR = obj.position.y + hip_wl * math.sin(beta)

    [features.FR, features_check] = evaluate_feature(x.FR, y.FR, sens, features_check)

    x.RR = obj.position.x - hip_wl * math.cos(-psi)
    y.RR = obj.position.y - hip_wl * math.sin(psi)
    [features.RR, features_check] = evaluate_feature(x.RR, y.RR, sens, features_check)

    x.RL = obj.position.x - hip_wl * math.cos(-beta)
    y.RL = obj.position.y - hip_wl * math.sin(beta)
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

    #if more than two features are availabel
    X = np.asarray( [x.FL, x.FM, x.FR, x.MR, x.RR, x.RM, x.RL, x.ML]) # Vector of x position for the Features
    Y = np.asarray( [y.FL, y.FM, y.FR, y.MR, y.RR, y.RM, y.RL, y.ML]) # Vector of y position for the Features
    FOV_features = np.asarray([features.FL, features.FM, features.FR, features.MR, features.RR, features.RM, features.RL, features.ML])  # Vector of y position for the Features
    hidden_features = evaluate_hidden_features(X,Y)

    features_list = FOV_features*hidden_features


    [features.FL, features.FM, features.FR, features.MR, features.RR, features.RM, features.RL, features.ML] = features_list

    #plt.plot(y.RR, x.RR, 'g^', y.RL, x.RL, 'go', y.FR, x.FR, 'r^', y.FL, x.FL, 'ro', y.FM, x.FM, 'rs', y.ML, x.ML, 'bo', y.MR, x.MR, 'b^',  y.RM, x.RM, 'gs' )
    #plt.show()

    return [features, features_check]

def evaluate_hidden_features(X,Y):
    dist = (X ** 2 + Y ** 2) ** 0.5
    angle = np.arctan(-Y/X)

    ## Eliminate the furtherst and
    furthest_feature = np.argmax(dist)
    hidden_furthest = np.ones(8)
    hidden_furthest[furthest_feature] = 0
    hidden_furthest[last_feature(furthest_feature)] = 0
    hidden_furthest[next_feature(furthest_feature)] = 0

    # Find nearest feature
    nearest_feature1 = np.argmin(dist)
    dist[nearest_feature1]= 999
    nearest_feature2 = np.argmin(dist)

    if nearest_feature1 <= 2 and nearest_feature2 <= 2: ##Front is the main side
        pos_angle1 = 0
        pos_angle2 = 2
    elif 2 <= nearest_feature1 <= 4 and 2 <= nearest_feature2 <= 4: ##Rigth is the main side
        pos_angle1 = 2
        pos_angle2 = 4
    elif 4 <= nearest_feature1 <= 6 and 4 <= nearest_feature2 <= 6: ##Back is the main side
        pos_angle1 = 4
        pos_angle2 = 6
    elif (6 <= nearest_feature1 or nearest_feature1 ==0) and (6 <= nearest_feature2 or nearest_feature2 ==0): ##Left is the main side
        pos_angle1 = 6
        pos_angle2 = 0

    if angle[pos_angle1]>angle[pos_angle2]:
        angle_big = angle[pos_angle1]
        angle_small = angle[pos_angle2]
    else:
        angle_big = angle[pos_angle2]
        angle_small = angle[pos_angle1]

    hidden_angle = np.ones(8)

    for i in range(len(angle)):
        if angle_small <= angle[i] <= angle_big:
            hidden_angle[i] = 0
    hidden_angle[pos_angle1] = 1
    hidden_angle[pos_angle1+1] = 1
    hidden_angle[pos_angle2] = 1

    hidden = hidden_angle * hidden_furthest

    return hidden

def last_feature(x):
    y = x - 1
    if y == -1:
        y = 7
    return y

def next_feature(x):
    y = x + 1
    if y == 8:
        y = 0
    return y

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


'''
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

'''
if __name__ == '__main__':
    sensor_model()

