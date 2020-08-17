package object_list;

public interface Features extends org.ros.internal.message.Message {
  static final java.lang.String _TYPE = "object_list/Features";
  static final java.lang.String _DEFINITION = "uint8 FL\nuint8 FM\nuint8 FR\nuint8 MR\nuint8 RR\nuint8 RM\nuint8 RL\nuint8 ML\n";
  static final boolean _IS_SERVICE = false;
  static final boolean _IS_ACTION = false;
  byte getFL();
  void setFL(byte value);
  byte getFM();
  void setFM(byte value);
  byte getFR();
  void setFR(byte value);
  byte getMR();
  void setMR(byte value);
  byte getRR();
  void setRR(byte value);
  byte getRM();
  void setRM(byte value);
  byte getRL();
  void setRL(byte value);
  byte getML();
  void setML(byte value);
}
