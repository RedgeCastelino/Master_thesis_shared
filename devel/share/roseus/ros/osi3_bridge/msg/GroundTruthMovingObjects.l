;; Auto-generated. Do not edit!


(when (boundp 'osi3_bridge::GroundTruthMovingObjects)
  (if (not (find-package "OSI3_BRIDGE"))
    (make-package "OSI3_BRIDGE"))
  (shadow 'GroundTruthMovingObjects (find-package "OSI3_BRIDGE")))
(unless (find-package "OSI3_BRIDGE::GROUNDTRUTHMOVINGOBJECTS")
  (make-package "OSI3_BRIDGE::GROUNDTRUTHMOVINGOBJECTS"))

(in-package "ROS")
;;//! \htmlinclude GroundTruthMovingObjects.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass osi3_bridge::GroundTruthMovingObjects
  :super ros::object
  :slots (_header _objects ))

(defmethod osi3_bridge::GroundTruthMovingObjects
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:objects __objects) (let (r) (dotimes (i 0) (push (instance osi3_bridge::MovingObject :init) r)) r))
    )
   (send-super :init)
   (setq _header __header)
   (setq _objects __objects)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:objects
   (&rest __objects)
   (if (keywordp (car __objects))
       (send* _objects __objects)
     (progn
       (if __objects (setq _objects (car __objects)))
       _objects)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; osi3_bridge/MovingObject[] _objects
    (apply #'+ (send-all _objects :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; osi3_bridge/MovingObject[] _objects
     (write-long (length _objects) s)
     (dolist (elem _objects)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; osi3_bridge/MovingObject[] _objects
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _objects (let (r) (dotimes (i n) (push (instance osi3_bridge::MovingObject :init) r)) r))
     (dolist (elem- _objects)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get osi3_bridge::GroundTruthMovingObjects :md5sum-) "b5c10f964cf85cf58aa709fc3567f543")
(setf (get osi3_bridge::GroundTruthMovingObjects :datatype-) "osi3_bridge/GroundTruthMovingObjects")
(setf (get osi3_bridge::GroundTruthMovingObjects :definition-)
      "Header header
osi3_bridge/MovingObject[] objects

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



(provide :osi3_bridge/GroundTruthMovingObjects "b5c10f964cf85cf58aa709fc3567f543")


