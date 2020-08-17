package vehicle_control;

public interface Trajectory extends org.ros.internal.message.Message {
  static final java.lang.String _TYPE = "vehicle_control/Trajectory";
  static final java.lang.String _DEFINITION = "Header header\nfloat64[] time\nfloat64[] x\nfloat64[] y\nfloat64[] v\nfloat64[] yaw\nfloat64 reftime\n";
  static final boolean _IS_SERVICE = false;
  static final boolean _IS_ACTION = false;
  std_msgs.Header getHeader();
  void setHeader(std_msgs.Header value);
  double[] getTime();
  void setTime(double[] value);
  double[] getX();
  void setX(double[] value);
  double[] getY();
  void setY(double[] value);
  double[] getV();
  void setV(double[] value);
  double[] getYaw();
  void setYaw(double[] value);
  double getReftime();
  void setReftime(double value);
}
