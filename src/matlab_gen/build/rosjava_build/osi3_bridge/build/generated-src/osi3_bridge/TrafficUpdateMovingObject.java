package osi3_bridge;

public interface TrafficUpdateMovingObject extends org.ros.internal.message.Message {
  static final java.lang.String _TYPE = "osi3_bridge/TrafficUpdateMovingObject";
  static final java.lang.String _DEFINITION = "Header header\nosi3_bridge/MovingObject object\n";
  static final boolean _IS_SERVICE = false;
  static final boolean _IS_ACTION = false;
  std_msgs.Header getHeader();
  void setHeader(std_msgs.Header value);
  osi3_bridge.MovingObject getObject();
  void setObject(osi3_bridge.MovingObject value);
}
