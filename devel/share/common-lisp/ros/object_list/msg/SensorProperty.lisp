; Auto-generated. Do not edit!


(cl:in-package object_list-msg)


;//! \htmlinclude SensorProperty.msg.html

(cl:defclass <SensorProperty> (roslisp-msg-protocol:ros-message)
  ((sensor_id
    :reader sensor_id
    :initarg :sensor_id
    :type cl:integer
    :initform 0)
   (sensortype
    :reader sensortype
    :initarg :sensortype
    :type cl:float
    :initform 0.0)
   (posx_variance
    :reader posx_variance
    :initarg :posx_variance
    :type cl:float
    :initform 0.0)
   (posy_variance
    :reader posy_variance
    :initarg :posy_variance
    :type cl:float
    :initform 0.0)
   (velx_variance
    :reader velx_variance
    :initarg :velx_variance
    :type cl:float
    :initform 0.0)
   (vely_variance
    :reader vely_variance
    :initarg :vely_variance
    :type cl:float
    :initform 0.0)
   (trust_existance
    :reader trust_existance
    :initarg :trust_existance
    :type cl:float
    :initform 0.0)
   (trust_car
    :reader trust_car
    :initarg :trust_car
    :type cl:float
    :initform 0.0)
   (trust_truck
    :reader trust_truck
    :initarg :trust_truck
    :type cl:float
    :initform 0.0)
   (trust_motorcycle
    :reader trust_motorcycle
    :initarg :trust_motorcycle
    :type cl:float
    :initform 0.0)
   (trust_bicycle
    :reader trust_bicycle
    :initarg :trust_bicycle
    :type cl:float
    :initform 0.0)
   (trust_pedestrian
    :reader trust_pedestrian
    :initarg :trust_pedestrian
    :type cl:float
    :initform 0.0)
   (trust_stationary
    :reader trust_stationary
    :initarg :trust_stationary
    :type cl:float
    :initform 0.0)
   (trust_other
    :reader trust_other
    :initarg :trust_other
    :type cl:float
    :initform 0.0))
)

