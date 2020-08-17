package osi3_bridge;

public interface MovingObject extends org.ros.internal.message.Message {
  static final java.lang.String _TYPE = "osi3_bridge/MovingObject";
  static final java.lang.String _DEFINITION = "uint64 id\nosi3_bridge/Dimension3d dimension\ngeometry_msgs/Vector3 position\nosi3_bridge/Orientation3d orientation\ngeometry_msgs/Vector3 velocity\ngeometry_msgs/Vector3 acceleration\nuint8 type\n\nuint8 TYPE_UNKNOWN = 0\nuint8 TYPE_OTHER = 1\nuint8 TYPE_CAR = 2\nuint8 TYPE_PEDESTRIAN = 3\nuint8 TYPE_ANIMAL = 4\nuint8 TYPE_TRUCK = 5\nuint8 TYPE_TRAILER = 6\nuint8 TYPE_MOTORBIKE = 7\nuint8 TYPE_BICYCLE = 8\nuint8 TYPE_BUS = 9\nuint8 TYPE_TRAM = 10\nuint8 TYPE_TRAIN = 11\nuint8 TYPE_WHEELCHAIR = 12\n\n";
  static final boolean _IS_SERVICE = false;
  static final boolean _IS_ACTION = false;
  static final byte TYPE_UNKNOWN = 0;
  static final byte TYPE_OTHER = 1;
  static final byte TYPE_CAR = 2;
  static final byte TYPE_PEDESTRIAN = 3;
  static final byte TYPE_ANIMAL = 4;
  static final byte TYPE_TRUCK = 5;
  static final byte TYPE_TRAILER = 6;
  static final byte TYPE_MOTORBIKE = 7;
  static final byte TYPE_BICYCLE = 8;
  static final byte TYPE_BUS = 9;
  static final byte TYPE_TRAM = 10;
  static final byte TYPE_TRAIN = 11;
  static final byte TYPE_WHEELCHAIR = 12;
  long getId();
  void setId(long value);
  osi3_bridge.Dimension3d getDimension();
  void setDimension(osi3_bridge.Dimension3d value);
  geometry_msgs.Vector3 getPosition();
  void setPosition(geometry_msgs.Vector3 value);
  osi3_bridge.Orientation3d getOrientation();
  void setOrientation(osi3_bridge.Orientation3d value);
  geometry_msgs.Vector3 getVelocity();
  void setVelocity(geometry_msgs.Vector3 value);
  geometry_msgs.Vector3 getAcceleration();
  void setAcceleration(geometry_msgs.Vector3 value);
  byte getType();
  void setType(byte value);
}
