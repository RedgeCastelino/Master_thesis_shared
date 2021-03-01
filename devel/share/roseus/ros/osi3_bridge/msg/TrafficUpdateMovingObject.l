;; Auto-generated. Do not edit!


(when (boundp 'osi3_bridge::TrafficUpdateMovingObject)
  (if (not (find-package "OSI3_BRIDGE"))
    (make-package "OSI3_BRIDGE"))
  (shadow 'TrafficUpdateMovingObject (find-package "OSI3_BRIDGE")))
(unless (find-package "OSI3_BRIDGE::TRAFFICUPDATEMOVINGOBJECT")
  (make-package "OSI3_BRIDGE::TRAFFICUPDATEMOVINGOBJECT"))

(in-package "ROS")
;;//! \htmlinclude TrafficUpdateMovingObject.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass osi3_bridge::TrafficUpdateMovingObject
  :super ros::object
  :slots (_header _object ))

(defmethod osi3_bridge::TrafficUpdateMovingObject
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:object __object) (instance osi3_bridge::MovingObject :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _object __object)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:object
   (&rest __object)
   (if (keywordp (car __object))
       (send* _object __object)
     (progn
       (if __object (setq _object (car __object)))
       _object)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; osi3_bridge/MovingObject _object
    (send _object :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; osi3_bridge/MovingObject _object
       (send _object :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; osi3_bridge/MovingObject _object
     (send _object :deserialize buf ptr-) (incf ptr- (send _object :serialization-length))
   ;;
   self)
  )

(setf (get osi3_bridge::TrafficUpdateMovingObject :md5sum-) "b26e20bf46b692e8759e85b824c5ffc2")
(setf (get osi3_bridge::TrafficUpdateMovingObject :datatype-) "osi3_bridge/TrafficUpdateMovingObject")
(setf (get osi3_bridge::TrafficUpdateMovingObject :definition-)
      "Header header
osi3_bridge/MovingObject object

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: osi3_bridge/MovingObject
uint64 id
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



(provide :osi3_bridge/TrafficUpdateMovingObject "b26e20bf46b692e8759e85b824c5ffc2")


