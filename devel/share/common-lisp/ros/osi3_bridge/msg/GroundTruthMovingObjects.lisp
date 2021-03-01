; Auto-generated. Do not edit!


(cl:in-package osi3_bridge-msg)


;//! \htmlinclude GroundTruthMovingObjects.msg.html

(cl:defclass <GroundTruthMovingObjects> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (objects
    :reader objects
    :initarg :objects
    :type (cl:vector osi3_bridge-msg:MovingObject)
   :initform (cl:make-array 0 :element-type 'osi3_bridge-msg:MovingObject :initial-element (cl:make-instance 'osi3_bridge-msg:MovingObject))))
)

(cl:defclass GroundTruthMovingObjects (<GroundTruthMovingObjects>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GroundTruthMovingObjects>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GroundTruthMovingObjects)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name osi3_bridge-msg:<GroundTruthMovingObjects> is deprecated: use osi3_bridge-msg:GroundTruthMovingObjects instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <GroundTruthMovingObjects>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader osi3_bridge-msg:header-val is deprecated.  Use osi3_bridge-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'objects-val :lambda-list '(m))
(cl:defmethod objects-val ((m <GroundTruthMovingObjects>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader osi3_bridge-msg:objects-val is deprecated.  Use osi3_bridge-msg:objects instead.")
  (objects m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GroundTruthMovingObjects>) ostream)
  "Serializes a message object of type '<GroundTruthMovingObjects>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'objects))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'objects))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GroundTruthMovingObjects>) istream)
  "Deserializes a message object of type '<GroundTruthMovingObjects>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'objects) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'objects)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'osi3_bridge-msg:MovingObject))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GroundTruthMovingObjects>)))
  "Returns string type for a message object of type '<GroundTruthMovingObjects>"
  "osi3_bridge/GroundTruthMovingObjects")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GroundTruthMovingObjects)))
  "Returns string type for a message object of type 'GroundTruthMovingObjects"
  "osi3_bridge/GroundTruthMovingObjects")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GroundTruthMovingObjects>)))
  "Returns md5sum for a message object of type '<GroundTruthMovingObjects>"
  "b5c10f964cf85cf58aa709fc3567f543")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GroundTruthMovingObjects)))
  "Returns md5sum for a message object of type 'GroundTruthMovingObjects"
  "b5c10f964cf85cf58aa709fc3567f543")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GroundTruthMovingObjects>)))
  "Returns full string definition for message of type '<GroundTruthMovingObjects>"
  (cl:format cl:nil "Header header~%osi3_bridge/MovingObject[] objects~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: osi3_bridge/MovingObject~%uint64 id~%osi3_bridge/Dimension3d dimension~%geometry_msgs/Vector3 position~%osi3_bridge/Orientation3d orientation~%geometry_msgs/Vector3 velocity~%geometry_msgs/Vector3 acceleration~%uint8 type~%~%uint8 TYPE_UNKNOWN = 0~%uint8 TYPE_OTHER = 1~%uint8 TYPE_CAR = 2~%uint8 TYPE_PEDESTRIAN = 3~%uint8 TYPE_ANIMAL = 4~%uint8 TYPE_TRUCK = 5~%uint8 TYPE_TRAILER = 6~%uint8 TYPE_MOTORBIKE = 7~%uint8 TYPE_BICYCLE = 8~%uint8 TYPE_BUS = 9~%uint8 TYPE_TRAM = 10~%uint8 TYPE_TRAIN = 11~%uint8 TYPE_WHEELCHAIR = 12~%~%~%================================================================================~%MSG: osi3_bridge/Dimension3d~%float64 length~%float64 width~%float64 height~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: osi3_bridge/Orientation3d~%float64 roll~%float64 pitch~%float64 yaw~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GroundTruthMovingObjects)))
  "Returns full string definition for message of type 'GroundTruthMovingObjects"
  (cl:format cl:nil "Header header~%osi3_bridge/MovingObject[] objects~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: osi3_bridge/MovingObject~%uint64 id~%osi3_bridge/Dimension3d dimension~%geometry_msgs/Vector3 position~%osi3_bridge/Orientation3d orientation~%geometry_msgs/Vector3 velocity~%geometry_msgs/Vector3 acceleration~%uint8 type~%~%uint8 TYPE_UNKNOWN = 0~%uint8 TYPE_OTHER = 1~%uint8 TYPE_CAR = 2~%uint8 TYPE_PEDESTRIAN = 3~%uint8 TYPE_ANIMAL = 4~%uint8 TYPE_TRUCK = 5~%uint8 TYPE_TRAILER = 6~%uint8 TYPE_MOTORBIKE = 7~%uint8 TYPE_BICYCLE = 8~%uint8 TYPE_BUS = 9~%uint8 TYPE_TRAM = 10~%uint8 TYPE_TRAIN = 11~%uint8 TYPE_WHEELCHAIR = 12~%~%~%================================================================================~%MSG: osi3_bridge/Dimension3d~%float64 length~%float64 width~%float64 height~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: osi3_bridge/Orientation3d~%float64 roll~%float64 pitch~%float64 yaw~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GroundTruthMovingObjects>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'objects) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GroundTruthMovingObjects>))
  "Converts a ROS message object to a list"
  (cl:list 'GroundTruthMovingObjects
    (cl:cons ':header (header msg))
    (cl:cons ':objects (objects msg))
))
