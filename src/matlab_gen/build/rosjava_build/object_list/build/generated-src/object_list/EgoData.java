package object_list;

public interface EgoData extends org.ros.internal.message.Message {
  static final java.lang.String _TYPE = "object_list/EgoData";
  static final java.lang.String _DEFINITION = "Header header\nobject_list/Geometric geometric\nobject_list/Dimension dimension\n\n";
  static final boolean _IS_SERVICE = false;
  static final boolean _IS_ACTION = false;
  std_msgs.Header getHeader();
  void setHeader(std_msgs.Header value);
  object_list.Geometric getGeometric();
  void setGeometric(object_list.Geometric value);
  object_list.Dimension getDimension();
  void setDimension(object_list.Dimension value);
}
