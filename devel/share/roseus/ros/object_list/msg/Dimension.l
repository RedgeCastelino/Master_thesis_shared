;; Auto-generated. Do not edit!


(when (boundp 'object_list::Dimension)
  (if (not (find-package "OBJECT_LIST"))
    (make-package "OBJECT_LIST"))
  (shadow 'Dimension (find-package "OBJECT_LIST")))
(unless (find-package "OBJECT_LIST::DIMENSION")
  (make-package "OBJECT_LIST::DIMENSION"))

(in-package "ROS")
;;//! \htmlinclude Dimension.msg.html


(defclass object_list::Dimension
  :super ros::object
  :slots (_length _width _length_variance _width_variance ))

(defmethod object_list::Dimension
  (:init
   (&key
    ((:length __length) 0.0)
    ((:width __width) 0.0)
    ((:length_variance __length_variance) 0.0)
    ((:width_variance __width_variance) 0.0)
    )
   (send-super :init)
   (setq _length (float __length))
   (setq _width (float __width))
   (setq _length_variance (float __length_variance))
   (setq _width_variance (float __width_variance))
   self)
  (:length
   (&optional __length)
   (if __length (setq _length __length)) _length)
  (:width
   (&optional __width)
   (if __width (setq _width __width)) _width)
  (:length_variance
   (&optional __length_variance)
   (if __length_variance (setq _length_variance __length_variance)) _length_variance)
  (:width_variance
   (&optional __width_variance)
   (if __width_variance (setq _width_variance __width_variance)) _width_variance)
  (:serialization-length
   ()
   (+
    ;; float64 _length
    8
    ;; float64 _width
    8
    ;; float64 _length_variance
    8
    ;; float64 _width_variance
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _length
       (sys::poke _length (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _width
       (sys::poke _width (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _length_variance
       (sys::poke _length_variance (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _width_variance
       (sys::poke _width_variance (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _length
     (setq _length (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _width
     (setq _width (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _length_variance
     (setq _length_variance (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _width_variance
     (setq _width_variance (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get object_list::Dimension :md5sum-) "01a8c17587dd313244e2f2fd574d1415")
(setf (get object_list::Dimension :datatype-) "object_list/Dimension")
(setf (get object_list::Dimension :definition-)
      "float64 length
float64 width
float64 length_variance
float64 width_variance


")



(provide :object_list/Dimension "01a8c17587dd313244e2f2fd574d1415")


