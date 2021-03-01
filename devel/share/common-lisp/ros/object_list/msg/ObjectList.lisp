; Auto-generated. Do not edit!


(cl:in-package object_list-msg)


;//! \htmlinclude ObjectList.msg.html

(cl:defclass <ObjectList> (roslisp-msg-protocol:ros-message)
  ((obj_id
    :reader obj_id
    :initarg :obj_id
    :type cl:integer
    :initform 0)
   (time
    :reader time
    :initarg :time
    :type cl:float
    :initform 0.0)
   (geometric
    :reader geometric
    :initarg :geometric
    :type object_list-msg:Geometric
    :initform (cl:make-instance 'object_list-msg:Geometric))
   (covariance
    :reader covariance
    :initarg :covariance
    :type (cl:vector cl:float)
   :initform (cl:make-array 36 :element-type 'cl:float :initial-element 0.0))
   (dimension
    :reader dimension
    :initarg :dimension
    :type object_list-msg:Dimension
    :initform (cl:make-instance 'object_list-msg:Dimension))
   (prop_existence
    :reader prop_existence
    :initarg :prop_existence
    :type cl:float
    :initform 0.0)
   (prop_nonexistence
    :reader prop_nonexistence
    :initarg :prop_nonexistence
    :type cl:float
    :initform 0.0)
   (prop_persistance
    :reader prop_persistance
    :initarg :prop_persistance
    :type cl:float
    :initform 0.0)
   (prop_mov
    :reader prop_mov
    :initarg :prop_mov
    :type cl:float
    :initform 0.0)
   (classification
    :reader classification
    :initarg :classification
    :type object_list-msg:Classification
    :initform (cl:make-instance 'object_list-msg:Classification))
   (classification_mass
    :reader classification_mass
    :initarg :classification_mass
    :type (cl:vector cl:float)
   :initform (cl:make-array 12 :element-type 'cl:float :initial-element 0.0))
   (features
    :reader features
    :initarg :features
    :type object_list-msg:Features
    :initform (cl:make-instance 'object_list-msg:Features))
   (sensors_fused
    :reader sensors_fused
    :initarg :sensors_fused
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass ObjectList (<ObjectList>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ObjectList>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ObjectList)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name object_list-msg:<ObjectList> is deprecated: use object_list-msg:ObjectList instead.")))

(cl:ensure-generic-function 'obj_id-val :lambda-list '(m))
(cl:defmethod obj_id-val ((m <ObjectList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:obj_id-val is deprecated.  Use object_list-msg:obj_id instead.")
  (obj_id m))

(cl:ensure-generic-function 'time-val :lambda-list '(m))
(cl:defmethod time-val ((m <ObjectList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:time-val is deprecated.  Use object_list-msg:time instead.")
  (time m))

(cl:ensure-generic-function 'geometric-val :lambda-list '(m))
(cl:defmethod geometric-val ((m <ObjectList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:geometric-val is deprecated.  Use object_list-msg:geometric instead.")
  (geometric m))

(cl:ensure-generic-function 'covariance-val :lambda-list '(m))
(cl:defmethod covariance-val ((m <ObjectList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:covariance-val is deprecated.  Use object_list-msg:covariance instead.")
  (covariance m))

(cl:ensure-generic-function 'dimension-val :lambda-list '(m))
(cl:defmethod dimension-val ((m <ObjectList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:dimension-val is deprecated.  Use object_list-msg:dimension instead.")
  (dimension m))

(cl:ensure-generic-function 'prop_existence-val :lambda-list '(m))
(cl:defmethod prop_existence-val ((m <ObjectList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:prop_existence-val is deprecated.  Use object_list-msg:prop_existence instead.")
  (prop_existence m))

(cl:ensure-generic-function 'prop_nonexistence-val :lambda-list '(m))
(cl:defmethod prop_nonexistence-val ((m <ObjectList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:prop_nonexistence-val is deprecated.  Use object_list-msg:prop_nonexistence instead.")
  (prop_nonexistence m))

(cl:ensure-generic-function 'prop_persistance-val :lambda-list '(m))
(cl:defmethod prop_persistance-val ((m <ObjectList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:prop_persistance-val is deprecated.  Use object_list-msg:prop_persistance instead.")
  (prop_persistance m))

(cl:ensure-generic-function 'prop_mov-val :lambda-list '(m))
(cl:defmethod prop_mov-val ((m <ObjectList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:prop_mov-val is deprecated.  Use object_list-msg:prop_mov instead.")
  (prop_mov m))

(cl:ensure-generic-function 'classification-val :lambda-list '(m))
(cl:defmethod classification-val ((m <ObjectList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:classification-val is deprecated.  Use object_list-msg:classification instead.")
  (classification m))

(cl:ensure-generic-function 'classification_mass-val :lambda-list '(m))
(cl:defmethod classification_mass-val ((m <ObjectList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:classification_mass-val is deprecated.  Use object_list-msg:classification_mass instead.")
  (classification_mass m))

(cl:ensure-generic-function 'features-val :lambda-list '(m))
(cl:defmethod features-val ((m <ObjectList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:features-val is deprecated.  Use object_list-msg:features instead.")
  (features m))

(cl:ensure-generic-function 'sensors_fused-val :lambda-list '(m))
(cl:defmethod sensors_fused-val ((m <ObjectList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:sensors_fused-val is deprecated.  Use object_list-msg:sensors_fused instead.")
  (sensors_fused m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ObjectList>) ostream)
  "Serializes a message object of type '<ObjectList>"
  (cl:let* ((signed (cl:slot-value msg 'obj_id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'time))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'geometric) ostream)
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'covariance))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'dimension) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'prop_existence))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'prop_nonexistence))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'prop_persistance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'prop_mov))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'classification) ostream)
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'classification_mass))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'features) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'sensors_fused))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    ))
   (cl:slot-value msg 'sensors_fused))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ObjectList>) istream)
  "Deserializes a message object of type '<ObjectList>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'obj_id) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'time) (roslisp-utils:decode-double-float-bits bits)))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'geometric) istream)
  (cl:setf (cl:slot-value msg 'covariance) (cl:make-array 36))
  (cl:let ((vals (cl:slot-value msg 'covariance)))
    (cl:dotimes (i 36)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'dimension) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'prop_existence) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'prop_nonexistence) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'prop_persistance) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'prop_mov) (roslisp-utils:decode-double-float-bits bits)))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'classification) istream)
  (cl:setf (cl:slot-value msg 'classification_mass) (cl:make-array 12))
  (cl:let ((vals (cl:slot-value msg 'classification_mass)))
    (cl:dotimes (i 12)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'features) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'sensors_fused) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'sensors_fused)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ObjectList>)))
  "Returns string type for a message object of type '<ObjectList>"
  "object_list/ObjectList")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ObjectList)))
  "Returns string type for a message object of type 'ObjectList"
  "object_list/ObjectList")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ObjectList>)))
  "Returns md5sum for a message object of type '<ObjectList>"
  "d5793b04b71b063f6fee4d02602a19de")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ObjectList)))
  "Returns md5sum for a message object of type 'ObjectList"
  "d5793b04b71b063f6fee4d02602a19de")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ObjectList>)))
  "Returns full string definition for message of type '<ObjectList>"
  (cl:format cl:nil "int32 obj_id~%float64 time~%Geometric geometric~%float64[36] covariance~%Dimension dimension~%float64 prop_existence~%float64 prop_nonexistence~%float64 prop_persistance~%float64 prop_mov ~%Classification classification~%float64[12] classification_mass~%Features features~%int64[] sensors_fused~%~%================================================================================~%MSG: object_list/Geometric~%float64 x~%float64 y~%float64 vx~%float64 vy~%float64 ax~%float64 ay~%float64 yaw~%float64 yawrate~%~%================================================================================~%MSG: object_list/Dimension~%float64 length~%float64 width~%float64 length_variance~%float64 width_variance~%~%~%================================================================================~%MSG: object_list/Classification~%float32 car~%float32 truck~%float32 motorcycle~%float32 bicycle~%float32 pedestrian~%float32 stacionary~%float32 other~%~%================================================================================~%MSG: object_list/Features~%uint8 FL~%uint8 FM~%uint8 FR~%uint8 MR~%uint8 RR~%uint8 RM~%uint8 RL~%uint8 ML~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ObjectList)))
  "Returns full string definition for message of type 'ObjectList"
  (cl:format cl:nil "int32 obj_id~%float64 time~%Geometric geometric~%float64[36] covariance~%Dimension dimension~%float64 prop_existence~%float64 prop_nonexistence~%float64 prop_persistance~%float64 prop_mov ~%Classification classification~%float64[12] classification_mass~%Features features~%int64[] sensors_fused~%~%================================================================================~%MSG: object_list/Geometric~%float64 x~%float64 y~%float64 vx~%float64 vy~%float64 ax~%float64 ay~%float64 yaw~%float64 yawrate~%~%================================================================================~%MSG: object_list/Dimension~%float64 length~%float64 width~%float64 length_variance~%float64 width_variance~%~%~%================================================================================~%MSG: object_list/Classification~%float32 car~%float32 truck~%float32 motorcycle~%float32 bicycle~%float32 pedestrian~%float32 stacionary~%float32 other~%~%================================================================================~%MSG: object_list/Features~%uint8 FL~%uint8 FM~%uint8 FR~%uint8 MR~%uint8 RR~%uint8 RM~%uint8 RL~%uint8 ML~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ObjectList>))
  (cl:+ 0
     4
     8
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'geometric))
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'covariance) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'dimension))
     8
     8
     8
     8
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'classification))
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'classification_mass) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'features))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'sensors_fused) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ObjectList>))
  "Converts a ROS message object to a list"
  (cl:list 'ObjectList
    (cl:cons ':obj_id (obj_id msg))
    (cl:cons ':time (time msg))
    (cl:cons ':geometric (geometric msg))
    (cl:cons ':covariance (covariance msg))
    (cl:cons ':dimension (dimension msg))
    (cl:cons ':prop_existence (prop_existence msg))
    (cl:cons ':prop_nonexistence (prop_nonexistence msg))
    (cl:cons ':prop_persistance (prop_persistance msg))
    (cl:cons ':prop_mov (prop_mov msg))
    (cl:cons ':classification (classification msg))
    (cl:cons ':classification_mass (classification_mass msg))
    (cl:cons ':features (features msg))
    (cl:cons ':sensors_fused (sensors_fused msg))
))
