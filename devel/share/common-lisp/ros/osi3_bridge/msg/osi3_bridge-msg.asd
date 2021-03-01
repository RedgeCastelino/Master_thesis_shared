
(cl:in-package :asdf)

(defsystem "osi3_bridge-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Dimension3d" :depends-on ("_package_Dimension3d"))
    (:file "_package_Dimension3d" :depends-on ("_package"))
    (:file "GroundTruthMovingObjects" :depends-on ("_package_GroundTruthMovingObjects"))
    (:file "_package_GroundTruthMovingObjects" :depends-on ("_package"))
    (:file "MovingObject" :depends-on ("_package_MovingObject"))
    (:file "_package_MovingObject" :depends-on ("_package"))
    (:file "Orientation3d" :depends-on ("_package_Orientation3d"))
    (:file "_package_Orientation3d" :depends-on ("_package"))
    (:file "TrafficUpdateMovingObject" :depends-on ("_package_TrafficUpdateMovingObject"))
    (:file "_package_TrafficUpdateMovingObject" :depends-on ("_package"))
  ))