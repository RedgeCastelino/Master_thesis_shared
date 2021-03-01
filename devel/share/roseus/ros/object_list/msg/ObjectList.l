;; Auto-generated. Do not edit!


(when (boundp 'object_list::ObjectList)
  (if (not (find-package "OBJECT_LIST"))
    (make-package "OBJECT_LIST"))
  (shadow 'ObjectList (find-package "OBJECT_LIST")))
(unless (find-package "OBJECT_LIST::OBJECTLIST")
  (make-package "OBJECT_LIST::OBJECTLIST"))

(in-package "ROS")
;;//! \htmlinclude ObjectList.msg.html


(defclass object_list::ObjectList
  :super ros::object
  :slots (_obj_id _time _geometric _covariance _dimension _prop_existence _prop_nonexistence _prop_persistance _prop_mov _classification _classification_mass _features _sensors_fused ))

(defmethod object_list::ObjectList
  (:init
   (&key
    ((:obj_id __obj_id) 0)
    ((:time __time) 0.0)
    ((:geometric __geometric) (instance object_list::Geometric :init))
    ((:covariance __covariance) (make-array 36 :initial-element 0.0 :element-type :float))
    ((:dimension __dimension) (instance object_list::Dimension :init))
    ((:prop_existence __prop_existence) 0.0)
    ((:prop_nonexistence __prop_nonexistence) 0.0)
    ((:prop_persistance __prop_persistance) 0.0)
    ((:prop_mov __prop_mov) 0.0)
    ((:classification __classification) (instance object_list::Classification :init))
    ((:classification_mass __classification_mass) (make-array 12 :initial-element 0.0 :element-type :float))
    ((:features __features) (instance object_list::Features :init))
    ((:sensors_fused __sensors_fused) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _obj_id (round __obj_id))
   (setq _time (float __time))
   (setq _geometric __geometric)
   (setq _covariance __covariance)
   (setq _dimension __dimension)
   (setq _prop_existence (float __prop_existence))
   (setq _prop_nonexistence (float __prop_nonexistence))
   (setq _prop_persistance (float __prop_persistance))
   (setq _prop_mov (float __prop_mov))
   (setq _classification __classification)
   (setq _classification_mass __classification_mass)
   (setq _features __features)
   (setq _sensors_fused __sensors_fused)
   self)
  (:obj_id
   (&optional __obj_id)
   (if __obj_id (setq _obj_id __obj_id)) _obj_id)
  (:time
   (&optional __time)
   (if __time (setq _time __time)) _time)
  (:geometric
   (&rest __geometric)
   (if (keywordp (car __geometric))
       (send* _geometric __geometric)
     (progn
       (if __geometric (setq _geometric (car __geometric)))
       _geometric)))
  (:covariance
   (&optional __covariance)
   (if __covariance (setq _covariance __covariance)) _covariance)
  (:dimension
   (&rest __dimension)
   (if (keywordp (car __dimension))
       (send* _dimension __dimension)
     (progn
       (if __dimension (setq _dimension (car __dimension)))
       _dimension)))
  (:prop_existence
   (&optional __prop_existence)
   (if __prop_existence (setq _prop_existence __prop_existence)) _prop_existence)
  (:prop_nonexistence
   (&optional __prop_nonexistence)
   (if __prop_nonexistence (setq _prop_nonexistence __prop_nonexistence)) _prop_nonexistence)
  (:prop_persistance
   (&optional __prop_persistance)
   (if __prop_persistance (setq _prop_persistance __prop_persistance)) _prop_persistance)
  (:prop_mov
   (&optional __prop_mov)
   (if __prop_mov (setq _prop_mov __prop_mov)) _prop_mov)
  (:classification
   (&rest __classification)
   (if (keywordp (car __classification))
       (send* _classification __classification)
     (progn
       (if __classification (setq _classification (car __classification)))
       _classification)))
  (:classification_mass
   (&optional __classification_mass)
   (if __classification_mass (setq _classification_mass __classification_mass)) _classification_mass)
  (:features
   (&rest __features)
   (if (keywordp (car __features))
       (send* _features __features)
     (progn
       (if __features (setq _features (car __features)))
       _features)))
  (:sensors_fused
   (&optional __sensors_fused)
   (if __sensors_fused (setq _sensors_fused __sensors_fused)) _sensors_fused)
  (:serialization-length
   ()
   (+
    ;; int32 _obj_id
    4
    ;; float64 _time
    8
    ;; object_list/Geometric _geometric
    (send _geometric :serialization-length)
    ;; float64[36] _covariance
    (* 8    36)
    ;; object_list/Dimension _dimension
    (send _dimension :serialization-length)
    ;; float64 _prop_existence
    8
    ;; float64 _prop_nonexistence
    8
    ;; float64 _prop_persistance
    8
    ;; float64 _prop_mov
    8
    ;; object_list/Classification _classification
    (send _classification :serialization-length)
    ;; float64[12] _classification_mass
    (* 8    12)
    ;; object_list/Features _features
    (send _features :serialization-length)
    ;; int64[] _sensors_fused
    (* 8    (length _sensors_fused)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _obj_id
       (write-long _obj_id s)
     ;; float64 _time
       (sys::poke _time (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; object_list/Geometric _geometric
       (send _geometric :serialize s)
     ;; float64[36] _covariance
     (dotimes (i 36)
       (sys::poke (elt _covariance i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; object_list/Dimension _dimension
       (send _dimension :serialize s)
     ;; float64 _prop_existence
       (sys::poke _prop_existence (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _prop_nonexistence
       (sys::poke _prop_nonexistence (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _prop_persistance
       (sys::poke _prop_persistance (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _prop_mov
       (sys::poke _prop_mov (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; object_list/Classification _classification
       (send _classification :serialize s)
     ;; float64[12] _classification_mass
     (dotimes (i 12)
       (sys::poke (elt _classification_mass i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; object_list/Features _features
       (send _features :serialize s)
     ;; int64[] _sensors_fused
     (write-long (length _sensors_fused) s)
     (dotimes (i (length _sensors_fused))
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke (elt _sensors_fused i) (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class (elt _sensors_fused i)) (= (length ((elt _sensors_fused i) . bv)) 2)) ;; bignum
              (write-long (ash (elt ((elt _sensors_fused i) . bv) 0) 0) s)
              (write-long (ash (elt ((elt _sensors_fused i) . bv) 1) -1) s))
             ((and (class (elt _sensors_fused i)) (= (length ((elt _sensors_fused i) . bv)) 1)) ;; big1
              (write-long (elt ((elt _sensors_fused i) . bv) 0) s)
              (write-long (if (>= (elt _sensors_fused i) 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long (elt _sensors_fused i) s)(write-long (if (>= (elt _sensors_fused i) 0) 0 #xffffffff) s)))
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _obj_id
     (setq _obj_id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float64 _time
     (setq _time (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; object_list/Geometric _geometric
     (send _geometric :deserialize buf ptr-) (incf ptr- (send _geometric :serialization-length))
   ;; float64[36] _covariance
   (dotimes (i (length _covariance))
     (setf (elt _covariance i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;; object_list/Dimension _dimension
     (send _dimension :deserialize buf ptr-) (incf ptr- (send _dimension :serialization-length))
   ;; float64 _prop_existence
     (setq _prop_existence (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _prop_nonexistence
     (setq _prop_nonexistence (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _prop_persistance
     (setq _prop_persistance (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _prop_mov
     (setq _prop_mov (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; object_list/Classification _classification
     (send _classification :deserialize buf ptr-) (incf ptr- (send _classification :serialization-length))
   ;; float64[12] _classification_mass
   (dotimes (i (length _classification_mass))
     (setf (elt _classification_mass i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;; object_list/Features _features
     (send _features :deserialize buf ptr-) (incf ptr- (send _features :serialization-length))
   ;; int64[] _sensors_fused
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _sensors_fused (instantiate integer-vector n))
     (dotimes (i n)
#+(or :alpha :irix6 :x86_64)
      (setf (elt _sensors_fused i) (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf (elt _sensors_fused i) (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
     ))
   ;;
   self)
  )

(setf (get object_list::ObjectList :md5sum-) "d5793b04b71b063f6fee4d02602a19de")
(setf (get object_list::ObjectList :datatype-) "object_list/ObjectList")
(setf (get object_list::ObjectList :definition-)
      "int32 obj_id
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

")



(provide :object_list/ObjectList "d5793b04b71b063f6fee4d02602a19de")


