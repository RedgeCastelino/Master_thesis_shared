classdef Geometric < robotics.ros.Message
    %Geometric MATLAB implementation of object_list/Geometric
    %   This class was automatically generated by
    %   robotics.ros.msg.internal.gen.MessageClassGenerator.
    
    %   Copyright 2014-2020 The MathWorks, Inc.
    
    %#ok<*INUSD>
    
    properties (Constant)
        MessageType = 'object_list/Geometric' % The ROS message type
    end
    
    properties (Constant, Hidden)
        MD5Checksum = '74a252effe5544c6405c61fc1ab21633' % The MD5 Checksum of the message definition
    end
    
    properties (Access = protected)
        JavaMessage % The Java message object
    end
    
    properties (Dependent)
        X
        Y
        Vx
        Vy
        Ax
        Ay
        Yaw
        Yawrate
    end
    
    properties (Constant, Hidden)
        PropertyList = {'Ax', 'Ay', 'Vx', 'Vy', 'X', 'Y', 'Yaw', 'Yawrate'} % List of non-constant message properties
        ROSPropertyList = {'ax', 'ay', 'vx', 'vy', 'x', 'y', 'yaw', 'yawrate'} % List of non-constant ROS message properties
    end
    
    methods
        function obj = Geometric(msg)
            %Geometric Construct the message object Geometric
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
        
        function x = get.X(obj)
            %get.X Get the value for property X
            x = double(obj.JavaMessage.getX);
        end
        
        function set.X(obj, x)
            %set.X Set the value for property X
            validateattributes(x, {'numeric'}, {'nonempty', 'scalar'}, 'Geometric', 'X');
            
            obj.JavaMessage.setX(x);
        end
        
        function y = get.Y(obj)
            %get.Y Get the value for property Y
            y = double(obj.JavaMessage.getY);
        end
        
        function set.Y(obj, y)
            %set.Y Set the value for property Y
            validateattributes(y, {'numeric'}, {'nonempty', 'scalar'}, 'Geometric', 'Y');
            
            obj.JavaMessage.setY(y);
        end
        
        function vx = get.Vx(obj)
            %get.Vx Get the value for property Vx
            vx = double(obj.JavaMessage.getVx);
        end
        
        function set.Vx(obj, vx)
            %set.Vx Set the value for property Vx
            validateattributes(vx, {'numeric'}, {'nonempty', 'scalar'}, 'Geometric', 'Vx');
            
            obj.JavaMessage.setVx(vx);
        end
        
        function vy = get.Vy(obj)
            %get.Vy Get the value for property Vy
            vy = double(obj.JavaMessage.getVy);
        end
        
        function set.Vy(obj, vy)
            %set.Vy Set the value for property Vy
            validateattributes(vy, {'numeric'}, {'nonempty', 'scalar'}, 'Geometric', 'Vy');
            
            obj.JavaMessage.setVy(vy);
        end
        
        function ax = get.Ax(obj)
            %get.Ax Get the value for property Ax
            ax = double(obj.JavaMessage.getAx);
        end
        
        function set.Ax(obj, ax)
            %set.Ax Set the value for property Ax
            validateattributes(ax, {'numeric'}, {'nonempty', 'scalar'}, 'Geometric', 'Ax');
            
            obj.JavaMessage.setAx(ax);
        end
        
        function ay = get.Ay(obj)
            %get.Ay Get the value for property Ay
            ay = double(obj.JavaMessage.getAy);
        end
        
        function set.Ay(obj, ay)
            %set.Ay Set the value for property Ay
            validateattributes(ay, {'numeric'}, {'nonempty', 'scalar'}, 'Geometric', 'Ay');
            
            obj.JavaMessage.setAy(ay);
        end
        
        function yaw = get.Yaw(obj)
            %get.Yaw Get the value for property Yaw
            yaw = double(obj.JavaMessage.getYaw);
        end
        
        function set.Yaw(obj, yaw)
            %set.Yaw Set the value for property Yaw
            validateattributes(yaw, {'numeric'}, {'nonempty', 'scalar'}, 'Geometric', 'Yaw');
            
            obj.JavaMessage.setYaw(yaw);
        end
        
        function yawrate = get.Yawrate(obj)
            %get.Yawrate Get the value for property Yawrate
            yawrate = double(obj.JavaMessage.getYawrate);
        end
        
        function set.Yawrate(obj, yawrate)
            %set.Yawrate Set the value for property Yawrate
            validateattributes(yawrate, {'numeric'}, {'nonempty', 'scalar'}, 'Geometric', 'Yawrate');
            
            obj.JavaMessage.setYawrate(yawrate);
        end
    end
    
    methods (Access = protected)
        function cpObj = copyElement(obj)
            %copyElement Implements deep copy behavior for message
            
            % Call default copy method for shallow copy
            cpObj = copyElement@robotics.ros.Message(obj);
            
            % Create a new Java message object
            cpObj.JavaMessage = obj.createNewJavaMessage;
            
            % Iterate over all primitive properties
            cpObj.X = obj.X;
            cpObj.Y = obj.Y;
            cpObj.Vx = obj.Vx;
            cpObj.Vy = obj.Vy;
            cpObj.Ax = obj.Ax;
            cpObj.Ay = obj.Ay;
            cpObj.Yaw = obj.Yaw;
            cpObj.Yawrate = obj.Yawrate;
        end
        
        function reload(obj, strObj)
            %reload Called by loadobj to assign properties
            obj.X = strObj.X;
            obj.Y = strObj.Y;
            obj.Vx = strObj.Vx;
            obj.Vy = strObj.Vy;
            obj.Ax = strObj.Ax;
            obj.Ay = strObj.Ay;
            obj.Yaw = strObj.Yaw;
            obj.Yawrate = strObj.Yawrate;
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
            
            strObj.X = obj.X;
            strObj.Y = obj.Y;
            strObj.Vx = obj.Vx;
            strObj.Vy = obj.Vy;
            strObj.Ax = obj.Ax;
            strObj.Ay = obj.Ay;
            strObj.Yaw = obj.Yaw;
            strObj.Yawrate = obj.Yawrate;
        end
    end
    
    methods (Static, Access = {?matlab.unittest.TestCase, ?robotics.ros.Message})
        function obj = loadobj(strObj)
            %loadobj Implements loading of message from MAT file
            
            % Return an empty object array if the structure element is not defined
            if isempty(strObj)
                obj = robotics.ros.custom.msggen.object_list.Geometric.empty(0,1);
                return
            end
            
            % Create an empty message object
            obj = robotics.ros.custom.msggen.object_list.Geometric;
            obj.reload(strObj);
        end
    end
end
