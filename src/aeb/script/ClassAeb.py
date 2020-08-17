import rospy

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


