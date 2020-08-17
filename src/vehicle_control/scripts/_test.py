#!/usr/bin/env python
import matlab.engine
import os
import numpy as np
import time

print('Initializing MATLAB')
eng = matlab.engine.start_matlab()
print('MATLAB Initialized')
# Define Matlab path
eng.cd(os.getcwd())
m = 200;

rX = 127.97515106201172;  # current x - point of EGO((1x1) scalar)
rY = 0.0;  # current y - point of EGO((1x1) scalar)
yaw = 0.0;  # current yaw angle of EGO((1x1) scalar)
v = 0.1;  # current velocity of EGO((1x1) scalar)
ax = 0.0;  # current acceleration in x of EGO((1x1) scalar)
ay = 0.0;  # current acceleration in y of EGO((1x1) scalar)
i=1
while True:

    tic= time.time()
    if i< 400:
        vel = 2.0
    else:
        vel = 4.0


    rXtraj=matlab.double(tuple(np.linspace(0, vel*2.0, num=m)))       # Trajectory x-points                 ((1xm) vector)
    rYtraj=matlab.double(tuple(np.linspace(0,0,num=m)))         # Trajectory y-points                 ((1xm) vector)
    PsiTraj=matlab.double(tuple(np.linspace(0,0,num=m)))        # Trajectory yaw angle                ((1xm) vector)
    tTraj=matlab.double(tuple(np.linspace(0,2.0,num=m)))          # Trajectory time_stamp               ((1xm) vector)
    vTraj=matlab.double(tuple(np.linspace(vel,vel,num=m)))      # Trajectory velocity                 ((1xm) vector)


    #t = 0.0;    # current time((1x1) scalar)
    #n = 1.0;    # current loop index((1x1) scalar)
    #print('rXtraj {}, rYtraj {}, vTraj {}, PsiTraj {}, tTraj {}, rX {}, rY {}, yaw {}, v {}'.format(rXtraj, rYtraj, vTraj,
     #                                                                                             PsiTraj, tTraj, rX,
     #                                                                                             rY, yaw, v, ax, ay))

    #print (rYtraj)
    res = eng.Vehicle(rXtraj, rYtraj, vTraj, PsiTraj, tTraj, rX, rY, yaw, v, ax, ay, nargout=6)
    rX = res[0]      # Updated x - point of EGO m - Map Frame
    rY = res[1]      # Updated y - point of EGO m - Map Frame
    yaw = res[5]     # Updated yaw angle of EGO rad

    # Rotate from EGO to Map frame
    v = res[2] # Lateral Velocity = 0   Updated velocity of EGO  m/s - Map Frame
    ax = res[3]
    ay = res[4]
    # rXnew: Updated x - point of EGO((1x1) scalar)
    # rYnew: Updated y - point of EGO((1x1) scalar)
    # vnew:  Updated velocity of EGO((1x1) scalar)
    # axnew: Updated accel in x of EGO((1x1) scalar)
    # aynew: Updated accel in y of EGO((1x1) scalar)
    # Psinew: Updated yaw angle of EGO((1x1) scalar)
    #print(i)
    #print(res)
    toc=time.time()
    print("frequency")
    print(1/(-tic+toc))
    i = i+1

