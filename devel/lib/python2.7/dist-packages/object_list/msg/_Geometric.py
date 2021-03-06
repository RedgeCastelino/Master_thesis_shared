# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from object_list/Geometric.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Geometric(genpy.Message):
  _md5sum = "74a252effe5544c6405c61fc1ab21633"
  _type = "object_list/Geometric"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """float64 x
float64 y
float64 vx
float64 vy
float64 ax
float64 ay
float64 yaw
float64 yawrate
"""
  __slots__ = ['x','y','vx','vy','ax','ay','yaw','yawrate']
  _slot_types = ['float64','float64','float64','float64','float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       x,y,vx,vy,ax,ay,yaw,yawrate

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Geometric, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.x is None:
        self.x = 0.
      if self.y is None:
        self.y = 0.
      if self.vx is None:
        self.vx = 0.
      if self.vy is None:
        self.vy = 0.
      if self.ax is None:
        self.ax = 0.
      if self.ay is None:
        self.ay = 0.
      if self.yaw is None:
        self.yaw = 0.
      if self.yawrate is None:
        self.yawrate = 0.
    else:
      self.x = 0.
      self.y = 0.
      self.vx = 0.
      self.vy = 0.
      self.ax = 0.
      self.ay = 0.
      self.yaw = 0.
      self.yawrate = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_8d().pack(_x.x, _x.y, _x.vx, _x.vy, _x.ax, _x.ay, _x.yaw, _x.yawrate))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 64
      (_x.x, _x.y, _x.vx, _x.vy, _x.ax, _x.ay, _x.yaw, _x.yawrate,) = _get_struct_8d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_8d().pack(_x.x, _x.y, _x.vx, _x.vy, _x.ax, _x.ay, _x.yaw, _x.yawrate))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 64
      (_x.x, _x.y, _x.vx, _x.vy, _x.ax, _x.ay, _x.yaw, _x.yawrate,) = _get_struct_8d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_8d = None
def _get_struct_8d():
    global _struct_8d
    if _struct_8d is None:
        _struct_8d = struct.Struct("<8d")
    return _struct_8d
