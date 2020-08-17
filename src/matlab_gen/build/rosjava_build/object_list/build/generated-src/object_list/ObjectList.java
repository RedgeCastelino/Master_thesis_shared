package object_list;

public interface ObjectList extends org.ros.internal.message.Message {
  static final java.lang.String _TYPE = "object_list/ObjectList";
  static final java.lang.String _DEFINITION = "int32 obj_id\nGeometric geometric\nfloat64[36] covariance\nDimension dimension\nfloat32 prop_existence\nfloat32 prop_mov \nClassification classification\nFeatures features\n";
  static final boolean _IS_SERVICE = false;
  static final boolean _IS_ACTION = false;
  int getObjId();
  void setObjId(int value);
  object_list.Geometric getGeometric();
  void setGeometric(object_list.Geometric value);
  double[] getCovariance();
  void setCovariance(double[] value);
  object_list.Dimension getDimension();
  void setDimension(object_list.Dimension value);
  float getPropExistence();
  void setPropExistence(float value);
  float getPropMov();
  void setPropMov(float value);
  object_list.Classification getClassification();
  void setClassification(object_list.Classification value);
  object_list.Features getFeatures();
  void setFeatures(object_list.Features value);
}
