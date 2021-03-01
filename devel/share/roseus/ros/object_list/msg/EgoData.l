;; Auto-generated. Do not edit!


(when (boundp 'object_list::EgoData)
  (if (not (find-package "OBJECT_LIST"))
    (make-package "OBJECT_LIST"))
  (shadow 'EgoData (find-package "OBJECT_LIST")))
(unless (find-package "OBJECT_LIST::EGODATA")
  (make-package "OBJECT_LIST::EGODATA"))

(in-package "ROS")
;;//! \htmlinclude EgoData.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass object_list::EgoData
  :super ros::object
  :slots (_header _geometric _dimension ))

(defmethod object_list::EgoData
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:geometric __geometric) (instance object_list::Geometric :init))
    ((:dimension __dimension) (instance object_list::Dimension :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _geometric __geometric)
   (setq _dimension __dimension)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:geometric
   (&rest __geometric)
   (if (keywordp (car __geometric))
       (send* _geometric __geometric)
     (progn
       (if __geometric (setq _geometric (car __geometric)))
       _geometric)))
  (:dimension
   (&rest __dimension)
   (if (keywordp (car __dimension))
       (send* _dimension __dimension)
     (progn
       (if __dimension (setq _dimension (car __dimension)))
       _dimension)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; object_list/Geometric _geometric
    (send _geometric :serialization-length)
    ;; object_list/Dimension _dimension
    (send _dimension :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; object_list/Geometric _geometric
       (send _geometric :serialize s)
     ;; object_list/Dimension _dimension
       (send _dimension :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; object_list/Geometric _geometric
     (send _geometric :deserialize buf ptr-) (incf ptr- (send _geometric :serialization-length))
   ;; object_list/Dimension _dimension
     (send _dimension :deserialize buf ptr-) (incf ptr- (send _dimension :serialization-length))
   ;;
   self)
  )

(setf (get object_list::EgoData :md5sum-) "e7e294d9eaab8d77f6809dd7e07899e8")
(setf (get object_list::EgoData :datatype-) "object_list/EgoData")
(setf (get object_list::EgoData :definition-)
      "Header header
object_list/Geometric geometric
object_list/Dimension dimension


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


")



(provide :object_list/EgoData "e7e294d9eaab8d77f6809dd7e07899e8")


