; Auto-generated. Do not edit!


(cl:in-package osi3_bridge-msg)


;//! \htmlinclude TrafficUpdateMovingObject.msg.html

(cl:defclass <TrafficUpdateMovingObject> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (object
    :reader object
    :initarg :object
    :type osi3_bridge-msg:MovingObject
    :initform (cl:make-instance 'osi3_bridge-msg:MovingObject)))
)

(cl:defclass TrafficUpdateMovingObject (<TrafficUpdateMovingObject>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TrafficUpdateMovingObject>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TrafficUpdateMovingObject)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name osi3_bridge-msg:<TrafficUpdateMovingObject> is deprecated: use osi3_bridge-msg:TrafficUpdateMovingObject instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <TrafficUpdateMovingObject>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader osi3_bridge-msg:header-val is deprecated.  Use osi3_bridge-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'object-val :lambda-list '(m))
(cl:defmethod object-val ((m <TrafficUpdateMovingObject>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader osi3_bridge-msg:object-val is deprecated.  Use osi3_bridge-msg:object instead.")
  (object m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TrafficUpdateMovingObject>) ostream)
  "Serializes a message object of type '<TrafficUpdateMovingObject>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'object) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TrafficUpdateMovingObject>) istream)
  "Deserializes a message object of type '<TrafficUpdateMovingObject>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'object) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TrafficUpdateMovingObject>)))
  "Returns string type for a message object of type '<TrafficUpdateMovingObject>"
  "osi3_bridge/TrafficUpdateMovingObject")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TrafficUpdateMovingObject)))
  "Returns string type for a message object of type 'TrafficUpdateMovingObject"
  "osi3_bridge/TrafficUpdateMovingObject")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TrafficUpdateMovingObject>)))
  "Returns md5sum for a message object of type '<TrafficUpdateMovingObject>"
  "b26e20bf46b692e8759e85b824c5ffc2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TrafficUpdateMovingObject)))
  "Returns md5sum for a message object of type 'TrafficUpdateMovingObject"
  "b26e20bf46b692e8759e85b824c5ffc2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TrafficUpdateMovingObject>)))
  "Returns full string definition for message of type '<TrafficUpdateMovingObject>"
  (cl:format cl:nil "Header header~%osi3_bridge/MovingObject object~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: osi3_bridge/MovingObject~%uint64 id~%osi3_bridge/Dimension3d dimension~%geometry_msgs/Vector3 position~%osi3_bridge/Orientation3d orientation~%geometry_msgs/Vector3 velocity~%geometry_msgs/Vector3 acceleration~%uint8 type~%~%uint8 TYPE_UNKNOWN = 0~%uint8 TYPE_OTHER = 1~%uint8 TYPE_CAR = 2~%uint8 TYPE_PEDESTRIAN = 3~%uint8 TYPE_ANIMAL = 4~%uint8 TYPE_TRUCK = 5~%uint8 TYPE_TRAILER = 6~%uint8 TYPE_MOTORBIKE = 7~%uint8 TYPE_BICYCLE = 8~%uint8 TYPE_BUS = 9~%uint8 TYPE_TRAM = 10~%uint8 TYPE_TRAIN = 11~%uint8 TYPE_WHEELCHAIR = 12~%~%~%================================================================================~%MSG: osi3_bridge/Dimension3d~%float64 length~%float64 width~%float64 height~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: osi3_bridge/Orientation3d~%float64 roll~%float64 pitch~%float64 yaw~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TrafficUpdateMovingObject)))
  "Returns full string definition for message of type 'TrafficUpdateMovingObject"
  (cl:format cl:nil "Header header~%osi3_bridge/MovingObject object~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: osi3_bridge/MovingObject~%uint64 id~%osi3_bridge/Dimension3d dimension~%geometry_msgs/Vector3 position~%osi3_bridge/Orientation3d orientation~%geometry_msgs/Vector3 velocity~%geometry_msgs/Vector3 acceleration~%uint8 type~%~%uint8 TYPE_UNKNOWN = 0~%uint8 TYPE_OTHER = 1~%uint8 TYPE_CAR = 2~%uint8 TYPE_PEDESTRIAN = 3~%uint8 TYPE_ANIMAL = 4~%uint8 TYPE_TRUCK = 5~%uint8 TYPE_TRAILER = 6~%uint8 TYPE_MOTORBIKE = 7~%uint8 TYPE_BICYCLE = 8~%uint8 TYPE_BUS = 9~%uint8 TYPE_TRAM = 10~%uint8 TYPE_TRAIN = 11~%uint8 TYPE_WHEELCHAIR = 12~%~%~%================================================================================~%MSG: osi3_bridge/Dimension3d~%float64 length~%float64 width~%float64 height~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: osi3_bridge/Orientation3d~%float64 roll~%float64 pitch~%float64 yaw~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TrafficUpdateMovingObject>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'object))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TrafficUpdateMovingObject>))
  "Converts a ROS message object to a list"
  (cl:list 'TrafficUpdateMovingObject
    (cl:cons ':header (header msg))
    (cl:cons ':object (object msg))
))
