% setenv('ROS_MASTER_URI','http://192.168.178.33:11311');
% setenv('ROS_IP','192.168.178.33');

%rosinit('192.168.178.33');

%sub = rossubscriber('/trajectory','trajectory','simulated_vehicle');

%function simulated_vehicle


% came from python, trajectory time, positionx, positiony, velocity and yaw
% came from python ego 
% [ftime, fposx, fposy, fv, fyaw, egox, egoy, ego




% Input:
% rXtraj    :             Trajectory x-points                                       ( (1xm) vector)
% rYtraj    :             Trajectory y-points                                      ( (1xm) vector)
% vTraj     :             Trajectory velocity                                       ( (1xm) vector)
% PsiTraj   :             Trajectory yaw angle                                   ( (1xm) vector)
% tTraj     :             Trajectory time_stamp                              ( (1xm) vector)
% rX           :             current x-point of EGO                               ( (1x1) scalar)
% rY           :             current y-point of EGO                              ( (1x1) scalar)
% Psi         :             current yaw angle of EGO                          ( (1x1) scalar)
% v            :             current velocity of EGO                              ( (1x1) scalar)
% ax          :             current acceleration in x of EGO               ( (1x1) scalar)
% ay          :             current acceleration in y of EGO               ( (1x1) scalar)
% t             :             current time                                                  ( (1x1) scalar)
% n            :             current loop index                                       ( (1x1) scalar)

rXtraj=5;
rYtraj =8;
vTraj=1;
PsiTraj = 5; 
tTraj = 9; 
rX = 0; 
rY = 0;
Psi =0;
v=0;
ax =0;
ay=0;
t =0 
n =1;

[rXnew,rYnew,vnew,axnew,aynew,Psinew] = AMS_Simulation_Model_mex(rXtraj, rYtraj, vTraj, PsiTraj, tTraj, rX, rY, Psi, v, ax, ay, t, n)

% Output:
% rXnew   :             Updated x-point of EGO                             ( (1x1) scalar)
% rYnew   :             Updated y-point of EGO                             ( (1x1) scalar)
% vnew     :             Updated velocity of EGO                            ( (1x1) scalar)
% axnew  :             Updated accel in x of EGO                         ( (1x1) scalar)
% aynew  :             Updated accel in y of EGO                         ( (1x1) scalar)
% Psinew  :             Updated yaw angle of EGO                       ( (1x1) scalar)
 

%end