;; Auto-generated. Do not edit!


(when (boundp 'object_list::ObjectsList)
  (if (not (find-package "OBJECT_LIST"))
    (make-package "OBJECT_LIST"))
  (shadow 'ObjectsList (find-package "OBJECT_LIST")))
(unless (find-package "OBJECT_LIST::OBJECTSLIST")
  (make-package "OBJECT_LIST::OBJECTSLIST"))

(in-package "ROS")
;;//! \htmlinclude ObjectsList.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass object_list::ObjectsList
  :super ros::object
  :slots (_header _obj_list _sensor_property ))

(defmethod object_list::ObjectsList
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:obj_list __obj_list) (let (r) (dotimes (i 0) (push (instance object_list::ObjectList :init) r)) r))
    ((:sensor_property __sensor_property) (instance object_list::SensorProperty :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _obj_list __obj_list)
   (setq _sensor_property __sensor_property)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:obj_list
   (&rest __obj_list)
   (if (keywordp (car __obj_list))
       (send* _obj_list __obj_list)
     (progn
       (if __obj_list (setq _obj_list (car __obj_list)))
       _obj_list)))
  (:sensor_property
   (&rest __sensor_property)
   (if (keywordp (car __sensor_property))
       (send* _sensor_property __sensor_property)
     (progn
       (if __sensor_property (setq _sensor_property (car __sensor_property)))
       _sensor_property)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; object_list/ObjectList[] _obj_list
    (apply #'+ (send-all _obj_list :serialization-length)) 4
    ;; object_list/SensorProperty _sensor_property
    (send _sensor_property :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; object_list/ObjectList[] _obj_list
     (write-long (length _obj_list) s)
     (dolist (elem _obj_list)
       (send elem :serialize s)
       )
     ;; object_list/SensorProperty _sensor_property
       (send _sensor_property :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; object_list/ObjectList[] _obj_list
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _obj_list (let (r) (dotimes (i n) (push (instance object_list::ObjectList :init) r)) r))
     (dolist (elem- _obj_list)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; object_list/SensorProperty _sensor_property
     (send _sensor_property :deserialize buf ptr-) (incf ptr- (send _sensor_property :serialization-length))
   ;;
   self)
  )

(setf (get object_list::ObjectsList :md5sum-) "d69ee6a3db897657f81853c8b3814ced")
(setf (get object_list::ObjectsList :datatype-) "object_list/ObjectsList")
(setf (get object_list::ObjectsList :definition-)
      "Header header
ObjectList[] obj_list
SensorProperty sensor_property

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
MSG: object_list/ObjectList
int32 obj_id
float64 time
Geometric geometric
float64[36] covariance
Dimension dimension
float64 prop_existence
float64 prop_nonexistence
float64 prop_persistance
float64 prop_mov 
Classification classification
float64[12] classification_mass
Features features
int64[] sensors_fused

================================================================================
MSG: object_list/Geometric
float64 x
float64 y
float64 vx
float64 vy
float64 ax
float64 ay
float64 yaw
float64 yawrate

================================================================================
MSG: object_list/Dimension
float64 length
float64 width
float64 length_variance
float64 width_variance


================================================================================
MSG: object_list/Classification
float32 car
float32 truck
float32 motorcycle
float32 bicycle
float32 pedestrian
float32 stacionary
float32 other

================================================================================
MSG: object_list/Features
uint8 FL
uint8 FM
uint8 FR
uint8 MR
uint8 RR
uint8 RM
uint8 RL
uint8 ML

================================================================================
MSG: object_list/SensorProperty
int32 sensor_id
float64 sensortype
float64 posx_variance
float64 posy_variance
float64 velx_variance
float64 vely_variance
float64 trust_existance
float64 trust_car
float64 trust_truck
float64 trust_motorcycle
float64 trust_bicycle
float64 trust_pedestrian
float64 trust_stationary
float64 trust_other 

")



(provide :object_list/ObjectsList "d69ee6a3db897657f81853c8b3814ced")


