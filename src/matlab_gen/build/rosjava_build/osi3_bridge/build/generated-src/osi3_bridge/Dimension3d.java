package osi3_bridge;

public interface Dimension3d extends org.ros.internal.message.Message {
  static final java.lang.String _TYPE = "osi3_bridge/Dimension3d";
  static final java.lang.String _DEFINITION = "float64 length\nfloat64 width\nfloat64 height\n";
  static final boolean _IS_SERVICE = false;
  static final boolean _IS_ACTION = false;
  double getLength();
  void setLength(double value);
  double getWidth();
  void setWidth(double value);
  double getHeight();
  void setHeight(double value);
}
