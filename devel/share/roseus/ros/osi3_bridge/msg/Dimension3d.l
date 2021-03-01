;; Auto-generated. Do not edit!


(when (boundp 'osi3_bridge::Dimension3d)
  (if (not (find-package "OSI3_BRIDGE"))
    (make-package "OSI3_BRIDGE"))
  (shadow 'Dimension3d (find-package "OSI3_BRIDGE")))
(unless (find-package "OSI3_BRIDGE::DIMENSION3D")
  (make-package "OSI3_BRIDGE::DIMENSION3D"))

(in-package "ROS")
;;//! \htmlinclude Dimension3d.msg.html


(defclass osi3_bridge::Dimension3d
  :super ros::object
  :slots (_length _width _height ))

(defmethod osi3_bridge::Dimension3d
  (:init
   (&key
    ((:length __length) 0.0)
    ((:width __width) 0.0)
    ((:height __height) 0.0)
    )
   (send-super :init)
   (setq _length (float __length))
   (setq _width (float __width))
   (setq _height (float __height))
   self)
  (:length
   (&optional __length)
   (if __length (setq _length __length)) _length)
  (:width
   (&optional __width)
   (if __width (setq _width __width)) _width)
  (:height
   (&optional __height)
   (if __height (setq _height __height)) _height)
  (:serialization-length
   ()
   (+
    ;; float64 _length
    8
    ;; float64 _width
    8
    ;; float64 _height
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
     ;; float64 _height
       (sys::poke _height (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _length
     (setq _length (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _width
     (setq _width (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _height
     (setq _height (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get osi3_bridge::Dimension3d :md5sum-) "95f1c31b94fb56f33a669e4bf805939a")
(setf (get osi3_bridge::Dimension3d :datatype-) "osi3_bridge/Dimension3d")
(setf (get osi3_bridge::Dimension3d :definition-)
      "float64 length
float64 width
float64 height

")



(provide :osi3_bridge/Dimension3d "95f1c31b94fb56f33a669e4bf805939a")


