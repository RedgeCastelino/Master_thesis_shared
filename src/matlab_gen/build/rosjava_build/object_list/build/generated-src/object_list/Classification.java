package object_list;

public interface Classification extends org.ros.internal.message.Message {
  static final java.lang.String _TYPE = "object_list/Classification";
  static final java.lang.String _DEFINITION = "float32 car\nfloat32 truck\nfloat32 motorcycle\nfloat32 bicycle\nfloat32 pedestrian\nfloat32 stacionary\nfloat32 other\n";
  static final boolean _IS_SERVICE = false;
  static final boolean _IS_ACTION = false;
  float getCar();
  void setCar(float value);
  float getTruck();
  void setTruck(float value);
  float getMotorcycle();
  void setMotorcycle(float value);
  float getBicycle();
  void setBicycle(float value);
  float getPedestrian();
  void setPedestrian(float value);
  float getStacionary();
  void setStacionary(float value);
  float getOther();
  void setOther(float value);
}
