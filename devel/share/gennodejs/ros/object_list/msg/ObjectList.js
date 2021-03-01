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
let Classification = require('./Classification.js');
let Features = require('./Features.js');

//-----------------------------------------------------------

class ObjectList {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.obj_id = null;
      this.time = null;
      this.geometric = null;
      this.covariance = null;
      this.dimension = null;
      this.prop_existence = null;
      this.prop_nonexistence = null;
      this.prop_persistance = null;
      this.prop_mov = null;
      this.classification = null;
      this.classification_mass = null;
      this.features = null;
      this.sensors_fused = null;
    }
    else {
      if (initObj.hasOwnProperty('obj_id')) {
        this.obj_id = initObj.obj_id
      }
      else {
        this.obj_id = 0;
      }
      if (initObj.hasOwnProperty('time')) {
        this.time = initObj.time
      }
      else {
        this.time = 0.0;
      }
      if (initObj.hasOwnProperty('geometric')) {
        this.geometric = initObj.geometric
      }
      else {
        this.geometric = new Geometric();
      }
      if (initObj.hasOwnProperty('covariance')) {
        this.covariance = initObj.covariance
      }
      else {
        this.covariance = new Array(36).fill(0);
      }
      if (initObj.hasOwnProperty('dimension')) {
        this.dimension = initObj.dimension
      }
      else {
        this.dimension = new Dimension();
      }
      if (initObj.hasOwnProperty('prop_existence')) {
        this.prop_existence = initObj.prop_existence
      }
      else {
        this.prop_existence = 0.0;
      }
      if (initObj.hasOwnProperty('prop_nonexistence')) {
        this.prop_nonexistence = initObj.prop_nonexistence
      }
      else {
        this.prop_nonexistence = 0.0;
      }
      if (initObj.hasOwnProperty('prop_persistance')) {
        this.prop_persistance = initObj.prop_persistance
      }
      else {
        this.prop_persistance = 0.0;
      }
      if (initObj.hasOwnProperty('prop_mov')) {
        this.prop_mov = initObj.prop_mov
      }
      else {
        this.prop_mov = 0.0;
      }
      if (initObj.hasOwnProperty('classification')) {
        this.classification = initObj.classification
      }
      else {
        this.classification = new Classification();
      }
      if (initObj.hasOwnProperty('classification_mass')) {
        this.classification_mass = initObj.classification_mass
      }
      else {
        this.classification_mass = new Array(12).fill(0);
      }
      if (initObj.hasOwnProperty('features')) {
        this.features = initObj.features
      }
      else {
        this.features = new Features();
      }
      if (initObj.hasOwnProperty('sensors_fused')) {
        this.sensors_fused = initObj.sensors_fused
      }
      else {
        this.sensors_fused = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ObjectList
    // Serialize message field [obj_id]
    bufferOffset = _serializer.int32(obj.obj_id, buffer, bufferOffset);
    // Serialize message field [time]
    bufferOffset = _serializer.float64(obj.time, buffer, bufferOffset);
    // Serialize message field [geometric]
    bufferOffset = Geometric.serialize(obj.geometric, buffer, bufferOffset);
    // Check that the constant length array field [covariance] has the right length
    if (obj.covariance.length !== 36) {
      throw new Error('Unable to serialize array field covariance - length must be 36')
    }
    // Serialize message field [covariance]
    bufferOffset = _arraySerializer.float64(obj.covariance, buffer, bufferOffset, 36);
    // Serialize message field [dimension]
    bufferOffset = Dimension.serialize(obj.dimension, buffer, bufferOffset);
    // Serialize message field [prop_existence]
    bufferOffset = _serializer.float64(obj.prop_existence, buffer, bufferOffset);
    // Serialize message field [prop_nonexistence]
    bufferOffset = _serializer.float64(obj.prop_nonexistence, buffer, bufferOffset);
    // Serialize message field [prop_persistance]
    bufferOffset = _serializer.float64(obj.prop_persistance, buffer, bufferOffset);
    // Serialize message field [prop_mov]
    bufferOffset = _serializer.float64(obj.prop_mov, buffer, bufferOffset);
    // Serialize message field [classification]
    bufferOffset = Classification.serialize(obj.classification, buffer, bufferOffset);
    // Check that the constant length array field [classification_mass] has the right length
    if (obj.classification_mass.length !== 12) {
      throw new Error('Unable to serialize array field classification_mass - length must be 12')
    }
    // Serialize message field [classification_mass]
    bufferOffset = _arraySerializer.float64(obj.classification_mass, buffer, bufferOffset, 12);
    // Serialize message field [features]
    bufferOffset = Features.serialize(obj.features, buffer, bufferOffset);
    // Serialize message field [sensors_fused]
    bufferOffset = _arraySerializer.int64(obj.sensors_fused, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ObjectList
    let len;
    let data = new ObjectList(null);
    // Deserialize message field [obj_id]
    data.obj_id = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [time]
    data.time = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [geometric]
    data.geometric = Geometric.deserialize(buffer, bufferOffset);
    // Deserialize message field [covariance]
    data.covariance = _arrayDeserializer.float64(buffer, bufferOffset, 36)
    // Deserialize message field [dimension]
    data.dimension = Dimension.deserialize(buffer, bufferOffset);
    // Deserialize message field [prop_existence]
    data.prop_existence = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [prop_nonexistence]
    data.prop_nonexistence = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [prop_persistance]
    data.prop_persistance = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [prop_mov]
    data.prop_mov = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [classification]
    data.classification = Classification.deserialize(buffer, bufferOffset);
    // Deserialize message field [classification_mass]
    data.classification_mass = _arrayDeserializer.float64(buffer, bufferOffset, 12)
    // Deserialize message field [features]
    data.features = Features.deserialize(buffer, bufferOffset);
    // Deserialize message field [sensors_fused]
    data.sensors_fused = _arrayDeserializer.int64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 8 * object.sensors_fused.length;
    return length + 564;
  }

  static datatype() {
    // Returns string type for a message object
    return 'object_list/ObjectList';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd5793b04b71b063f6fee4d02602a19de';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 obj_id
    float64 time
    Geometric geometric
    float64[36] covariance
    Dimension dimension
    float64 prop_existence
    float64 prop_nonexistence
    float64 prop_persistance
    float64 prop_mov 
    Classification classification
    float64[12] classification_mass
    Features features
    int64[] sensors_fused
    
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
    
    
    ================================================================================
    MSG: object_list/Classification
    float32 car
    float32 truck
    float32 motorcycle
    float32 bicycle
    float32 pedestrian
    float32 stacionary
    float32 other
    
    ================================================================================
    MSG: object_list/Features
    uint8 FL
    uint8 FM
    uint8 FR
    uint8 MR
    uint8 RR
    uint8 RM
    uint8 RL
    uint8 ML
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ObjectList(null);
    if (msg.obj_id !== undefined) {
      resolved.obj_id = msg.obj_id;
    }
    else {
      resolved.obj_id = 0
    }

    if (msg.time !== undefined) {
      resolved.time = msg.time;
    }
    else {
      resolved.time = 0.0
    }

    if (msg.geometric !== undefined) {
      resolved.geometric = Geometric.Resolve(msg.geometric)
    }
    else {
      resolved.geometric = new Geometric()
    }

    if (msg.covariance !== undefined) {
      resolved.covariance = msg.covariance;
    }
    else {
      resolved.covariance = new Array(36).fill(0)
    }

    if (msg.dimension !== undefined) {
      resolved.dimension = Dimension.Resolve(msg.dimension)
    }
    else {
      resolved.dimension = new Dimension()
    }

    if (msg.prop_existence !== undefined) {
      resolved.prop_existence = msg.prop_existence;
    }
    else {
      resolved.prop_existence = 0.0
    }

    if (msg.prop_nonexistence !== undefined) {
      resolved.prop_nonexistence = msg.prop_nonexistence;
    }
    else {
      resolved.prop_nonexistence = 0.0
    }

    if (msg.prop_persistance !== undefined) {
      resolved.prop_persistance = msg.prop_persistance;
    }
    else {
      resolved.prop_persistance = 0.0
    }

    if (msg.prop_mov !== undefined) {
      resolved.prop_mov = msg.prop_mov;
    }
    else {
      resolved.prop_mov = 0.0
    }

    if (msg.classification !== undefined) {
      resolved.classification = Classification.Resolve(msg.classification)
    }
    else {
      resolved.classification = new Classification()
    }

    if (msg.classification_mass !== undefined) {
      resolved.classification_mass = msg.classification_mass;
    }
    else {
      resolved.classification_mass = new Array(12).fill(0)
    }

    if (msg.features !== undefined) {
      resolved.features = Features.Resolve(msg.features)
    }
    else {
      resolved.features = new Features()
    }

    if (msg.sensors_fused !== undefined) {
      resolved.sensors_fused = msg.sensors_fused;
    }
    else {
      resolved.sensors_fused = []
    }

    return resolved;
    }
};

module.exports = ObjectList;
