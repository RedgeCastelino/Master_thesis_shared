import math
import rospy
import numpy as np

class KF:

	def __init__(self):
		self.id = 0
		### for camera first
		if rospy.get_param("sensortype") == 1:
			self.sigma2omegax = rospy.get_param("posxerr") # variance noise posx
			self.sigma2omegay = rospy.get_param("posyerr") #variance noise posy
			self.c_m = np.array([[self.sigma2omegax, 0], [0, self.sigma2omegay]])
			self.sigma2etax = rospy.get_param("processnoise")  # system noise obj  (x-jerk)
			self.sigma2egoetax = rospy.get_param("processnoise") # system noise ego (x-jerk)
			self.sigma2etay = rospy.get_param("processnoise")  # system noise obj(y-jerk)
			self.sigma2egoetay = rospy.get_param("processnoise") # system noise obj (y-jerk)
			self.c_s = np.array([[self.sigma2etax, 0, 0, 0],[0, self.sigma2egoetax, 0, 0],[0, 0, self.sigma2egoetay, 0] ,[0, 0, self.sigma2etay, 0]])
			self.c = np.array([[1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0]])
			self.a = np.zeros((6, 6))
			self.b = np.zeros((6, 4))
			self.xnn = np.array([[0], [0], [0], [0], [0], [0]])  # colomn vector
			self.d = np.array([[ 0, 0, 0, 0], [0, 0, 0, 0]])
			self.xn_nm1 = np.array([[0], [0], [0], [0], [0], [0]])  # column vector

			self.pnn = np.zeros((6, 6))
			np.fill_diagonal(self.pnn, 1)
			self.pn_nm1 = np.zeros((6, 6))
			self.gamma_n = np.zeros((2, 1))
			self.s_n = np.zeros((2, 2))
			self.k_n = np.zeros((6, 2))
			self.yn = np.array([[0], [0]])  # colomn vector
			#self.b = np.array([[0], [0], [0], [0], [0], [0]])
			self.u = np.array([[0], [0],[0],[0]])

			self.g = np.array([[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]])
		elif rospy.get_param("sensortype") == 0:
			self.sigma2omegax = rospy.get_param("rangerr")
			self.sigma2omegay = rospy.get_param("rangerr")  # variance noise posy
			self.sigma2omegavx = rospy.get_param("velerr")
			self.sigma2omegavy = rospy.get_param("velerr")

			self.c_m = np.array([[self.sigma2omegax, 0,0,0], [0, self.sigma2omegay,0,0],[0,0,self.sigma2omegavx,0],[0,0,0,self.sigma2omegavy]])
			self.sigma2etax = rospy.get_param("processnoise")  # system noise (jerk)
			self.sigma2egoetax = rospy.get_param("processnoise")  # system noise (jerk)
			self.sigma2etay = rospy.get_param("processnoise")  # system noise (jerk)
			self.sigma2egoetay = rospy.get_param("processnoise")  # system noise (jerk)
			self.c_s = np.array([[self.sigma2etax, 0, 0, 0], [0, self.sigma2egoetax, 0, 0],
								 [0, 0, self.sigma2egoetay, 0],[0, 0, self.sigma2etay, 0]])
			self.c = np.array([[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0,0,0,1,0,0],[0,0,0,0,1,0]])
			self.d = np.array([[ 0, 0, 0, 0],[ -1, 0, 0, 0],[ 0, 0, 0, 0] ,[0, 0, -1, 0]])
			self.a = np.zeros((6, 6))
			self.b = np.zeros((6, 4))
			self.xnn = np.array([[0], [0], [0], [0], [0], [0]])  # colomn vector

			self.xn_nm1 = np.array([[0], [0], [0], [0], [0], [0]])  # column vector

			self.pnn = np.zeros((6, 6))
			np.fill_diagonal(self.pnn, 1)
			self.pn_nm1 = np.zeros((6, 6))
			self.gamma_n = np.zeros((2, 1))
			self.s_n = np.zeros((2, 2))
			self.k_n = np.zeros((6, 2))
			self.yn = np.array([[0], [0],[0],[0]])  # colomn vector
			self.g = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
			#self.b = np.array([[0], [0], [0], [0], [0], [0]])
			self.u = np.array([[0], [0],[0],[0]])


		self.newtime= 0
		self.oldtime= 0
		self.track= 0

class rotatedata:
	def __init__(self):
		self.posx = 0
		self.posy = 0
		self.velx = 0
		self.vely = 0
		self.accx = 0
		self.accy = 0