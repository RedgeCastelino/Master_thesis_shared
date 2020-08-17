
function [rXnew,rYnew,vnew,axnew,aynew,Psinew]= Vehicle(rXtraj, rYtraj, vTraj, PsiTraj, tTraj, rX, rY, Psi, v, ax, ay)
    %% Input

%     m=200;
% % 
%     rXtraj=linspace(0,1,m);    % Trajectory x-points                 ((1xm) vector)
%     rYtraj=linspace(0,0,m);    % Trajectory y-points                 ((1xm) vector)
%     PsiTraj=linspace(0,0,m);   % Trajectory yaw angle                ((1xm) vector)
%     tTraj=linspace(0,2,m);  % Trajectory time_stamp               ((1xm) vector)
%     vel=rXtraj(1,m)*tTraj(1,m);
%     vTraj=linspace(vel,vel,m);     % Trajectory velocity                 ((1xm) vector)
% 
%     rX=0;        % current x-point of EGO              ((1x1) scalar)
%     rY=0;        % current y-point of EGO              ((1x1) scalar)
%     Psi=0;       % current yaw angle of EGO            ((1x1) scalar)
%     v=vel;         % current velocity of EGO             ((1x1) scalar)
%     ax=0;        % current acceleration in x of EGO    ((1x1) scalar)
%     ay=0;        % current acceleration in y of EGO    ((1x1) scalar)
%     t=0;         % current time                        ((1x1) scalar)
%     n=1;         % current loop index                  ((1x1) scalar)



    %% MEX Function

    [rXnew,rYnew,vnew,axnew,aynew,Psinew] = AMS_Simulation_Model_2_mex(rXtraj, rYtraj, vTraj, PsiTraj, tTraj, rX, rY, Psi, v, ax, ay);


    %% Output:

    % rXnew   :             Updated x-point of EGO                             ( (1x1) scalar)
    % rYnew   :             Updated y-point of EGO                             ( (1x1) scalar)
    % vnew     :             Updated velocity of EGO                            ( (1x1) scalar)
    % axnew  :             Updated accel in x of EGO                         ( (1x1) scalar)
    % aynew  :             Updated accel in y of EGO                         ( (1x1) scalar)
    % Psinew  :             Updated yaw angle of EGO                       ( (1x1) scalar)
end
