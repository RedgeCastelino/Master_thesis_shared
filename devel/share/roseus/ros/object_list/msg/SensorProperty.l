;; Auto-generated. Do not edit!


(when (boundp 'object_list::SensorProperty)
  (if (not (find-package "OBJECT_LIST"))
    (make-package "OBJECT_LIST"))
  (shadow 'SensorProperty (find-package "OBJECT_LIST")))
(unless (find-package "OBJECT_LIST::SENSORPROPERTY")
  (make-package "OBJECT_LIST::SENSORPROPERTY"))

(in-package "ROS")
;;//! \htmlinclude SensorProperty.msg.html


(defclass object_list::SensorProperty
  :super ros::object
  :slots (_sensor_id _sensortype _posx_variance _posy_variance _velx_variance _vely_variance _trust_existance _trust_car _trust_truck _trust_motorcycle _trust_bicycle _trust_pedestrian _trust_stationary _trust_other ))

(defmethod object_list::SensorProperty
  (:init
   (&key
    ((:sensor_id __sensor_id) 0)
    ((:sensortype __sensortype) 0.0)
    ((:posx_variance __posx_variance) 0.0)
    ((:posy_variance __posy_variance) 0.0)
    ((:velx_variance __velx_variance) 0.0)
    ((:vely_variance __vely_variance) 0.0)
    ((:trust_existance __trust_existance) 0.0)
    ((:trust_car __trust_car) 0.0)
    ((:trust_truck __trust_truck) 0.0)
    ((:trust_motorcycle __trust_motorcycle) 0.0)
    ((:trust_bicycle __trust_bicycle) 0.0)
    ((:trust_pedestrian __trust_pedestrian) 0.0)
    ((:trust_stationary __trust_stationary) 0.0)
    ((:trust_other __trust_other) 0.0)
    )
   (send-super :init)
   (setq _sensor_id (round __sensor_id))
   (setq _sensortype (float __sensortype))
   (setq _posx_variance (float __posx_variance))
   (setq _posy_variance (float __posy_variance))
   (setq _velx_variance (float __velx_variance))
   (setq _vely_variance (float __vely_variance))
   (setq _trust_existance (float __trust_existance))
   (setq _trust_car (float __trust_car))
   (setq _trust_truck (float __trust_truck))
   (setq _trust_motorcycle (float __trust_motorcycle))
   (setq _trust_bicycle (float __trust_bicycle))
   (setq _trust_pedestrian (float __trust_pedestrian))
   (setq _trust_stationary (float __trust_stationary))
   (setq _trust_other (float __trust_other))
   self)
  (:sensor_id
   (&optional __sensor_id)
   (if __sensor_id (setq _sensor_id __sensor_id)) _sensor_id)
  (:sensortype
   (&optional __sensortype)
   (if __sensortype (setq _sensortype __sensortype)) _sensortype)
  (:posx_variance
   (&optional __posx_variance)
   (if __posx_variance (setq _posx_variance __posx_variance)) _posx_variance)
  (:posy_variance
   (&optional __posy_variance)
   (if __posy_variance (setq _posy_variance __posy_variance)) _posy_variance)
  (:velx_variance
   (&optional __velx_variance)
   (if __velx_variance (setq _velx_variance __velx_variance)) _velx_variance)
  (:vely_variance
   (&optional __vely_variance)
   (if __vely_variance (setq _vely_variance __vely_variance)) _vely_variance)
  (:trust_existance
   (&optional __trust_existance)
   (if __trust_existance (setq _trust_existance __trust_existance)) _trust_existance)
  (:trust_car
   (&optional __trust_car)
   (if __trust_car (setq _trust_car __trust_car)) _trust_car)
  (:trust_truck
   (&optional __trust_truck)
   (if __trust_truck (setq _trust_truck __trust_truck)) _trust_truck)
  (:trust_motorcycle
   (&optional __trust_motorcycle)
   (if __trust_motorcycle (setq _trust_motorcycle __trust_motorcycle)) _trust_motorcycle)
  (:trust_bicycle
   (&optional __trust_bicycle)
   (if __trust_bicycle (setq _trust_bicycle __trust_bicycle)) _trust_bicycle)
  (:trust_pedestrian
   (&optional __trust_pedestrian)
   (if __trust_pedestrian (setq _trust_pedestrian __trust_pedestrian)) _trust_pedestrian)
  (:trust_stationary
   (&optional __trust_stationary)
   (if __trust_stationary (setq _trust_stationary __trust_stationary)) _trust_stationary)
  (:trust_other
   (&optional __trust_other)
   (if __trust_other (setq _trust_other __trust_other)) _trust_other)
  (:serialization-length
   ()
   (+
    ;; int32 _sensor_id
    4
    ;; float64 _sensortype
    8
    ;; float64 _posx_variance
    8
    ;; float64 _posy_variance
    8
    ;; float64 _velx_variance
    8
    ;; float64 _vely_variance
    8
    ;; float64 _trust_existance
    8
    ;; float64 _trust_car
    8
    ;; float64 _trust_truck
    8
    ;; float64 _trust_motorcycle
    8
    ;; float64 _trust_bicycle
    8
    ;; float64 _trust_pedestrian
    8
    ;; float64 _trust_stationary
    8
    ;; float64 _trust_other
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _sensor_id
       (write-long _sensor_id s)
     ;; float64 _sensortype
       (sys::poke _sensortype (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _posx_variance
       (sys::poke _posx_variance (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _posy_variance
       (sys::poke _posy_variance (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _velx_variance
       (sys::poke _velx_variance (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _vely_variance
       (sys::poke _vely_variance (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _trust_existance
       (sys::poke _trust_existance (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _trust_car
       (sys::poke _trust_car (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _trust_truck
       (sys::poke _trust_truck (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _trust_motorcycle
       (sys::poke _trust_motorcycle (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _trust_bicycle
       (sys::poke _trust_bicycle (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _trust_pedestrian
       (sys::poke _trust_pedestrian (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _trust_stationary
       (sys::poke _trust_stationary (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _trust_other
       (sys::poke _trust_other (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _sensor_id
     (setq _sensor_id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float64 _sensortype
     (setq _sensortype (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _posx_variance
     (setq _posx_variance (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _posy_variance
     (setq _posy_variance (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _velx_variance
     (setq _velx_variance (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _vely_variance
     (setq _vely_variance (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _trust_existance
     (setq _trust_existance (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _trust_car
     (setq _trust_car (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _trust_truck
     (setq _trust_truck (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _trust_motorcycle
     (setq _trust_motorcycle (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _trust_bicycle
     (setq _trust_bicycle (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _trust_pedestrian
     (setq _trust_pedestrian (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _trust_stationary
     (setq _trust_stationary (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _trust_other
     (setq _trust_other (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get object_list::SensorProperty :md5sum-) "b92131fc47bc49b0227fc3ddb6760ee8")
(setf (get object_list::SensorProperty :datatype-) "object_list/SensorProperty")
(setf (get object_list::SensorProperty :definition-)
      "int32 sensor_id
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



(provide :object_list/SensorProperty "b92131fc47bc49b0227fc3ddb6760ee8")


