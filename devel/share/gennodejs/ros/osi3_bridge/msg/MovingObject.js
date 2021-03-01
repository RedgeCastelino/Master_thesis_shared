// Auto-generated. Do not edit!

// (in-package osi3_bridge.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let Dimension3d = require('./Dimension3d.js');
let Orientation3d = require('./Orientation3d.js');
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class MovingObject {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.id = null;
      this.dimension = null;
      this.position = null;
      this.orientation = null;
      this.velocity = null;
      this.acceleration = null;
      this.type = null;
    }
    else {
      if (initObj.hasOwnProperty('id')) {
        this.id = initObj.id
      }
      else {
        this.id = 0;
      }
      if (initObj.hasOwnProperty('dimension')) {
        this.dimension = initObj.dimension
      }
      else {
        this.dimension = new Dimension3d();
      }
      if (initObj.hasOwnProperty('position')) {
        this.position = initObj.position
      }
      else {
        this.position = new geometry_msgs.msg.Vector3();
      }
      if (initObj.hasOwnProperty('orientation')) {
        this.orientation = initObj.orientation
      }
      else {
        this.orientation = new Orientation3d();
      }
      if (initObj.hasOwnProperty('velocity')) {
        this.velocity = initObj.velocity
      }
      else {
        this.velocity = new geometry_msgs.msg.Vector3();
      }
      if (initObj.hasOwnProperty('acceleration')) {
        this.acceleration = initObj.acceleration
      }
      else {
        this.acceleration = new geometry_msgs.msg.Vector3();
      }
      if (initObj.hasOwnProperty('type')) {
        this.type = initObj.type
      }
      else {
        this.type = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MovingObject
    // Serialize message field [id]
    bufferOffset = _serializer.uint64(obj.id, buffer, bufferOffset);
    // Serialize message field [dimension]
    bufferOffset = Dimension3d.serialize(obj.dimension, buffer, bufferOffset);
    // Serialize message field [position]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.position, buffer, bufferOffset);
    // Serialize message field [orientation]
    bufferOffset = Orientation3d.serialize(obj.orientation, buffer, bufferOffset);
    // Serialize message field [velocity]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.velocity, buffer, bufferOffset);
    // Serialize message field [acceleration]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.acceleration, buffer, bufferOffset);
    // Serialize message field [type]
    bufferOffset = _serializer.uint8(obj.type, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MovingObject
    let len;
    let data = new MovingObject(null);
    // Deserialize message field [id]
    data.id = _deserializer.uint64(buffer, bufferOffset);
    // Deserialize message field [dimension]
    data.dimension = Dimension3d.deserialize(buffer, bufferOffset);
    // Deserialize message field [position]
    data.position = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    // Deserialize message field [orientation]
    data.orientation = Orientation3d.deserialize(buffer, bufferOffset);
    // Deserialize message field [velocity]
    data.velocity = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    // Deserialize message field [acceleration]
    data.acceleration = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    // Deserialize message field [type]
    data.type = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 129;
  }

  static datatype() {
    // Returns string type for a message object
    return 'osi3_bridge/MovingObject';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '1d813c673962ef31735dd456446e05b5';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    const resolved = new MovingObject(null);
    if (msg.id !== undefined) {
      resolved.id = msg.id;
    }
    else {
      resolved.id = 0
    }

    if (msg.dimension !== undefined) {
      resolved.dimension = Dimension3d.Resolve(msg.dimension)
    }
    else {
      resolved.dimension = new Dimension3d()
    }

    if (msg.position !== undefined) {
      resolved.position = geometry_msgs.msg.Vector3.Resolve(msg.position)
    }
    else {
      resolved.position = new geometry_msgs.msg.Vector3()
    }

    if (msg.orientation !== undefined) {
      resolved.orientation = Orientation3d.Resolve(msg.orientation)
    }
    else {
      resolved.orientation = new Orientation3d()
    }

    if (msg.velocity !== undefined) {
      resolved.velocity = geometry_msgs.msg.Vector3.Resolve(msg.velocity)
    }
    else {
      resolved.velocity = new geometry_msgs.msg.Vector3()
    }

    if (msg.acceleration !== undefined) {
      resolved.acceleration = geometry_msgs.msg.Vector3.Resolve(msg.acceleration)
    }
    else {
      resolved.acceleration = new geometry_msgs.msg.Vector3()
    }

    if (msg.type !== undefined) {
      resolved.type = msg.type;
    }
    else {
      resolved.type = 0
    }

    return resolved;
    }
};

// Constants for message
MovingObject.Constants = {
  TYPE_UNKNOWN: 0,
  TYPE_OTHER: 1,
  TYPE_CAR: 2,
  TYPE_PEDESTRIAN: 3,
  TYPE_ANIMAL: 4,
  TYPE_TRUCK: 5,
  TYPE_TRAILER: 6,
  TYPE_MOTORBIKE: 7,
  TYPE_BICYCLE: 8,
  TYPE_BUS: 9,
  TYPE_TRAM: 10,
  TYPE_TRAIN: 11,
  TYPE_WHEELCHAIR: 12,
}

module.exports = MovingObject;
