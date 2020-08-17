import math
import rospy
import numpy as np
### for camera first
class KF:

	def __init__(self):
		self.id = 0
		self.sigma2omegax = 0.000001  # variance noise posx
		self.sigma2omegay = 0.00000001  # variance noise posy
		self.c_m = np.array([[self.sigma2omegax, 0],[0,self.sigma2omegay]])
		self.sigma2etax=0.00001 #system noise (jerk)
		self.sigma2etay=0.00001 #system noise (jerk)
		self.c_s = np.array([[self.sigma2etax, 0],[0,self.sigma2etay]])
		self.c = np.array([[1,0,0,0,0,0],[0,0,0,1,0,0]])
		self.a = np.zeros((6,6))
		self.xnn= np.array([[0],[0],[0],[0],[0],[0]]) # colomn vector

		self.xn_nm1= self.xnn #column vector

		self.pnn= np.zeros((6,6))
		np.fill_diagonal(self.pnn,1)
		self.pn_nm1 = np.zeros((6,6))
		self.gamma_n = np.zeros((2,1))
		self.s_n = np.zeros((2,2))
		self.k_n = np.zeros((6,2))
		self.yn = np.array([[0],[0]])# colomn vector

		self.g = np.array([[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]])

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