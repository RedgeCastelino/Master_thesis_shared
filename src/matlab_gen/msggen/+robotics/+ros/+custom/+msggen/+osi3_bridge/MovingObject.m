classdef MovingObject < robotics.ros.Message
    %MovingObject MATLAB implementation of osi3_bridge/MovingObject
    %   This class was automatically generated by
    %   robotics.ros.msg.internal.gen.MessageClassGenerator.
    
    %   Copyright 2014-2020 The MathWorks, Inc.
    
    %#ok<*INUSD>
    
    properties (Constant)
        MessageType = 'osi3_bridge/MovingObject' % The ROS message type
    end
    
    properties (Constant, Hidden)
        MD5Checksum = '1d813c673962ef31735dd456446e05b5' % The MD5 Checksum of the message definition
    end
    
    properties (Access = protected)
        JavaMessage % The Java message object
    end
    
    properties (Constant)
        TYPEUNKNOWN = uint8(0)
        TYPEOTHER = uint8(1)
        TYPECAR = uint8(2)
        TYPEPEDESTRIAN = uint8(3)
        TYPEANIMAL = uint8(4)
        TYPETRUCK = uint8(5)
        TYPETRAILER = uint8(6)
        TYPEMOTORBIKE = uint8(7)
        TYPEBICYCLE = uint8(8)
        TYPEBUS = uint8(9)
        TYPETRAM = uint8(10)
        TYPETRAIN = uint8(11)
        TYPEWHEELCHAIR = uint8(12)
    end
    
    properties (Constant, Access = protected)
        GeometryMsgsVector3Class = robotics.ros.msg.internal.MessageFactory.getClassForType('geometry_msgs/Vector3') % Dispatch to MATLAB class for message type geometry_msgs/Vector3
        Osi3BridgeDimension3dClass = robotics.ros.msg.internal.MessageFactory.getClassForType('osi3_bridge/Dimension3d') % Dispatch to MATLAB class for message type osi3_bridge/Dimension3d
        Osi3BridgeOrientation3dClass = robotics.ros.msg.internal.MessageFactory.getClassForType('osi3_bridge/Orientation3d') % Dispatch to MATLAB class for message type osi3_bridge/Orientation3d
    end
    
    properties (Dependent)
        Id
        Dimension
        Position
        Orientation
        Velocity
        Acceleration
        Type
    end
    
    properties (Access = protected)
        Cache = struct('Dimension', [], 'Position', [], 'Orientation', [], 'Velocity', [], 'Acceleration', []) % The cache for fast data access
    end
    
    properties (Constant, Hidden)
        PropertyList = {'Acceleration', 'Dimension', 'Id', 'Orientation', 'Position', 'Type', 'Velocity'} % List of non-constant message properties
        ROSPropertyList = {'acceleration', 'dimension', 'id', 'orientation', 'position', 'type', 'velocity'} % List of non-constant ROS message properties
    end
    
    methods
        function obj = MovingObject(msg)
            %MovingObject Construct the message object MovingObject
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
        
        function id = get.Id(obj)
            %get.Id Get the value for property Id
            id = typecast(int64(obj.JavaMessage.getId), 'uint64');
        end
        
        function set.Id(obj, id)
            %set.Id Set the value for property Id
            validateattributes(id, {'numeric'}, {'nonempty', 'scalar'}, 'MovingObject', 'Id');
            
            obj.JavaMessage.setId(id);
        end
        
        function dimension = get.Dimension(obj)
            %get.Dimension Get the value for property Dimension
            if isempty(obj.Cache.Dimension)
                obj.Cache.Dimension = feval(obj.Osi3BridgeDimension3dClass, obj.JavaMessage.getDimension);
            end
            dimension = obj.Cache.Dimension;
        end
        
        function set.Dimension(obj, dimension)
            %set.Dimension Set the value for property Dimension
            validateattributes(dimension, {obj.Osi3BridgeDimension3dClass}, {'nonempty', 'scalar'}, 'MovingObject', 'Dimension');
            
            obj.JavaMessage.setDimension(dimension.getJavaObject);
            
            % Update cache if necessary
            if ~isempty(obj.Cache.Dimension)
                obj.Cache.Dimension.setJavaObject(dimension.getJavaObject);
            end
        end
        
        function position = get.Position(obj)
            %get.Position Get the value for property Position
            if isempty(obj.Cache.Position)
                obj.Cache.Position = feval(obj.GeometryMsgsVector3Class, obj.JavaMessage.getPosition);
            end
            position = obj.Cache.Position;
        end
        
        function set.Position(obj, position)
            %set.Position Set the value for property Position
            validateattributes(position, {obj.GeometryMsgsVector3Class}, {'nonempty', 'scalar'}, 'MovingObject', 'Position');
            
            obj.JavaMessage.setPosition(position.getJavaObject);
            
            % Update cache if necessary
            if ~isempty(obj.Cache.Position)
                obj.Cache.Position.setJavaObject(position.getJavaObject);
            end
        end
        
        function orientation = get.Orientation(obj)
            %get.Orientation Get the value for property Orientation
            if isempty(obj.Cache.Orientation)
                obj.Cache.Orientation = feval(obj.Osi3BridgeOrientation3dClass, obj.JavaMessage.getOrientation);
            end
            orientation = obj.Cache.Orientation;
        end
        
        function set.Orientation(obj, orientation)
            %set.Orientation Set the value for property Orientation
            validateattributes(orientation, {obj.Osi3BridgeOrientation3dClass}, {'nonempty', 'scalar'}, 'MovingObject', 'Orientation');
            
            obj.JavaMessage.setOrientation(orientation.getJavaObject);
            
            % Update cache if necessary
            if ~isempty(obj.Cache.Orientation)
                obj.Cache.Orientation.setJavaObject(orientation.getJavaObject);
            end
        end
        
        function velocity = get.Velocity(obj)
            %get.Velocity Get the value for property Velocity
            if isempty(obj.Cache.Velocity)
                obj.Cache.Velocity = feval(obj.GeometryMsgsVector3Class, obj.JavaMessage.getVelocity);
            end
            velocity = obj.Cache.Velocity;
        end
        
        function set.Velocity(obj, velocity)
            %set.Velocity Set the value for property Velocity
            validateattributes(velocity, {obj.GeometryMsgsVector3Class}, {'nonempty', 'scalar'}, 'MovingObject', 'Velocity');
            
            obj.JavaMessage.setVelocity(velocity.getJavaObject);
            
            % Update cache if necessary
            if ~isempty(obj.Cache.Velocity)
                obj.Cache.Velocity.setJavaObject(velocity.getJavaObject);
            end
        end
        
        function acceleration = get.Acceleration(obj)
            %get.Acceleration Get the value for property Acceleration
            if isempty(obj.Cache.Acceleration)
                obj.Cache.Acceleration = feval(obj.GeometryMsgsVector3Class, obj.JavaMessage.getAcceleration);
            end
            acceleration = obj.Cache.Acceleration;
        end
        
        function set.Acceleration(obj, acceleration)
            %set.Acceleration Set the value for property Acceleration
            validateattributes(acceleration, {obj.GeometryMsgsVector3Class}, {'nonempty', 'scalar'}, 'MovingObject', 'Acceleration');
            
            obj.JavaMessage.setAcceleration(acceleration.getJavaObject);
            
            % Update cache if necessary
            if ~isempty(obj.Cache.Acceleration)
                obj.Cache.Acceleration.setJavaObject(acceleration.getJavaObject);
            end
        end
        
        function type = get.Type(obj)
            %get.Type Get the value for property Type
            type = typecast(int8(obj.JavaMessage.getType), 'uint8');
        end
        
        function set.Type(obj, type)
            %set.Type Set the value for property Type
            validateattributes(type, {'numeric'}, {'nonempty', 'scalar'}, 'MovingObject', 'Type');
            
            obj.JavaMessage.setType(type);
        end
    end
    
    methods (Access = protected)
        function resetCache(obj)
            %resetCache Resets any cached properties
            obj.Cache.Dimension = [];
            obj.Cache.Position = [];
            obj.Cache.Orientation = [];
            obj.Cache.Velocity = [];
            obj.Cache.Acceleration = [];
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
            cpObj.Id = obj.Id;
            cpObj.Type = obj.Type;
            
            % Recursively copy compound properties
            cpObj.Dimension = copy(obj.Dimension);
            cpObj.Position = copy(obj.Position);
            cpObj.Orientation = copy(obj.Orientation);
            cpObj.Velocity = copy(obj.Velocity);
            cpObj.Acceleration = copy(obj.Acceleration);
        end
        
        function reload(obj, strObj)
            %reload Called by loadobj to assign properties
            obj.Id = strObj.Id;
            obj.Type = strObj.Type;
            obj.Dimension = feval([obj.Osi3BridgeDimension3dClass '.loadobj'], strObj.Dimension);
            obj.Position = feval([obj.GeometryMsgsVector3Class '.loadobj'], strObj.Position);
            obj.Orientation = feval([obj.Osi3BridgeOrientation3dClass '.loadobj'], strObj.Orientation);
            obj.Velocity = feval([obj.GeometryMsgsVector3Class '.loadobj'], strObj.Velocity);
            obj.Acceleration = feval([obj.GeometryMsgsVector3Class '.loadobj'], strObj.Acceleration);
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
            
            strObj.Id = obj.Id;
            strObj.Type = obj.Type;
            strObj.Dimension = saveobj(obj.Dimension);
            strObj.Position = saveobj(obj.Position);
            strObj.Orientation = saveobj(obj.Orientation);
            strObj.Velocity = saveobj(obj.Velocity);
            strObj.Acceleration = saveobj(obj.Acceleration);
        end
    end
    
    methods (Static, Access = {?matlab.unittest.TestCase, ?robotics.ros.Message})
        function obj = loadobj(strObj)
            %loadobj Implements loading of message from MAT file
            
            % Return an empty object array if the structure element is not defined
            if isempty(strObj)
                obj = robotics.ros.custom.msggen.osi3_bridge.MovingObject.empty(0,1);
                return
            end
            
            % Create an empty message object
            obj = robotics.ros.custom.msggen.osi3_bridge.MovingObject;
            obj.reload(strObj);
        end
    end
end