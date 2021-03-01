// Auto-generated. Do not edit!

// (in-package object_list.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Dimension {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.length = null;
      this.width = null;
      this.length_variance = null;
      this.width_variance = null;
    }
    else {
      if (initObj.hasOwnProperty('length')) {
        this.length = initObj.length
      }
      else {
        this.length = 0.0;
      }
      if (initObj.hasOwnProperty('width')) {
        this.width = initObj.width
      }
      else {
        this.width = 0.0;
      }
      if (initObj.hasOwnProperty('length_variance')) {
        this.length_variance = initObj.length_variance
      }
      else {
        this.length_variance = 0.0;
      }
      if (initObj.hasOwnProperty('width_variance')) {
        this.width_variance = initObj.width_variance
      }
      else {
        this.width_variance = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Dimension
    // Serialize message field [length]
    bufferOffset = _serializer.float64(obj.length, buffer, bufferOffset);
    // Serialize message field [width]
    bufferOffset = _serializer.float64(obj.width, buffer, bufferOffset);
    // Serialize message field [length_variance]
    bufferOffset = _serializer.float64(obj.length_variance, buffer, bufferOffset);
    // Serialize message field [width_variance]
    bufferOffset = _serializer.float64(obj.width_variance, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Dimension
    let len;
    let data = new Dimension(null);
    // Deserialize message field [length]
    data.length = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [width]
    data.width = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [length_variance]
    data.length_variance = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [width_variance]
    data.width_variance = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 32;
  }

  static datatype() {
    // Returns string type for a message object
    return 'object_list/Dimension';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '01a8c17587dd313244e2f2fd574d1415';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    const resolved = new Dimension(null);
    if (msg.length !== undefined) {
      resolved.length = msg.length;
    }
    else {
      resolved.length = 0.0
    }

    if (msg.width !== undefined) {
      resolved.width = msg.width;
    }
    else {
      resolved.width = 0.0
    }

    if (msg.length_variance !== undefined) {
      resolved.length_variance = msg.length_variance;
    }
    else {
      resolved.length_variance = 0.0
    }

    if (msg.width_variance !== undefined) {
      resolved.width_variance = msg.width_variance;
    }
    else {
      resolved.width_variance = 0.0
    }

    return resolved;
    }
};

module.exports = Dimension;
