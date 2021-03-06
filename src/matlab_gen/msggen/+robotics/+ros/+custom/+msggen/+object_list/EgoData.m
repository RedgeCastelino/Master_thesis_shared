classdef EgoData < robotics.ros.Message
    %EgoData MATLAB implementation of object_list/EgoData
    %   This class was automatically generated by
    %   robotics.ros.msg.internal.gen.MessageClassGenerator.
    
    %   Copyright 2014-2020 The MathWorks, Inc.
    
    %#ok<*INUSD>
    
    properties (Constant)
        MessageType = 'object_list/EgoData' % The ROS message type
    end
    
    properties (Constant, Hidden)
        MD5Checksum = '504c209a03982f6d37907b8642fe1667' % The MD5 Checksum of the message definition
    end
    
    properties (Access = protected)
        JavaMessage % The Java message object
    end
    
    properties (Constant, Access = protected)
        ObjectListDimensionClass = robotics.ros.msg.internal.MessageFactory.getClassForType('object_list/Dimension') % Dispatch to MATLAB class for message type object_list/Dimension
        ObjectListGeometricClass = robotics.ros.msg.internal.MessageFactory.getClassForType('object_list/Geometric') % Dispatch to MATLAB class for message type object_list/Geometric
        StdMsgsHeaderClass = robotics.ros.msg.internal.MessageFactory.getClassForType('std_msgs/Header') % Dispatch to MATLAB class for message type std_msgs/Header
    end
    
    properties (Dependent)
        Header
        Geometric
        Dimension
    end
    
    properties (Access = protected)
        Cache = struct('Header', [], 'Geometric', [], 'Dimension', []) % The cache for fast data access
    end
    
    properties (Constant, Hidden)
        PropertyList = {'Dimension', 'Geometric', 'Header'} % List of non-constant message properties
        ROSPropertyList = {'dimension', 'geometric', 'header'} % List of non-constant ROS message properties
    end
    
    methods
        function obj = EgoData(msg)
            %EgoData Construct the message object EgoData
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
            validateattributes(header, {obj.StdMsgsHeaderClass}, {'nonempty', 'scalar'}, 'EgoData', 'Header');
            
            obj.JavaMessage.setHeader(header.getJavaObject);
            
            % Update cache if necessary
            if ~isempty(obj.Cache.Header)
                obj.Cache.Header.setJavaObject(header.getJavaObject);
            end
        end
        
        function geometric = get.Geometric(obj)
            %get.Geometric Get the value for property Geometric
            if isempty(obj.Cache.Geometric)
                obj.Cache.Geometric = feval(obj.ObjectListGeometricClass, obj.JavaMessage.getGeometric);
            end
            geometric = obj.Cache.Geometric;
        end
        
        function set.Geometric(obj, geometric)
            %set.Geometric Set the value for property Geometric
            validateattributes(geometric, {obj.ObjectListGeometricClass}, {'nonempty', 'scalar'}, 'EgoData', 'Geometric');
            
            obj.JavaMessage.setGeometric(geometric.getJavaObject);
            
            % Update cache if necessary
            if ~isempty(obj.Cache.Geometric)
                obj.Cache.Geometric.setJavaObject(geometric.getJavaObject);
            end
        end
        
        function dimension = get.Dimension(obj)
            %get.Dimension Get the value for property Dimension
            if isempty(obj.Cache.Dimension)
                obj.Cache.Dimension = feval(obj.ObjectListDimensionClass, obj.JavaMessage.getDimension);
            end
            dimension = obj.Cache.Dimension;
        end
        
        function set.Dimension(obj, dimension)
            %set.Dimension Set the value for property Dimension
            validateattributes(dimension, {obj.ObjectListDimensionClass}, {'nonempty', 'scalar'}, 'EgoData', 'Dimension');
            
            obj.JavaMessage.setDimension(dimension.getJavaObject);
            
            % Update cache if necessary
            if ~isempty(obj.Cache.Dimension)
                obj.Cache.Dimension.setJavaObject(dimension.getJavaObject);
            end
        end
    end
    
    methods (Access = protected)
        function resetCache(obj)
            %resetCache Resets any cached properties
            obj.Cache.Header = [];
            obj.Cache.Geometric = [];
            obj.Cache.Dimension = [];
        end
        
        function cpObj = copyElement(obj)
            %copyElement Implements deep copy behavior for message
            
            % Call default copy method for shallow copy
            cpObj = copyElement@robotics.ros.Message(obj);
            
            % Clear any existing cached properties
            cpObj.resetCache;
            
            % Create a new Java message object
            cpObj.JavaMessage = obj.createNewJavaMessage;
            
            % Recursively copy compound properties
            cpObj.Header = copy(obj.Header);
            cpObj.Geometric = copy(obj.Geometric);
            cpObj.Dimension = copy(obj.Dimension);
        end
        
        function reload(obj, strObj)
            %reload Called by loadobj to assign properties
            obj.Header = feval([obj.StdMsgsHeaderClass '.loadobj'], strObj.Header);
            obj.Geometric = feval([obj.ObjectListGeometricClass '.loadobj'], strObj.Geometric);
            obj.Dimension = feval([obj.ObjectListDimensionClass '.loadobj'], strObj.Dimension);
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
            
            strObj.Header = saveobj(obj.Header);
            strObj.Geometric = saveobj(obj.Geometric);
            strObj.Dimension = saveobj(obj.Dimension);
        end
    end
    
    methods (Static, Access = {?matlab.unittest.TestCase, ?robotics.ros.Message})
        function obj = loadobj(strObj)
            %loadobj Implements loading of message from MAT file
            
            % Return an empty object array if the structure element is not defined
            if isempty(strObj)
                obj = robotics.ros.custom.msggen.object_list.EgoData.empty(0,1);
                return
            end
            
            % Create an empty message object
            obj = robotics.ros.custom.msggen.object_list.EgoData;
            obj.reload(strObj);
        end
    end
end
