import math
import rospy
import math

class Fov:
    def __init__(self):
        self.angle = 2 * math.pi  # rad
        self.r = 100  # m

class Pos:
    def __init__(self):
        self.y = 0  # m
        self.x = 0  # m

class Rot:
    def __init__(self):
        self.yaw = 0  # m

class Sens:
    def __init__(self):
        self.fov = Fov()
        self.fov.angle= rospy.get_param("angle") * math.pi/180
        self.fov.r = rospy.get_param("senrange")
        #self.fov.angle= rospy.get_param("angle")
        #self.fov.r = rospy.get_param("senrange")
        self.pos = Pos()
        self.pos.x =  rospy.get_param("posx")
        self.pos.y = rospy.get_param("posy")

        self.rot = Rot()
        self.rot.yaw = rospy.get_param("yaw")

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

        self.vel = Vel()
        self.vel.x =  0
        self.vel.y = 0
        self.acc = Acc()
        self.acc.x =  0
        self.acc.y = 0
        self.neworientation = 0
        self.oldorientation = 0
        self.oldyaw = 0
        self.newyaw = 0
        self.yawrate = 0

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