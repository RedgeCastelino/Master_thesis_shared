package osi3_bridge;

public interface GroundTruthMovingObjects extends org.ros.internal.message.Message {
  static final java.lang.String _TYPE = "osi3_bridge/GroundTruthMovingObjects";
  static final java.lang.String _DEFINITION = "Header header\nosi3_bridge/MovingObject[] objects\n";
  static final boolean _IS_SERVICE = false;
  static final boolean _IS_ACTION = false;
  std_msgs.Header getHeader();
  void setHeader(std_msgs.Header value);
  java.util.List<osi3_bridge.MovingObject> getObjects();
  void setObjects(java.util.List<osi3_bridge.MovingObject> value);
}