(cl:defclass SensorProperty (<SensorProperty>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SensorProperty>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SensorProperty)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name object_list-msg:<SensorProperty> is deprecated: use object_list-msg:SensorProperty instead.")))

(cl:ensure-generic-function 'sensor_id-val :lambda-list '(m))
(cl:defmethod sensor_id-val ((m <SensorProperty>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:sensor_id-val is deprecated.  Use object_list-msg:sensor_id instead.")
  (sensor_id m))

(cl:ensure-generic-function 'sensortype-val :lambda-list '(m))
(cl:defmethod sensortype-val ((m <SensorProperty>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:sensortype-val is deprecated.  Use object_list-msg:sensortype instead.")
  (sensortype m))

(cl:ensure-generic-function 'posx_variance-val :lambda-list '(m))
(cl:defmethod posx_variance-val ((m <SensorProperty>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:posx_variance-val is deprecated.  Use object_list-msg:posx_variance instead.")
  (posx_variance m))

(cl:ensure-generic-function 'posy_variance-val :lambda-list '(m))
(cl:defmethod posy_variance-val ((m <SensorProperty>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:posy_variance-val is deprecated.  Use object_list-msg:posy_variance instead.")
  (posy_variance m))

(cl:ensure-generic-function 'velx_variance-val :lambda-list '(m))
(cl:defmethod velx_variance-val ((m <SensorProperty>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:velx_variance-val is deprecated.  Use object_list-msg:velx_variance instead.")
  (velx_variance m))

(cl:ensure-generic-function 'vely_variance-val :lambda-list '(m))
(cl:defmethod vely_variance-val ((m <SensorProperty>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:vely_variance-val is deprecated.  Use object_list-msg:vely_variance instead.")
  (vely_variance m))

(cl:ensure-generic-function 'trust_existance-val :lambda-list '(m))
(cl:defmethod trust_existance-val ((m <SensorProperty>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:trust_existance-val is deprecated.  Use object_list-msg:trust_existance instead.")
  (trust_existance m))

(cl:ensure-generic-function 'trust_car-val :lambda-list '(m))
(cl:defmethod trust_car-val ((m <SensorProperty>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:trust_car-val is deprecated.  Use object_list-msg:trust_car instead.")
  (trust_car m))

(cl:ensure-generic-function 'trust_truck-val :lambda-list '(m))
(cl:defmethod trust_truck-val ((m <SensorProperty>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:trust_truck-val is deprecated.  Use object_list-msg:trust_truck instead.")
  (trust_truck m))

(cl:ensure-generic-function 'trust_motorcycle-val :lambda-list '(m))
(cl:defmethod trust_motorcycle-val ((m <SensorProperty>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:trust_motorcycle-val is deprecated.  Use object_list-msg:trust_motorcycle instead.")
  (trust_motorcycle m))

(cl:ensure-generic-function 'trust_bicycle-val :lambda-list '(m))
(cl:defmethod trust_bicycle-val ((m <SensorProperty>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:trust_bicycle-val is deprecated.  Use object_list-msg:trust_bicycle instead.")
  (trust_bicycle m))

(cl:ensure-generic-function 'trust_pedestrian-val :lambda-list '(m))
(cl:defmethod trust_pedestrian-val ((m <SensorProperty>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:trust_pedestrian-val is deprecated.  Use object_list-msg:trust_pedestrian instead.")
  (trust_pedestrian m))

(cl:ensure-generic-function 'trust_stationary-val :lambda-list '(m))
(cl:defmethod trust_stationary-val ((m <SensorProperty>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:trust_stationary-val is deprecated.  Use object_list-msg:trust_stationary instead.")
  (trust_stationary m))

(cl:ensure-generic-function 'trust_other-val :lambda-list '(m))
(cl:defmethod trust_other-val ((m <SensorProperty>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:trust_other-val is deprecated.  Use object_list-msg:trust_other instead.")
  (trust_other m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SensorProperty>) ostream)
  "Serializes a message object of type '<SensorProperty>"
  (cl:let* ((signed (cl:slot-value msg 'sensor_id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'sensortype))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'posx_variance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'posy_variance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'velx_variance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'vely_variance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'trust_existance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'trust_car))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'trust_truck))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'trust_motorcycle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'trust_bicycle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'trust_pedestrian))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'trust_stationary))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'trust_other))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SensorProperty>) istream)
  "Deserializes a message object of type '<SensorProperty>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'sensor_id) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'sensortype) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'posx_variance) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'posy_variance) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'velx_variance) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'vely_variance) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'trust_existance) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'trust_car) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'trust_truck) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'trust_motorcycle) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'trust_bicycle) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'trust_pedestrian) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'trust_stationary) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'trust_other) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SensorProperty>)))
  "Returns string type for a message object of type '<SensorProperty>"
  "object_list/SensorProperty")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SensorProperty)))
  "Returns string type for a message object of type 'SensorProperty"
  "object_list/SensorProperty")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SensorProperty>)))
  "Returns md5sum for a message object of type '<SensorProperty>"
  "b92131fc47bc49b0227fc3ddb6760ee8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SensorProperty)))
  "Returns md5sum for a message object of type 'SensorProperty"
  "b92131fc47bc49b0227fc3ddb6760ee8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SensorProperty>)))
  "Returns full string definition for message of type '<SensorProperty>"
  (cl:format cl:nil "int32 sensor_id~%float64 sensortype~%float64 posx_variance~%float64 posy_variance~%float64 velx_variance~%float64 vely_variance~%float64 trust_existance~%float64 trust_car~%float64 trust_truck~%float64 trust_motorcycle~%float64 trust_bicycle~%float64 trust_pedestrian~%float64 trust_stationary~%float64 trust_other ~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SensorProperty)))
  "Returns full string definition for message of type 'SensorProperty"
  (cl:format cl:nil "int32 sensor_id~%float64 sensortype~%float64 posx_variance~%float64 posy_variance~%float64 velx_variance~%float64 vely_variance~%float64 trust_existance~%float64 trust_car~%float64 trust_truck~%float64 trust_motorcycle~%float64 trust_bicycle~%float64 trust_pedestrian~%float64 trust_stationary~%float64 trust_other ~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SensorProperty>))
  (cl:+ 0
     4
     8
     8
     8
     8
     8
     8
     8
     8
     8
     8
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SensorProperty>))
  "Converts a ROS message object to a list"
  (cl:list 'SensorProperty
    (cl:cons ':sensor_id (sensor_id msg))
    (cl:cons ':sensortype (sensortype msg))
    (cl:cons ':posx_variance (posx_variance msg))
    (cl:cons ':posy_variance (posy_variance msg))
    (cl:cons ':velx_variance (velx_variance msg))
    (cl:cons ':vely_variance (vely_variance msg))
    (cl:cons ':trust_existance (trust_existance msg))
    (cl:cons ':trust_car (trust_car msg))
    (cl:cons ':trust_truck (trust_truck msg))
    (cl:cons ':trust_motorcycle (trust_motorcycle msg))
    (cl:cons ':trust_bicycle (trust_bicycle msg))
    (cl:cons ':trust_pedestrian (trust_pedestrian msg))
    (cl:cons ':trust_stationary (trust_stationary msg))
    (cl:cons ':trust_other (trust_other msg))
))
