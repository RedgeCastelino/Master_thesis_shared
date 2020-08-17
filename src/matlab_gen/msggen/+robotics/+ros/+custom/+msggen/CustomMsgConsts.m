classdef CustomMsgConsts
    %CustomMsgConsts This class stores all message types
    %   The message types are constant properties, which in turn resolve
    %   to the strings of the actual types.
    
    %   Copyright 2014-2020 The MathWorks, Inc.
    
    properties (Constant)
        object_list_Classification = 'object_list/Classification'
        object_list_Dimension = 'object_list/Dimension'
        object_list_EgoData = 'object_list/EgoData'
        object_list_Features = 'object_list/Features'
        object_list_Geometric = 'object_list/Geometric'
        object_list_ObjectList = 'object_list/ObjectList'
        object_list_ObjectsList = 'object_list/ObjectsList'
        osi3_bridge_Dimension3d = 'osi3_bridge/Dimension3d'
        osi3_bridge_GroundTruthMovingObjects = 'osi3_bridge/GroundTruthMovingObjects'
        osi3_bridge_MovingObject = 'osi3_bridge/MovingObject'
        osi3_bridge_Orientation3d = 'osi3_bridge/Orientation3d'
        osi3_bridge_TrafficUpdateMovingObject = 'osi3_bridge/TrafficUpdateMovingObject'
        vehicle_control_Trajectory = 'vehicle_control/Trajectory'
    end
    
    methods (Static, Hidden)
        function messageList = getMessageList
            %getMessageList Generate a cell array with all message types.
            %   The list will be sorted alphabetically.
            
            persistent msgList
            if isempty(msgList)
                msgList = cell(13, 1);
                msgList{1} = 'object_list/Classification';
                msgList{2} = 'object_list/Dimension';
                msgList{3} = 'object_list/EgoData';
                msgList{4} = 'object_list/Features';
                msgList{5} = 'object_list/Geometric';
                msgList{6} = 'object_list/ObjectList';
                msgList{7} = 'object_list/ObjectsList';
                msgList{8} = 'osi3_bridge/Dimension3d';
                msgList{9} = 'osi3_bridge/GroundTruthMovingObjects';
                msgList{10} = 'osi3_bridge/MovingObject';
                msgList{11} = 'osi3_bridge/Orientation3d';
                msgList{12} = 'osi3_bridge/TrafficUpdateMovingObject';
                msgList{13} = 'vehicle_control/Trajectory';
            end
            
            messageList = msgList;
        end
        
        function serviceList = getServiceList
            %getServiceList Generate a cell array with all service types.
            %   The list will be sorted alphabetically.
            
            persistent svcList
            if isempty(svcList)
                svcList = cell(0, 1);
            end
            
            % The message list was already sorted, so don't need to sort
            % again.
            serviceList = svcList;
        end
        
        function actionList = getActionList
            %getActionList Generate a cell array with all action types.
            %   The list will be sorted alphabetically.
            
            persistent actList
            if isempty(actList)
                actList = cell(0, 1);
            end
            
            % The message list was already sorted, so don't need to sort
            % again.
            actionList = actList;
        end
    end
end
