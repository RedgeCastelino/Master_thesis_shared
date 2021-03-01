// Auto-generated. Do not edit!

// (in-package osi3_bridge.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let MovingObject = require('./MovingObject.js');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class GroundTruthMovingObjects {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.objects = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('objects')) {
        this.objects = initObj.objects
      }
      else {
        this.objects = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GroundTruthMovingObjects
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [objects]
    // Serialize the length for message field [objects]
    bufferOffset = _serializer.uint32(obj.objects.length, buffer, bufferOffset);
    obj.objects.forEach((val) => {
      bufferOffset = MovingObject.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GroundTruthMovingObjects
    let len;
    let data = new GroundTruthMovingObjects(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [objects]
    // Deserialize array length for message field [objects]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.objects = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.objects[i] = MovingObject.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += 129 * object.objects.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'osi3_bridge/GroundTruthMovingObjects';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b5c10f964cf85cf58aa709fc3567f543';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    osi3_bridge/MovingObject[] objects
    
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
    string frame_id
    
    ================================================================================
    MSG: osi3_bridge/MovingObject
    uint64 id
    osi3_bridge/Dimension3d dimension
    geometry_msgs/Vector3 position
    osi3_bridge/Orientation3d orientation
    geometry_msgs/Vector3 velocity
    geometry_msgs/Vector3 acceleration
    uint8 type
    
    uint8 TYPE_UNKNOWN = 0
    uint8 TYPE_OTHER = 1
    uint8 TYPE_CAR = 2
    uint8 TYPE_PEDESTRIAN = 3
    uint8 TYPE_ANIMAL = 4
    uint8 TYPE_TRUCK = 5
    uint8 TYPE_TRAILER = 6
    uint8 TYPE_MOTORBIKE = 7
    uint8 TYPE_BICYCLE = 8
    uint8 TYPE_BUS = 9
    uint8 TYPE_TRAM = 10
    uint8 TYPE_TRAIN = 11
    uint8 TYPE_WHEELCHAIR = 12
    
    
    ================================================================================
    MSG: osi3_bridge/Dimension3d
    float64 length
    float64 width
    float64 height
    
    ================================================================================
    MSG: geometry_msgs/Vector3
    # This represents a vector in free space. 
    # It is only meant to represent a direction. Therefore, it does not
    # make sense to apply a translation to it (e.g., when applying a 
    # generic rigid transformation to a Vector3, tf2 will only apply the
    # rotation). If you want your data to be translatable too, use the
    # geometry_msgs/Point message instead.
    
    float64 x
    float64 y
    float64 z
    ================================================================================
    MSG: osi3_bridge/Orientation3d
    float64 roll
    float64 pitch
    float64 yaw
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new GroundTruthMovingObjects(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.objects !== undefined) {
      resolved.objects = new Array(msg.objects.length);
      for (let i = 0; i < resolved.objects.length; ++i) {
        resolved.objects[i] = MovingObject.Resolve(msg.objects[i]);
      }
    }
    else {
      resolved.objects = []
    }

    return resolved;
    }
};

module.exports = GroundTruthMovingObjects;
