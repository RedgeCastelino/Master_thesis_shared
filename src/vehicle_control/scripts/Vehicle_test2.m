
clear all; 
%close all; 
%clc;



m=100;
% % 
%vel = 6;

%Psi=pi()/4;       % current yaw angle of EGO            ((1x1) scalar)
Psi=0.3;
max_time=2;
rtraj=linspace(0,22.22,m);
Xtraj=rtraj*cos(Psi);    % Trajectory x-points                 ((1xm) vector)
Ytraj=rtraj*sin(Psi);    % Trajectory y-points                 ((1xm) vector)

rXtraj=Xtraj;
rYtraj=Ytraj;
PsiTraj=linspace(Psi,Psi,m);   % Trajectory yaw angle                ((1xm) vector)
tTraj=linspace(0,max_time,m);  % Trajectory time_stamp               ((1xm) vector)
time_step=max_time/m
vel=rtraj(1,m)/tTraj(1,m)
vTraj=linspace(vel,vel,m);     % Trajectory velocity                 ((1xm) vector)
% 
rX=0;        % current x-point of EGO              ((1x1) scalar)
rY=0;        % current y-point of EGO              ((1x1) scalar)

v=0.03;         % current velocity of EGO             ((1x1) scalar)
ax=0;        % current acceleration in x of EGO    ((1x1) scalar)
ay=0;        % current acceleration in y of EGO    ((1x1) scalar)
t=0;         % current time                        ((1x1) scalar)
n=1;         % current loop index                  ((1x1) scalar)

i=1;
max=4000;
veccont=linspace(1,max,max)*0.01;  
vecv=linspace(0,0,max);    % Trajectory x-points                 ((1xm) vector)
vecacc=linspace(0,0,max);    % Trajectory y-points                 ((1xm) vector)
vecpos=linspace(0,0,max);   % Trajectory yaw angle                ((1xm) vector)
vecaccy = linspace(0,0,max);
vecx=linspace(0,0,max);   % Trajectory yaw angle                ((1xm) vector)
vecy = linspace(0,0,max);
vec_calc_v=linspace(0,0,max);
vectime=linspace(0,0,max);

    while i<=max
    %% MEX Function
        tic;
        %rX_vec(i)=rX;
        %v_vec(i) = v;
        %ax_vec(i)= ax;
        
        if i >= 2500
            rXtraj=linspace(rX,rX,m);    % Trajectory x-points                 ((1xm) vector)
            rYtraj= linspace(rY,rY,m); 
            vel=0.0;
            vTraj=linspace(vel,vel,m);     % Trajectory velocity                 ((1xm) vector)
        end
            

        [rXnew,rYnew,vnew,axnew,aynew,Psinew] = AMS_Simulation_Model_4_mex(rXtraj, rYtraj, vTraj, PsiTraj, tTraj, rX, rY, Psi, v, ax, ay,tTraj(1));
        
        calc_v = (rXnew-rX)/time_step;
        rX=rXnew;
        rY=rYnew;
        v = vnew;
        ax = axnew;
        ay = aynew; 
        Psi = Psinew;
        
        
        
        if v < 0.01
            v = 0.01;
        end
        %fprintf(' Position x %i Velocity x %i Acceleration x %i \n',rX, v,ax)
        
        vecv(i)=v;
        vecacc(i)=ax;
        vecx(i)=rX;
        vecy(i)=rY;
        vecaccy(i)=ay;
        vec_calc_v(i)=calc_v;
        %pause(0.01)
        
        tTraj=tTraj+time_step;  % Trajectory time_stamp               ((1xm) vector)
        
        rXtraj=rX+Xtraj;
        rYtraj=rY+Ytraj;
        
        
        i=i+1;
        time=toc;
        %time =time_tic-time_toc
        vectime(i)=time;

     end
figure
plot(veccont,vecv,'b',veccont,vecacc,'g',veccont,vecaccy,'r',veccont,vecx,'k')

     %hold on 
     %plot(v_vec)
     %plot(ax_vec)

figure     
plot(vecx,vecy,'bo')

figure
plot(veccont,vecv,'b',veccont,vec_calc_v,'g')

%figure 
%plot(vectime)

        
    %% Output:

    % rXnew   :             Updated x-point of EGO                             ( (1x1) scalar)
    % rYnew   :             Updated y-point of EGO                             ( (1x1) scalar)
    % vnew     :             Updated velocity of EGO                            ( (1x1) scalar)
    % axnew  :             Updated accel in x of EGO                         ( (1x1) scalar)
    % aynew  :             Updated accel in y of EGO                         ( (1x1) scalar)
    % Psinew  :             Updated yaw angle of EGO                       ( (1x1) scalar)
