// Auto-generated. Do not edit!

// (in-package object_list.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let ObjectList = require('./ObjectList.js');
let SensorProperty = require('./SensorProperty.js');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class ObjectsList {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.obj_list = null;
      this.sensor_property = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('obj_list')) {
        this.obj_list = initObj.obj_list
      }
      else {
        this.obj_list = [];
      }
      if (initObj.hasOwnProperty('sensor_property')) {
        this.sensor_property = initObj.sensor_property
      }
      else {
        this.sensor_property = new SensorProperty();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ObjectsList
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [obj_list]
    // Serialize the length for message field [obj_list]
    bufferOffset = _serializer.uint32(obj.obj_list.length, buffer, bufferOffset);
    obj.obj_list.forEach((val) => {
      bufferOffset = ObjectList.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [sensor_property]
    bufferOffset = SensorProperty.serialize(obj.sensor_property, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ObjectsList
    let len;
    let data = new ObjectsList(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [obj_list]
    // Deserialize array length for message field [obj_list]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.obj_list = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.obj_list[i] = ObjectList.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [sensor_property]
    data.sensor_property = SensorProperty.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    object.obj_list.forEach((val) => {
      length += ObjectList.getMessageSize(val);
    });
    return length + 112;
  }

  static datatype() {
    // Returns string type for a message object
    return 'object_list/ObjectsList';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd69ee6a3db897657f81853c8b3814ced';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    ObjectList[] obj_list
    SensorProperty sensor_property
    
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
    MSG: object_list/ObjectList
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
    
    ================================================================================
    MSG: object_list/SensorProperty
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
    const resolved = new ObjectsList(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.obj_list !== undefined) {
      resolved.obj_list = new Array(msg.obj_list.length);
      for (let i = 0; i < resolved.obj_list.length; ++i) {
        resolved.obj_list[i] = ObjectList.Resolve(msg.obj_list[i]);
      }
    }
    else {
      resolved.obj_list = []
    }

    if (msg.sensor_property !== undefined) {
      resolved.sensor_property = SensorProperty.Resolve(msg.sensor_property)
    }
    else {
      resolved.sensor_property = new SensorProperty()
    }

    return resolved;
    }
};

module.exports = ObjectsList;
