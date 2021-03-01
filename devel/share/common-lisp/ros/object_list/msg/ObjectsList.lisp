; Auto-generated. Do not edit!


(cl:in-package object_list-msg)


;//! \htmlinclude ObjectsList.msg.html

(cl:defclass <ObjectsList> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (obj_list
    :reader obj_list
    :initarg :obj_list
    :type (cl:vector object_list-msg:ObjectList)
   :initform (cl:make-array 0 :element-type 'object_list-msg:ObjectList :initial-element (cl:make-instance 'object_list-msg:ObjectList)))
   (sensor_property
    :reader sensor_property
    :initarg :sensor_property
    :type object_list-msg:SensorProperty
    :initform (cl:make-instance 'object_list-msg:SensorProperty)))
)

(cl:defclass ObjectsList (<ObjectsList>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ObjectsList>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ObjectsList)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name object_list-msg:<ObjectsList> is deprecated: use object_list-msg:ObjectsList instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <ObjectsList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:header-val is deprecated.  Use object_list-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'obj_list-val :lambda-list '(m))
(cl:defmethod obj_list-val ((m <ObjectsList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:obj_list-val is deprecated.  Use object_list-msg:obj_list instead.")
  (obj_list m))

(cl:ensure-generic-function 'sensor_property-val :lambda-list '(m))
(cl:defmethod sensor_property-val ((m <ObjectsList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:sensor_property-val is deprecated.  Use object_list-msg:sensor_property instead.")
  (sensor_property m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ObjectsList>) ostream)
  "Serializes a message object of type '<ObjectsList>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'obj_list))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'obj_list))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'sensor_property) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ObjectsList>) istream)
  "Deserializes a message object of type '<ObjectsList>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'obj_list) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'obj_list)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'object_list-msg:ObjectList))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'sensor_property) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ObjectsList>)))
  "Returns string type for a message object of type '<ObjectsList>"
  "object_list/ObjectsList")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ObjectsList)))
  "Returns string type for a message object of type 'ObjectsList"
  "object_list/ObjectsList")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ObjectsList>)))
  "Returns md5sum for a message object of type '<ObjectsList>"
  "d69ee6a3db897657f81853c8b3814ced")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ObjectsList)))
  "Returns md5sum for a message object of type 'ObjectsList"
  "d69ee6a3db897657f81853c8b3814ced")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ObjectsList>)))
  "Returns full string definition for message of type '<ObjectsList>"
  (cl:format cl:nil "Header header~%ObjectList[] obj_list~%SensorProperty sensor_property~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: object_list/ObjectList~%int32 obj_id~%float64 time~%Geometric geometric~%float64[36] covariance~%Dimension dimension~%float64 prop_existence~%float64 prop_nonexistence~%float64 prop_persistance~%float64 prop_mov ~%Classification classification~%float64[12] classification_mass~%Features features~%int64[] sensors_fused~%~%================================================================================~%MSG: object_list/Geometric~%float64 x~%float64 y~%float64 vx~%float64 vy~%float64 ax~%float64 ay~%float64 yaw~%float64 yawrate~%~%================================================================================~%MSG: object_list/Dimension~%float64 length~%float64 width~%float64 length_variance~%float64 width_variance~%~%~%================================================================================~%MSG: object_list/Classification~%float32 car~%float32 truck~%float32 motorcycle~%float32 bicycle~%float32 pedestrian~%float32 stacionary~%float32 other~%~%================================================================================~%MSG: object_list/Features~%uint8 FL~%uint8 FM~%uint8 FR~%uint8 MR~%uint8 RR~%uint8 RM~%uint8 RL~%uint8 ML~%~%================================================================================~%MSG: object_list/SensorProperty~%int32 sensor_id~%float64 sensortype~%float64 posx_variance~%float64 posy_variance~%float64 velx_variance~%float64 vely_variance~%float64 trust_existance~%float64 trust_car~%float64 trust_truck~%float64 trust_motorcycle~%float64 trust_bicycle~%float64 trust_pedestrian~%float64 trust_stationary~%float64 trust_other ~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ObjectsList)))
  "Returns full string definition for message of type 'ObjectsList"
  (cl:format cl:nil "Header header~%ObjectList[] obj_list~%SensorProperty sensor_property~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: object_list/ObjectList~%int32 obj_id~%float64 time~%Geometric geometric~%float64[36] covariance~%Dimension dimension~%float64 prop_existence~%float64 prop_nonexistence~%float64 prop_persistance~%float64 prop_mov ~%Classification classification~%float64[12] classification_mass~%Features features~%int64[] sensors_fused~%~%================================================================================~%MSG: object_list/Geometric~%float64 x~%float64 y~%float64 vx~%float64 vy~%float64 ax~%float64 ay~%float64 yaw~%float64 yawrate~%~%================================================================================~%MSG: object_list/Dimension~%float64 length~%float64 width~%float64 length_variance~%float64 width_variance~%~%~%================================================================================~%MSG: object_list/Classification~%float32 car~%float32 truck~%float32 motorcycle~%float32 bicycle~%float32 pedestrian~%float32 stacionary~%float32 other~%~%================================================================================~%MSG: object_list/Features~%uint8 FL~%uint8 FM~%uint8 FR~%uint8 MR~%uint8 RR~%uint8 RM~%uint8 RL~%uint8 ML~%~%================================================================================~%MSG: object_list/SensorProperty~%int32 sensor_id~%float64 sensortype~%float64 posx_variance~%float64 posy_variance~%float64 velx_variance~%float64 vely_variance~%float64 trust_existance~%float64 trust_car~%float64 trust_truck~%float64 trust_motorcycle~%float64 trust_bicycle~%float64 trust_pedestrian~%float64 trust_stationary~%float64 trust_other ~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ObjectsList>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'obj_list) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'sensor_property))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ObjectsList>))
  "Converts a ROS message object to a list"
  (cl:list 'ObjectsList
    (cl:cons ':header (header msg))
    (cl:cons ':obj_list (obj_list msg))
    (cl:cons ':sensor_property (sensor_property msg))
))
