package object_list;

public interface Dimension extends org.ros.internal.message.Message {
  static final java.lang.String _TYPE = "object_list/Dimension";
  static final java.lang.String _DEFINITION = "float64 length\nfloat64 width\n";
  static final boolean _IS_SERVICE = false;
  static final boolean _IS_ACTION = false;
  double getLength();
  void setLength(double value);
  double getWidth();
  void setWidth(double value);
}
