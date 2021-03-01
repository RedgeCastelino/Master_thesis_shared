; Auto-generated. Do not edit!


(cl:in-package object_list-msg)


;//! \htmlinclude EgoData.msg.html

(cl:defclass <EgoData> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (geometric
    :reader geometric
    :initarg :geometric
    :type object_list-msg:Geometric
    :initform (cl:make-instance 'object_list-msg:Geometric))
   (dimension
    :reader dimension
    :initarg :dimension
    :type object_list-msg:Dimension
    :initform (cl:make-instance 'object_list-msg:Dimension)))
)

(cl:defclass EgoData (<EgoData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <EgoData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'EgoData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name object_list-msg:<EgoData> is deprecated: use object_list-msg:EgoData instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <EgoData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:header-val is deprecated.  Use object_list-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'geometric-val :lambda-list '(m))
(cl:defmethod geometric-val ((m <EgoData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:geometric-val is deprecated.  Use object_list-msg:geometric instead.")
  (geometric m))

(cl:ensure-generic-function 'dimension-val :lambda-list '(m))
(cl:defmethod dimension-val ((m <EgoData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:dimension-val is deprecated.  Use object_list-msg:dimension instead.")
  (dimension m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <EgoData>) ostream)
  "Serializes a message object of type '<EgoData>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'geometric) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'dimension) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <EgoData>) istream)
  "Deserializes a message object of type '<EgoData>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'geometric) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'dimension) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<EgoData>)))
  "Returns string type for a message object of type '<EgoData>"
  "object_list/EgoData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'EgoData)))
  "Returns string type for a message object of type 'EgoData"
  "object_list/EgoData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<EgoData>)))
  "Returns md5sum for a message object of type '<EgoData>"
  "e7e294d9eaab8d77f6809dd7e07899e8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'EgoData)))
  "Returns md5sum for a message object of type 'EgoData"
  "e7e294d9eaab8d77f6809dd7e07899e8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<EgoData>)))
  "Returns full string definition for message of type '<EgoData>"
  (cl:format cl:nil "Header header~%object_list/Geometric geometric~%object_list/Dimension dimension~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: object_list/Geometric~%float64 x~%float64 y~%float64 vx~%float64 vy~%float64 ax~%float64 ay~%float64 yaw~%float64 yawrate~%~%================================================================================~%MSG: object_list/Dimension~%float64 length~%float64 width~%float64 length_variance~%float64 width_variance~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'EgoData)))
  "Returns full string definition for message of type 'EgoData"
  (cl:format cl:nil "Header header~%object_list/Geometric geometric~%object_list/Dimension dimension~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: object_list/Geometric~%float64 x~%float64 y~%float64 vx~%float64 vy~%float64 ax~%float64 ay~%float64 yaw~%float64 yawrate~%~%================================================================================~%MSG: object_list/Dimension~%float64 length~%float64 width~%float64 length_variance~%float64 width_variance~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <EgoData>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'geometric))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'dimension))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <EgoData>))
  "Converts a ROS message object to a list"
  (cl:list 'EgoData
    (cl:cons ':header (header msg))
    (cl:cons ':geometric (geometric msg))
    (cl:cons ':dimension (dimension msg))
))
