; Auto-generated. Do not edit!


(cl:in-package object_list-msg)


;//! \htmlinclude Dimension.msg.html

(cl:defclass <Dimension> (roslisp-msg-protocol:ros-message)
  ((length
    :reader length
    :initarg :length
    :type cl:float
    :initform 0.0)
   (width
    :reader width
    :initarg :width
    :type cl:float
    :initform 0.0)
   (length_variance
    :reader length_variance
    :initarg :length_variance
    :type cl:float
    :initform 0.0)
   (width_variance
    :reader width_variance
    :initarg :width_variance
    :type cl:float
    :initform 0.0))
)

(cl:defclass Dimension (<Dimension>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Dimension>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Dimension)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name object_list-msg:<Dimension> is deprecated: use object_list-msg:Dimension instead.")))

(cl:ensure-generic-function 'length-val :lambda-list '(m))
(cl:defmethod length-val ((m <Dimension>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:length-val is deprecated.  Use object_list-msg:length instead.")
  (length m))

(cl:ensure-generic-function 'width-val :lambda-list '(m))
(cl:defmethod width-val ((m <Dimension>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:width-val is deprecated.  Use object_list-msg:width instead.")
  (width m))

(cl:ensure-generic-function 'length_variance-val :lambda-list '(m))
(cl:defmethod length_variance-val ((m <Dimension>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:length_variance-val is deprecated.  Use object_list-msg:length_variance instead.")
  (length_variance m))

(cl:ensure-generic-function 'width_variance-val :lambda-list '(m))
(cl:defmethod width_variance-val ((m <Dimension>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader object_list-msg:width_variance-val is deprecated.  Use object_list-msg:width_variance instead.")
  (width_variance m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Dimension>) ostream)
  "Serializes a message object of type '<Dimension>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'length))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'width))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'length_variance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'width_variance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Dimension>) istream)
  "Deserializes a message object of type '<Dimension>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'length) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'width) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'length_variance) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'width_variance) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Dimension>)))
  "Returns string type for a message object of type '<Dimension>"
  "object_list/Dimension")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Dimension)))
  "Returns string type for a message object of type 'Dimension"
  "object_list/Dimension")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Dimension>)))
  "Returns md5sum for a message object of type '<Dimension>"
  "01a8c17587dd313244e2f2fd574d1415")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Dimension)))
  "Returns md5sum for a message object of type 'Dimension"
  "01a8c17587dd313244e2f2fd574d1415")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Dimension>)))
  "Returns full string definition for message of type '<Dimension>"
  (cl:format cl:nil "float64 length~%float64 width~%float64 length_variance~%float64 width_variance~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Dimension)))
  "Returns full string definition for message of type 'Dimension"
  (cl:format cl:nil "float64 length~%float64 width~%float64 length_variance~%float64 width_variance~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Dimension>))
  (cl:+ 0
     8
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Dimension>))
  "Converts a ROS message object to a list"
  (cl:list 'Dimension
    (cl:cons ':length (length msg))
    (cl:cons ':width (width msg))
    (cl:cons ':length_variance (length_variance msg))
    (cl:cons ':width_variance (width_variance msg))
))
