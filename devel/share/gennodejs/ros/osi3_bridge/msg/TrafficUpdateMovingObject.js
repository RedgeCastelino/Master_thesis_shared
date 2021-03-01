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

class TrafficUpdateMovingObject {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.object = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('object')) {
        this.object = initObj.object
      }
      else {
        this.object = new MovingObject();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TrafficUpdateMovingObject
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [object]
    bufferOffset = MovingObject.serialize(obj.object, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TrafficUpdateMovingObject
    let len;
    let data = new TrafficUpdateMovingObject(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [object]
    data.object = MovingObject.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 129;
  }

  static datatype() {
    // Returns string type for a message object
    return 'osi3_bridge/TrafficUpdateMovingObject';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b26e20bf46b692e8759e85b824c5ffc2';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    osi3_bridge/MovingObject object
    
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
    const resolved = new TrafficUpdateMovingObject(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.object !== undefined) {
      resolved.object = MovingObject.Resolve(msg.object)
    }
    else {
      resolved.object = new MovingObject()
    }

    return resolved;
    }
};

module.exports = TrafficUpdateMovingObject;
