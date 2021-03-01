#!/usr/bin/env python


import sys
import glob
import os


try:
    sys.path.append(glob.glob('/opt/carla-simulator/PythonAPI/carla/dist/carla-0.9.8-py2.7-linux-x86_64.egg')[0])

#    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
#        sys.version_info.major,
#        sys.version_info.minor,
#        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

# ==============================================================================
# -- add PythonAPI for release mode --------------------------------------------
# ==============================================================================
try:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/carla')
except IndexError:
    pass



import carla
import rospy
import numpy as np
import math
import time
from cv_bridge import CvBridge
cv_bridge = CvBridge()

from sensor_msgs.msg import CameraInfo, Image
from osi3_bridge.msg import GroundTruthMovingObjects, TrafficUpdateMovingObject, MovingObject

time.sleep(3) ## Wait the scenario setting


def CARLA_OSI_ROS():

    ## Connect with CARLA server
    #client = carla.Client('localhost', 2000)  ### It starts the communication between server and client
    client = carla.Client('10.116.64.35', 2000)
    client.set_timeout(10.0)  # seconds       ### After 10 seconds without communication with CARLA server the script stops
    world = client.get_world()

    #Start ROS node
    pub = rospy.Publisher('osi3_moving_obj', GroundTruthMovingObjects, queue_size=10)  #
    rospy.init_node('osi3_bridge',anonymous=False)  # Initiate the node camera and anonymous true permit opening this node a lot of time including number in the end of the node name
    rate = rospy.Rate(rospy.get_param("freq") )  # 100 hz
    #rate = rospy.Rate(0.1)  # 100 hz

    cameras = world.get_actors().filter('sensor.camera.rgb')
    cc = carla.ColorConverter.CityScapesPalette
    for camera in cameras:
        #camera.listen(lambda image: image.save_to_disk('/home/drechsler/01.png', cc))
        camera.listen(lambda image: get_data(image))

    def get_data(image):
        camera_data_array = np.ndarray(shape=(image.height, image.width, 4), dtype=np.uint8, buffer=image.raw_data)
        img_msg = cv_bridge.cv2_to_imgmsg(camera_data_array, encoding='bgra8')
        pub = rospy.Publisher('imagetimer', Image, queue_size=10)
        pub.publish(img_msg )


    while not rospy.is_shutdown():
        b = GroundTruthMovingObjects()
        #actor_list = world.get_actors()
        vehicles = world.get_actors().filter('vehicle.*')
        walkers = world.get_actors().filter('walker.*')


        for vehicle in vehicles:
            a = get_OSI(vehicle)
            a.type = get_classification(vehicle.type_id)
            b.objects = np.append(b.objects, a)

        for walker in walkers:
            a = get_OSI(walker)
            a.type = 3  # Pesdestrian
            b.objects = np.append(b.objects, a)

        if b.objects !=[]:

            b.header.stamp = rospy.Time.now()
            b.header.frame_id = "world"
            #rospy.loginfo(b)
            pub.publish(b)
            rate.sleep()

def get_OSI(actor):
    location = actor.get_location()
    velocity = actor.get_velocity()
    acceleration = actor.get_acceleration()
    rotation = actor.get_transform()
    a = MovingObject()
    a.id = actor.id

    a.position.x = location.x
    a.position.y = - location.y
    a.position.z = location.z
    a.velocity.x = velocity.x
    a.velocity.y = - velocity.y
    a.velocity.z = velocity.z
    a.acceleration.x = acceleration.x
    a.acceleration.y = - acceleration.y
    a.acceleration.z = acceleration.z
    a.dimension.length = actor.bounding_box.extent.x * 2
    a.dimension.width = actor.bounding_box.extent.y * 2
    a.dimension.height = actor.bounding_box.extent.z * 2
    a.orientation.pitch = - rotation.rotation.pitch*math.pi/180
    a.orientation.yaw = - rotation.rotation.yaw*math.pi/180
    a.orientation.roll = rotation.rotation.roll*math.pi/180
    return a




def get_classification(name):

    # UNKNOWN = 0  #OTHER = 1 #CAR = 2  #PEDESTRIAN = 3  #ANIMAL = 4
    # TRUCK = 5 #TRAILER = 6  #MOTORBIKE = 7  #BICYCLE = 8  #BUS = 9
    # TRAM = 10  #TRAIN = 11 #WHEELCHAIR = 12
    if ("audi" in name or "bmw" in name or "chevrolet" in name or "citroen" in name or "dodge" in name or "jeep" in name or "lincoln" in name or "mercedes-benz" in name or "mini.cooperst" in name or "mustang" in name or "nissan" in name or "seat" in name or "tesla" in name or "toyota" in name or "volkswagen"in name):
        classi = 2 #car
    elif name ==("vehicle.carlamotors.carlacola"):
        classi = 5 #Truck
    elif ("harley-davidson" in name or "kawasaki" in name or "yamaha" in name):
        classi = 7 #Motorbike
    elif ("crossbike" in name or "diamondback" in name or "gazelle" in name):
        classi = 8 #Bicicle
    else:
        classi = 1 #Other
    return classi

if __name__ == '__main__':
    try:
        CARLA_OSI_ROS()
    except rospy.ROSInterruptException:
        pass

