; Auto-generated. Do not edit!


(cl:in-package osi3_bridge-msg)


;//! \htmlinclude MovingObject.msg.html

(cl:defclass <MovingObject> (roslisp-msg-protocol:ros-message)
  ((id
    :reader id
    :initarg :id
    :type cl:integer
    :initform 0)
   (dimension
    :reader dimension
    :initarg :dimension
    :type osi3_bridge-msg:Dimension3d
    :initform (cl:make-instance 'osi3_bridge-msg:Dimension3d))
   (position
    :reader position
    :initarg :position
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (orientation
    :reader orientation
    :initarg :orientation
    :type osi3_bridge-msg:Orientation3d
    :initform (cl:make-instance 'osi3_bridge-msg:Orientation3d))
   (velocity
    :reader velocity
    :initarg :velocity
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (acceleration
    :reader acceleration
    :initarg :acceleration
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (type
    :reader type
    :initarg :type
    :type cl:fixnum
    :initform 0))
)

(cl:defclass MovingObject (<MovingObject>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MovingObject>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MovingObject)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name osi3_bridge-msg:<MovingObject> is deprecated: use osi3_bridge-msg:MovingObject instead.")))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <MovingObject>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader osi3_bridge-msg:id-val is deprecated.  Use osi3_bridge-msg:id instead.")
  (id m))

(cl:ensure-generic-function 'dimension-val :lambda-list '(m))
(cl:defmethod dimension-val ((m <MovingObject>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader osi3_bridge-msg:dimension-val is deprecated.  Use osi3_bridge-msg:dimension instead.")
  (dimension m))

(cl:ensure-generic-function 'position-val :lambda-list '(m))
(cl:defmethod position-val ((m <MovingObject>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader osi3_bridge-msg:position-val is deprecated.  Use osi3_bridge-msg:position instead.")
  (position m))

(cl:ensure-generic-function 'orientation-val :lambda-list '(m))
(cl:defmethod orientation-val ((m <MovingObject>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader osi3_bridge-msg:orientation-val is deprecated.  Use osi3_bridge-msg:orientation instead.")
  (orientation m))

(cl:ensure-generic-function 'velocity-val :lambda-list '(m))
(cl:defmethod velocity-val ((m <MovingObject>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader osi3_bridge-msg:velocity-val is deprecated.  Use osi3_bridge-msg:velocity instead.")
  (velocity m))

(cl:ensure-generic-function 'acceleration-val :lambda-list '(m))
(cl:defmethod acceleration-val ((m <MovingObject>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader osi3_bridge-msg:acceleration-val is deprecated.  Use osi3_bridge-msg:acceleration instead.")
  (acceleration m))

(cl:ensure-generic-function 'type-val :lambda-list '(m))
(cl:defmethod type-val ((m <MovingObject>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader osi3_bridge-msg:type-val is deprecated.  Use osi3_bridge-msg:type instead.")
  (type m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<MovingObject>)))
    "Constants for message type '<MovingObject>"
  '((:TYPE_UNKNOWN . 0)
    (:TYPE_OTHER . 1)
    (:TYPE_CAR . 2)
    (:TYPE_PEDESTRIAN . 3)
    (:TYPE_ANIMAL . 4)
    (:TYPE_TRUCK . 5)
    (:TYPE_TRAILER . 6)
    (:TYPE_MOTORBIKE . 7)
    (:TYPE_BICYCLE . 8)
    (:TYPE_BUS . 9)
    (:TYPE_TRAM . 10)
    (:TYPE_TRAIN . 11)
    (:TYPE_WHEELCHAIR . 12))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'MovingObject)))
    "Constants for message type 'MovingObject"
  '((:TYPE_UNKNOWN . 0)
    (:TYPE_OTHER . 1)
    (:TYPE_CAR . 2)
    (:TYPE_PEDESTRIAN . 3)
    (:TYPE_ANIMAL . 4)
    (:TYPE_TRUCK . 5)
    (:TYPE_TRAILER . 6)
    (:TYPE_MOTORBIKE . 7)
    (:TYPE_BICYCLE . 8)
    (:TYPE_BUS . 9)
    (:TYPE_TRAM . 10)
    (:TYPE_TRAIN . 11)
    (:TYPE_WHEELCHAIR . 12))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MovingObject>) ostream)
  "Serializes a message object of type '<MovingObject>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 32) (cl:slot-value msg 'id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 40) (cl:slot-value msg 'id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 48) (cl:slot-value msg 'id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 56) (cl:slot-value msg 'id)) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'dimension) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'position) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'orientation) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'velocity) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'acceleration) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'type)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MovingObject>) istream)
  "Deserializes a message object of type '<MovingObject>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 32) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 40) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 48) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 56) (cl:slot-value msg 'id)) (cl:read-byte istream))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'dimension) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'position) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'orientation) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'velocity) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'acceleration) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'type)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MovingObject>)))
  "Returns string type for a message object of type '<MovingObject>"
  "osi3_bridge/MovingObject")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MovingObject)))
  "Returns string type for a message object of type 'MovingObject"
  "osi3_bridge/MovingObject")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MovingObject>)))
  "Returns md5sum for a message object of type '<MovingObject>"
  "1d813c673962ef31735dd456446e05b5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MovingObject)))
  "Returns md5sum for a message object of type 'MovingObject"
  "1d813c673962ef31735dd456446e05b5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MovingObject>)))
  "Returns full string definition for message of type '<MovingObject>"
  (cl:format cl:nil "uint64 id~%osi3_bridge/Dimension3d dimension~%geometry_msgs/Vector3 position~%osi3_bridge/Orientation3d orientation~%geometry_msgs/Vector3 velocity~%geometry_msgs/Vector3 acceleration~%uint8 type~%~%uint8 TYPE_UNKNOWN = 0~%uint8 TYPE_OTHER = 1~%uint8 TYPE_CAR = 2~%uint8 TYPE_PEDESTRIAN = 3~%uint8 TYPE_ANIMAL = 4~%uint8 TYPE_TRUCK = 5~%uint8 TYPE_TRAILER = 6~%uint8 TYPE_MOTORBIKE = 7~%uint8 TYPE_BICYCLE = 8~%uint8 TYPE_BUS = 9~%uint8 TYPE_TRAM = 10~%uint8 TYPE_TRAIN = 11~%uint8 TYPE_WHEELCHAIR = 12~%~%~%================================================================================~%MSG: osi3_bridge/Dimension3d~%float64 length~%float64 width~%float64 height~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: osi3_bridge/Orientation3d~%float64 roll~%float64 pitch~%float64 yaw~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MovingObject)))
  "Returns full string definition for message of type 'MovingObject"
  (cl:format cl:nil "uint64 id~%osi3_bridge/Dimension3d dimension~%geometry_msgs/Vector3 position~%osi3_bridge/Orientation3d orientation~%geometry_msgs/Vector3 velocity~%geometry_msgs/Vector3 acceleration~%uint8 type~%~%uint8 TYPE_UNKNOWN = 0~%uint8 TYPE_OTHER = 1~%uint8 TYPE_CAR = 2~%uint8 TYPE_PEDESTRIAN = 3~%uint8 TYPE_ANIMAL = 4~%uint8 TYPE_TRUCK = 5~%uint8 TYPE_TRAILER = 6~%uint8 TYPE_MOTORBIKE = 7~%uint8 TYPE_BICYCLE = 8~%uint8 TYPE_BUS = 9~%uint8 TYPE_TRAM = 10~%uint8 TYPE_TRAIN = 11~%uint8 TYPE_WHEELCHAIR = 12~%~%~%================================================================================~%MSG: osi3_bridge/Dimension3d~%float64 length~%float64 width~%float64 height~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: osi3_bridge/Orientation3d~%float64 roll~%float64 pitch~%float64 yaw~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MovingObject>))
  (cl:+ 0
     8
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'dimension))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'position))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'orientation))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'velocity))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'acceleration))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MovingObject>))
  "Converts a ROS message object to a list"
  (cl:list 'MovingObject
    (cl:cons ':id (id msg))
    (cl:cons ':dimension (dimension msg))
    (cl:cons ':position (position msg))
    (cl:cons ':orientation (orientation msg))
    (cl:cons ':velocity (velocity msg))
    (cl:cons ':acceleration (acceleration msg))
    (cl:cons ':type (type msg))
))
