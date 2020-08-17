package object_list;

public interface ObjectsList extends org.ros.internal.message.Message {
  static final java.lang.String _TYPE = "object_list/ObjectsList";
  static final java.lang.String _DEFINITION = "Header header\nObjectList[] obj_list\n";
  static final boolean _IS_SERVICE = false;
  static final boolean _IS_ACTION = false;
  std_msgs.Header getHeader();
  void setHeader(std_msgs.Header value);
  java.util.List<object_list.ObjectList> getObjList();
  void setObjList(java.util.List<object_list.ObjectList> value);
}
