classdef Trajectory < robotics.ros.Message
    %Trajectory MATLAB implementation of vehicle_control/Trajectory
    %   This class was automatically generated by
    %   robotics.ros.msg.internal.gen.MessageClassGenerator.
    
    %   Copyright 2014-2020 The MathWorks, Inc.
    
    %#ok<*INUSD>
    
    properties (Constant)
        MessageType = 'vehicle_control/Trajectory' % The ROS message type
    end
    
    properties (Constant, Hidden)
        MD5Checksum = '5ae3cb58eb43aac285127e05ab843c41' % The MD5 Checksum of the message definition
    end
    
    properties (Access = protected)
        JavaMessage % The Java message object
    end
    
    properties (Constant, Access = protected)
        StdMsgsHeaderClass = robotics.ros.msg.internal.MessageFactory.getClassForType('std_msgs/Header') % Dispatch to MATLAB class for message type std_msgs/Header
    end
    
    properties (Dependent)
        Header
        Reftime
        Time
        X
        Y
        V
        Yaw
    end
    
    properties (Access = protected)
        Cache = struct('Header', []) % The cache for fast data access
    end
    
    properties (Constant, Hidden)
        PropertyList = {'Header', 'Reftime', 'Time', 'V', 'X', 'Y', 'Yaw'} % List of non-constant message properties
        ROSPropertyList = {'header', 'reftime', 'time', 'v', 'x', 'y', 'yaw'} % List of non-constant ROS message properties
    end
    
    methods
        function obj = Trajectory(msg)
            %Trajectory Construct the message object Trajectory
            import com.mathworks.toolbox.robotics.ros.message.MessageInfo;
            
            % Support default constructor
            if nargin == 0
                obj.JavaMessage = obj.createNewJavaMessage;
                return;
            end
            
            % Construct appropriate empty array
            if isempty(msg)
                obj = obj.empty(0,1);
                return;
            end
            
            % Make scalar construction fast
            if isscalar(msg)
                % Check for correct input class
                if ~MessageInfo.compareTypes(msg(1), obj.MessageType)
                    error(message('robotics:ros:message:NoTypeMatch', obj.MessageType, ...
                        char(MessageInfo.getType(msg(1))) ));
                end
                obj.JavaMessage = msg(1);
                return;
            end
            
            % Check that this is a vector of scalar messages. Since this
            % is an object array, use arrayfun to verify.
            if ~all(arrayfun(@isscalar, msg))
                error(message('robotics:ros:message:MessageArraySizeError'));
            end
            
            % Check that all messages in the array have the correct type
            if ~all(arrayfun(@(x) MessageInfo.compareTypes(x, obj.MessageType), msg))
                error(message('robotics:ros:message:NoTypeMatchArray', obj.MessageType));
            end
            
            % Construct array of objects if necessary
            objType = class(obj);
            for i = 1:length(msg)
                obj(i,1) = feval(objType, msg(i)); %#ok<AGROW>
            end
        end
        
        function header = get.Header(obj)
            %get.Header Get the value for property Header
            if isempty(obj.Cache.Header)
                obj.Cache.Header = feval(obj.StdMsgsHeaderClass, obj.JavaMessage.getHeader);
            end
            header = obj.Cache.Header;
        end
        
        function set.Header(obj, header)
            %set.Header Set the value for property Header
            validateattributes(header, {obj.StdMsgsHeaderClass}, {'nonempty', 'scalar'}, 'Trajectory', 'Header');
            
            obj.JavaMessage.setHeader(header.getJavaObject);
            
            % Update cache if necessary
            if ~isempty(obj.Cache.Header)
                obj.Cache.Header.setJavaObject(header.getJavaObject);
            end
        end
        
        function reftime = get.Reftime(obj)
            %get.Reftime Get the value for property Reftime
            reftime = double(obj.JavaMessage.getReftime);
        end
        
        function set.Reftime(obj, reftime)
            %set.Reftime Set the value for property Reftime
            validateattributes(reftime, {'numeric'}, {'nonempty', 'scalar'}, 'Trajectory', 'Reftime');
            
            obj.JavaMessage.setReftime(reftime);
        end
        
        function time = get.Time(obj)
            %get.Time Get the value for property Time
            javaArray = obj.JavaMessage.getTime;
            array = obj.readJavaArray(javaArray, 'double');
            time = double(array);
        end
        
        function set.Time(obj, time)
            %set.Time Set the value for property Time
            if ~isvector(time) && isempty(time)
                % Allow empty [] input
                time = double.empty(0,1);
            end
            
            validateattributes(time, {'numeric'}, {'vector'}, 'Trajectory', 'Time');
            
            javaArray = obj.JavaMessage.getTime;
            array = obj.writeJavaArray(time, javaArray, 'double');
            obj.JavaMessage.setTime(array);
        end
        
        function x = get.X(obj)
            %get.X Get the value for property X
            javaArray = obj.JavaMessage.getX;
            array = obj.readJavaArray(javaArray, 'double');
            x = double(array);
        end
        
        function set.X(obj, x)
            %set.X Set the value for property X
            if ~isvector(x) && isempty(x)
                % Allow empty [] input
                x = double.empty(0,1);
            end
            
            validateattributes(x, {'numeric'}, {'vector'}, 'Trajectory', 'X');
            
            javaArray = obj.JavaMessage.getX;
            array = obj.writeJavaArray(x, javaArray, 'double');
            obj.JavaMessage.setX(array);
        end
        
        function y = get.Y(obj)
            %get.Y Get the value for property Y
            javaArray = obj.JavaMessage.getY;
            array = obj.readJavaArray(javaArray, 'double');
            y = double(array);
        end
        
        function set.Y(obj, y)
            %set.Y Set the value for property Y
            if ~isvector(y) && isempty(y)
                % Allow empty [] input
                y = double.empty(0,1);
            end
            
            validateattributes(y, {'numeric'}, {'vector'}, 'Trajectory', 'Y');
            
            javaArray = obj.JavaMessage.getY;
            array = obj.writeJavaArray(y, javaArray, 'double');
            obj.JavaMessage.setY(array);
        end
        
        function v = get.V(obj)
            %get.V Get the value for property V
            javaArray = obj.JavaMessage.getV;
            array = obj.readJavaArray(javaArray, 'double');
            v = double(array);
        end
        
        function set.V(obj, v)
            %set.V Set the value for property V
            if ~isvector(v) && isempty(v)
                % Allow empty [] input
                v = double.empty(0,1);
            end
            
            validateattributes(v, {'numeric'}, {'vector'}, 'Trajectory', 'V');
            
            javaArray = obj.JavaMessage.getV;
            array = obj.writeJavaArray(v, javaArray, 'double');
            obj.JavaMessage.setV(array);
        end
        
        function yaw = get.Yaw(obj)
            %get.Yaw Get the value for property Yaw
            javaArray = obj.JavaMessage.getYaw;
            array = obj.readJavaArray(javaArray, 'double');
            yaw = double(array);
        end
        
        function set.Yaw(obj, yaw)
            %set.Yaw Set the value for property Yaw
            if ~isvector(yaw) && isempty(yaw)
                % Allow empty [] input
                yaw = double.empty(0,1);
            end
            
            validateattributes(yaw, {'numeric'}, {'vector'}, 'Trajectory', 'Yaw');
            
            javaArray = obj.JavaMessage.getYaw;
            array = obj.writeJavaArray(yaw, javaArray, 'double');
            obj.JavaMessage.setYaw(array);
        end
    end
    
    methods (Access = protected)
        function resetCache(obj)
            %resetCache Resets any cached properties
            obj.Cache.Header = [];
        end
        
        function cpObj = copyElement(obj)
            %copyElement Implements deep copy behavior for message
            
            % Call default copy method for shallow copy
            cpObj = copyElement@robotics.ros.Message(obj);
            
            % Clear any existing cached properties
            cpObj.resetCache;
            
            % Create a new Java message object
            cpObj.JavaMessage = obj.createNewJavaMessage;
            
            % Iterate over all primitive properties
            cpObj.Reftime = obj.Reftime;
            cpObj.Time = obj.Time;
            cpObj.X = obj.X;
            cpObj.Y = obj.Y;
            cpObj.V = obj.V;
            cpObj.Yaw = obj.Yaw;
            
            % Recursively copy compound properties
            cpObj.Header = copy(obj.Header);
        end
        
        function reload(obj, strObj)
            %reload Called by loadobj to assign properties
            obj.Reftime = strObj.Reftime;
            obj.Time = strObj.Time;
            obj.X = strObj.X;
            obj.Y = strObj.Y;
            obj.V = strObj.V;
            obj.Yaw = strObj.Yaw;
            obj.Header = feval([obj.StdMsgsHeaderClass '.loadobj'], strObj.Header);
        end
    end
    
    methods (Access = ?robotics.ros.Message)
        function strObj = saveobj(obj)
            %saveobj Implements saving of message to MAT file
            
            % Return an empty element if object array is empty
            if isempty(obj)
                strObj = struct.empty;
                return
            end
            
            strObj.Reftime = obj.Reftime;
            strObj.Time = obj.Time;
            strObj.X = obj.X;
            strObj.Y = obj.Y;
            strObj.V = obj.V;
            strObj.Yaw = obj.Yaw;
            strObj.Header = saveobj(obj.Header);
        end
    end
    
    methods (Static, Access = {?matlab.unittest.TestCase, ?robotics.ros.Message})
        function obj = loadobj(strObj)
            %loadobj Implements loading of message from MAT file
            
            % Return an empty object array if the structure element is not defined
            if isempty(strObj)
                obj = robotics.ros.custom.msggen.vehicle_control.Trajectory.empty(0,1);
                return
            end
            
            % Create an empty message object
            obj = robotics.ros.custom.msggen.vehicle_control.Trajectory;
            obj.reload(strObj);
        end
    end
end
