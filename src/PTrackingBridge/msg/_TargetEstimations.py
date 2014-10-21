"""autogenerated by genpy from PTrackingBridge/TargetEstimations.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class TargetEstimations(genpy.Message):
  _md5sum = "83552043e9719a5333aaee79efac70b7"
  _type = "PTrackingBridge/TargetEstimations"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """std_msgs/Header header
int32[] identities
geometry_msgs/Point32[] positions
geometry_msgs/Point32[] standardDeviations
int32[] widths
int32[] heights
geometry_msgs/Point32[] velocities
geometry_msgs/Point32[] averagedVelocities

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/Point32
# This contains the position of a point in free space(with 32 bits of precision).
# It is recommeded to use Point wherever possible instead of Point32.  
# 
# This recommendation is to promote interoperability.  
#
# This message is designed to take up less space when sending
# lots of points at once, as in the case of a PointCloud.  

float32 x
float32 y
float32 z
"""
  __slots__ = ['header','identities','positions','standardDeviations','widths','heights','velocities','averagedVelocities']
  _slot_types = ['std_msgs/Header','int32[]','geometry_msgs/Point32[]','geometry_msgs/Point32[]','int32[]','int32[]','geometry_msgs/Point32[]','geometry_msgs/Point32[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,identities,positions,standardDeviations,widths,heights,velocities,averagedVelocities

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TargetEstimations, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.identities is None:
        self.identities = []
      if self.positions is None:
        self.positions = []
      if self.standardDeviations is None:
        self.standardDeviations = []
      if self.widths is None:
        self.widths = []
      if self.heights is None:
        self.heights = []
      if self.velocities is None:
        self.velocities = []
      if self.averagedVelocities is None:
        self.averagedVelocities = []
    else:
      self.header = std_msgs.msg.Header()
      self.identities = []
      self.positions = []
      self.standardDeviations = []
      self.widths = []
      self.heights = []
      self.velocities = []
      self.averagedVelocities = []

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
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.identities)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.identities))
      length = len(self.positions)
      buff.write(_struct_I.pack(length))
      for val1 in self.positions:
        _x = val1
        buff.write(_struct_3f.pack(_x.x, _x.y, _x.z))
      length = len(self.standardDeviations)
      buff.write(_struct_I.pack(length))
      for val1 in self.standardDeviations:
        _x = val1
        buff.write(_struct_3f.pack(_x.x, _x.y, _x.z))
      length = len(self.widths)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.widths))
      length = len(self.heights)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.heights))
      length = len(self.velocities)
      buff.write(_struct_I.pack(length))
      for val1 in self.velocities:
        _x = val1
        buff.write(_struct_3f.pack(_x.x, _x.y, _x.z))
      length = len(self.averagedVelocities)
      buff.write(_struct_I.pack(length))
      for val1 in self.averagedVelocities:
        _x = val1
        buff.write(_struct_3f.pack(_x.x, _x.y, _x.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.positions is None:
        self.positions = None
      if self.standardDeviations is None:
        self.standardDeviations = None
      if self.velocities is None:
        self.velocities = None
      if self.averagedVelocities is None:
        self.averagedVelocities = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.identities = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.positions = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point32()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _struct_3f.unpack(str[start:end])
        self.positions.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.standardDeviations = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point32()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _struct_3f.unpack(str[start:end])
        self.standardDeviations.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.widths = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.heights = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.velocities = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point32()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _struct_3f.unpack(str[start:end])
        self.velocities.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.averagedVelocities = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point32()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _struct_3f.unpack(str[start:end])
        self.averagedVelocities.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.identities)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.identities.tostring())
      length = len(self.positions)
      buff.write(_struct_I.pack(length))
      for val1 in self.positions:
        _x = val1
        buff.write(_struct_3f.pack(_x.x, _x.y, _x.z))
      length = len(self.standardDeviations)
      buff.write(_struct_I.pack(length))
      for val1 in self.standardDeviations:
        _x = val1
        buff.write(_struct_3f.pack(_x.x, _x.y, _x.z))
      length = len(self.widths)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.widths.tostring())
      length = len(self.heights)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.heights.tostring())
      length = len(self.velocities)
      buff.write(_struct_I.pack(length))
      for val1 in self.velocities:
        _x = val1
        buff.write(_struct_3f.pack(_x.x, _x.y, _x.z))
      length = len(self.averagedVelocities)
      buff.write(_struct_I.pack(length))
      for val1 in self.averagedVelocities:
        _x = val1
        buff.write(_struct_3f.pack(_x.x, _x.y, _x.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.positions is None:
        self.positions = None
      if self.standardDeviations is None:
        self.standardDeviations = None
      if self.velocities is None:
        self.velocities = None
      if self.averagedVelocities is None:
        self.averagedVelocities = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.identities = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.positions = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point32()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _struct_3f.unpack(str[start:end])
        self.positions.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.standardDeviations = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point32()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _struct_3f.unpack(str[start:end])
        self.standardDeviations.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.widths = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.heights = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.velocities = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point32()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _struct_3f.unpack(str[start:end])
        self.velocities.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.averagedVelocities = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point32()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _struct_3f.unpack(str[start:end])
        self.averagedVelocities.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_3f = struct.Struct("<3f")
