package osi3_bridge;

public interface Orientation3d extends org.ros.internal.message.Message {
  static final java.lang.String _TYPE = "osi3_bridge/Orientation3d";
  static final java.lang.String _DEFINITION = "float64 roll\nfloat64 pitch\nfloat64 yaw\n";
  static final boolean _IS_SERVICE = false;
  static final boolean _IS_ACTION = false;
  double getRoll();
  void setRoll(double value);
  double getPitch();
  void setPitch(double value);
  double getYaw();
  void setYaw(double value);
}
