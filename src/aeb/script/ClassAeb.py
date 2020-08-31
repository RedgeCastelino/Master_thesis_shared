import rospy
import numpy as np

## Inicialize the Aeb class
class Acc:
    def __init__(self):
        self.fw= abs(rospy.get_param("fw_acc")) #2.5                ## Deceleration provided by a normal driver [m/s^2]
        self.stage1 = abs(rospy.get_param("stg1_acc")) #2.0             ## Deceleration provided by the first severity stage [m/s^2]
        self.stage2 = abs(rospy.get_param("stg2_acc")) #3.0              ## Deceleration provided by the second severity stage [m/s^2]
        self.stage3 = abs(rospy.get_param("stg3_acc")) #5.0             ## Deceleration provided by the third severity stage [m/s^2]

class React:
    def __init__(self):
        self.driver = rospy.get_param("driver_react") #1.2   ## Reaction time of a normal driver [s]
        self.system = rospy.get_param("aeb_react") #0.5        ## Reaction time of the aeb system [s]  ######## Ask Varun

class Stoptime:
    def __init__(self):
        self.fw = 0.0
        self.stage1 = 0.0
        self.stage2 = 0.0
        self.stage3 = 0.0

class Aeb:
    def __init__(self):
        self.acc = Acc()
        self.react = React()
        self.offset = rospy.get_param("offsetx") #3.7                ## Offset kept as safety between the follower and the leader [m]
        self.ttc = 0.0  ## start as null
        self.stoptime = Stoptime()
        self.des_vel = rospy.get_param("des_vel")/3.6
        self.final_time = rospy.get_param("max_traj_time")
        self.time_step = 1 / rospy.get_param("freq")
        self.amount_data = int(self.final_time / self.time_step)     ## Calculate the amount of data to the trajectory
        self.timesteparray = np.linspace(self.time_step, self.final_time, num=self.amount_data)  ##
        self.x = 0
        self.y = 0
        self.yaw = 0
        self.status = 0
        self.last_status = 0


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




