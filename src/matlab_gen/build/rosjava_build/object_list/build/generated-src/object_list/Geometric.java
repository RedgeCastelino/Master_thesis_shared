package object_list;

public interface Geometric extends org.ros.internal.message.Message {
  static final java.lang.String _TYPE = "object_list/Geometric";
  static final java.lang.String _DEFINITION = "float64 x\nfloat64 y\nfloat64 vx\nfloat64 vy\nfloat64 ax\nfloat64 ay\nfloat64 yaw\nfloat64 yawrate\n";
  static final boolean _IS_SERVICE = false;
  static final boolean _IS_ACTION = false;
  double getX();
  void setX(double value);
  double getY();
  void setY(double value);
  double getVx();
  void setVx(double value);
  double getVy();
  void setVy(double value);
  double getAx();
  void setAx(double value);
  double getAy();
  void setAy(double value);
  double getYaw();
  void setYaw(double value);
  double getYawrate();
  void setYawrate(double value);
}
