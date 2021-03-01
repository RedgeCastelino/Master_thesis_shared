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

class SensorProperty {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.sensor_id = null;
      this.sensortype = null;
      this.posx_variance = null;
      this.posy_variance = null;
      this.velx_variance = null;
      this.vely_variance = null;
      this.trust_existance = null;
      this.trust_car = null;
      this.trust_truck = null;
      this.trust_motorcycle = null;
      this.trust_bicycle = null;
      this.trust_pedestrian = null;
      this.trust_stationary = null;
      this.trust_other = null;
    }
    else {
      if (initObj.hasOwnProperty('sensor_id')) {
        this.sensor_id = initObj.sensor_id
      }
      else {
        this.sensor_id = 0;
      }
      if (initObj.hasOwnProperty('sensortype')) {
        this.sensortype = initObj.sensortype
      }
      else {
        this.sensortype = 0.0;
      }
      if (initObj.hasOwnProperty('posx_variance')) {
        this.posx_variance = initObj.posx_variance
      }
      else {
        this.posx_variance = 0.0;
      }
      if (initObj.hasOwnProperty('posy_variance')) {
        this.posy_variance = initObj.posy_variance
      }
      else {
        this.posy_variance = 0.0;
      }
      if (initObj.hasOwnProperty('velx_variance')) {
        this.velx_variance = initObj.velx_variance
      }
      else {
        this.velx_variance = 0.0;
      }
      if (initObj.hasOwnProperty('vely_variance')) {
        this.vely_variance = initObj.vely_variance
      }
      else {
        this.vely_variance = 0.0;
      }
      if (initObj.hasOwnProperty('trust_existance')) {
        this.trust_existance = initObj.trust_existance
      }
      else {
        this.trust_existance = 0.0;
      }
      if (initObj.hasOwnProperty('trust_car')) {
        this.trust_car = initObj.trust_car
      }
      else {
        this.trust_car = 0.0;
      }
      if (initObj.hasOwnProperty('trust_truck')) {
        this.trust_truck = initObj.trust_truck
      }
      else {
        this.trust_truck = 0.0;
      }
      if (initObj.hasOwnProperty('trust_motorcycle')) {
        this.trust_motorcycle = initObj.trust_motorcycle
      }
      else {
        this.trust_motorcycle = 0.0;
      }
      if (initObj.hasOwnProperty('trust_bicycle')) {
        this.trust_bicycle = initObj.trust_bicycle
      }
      else {
        this.trust_bicycle = 0.0;
      }
      if (initObj.hasOwnProperty('trust_pedestrian')) {
        this.trust_pedestrian = initObj.trust_pedestrian
      }
      else {
        this.trust_pedestrian = 0.0;
      }
      if (initObj.hasOwnProperty('trust_stationary')) {
        this.trust_stationary = initObj.trust_stationary
      }
      else {
        this.trust_stationary = 0.0;
      }
      if (initObj.hasOwnProperty('trust_other')) {
        this.trust_other = initObj.trust_other
      }
      else {
        this.trust_other = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SensorProperty
    // Serialize message field [sensor_id]
    bufferOffset = _serializer.int32(obj.sensor_id, buffer, bufferOffset);
    // Serialize message field [sensortype]
    bufferOffset = _serializer.float64(obj.sensortype, buffer, bufferOffset);
    // Serialize message field [posx_variance]
    bufferOffset = _serializer.float64(obj.posx_variance, buffer, bufferOffset);
    // Serialize message field [posy_variance]
    bufferOffset = _serializer.float64(obj.posy_variance, buffer, bufferOffset);
    // Serialize message field [velx_variance]
    bufferOffset = _serializer.float64(obj.velx_variance, buffer, bufferOffset);
    // Serialize message field [vely_variance]
    bufferOffset = _serializer.float64(obj.vely_variance, buffer, bufferOffset);
    // Serialize message field [trust_existance]
    bufferOffset = _serializer.float64(obj.trust_existance, buffer, bufferOffset);
    // Serialize message field [trust_car]
    bufferOffset = _serializer.float64(obj.trust_car, buffer, bufferOffset);
    // Serialize message field [trust_truck]
    bufferOffset = _serializer.float64(obj.trust_truck, buffer, bufferOffset);
    // Serialize message field [trust_motorcycle]
    bufferOffset = _serializer.float64(obj.trust_motorcycle, buffer, bufferOffset);
    // Serialize message field [trust_bicycle]
    bufferOffset = _serializer.float64(obj.trust_bicycle, buffer, bufferOffset);
    // Serialize message field [trust_pedestrian]
    bufferOffset = _serializer.float64(obj.trust_pedestrian, buffer, bufferOffset);
    // Serialize message field [trust_stationary]
    bufferOffset = _serializer.float64(obj.trust_stationary, buffer, bufferOffset);
    // Serialize message field [trust_other]
    bufferOffset = _serializer.float64(obj.trust_other, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SensorProperty
    let len;
    let data = new SensorProperty(null);
    // Deserialize message field [sensor_id]
    data.sensor_id = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [sensortype]
    data.sensortype = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [posx_variance]
    data.posx_variance = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [posy_variance]
    data.posy_variance = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [velx_variance]
    data.velx_variance = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [vely_variance]
    data.vely_variance = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [trust_existance]
    data.trust_existance = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [trust_car]
    data.trust_car = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [trust_truck]
    data.trust_truck = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [trust_motorcycle]
    data.trust_motorcycle = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [trust_bicycle]
    data.trust_bicycle = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [trust_pedestrian]
    data.trust_pedestrian = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [trust_stationary]
    data.trust_stationary = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [trust_other]
    data.trust_other = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 108;
  }

  static datatype() {
    // Returns string type for a message object
    return 'object_list/SensorProperty';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b92131fc47bc49b0227fc3ddb6760ee8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 sensor_id
    float64 sensortype
    float64 posx_variance
    float64 posy_variance
    float64 velx_variance
    float64 vely_variance
    float64 trust_existance
    float64 trust_car
    float64 trust_truck
    float64 trust_motorcycle
    float64 trust_bicycle
    float64 trust_pedestrian
    float64 trust_stationary
    float64 trust_other 
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SensorProperty(null);
    if (msg.sensor_id !== undefined) {
      resolved.sensor_id = msg.sensor_id;
    }
    else {
      resolved.sensor_id = 0
    }

    if (msg.sensortype !== undefined) {
      resolved.sensortype = msg.sensortype;
    }
    else {
      resolved.sensortype = 0.0
    }

    if (msg.posx_variance !== undefined) {
      resolved.posx_variance = msg.posx_variance;
    }
    else {
      resolved.posx_variance = 0.0
    }

    if (msg.posy_variance !== undefined) {
      resolved.posy_variance = msg.posy_variance;
    }
    else {
      resolved.posy_variance = 0.0
    }

    if (msg.velx_variance !== undefined) {
      resolved.velx_variance = msg.velx_variance;
    }
    else {
      resolved.velx_variance = 0.0
    }

    if (msg.vely_variance !== undefined) {
      resolved.vely_variance = msg.vely_variance;
    }
    else {
      resolved.vely_variance = 0.0
    }

    if (msg.trust_existance !== undefined) {
      resolved.trust_existance = msg.trust_existance;
    }
    else {
      resolved.trust_existance = 0.0
    }

    if (msg.trust_car !== undefined) {
      resolved.trust_car = msg.trust_car;
    }
    else {
      resolved.trust_car = 0.0
    }

    if (msg.trust_truck !== undefined) {
      resolved.trust_truck = msg.trust_truck;
    }
    else {
      resolved.trust_truck = 0.0
    }

    if (msg.trust_motorcycle !== undefined) {
      resolved.trust_motorcycle = msg.trust_motorcycle;
    }
    else {
      resolved.trust_motorcycle = 0.0
    }

    if (msg.trust_bicycle !== undefined) {
      resolved.trust_bicycle = msg.trust_bicycle;
    }
    else {
      resolved.trust_bicycle = 0.0
    }

    if (msg.trust_pedestrian !== undefined) {
      resolved.trust_pedestrian = msg.trust_pedestrian;
    }
    else {
      resolved.trust_pedestrian = 0.0
    }

    if (msg.trust_stationary !== undefined) {
      resolved.trust_stationary = msg.trust_stationary;
    }
    else {
      resolved.trust_stationary = 0.0
    }

    if (msg.trust_other !== undefined) {
      resolved.trust_other = msg.trust_other;
    }
    else {
      resolved.trust_other = 0.0
    }

    return resolved;
    }
};

module.exports = SensorProperty;
