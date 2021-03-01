// Auto-generated. Do not edit!

// (in-package object_list.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let Geometric = require('./Geometric.js');
let Dimension = require('./Dimension.js');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class EgoData {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.geometric = null;
      this.dimension = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('geometric')) {
        this.geometric = initObj.geometric
      }
      else {
        this.geometric = new Geometric();
      }
      if (initObj.hasOwnProperty('dimension')) {
        this.dimension = initObj.dimension
      }
      else {
        this.dimension = new Dimension();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type EgoData
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [geometric]
    bufferOffset = Geometric.serialize(obj.geometric, buffer, bufferOffset);
    // Serialize message field [dimension]
    bufferOffset = Dimension.serialize(obj.dimension, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type EgoData
    let len;
    let data = new EgoData(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [geometric]
    data.geometric = Geometric.deserialize(buffer, bufferOffset);
    // Deserialize message field [dimension]
    data.dimension = Dimension.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 96;
  }

  static datatype() {
    // Returns string type for a message object
    return 'object_list/EgoData';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e7e294d9eaab8d77f6809dd7e07899e8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    object_list/Geometric geometric
    object_list/Dimension dimension
    
    
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
    MSG: object_list/Geometric
    float64 x
    float64 y
    float64 vx
    float64 vy
    float64 ax
    float64 ay
    float64 yaw
    float64 yawrate
    
    ================================================================================
    MSG: object_list/Dimension
    float64 length
    float64 width
    float64 length_variance
    float64 width_variance
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new EgoData(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.geometric !== undefined) {
      resolved.geometric = Geometric.Resolve(msg.geometric)
    }
    else {
      resolved.geometric = new Geometric()
    }

    if (msg.dimension !== undefined) {
      resolved.dimension = Dimension.Resolve(msg.dimension)
    }
    else {
      resolved.dimension = new Dimension()
    }

    return resolved;
    }
};

module.exports = EgoData;
