;; Auto-generated. Do not edit!


(when (boundp 'osi3_bridge::MovingObject)
  (if (not (find-package "OSI3_BRIDGE"))
    (make-package "OSI3_BRIDGE"))
  (shadow 'MovingObject (find-package "OSI3_BRIDGE")))
(unless (find-package "OSI3_BRIDGE::MOVINGOBJECT")
  (make-package "OSI3_BRIDGE::MOVINGOBJECT"))

(in-package "ROS")
;;//! \htmlinclude MovingObject.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(intern "*TYPE_UNKNOWN*" (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(shadow '*TYPE_UNKNOWN* (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(defconstant osi3_bridge::MovingObject::*TYPE_UNKNOWN* 0)
(intern "*TYPE_OTHER*" (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(shadow '*TYPE_OTHER* (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(defconstant osi3_bridge::MovingObject::*TYPE_OTHER* 1)
(intern "*TYPE_CAR*" (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(shadow '*TYPE_CAR* (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(defconstant osi3_bridge::MovingObject::*TYPE_CAR* 2)
(intern "*TYPE_PEDESTRIAN*" (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(shadow '*TYPE_PEDESTRIAN* (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(defconstant osi3_bridge::MovingObject::*TYPE_PEDESTRIAN* 3)
(intern "*TYPE_ANIMAL*" (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(shadow '*TYPE_ANIMAL* (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(defconstant osi3_bridge::MovingObject::*TYPE_ANIMAL* 4)
(intern "*TYPE_TRUCK*" (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(shadow '*TYPE_TRUCK* (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(defconstant osi3_bridge::MovingObject::*TYPE_TRUCK* 5)
(intern "*TYPE_TRAILER*" (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(shadow '*TYPE_TRAILER* (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(defconstant osi3_bridge::MovingObject::*TYPE_TRAILER* 6)
(intern "*TYPE_MOTORBIKE*" (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(shadow '*TYPE_MOTORBIKE* (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(defconstant osi3_bridge::MovingObject::*TYPE_MOTORBIKE* 7)
(intern "*TYPE_BICYCLE*" (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(shadow '*TYPE_BICYCLE* (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(defconstant osi3_bridge::MovingObject::*TYPE_BICYCLE* 8)
(intern "*TYPE_BUS*" (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(shadow '*TYPE_BUS* (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(defconstant osi3_bridge::MovingObject::*TYPE_BUS* 9)
(intern "*TYPE_TRAM*" (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(shadow '*TYPE_TRAM* (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(defconstant osi3_bridge::MovingObject::*TYPE_TRAM* 10)
(intern "*TYPE_TRAIN*" (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(shadow '*TYPE_TRAIN* (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(defconstant osi3_bridge::MovingObject::*TYPE_TRAIN* 11)
(intern "*TYPE_WHEELCHAIR*" (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(shadow '*TYPE_WHEELCHAIR* (find-package "OSI3_BRIDGE::MOVINGOBJECT"))
(defconstant osi3_bridge::MovingObject::*TYPE_WHEELCHAIR* 12)
(defclass osi3_bridge::MovingObject
  :super ros::object
  :slots (_id _dimension _position _orientation _velocity _acceleration _type ))

(defmethod osi3_bridge::MovingObject
  (:init
   (&key
    ((:id __id) 0)
    ((:dimension __dimension) (instance osi3_bridge::Dimension3d :init))
    ((:position __position) (instance geometry_msgs::Vector3 :init))
    ((:orientation __orientation) (instance osi3_bridge::Orientation3d :init))
    ((:velocity __velocity) (instance geometry_msgs::Vector3 :init))
    ((:acceleration __acceleration) (instance geometry_msgs::Vector3 :init))
    ((:type __type) 0)
    )
   (send-super :init)
   (setq _id (round __id))
   (setq _dimension __dimension)
   (setq _position __position)
   (setq _orientation __orientation)
   (setq _velocity __velocity)
   (setq _acceleration __acceleration)
   (setq _type (round __type))
   self)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:dimension
   (&rest __dimension)
   (if (keywordp (car __dimension))
       (send* _dimension __dimension)
     (progn
       (if __dimension (setq _dimension (car __dimension)))
       _dimension)))
  (:position
   (&rest __position)
   (if (keywordp (car __position))
       (send* _position __position)
     (progn
       (if __position (setq _position (car __position)))
       _position)))
  (:orientation
   (&rest __orientation)
   (if (keywordp (car __orientation))
       (send* _orientation __orientation)
     (progn
       (if __orientation (setq _orientation (car __orientation)))
       _orientation)))
  (:velocity
   (&rest __velocity)
   (if (keywordp (car __velocity))
       (send* _velocity __velocity)
     (progn
       (if __velocity (setq _velocity (car __velocity)))
       _velocity)))
  (:acceleration
   (&rest __acceleration)
   (if (keywordp (car __acceleration))
       (send* _acceleration __acceleration)
     (progn
       (if __acceleration (setq _acceleration (car __acceleration)))
       _acceleration)))
  (:type
   (&optional __type)
   (if __type (setq _type __type)) _type)
  (:serialization-length
   ()
   (+
    ;; uint64 _id
    8
    ;; osi3_bridge/Dimension3d _dimension
    (send _dimension :serialization-length)
    ;; geometry_msgs/Vector3 _position
    (send _position :serialization-length)
    ;; osi3_bridge/Orientation3d _orientation
    (send _orientation :serialization-length)
    ;; geometry_msgs/Vector3 _velocity
    (send _velocity :serialization-length)
    ;; geometry_msgs/Vector3 _acceleration
    (send _acceleration :serialization-length)
    ;; uint8 _type
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint64 _id
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _id (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _id) (= (length (_id . bv)) 2)) ;; bignum
              (write-long (ash (elt (_id . bv) 0) 0) s)
              (write-long (ash (elt (_id . bv) 1) -1) s))
             ((and (class _id) (= (length (_id . bv)) 1)) ;; big1
              (write-long (elt (_id . bv) 0) s)
              (write-long (if (>= _id 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _id s)(write-long (if (>= _id 0) 0 #xffffffff) s)))
     ;; osi3_bridge/Dimension3d _dimension
       (send _dimension :serialize s)
     ;; geometry_msgs/Vector3 _position
       (send _position :serialize s)
     ;; osi3_bridge/Orientation3d _orientation
       (send _orientation :serialize s)
     ;; geometry_msgs/Vector3 _velocity
       (send _velocity :serialize s)
     ;; geometry_msgs/Vector3 _acceleration
       (send _acceleration :serialize s)
     ;; uint8 _type
       (write-byte _type s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint64 _id
     
#+(or :alpha :irix6 :x86_64)
      (setf _id (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _id (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; osi3_bridge/Dimension3d _dimension
     (send _dimension :deserialize buf ptr-) (incf ptr- (send _dimension :serialization-length))
   ;; geometry_msgs/Vector3 _position
     (send _position :deserialize buf ptr-) (incf ptr- (send _position :serialization-length))
   ;; osi3_bridge/Orientation3d _orientation
     (send _orientation :deserialize buf ptr-) (incf ptr- (send _orientation :serialization-length))
   ;; geometry_msgs/Vector3 _velocity
     (send _velocity :deserialize buf ptr-) (incf ptr- (send _velocity :serialization-length))
   ;; geometry_msgs/Vector3 _acceleration
     (send _acceleration :deserialize buf ptr-) (incf ptr- (send _acceleration :serialization-length))
   ;; uint8 _type
     (setq _type (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get osi3_bridge::MovingObject :md5sum-) "1d813c673962ef31735dd456446e05b5")
(setf (get osi3_bridge::MovingObject :datatype-) "osi3_bridge/MovingObject")
(setf (get osi3_bridge::MovingObject :definition-)
      "uint64 id
osi3_bridge/Dimension3d dimension
geometry_msgs/Vector3 position
osi3_bridge/Orientation3d orientation
geometry_msgs/Vector3 velocity
geometry_msgs/Vector3 acceleration
uint8 type

uint8 TYPE_UNKNOWN = 0
uint8 TYPE_OTHER = 1
uint8 TYPE_CAR = 2
uint8 TYPE_PEDESTRIAN = 3
uint8 TYPE_ANIMAL = 4
uint8 TYPE_TRUCK = 5
uint8 TYPE_TRAILER = 6
uint8 TYPE_MOTORBIKE = 7
uint8 TYPE_BICYCLE = 8
uint8 TYPE_BUS = 9
uint8 TYPE_TRAM = 10
uint8 TYPE_TRAIN = 11
uint8 TYPE_WHEELCHAIR = 12


================================================================================
MSG: osi3_bridge/Dimension3d
float64 length
float64 width
float64 height

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: osi3_bridge/Orientation3d
float64 roll
float64 pitch
float64 yaw

")



(provide :osi3_bridge/MovingObject "1d813c673962ef31735dd456446e05b5")


