

%mySub= rosssubscriber('/sub_topic'); 

%  
% osi3_bridge/TrafficUpdateMovingObject
%% Create global data which will be also used inside the callback

global ego_data;
global pub;
global sub;
global osipub;


%% Start ROS node
setenv('ROS_MASTER_URI','http://10.116.64.27:11311')
rosinit

%rosinit;
%rosinit('10.116.64.27:40595');
%rosnode('Vehicle_Simulation')


%% Start publisher 
[pub,data]=rospublisher('ego_data','osi3_bridge/TrafficUpdateMovingObject');

%% Read, process and publish the first EGO position (from simulated environment)

sub_ego = rossubscriber('osi3_moving_obj','osi3_bridge/GroundTruthMovingObjects');
sub_traj= rossubscriber('/trajectory','vehicle_control/Trajectory');
osipub = rospublisher('/osi3_traffic_update','osi3_bridge/TrafficUpdateMovingObject');
    
pause(1);
gt = sub_ego.LatestMessage;
pause(0.5);
ego_data = find_ego(gt);
send(pub,ego_data);
pause(0.5)
r=rosrate(100); %100Hz
%% subscribe the Trajectory 
    
while 1    
    %sub = rossubscriber('/trajectory','vehicle_control/Trajectory',@callback);
    %sub = rossubscriber('/trajectory','vehicle_control/Trajectory');

    
%t=timer;
%set(t,'executionMode','fixedRate');
%set(t,'TimerFcn',@callback);
%set(t,'Period', 0.08);
%start(t)
    traj = sub_traj.LatestMessage;
    callback(traj,r);
    
end



%function callback(~,traj) %% use with rossubscriber
function callback(traj,r)
%function callback(~,~) %% use with timer
    tic;
    global ego_data;
    global pub;
    global osipub;

    
    %global sub;
    %traj = receive(sub,20)
     %ego_data has velocity in acceleration in ego_osi frame while ego has
     %velocities and accelerations in Map frame
     v = ego_data.Object.Velocity.X;  % current velocity of EGO                      (1x1) scalar

    if v<=0.1
        v=0.1;
    end
    
    timenow=rostime('now');
    timeNow=timenow.Sec+timenow.Nsec*1e-9;
    %timeNow-traj.Reftime
    %[ego_data.Object.Position.X,ego_data.Object.Position.Y,ego_data.Object.Velocity.X,ego_data.Object.Acceleration.X,ego_data.Object.Acceleration.Y,ego_data.Object.Orientation.Yaw] = AMS_Simulation_Model_3_mex(traj.X', traj.Y', traj.V', traj.Yaw', traj.Time', ego_data.Object.Position.X, ego_data.Object.Position.Y, ego_data.Object.Orientation.Yaw, v, ego_data.Object.Acceleration.X, ego_data.Object.Acceleration.Y,timeNow-traj.Reftime);  % run Matlab Funtion    
    [ego_data.Object.Position.X,ego_data.Object.Position.Y,ego_data.Object.Velocity.X,ego_data.Object.Acceleration.X,ego_data.Object.Acceleration.Y,YAW] = AMS_Simulation_Model_2_mex(traj.X', traj.Y', traj.V', traj.Yaw', traj.Time', ego_data.Object.Position.X, ego_data.Object.Position.Y, ego_data.Object.Orientation.Yaw, v, ego_data.Object.Acceleration.X, ego_data.Object.Acceleration.Y);  % run Matlab Funtion
    %res = eng.Vehicle(rXtraj, rYtraj, vTraj, PsiTraj, tTraj, rX, rY, 0.0, v, ax, 0.0, nargout=6)  % run Matlab Funtion
    %res = eng.Vehicle(rXtraj, rYtraj, vTraj, PsiTraj, tTraj, rX, rY, yaw, v, ax, ay, nargout=6)  % run Matlab Funtion

    % Update ego_data with the output of the simulated vehicle
    %ego_data.object.orientation.yaw = YAW;    % Updated yaw angle of EGO rad
    ego_data.Header.Stamp = rostime('now');
    %%% Publish ego_data
    send(pub,ego_data);
    
    %%% Create and publish ego_osi which update the position of the vehicle
    %%% on the Simulation
    ego_osi = ego_data;
    
    % Rotate from EGO to Map frame
    [ego_osi.Object.Velocity.X, ego_osi.Object.Velocity.Y] = rotate(ego_data.Object.Velocity.X,0,0);%-ego_osi.Object.Orientation.Yaw); % Lateral Velocity = 0   Updated velocity of EGO  m/s - Map Frame
    [ego_osi.Object.Acceleration.X, ego_osi.Object.Acceleration.Y] = rotate(ego_data.Object.Acceleration.X,ego_data.Object.Acceleration.Y,0);%-ego_osi.Object.Orientation.Yaw); % Updated accel in y of EGO m/s2 Map Frame
    ego_osi.Header.FrameId="Map";
    waitfor(r);
    send(osipub,ego_osi);
    
    toc
end


function ego_data = find_ego(osi_objs)
    
    %Assign the object with smaller ID to EGO
    ID=osi_objs.Objects(1).Id;
    IDpos=1;
    ego_data = rosmessage('osi3_bridge/TrafficUpdateMovingObject');
    for i = 2:length(osi_objs.Objects)
        if osi_objs.Objects(i).Id < ID   % take into account that the EGO is the first spawn Object
            ID = osi_objs.Objects(i).Id;
            IDpos = i;
        end
    end
    ego_data.Object = osi_objs.Objects(IDpos);
    ego_data.Header.Stamp = rostime("now");
    ego_data.Header.FrameId = "EGO";
    [ego_data.Object.Velocity.X, ego_data.Object.Velocity.Y] = rotate(ego_data.Object.Velocity.X, ego_data.Object.Velocity.Y,ego_data.Object.Orientation.Yaw);
    [ego_data.Object.Acceleration.X, ego_data.Object.Acceleration.Y] = rotate(ego_data.Object.Acceleration.X, ego_data.Object.Acceleration.Y,ego_data.Object.Orientation.Yaw);

end

function [rotx,roty] = rotate (x,y,angle)
    
    rotx = x * cos(angle) - y * sin(angle);
    roty = x * sin(angle) + y * cos(angle);

end

function z = safe_div(x,y)
     try
         z = x/y;
     catch
         z = 0;
     end
end

            

    





