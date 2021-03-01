// Generated by gencpp from file object_list/SensorProperty.msg
// DO NOT EDIT!


#ifndef OBJECT_LIST_MESSAGE_SENSORPROPERTY_H
#define OBJECT_LIST_MESSAGE_SENSORPROPERTY_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace object_list
{
template <class ContainerAllocator>
struct SensorProperty_
{
  typedef SensorProperty_<ContainerAllocator> Type;

  SensorProperty_()
    : sensor_id(0)
    , sensortype(0.0)
    , posx_variance(0.0)
    , posy_variance(0.0)
    , velx_variance(0.0)
    , vely_variance(0.0)
    , trust_existance(0.0)
    , trust_car(0.0)
    , trust_truck(0.0)
    , trust_motorcycle(0.0)
    , trust_bicycle(0.0)
    , trust_pedestrian(0.0)
    , trust_stationary(0.0)
    , trust_other(0.0)  {
    }
  SensorProperty_(const ContainerAllocator& _alloc)
    : sensor_id(0)
    , sensortype(0.0)
    , posx_variance(0.0)
    , posy_variance(0.0)
    , velx_variance(0.0)
    , vely_variance(0.0)
    , trust_existance(0.0)
    , trust_car(0.0)
    , trust_truck(0.0)
    , trust_motorcycle(0.0)
    , trust_bicycle(0.0)
    , trust_pedestrian(0.0)
    , trust_stationary(0.0)
    , trust_other(0.0)  {
  (void)_alloc;
    }



   typedef int32_t _sensor_id_type;
  _sensor_id_type sensor_id;

   typedef double _sensortype_type;
  _sensortype_type sensortype;

   typedef double _posx_variance_type;
  _posx_variance_type posx_variance;

   typedef double _posy_variance_type;
  _posy_variance_type posy_variance;

   typedef double _velx_variance_type;
  _velx_variance_type velx_variance;

   typedef double _vely_variance_type;
  _vely_variance_type vely_variance;

   typedef double _trust_existance_type;
  _trust_existance_type trust_existance;

   typedef double _trust_car_type;
  _trust_car_type trust_car;

   typedef double _trust_truck_type;
  _trust_truck_type trust_truck;

   typedef double _trust_motorcycle_type;
  _trust_motorcycle_type trust_motorcycle;

   typedef double _trust_bicycle_type;
  _trust_bicycle_type trust_bicycle;

   typedef double _trust_pedestrian_type;
  _trust_pedestrian_type trust_pedestrian;

   typedef double _trust_stationary_type;
  _trust_stationary_type trust_stationary;

   typedef double _trust_other_type;
  _trust_other_type trust_other;





  typedef boost::shared_ptr< ::object_list::SensorProperty_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::object_list::SensorProperty_<ContainerAllocator> const> ConstPtr;

}; // struct SensorProperty_

typedef ::object_list::SensorProperty_<std::allocator<void> > SensorProperty;

typedef boost::shared_ptr< ::object_list::SensorProperty > SensorPropertyPtr;
typedef boost::shared_ptr< ::object_list::SensorProperty const> SensorPropertyConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::object_list::SensorProperty_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::object_list::SensorProperty_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::object_list::SensorProperty_<ContainerAllocator1> & lhs, const ::object_list::SensorProperty_<ContainerAllocator2> & rhs)
{
  return lhs.sensor_id == rhs.sensor_id &&
    lhs.sensortype == rhs.sensortype &&
    lhs.posx_variance == rhs.posx_variance &&
    lhs.posy_variance == rhs.posy_variance &&
    lhs.velx_variance == rhs.velx_variance &&
    lhs.vely_variance == rhs.vely_variance &&
    lhs.trust_existance == rhs.trust_existance &&
    lhs.trust_car == rhs.trust_car &&
    lhs.trust_truck == rhs.trust_truck &&
    lhs.trust_motorcycle == rhs.trust_motorcycle &&
    lhs.trust_bicycle == rhs.trust_bicycle &&
    lhs.trust_pedestrian == rhs.trust_pedestrian &&
    lhs.trust_stationary == rhs.trust_stationary &&
    lhs.trust_other == rhs.trust_other;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::object_list::SensorProperty_<ContainerAllocator1> & lhs, const ::object_list::SensorProperty_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace object_list

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::object_list::SensorProperty_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::object_list::SensorProperty_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::object_list::SensorProperty_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::object_list::SensorProperty_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::object_list::SensorProperty_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::object_list::SensorProperty_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::object_list::SensorProperty_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b92131fc47bc49b0227fc3ddb6760ee8";
  }

  static const char* value(const ::object_list::SensorProperty_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb92131fc47bc49b0ULL;
  static const uint64_t static_value2 = 0x227fc3ddb6760ee8ULL;
};

template<class ContainerAllocator>
struct DataType< ::object_list::SensorProperty_<ContainerAllocator> >
{
  static const char* value()
  {
    return "object_list/SensorProperty";
  }

  static const char* value(const ::object_list::SensorProperty_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::object_list::SensorProperty_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 sensor_id\n"
"float64 sensortype\n"
"float64 posx_variance\n"
"float64 posy_variance\n"
"float64 velx_variance\n"
"float64 vely_variance\n"
"float64 trust_existance\n"
"float64 trust_car\n"
"float64 trust_truck\n"
"float64 trust_motorcycle\n"
"float64 trust_bicycle\n"
"float64 trust_pedestrian\n"
"float64 trust_stationary\n"
"float64 trust_other \n"
;
  }

  static const char* value(const ::object_list::SensorProperty_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::object_list::SensorProperty_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.sensor_id);
      stream.next(m.sensortype);
      stream.next(m.posx_variance);
      stream.next(m.posy_variance);
      stream.next(m.velx_variance);
      stream.next(m.vely_variance);
      stream.next(m.trust_existance);
      stream.next(m.trust_car);
      stream.next(m.trust_truck);
      stream.next(m.trust_motorcycle);
      stream.next(m.trust_bicycle);
      stream.next(m.trust_pedestrian);
      stream.next(m.trust_stationary);
      stream.next(m.trust_other);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SensorProperty_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::object_list::SensorProperty_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::object_list::SensorProperty_<ContainerAllocator>& v)
  {
    s << indent << "sensor_id: ";
    Printer<int32_t>::stream(s, indent + "  ", v.sensor_id);
    s << indent << "sensortype: ";
    Printer<double>::stream(s, indent + "  ", v.sensortype);
    s << indent << "posx_variance: ";
    Printer<double>::stream(s, indent + "  ", v.posx_variance);
    s << indent << "posy_variance: ";
    Printer<double>::stream(s, indent + "  ", v.posy_variance);
    s << indent << "velx_variance: ";
    Printer<double>::stream(s, indent + "  ", v.velx_variance);
    s << indent << "vely_variance: ";
    Printer<double>::stream(s, indent + "  ", v.vely_variance);
    s << indent << "trust_existance: ";
    Printer<double>::stream(s, indent + "  ", v.trust_existance);
    s << indent << "trust_car: ";
    Printer<double>::stream(s, indent + "  ", v.trust_car);
    s << indent << "trust_truck: ";
    Printer<double>::stream(s, indent + "  ", v.trust_truck);
    s << indent << "trust_motorcycle: ";
    Printer<double>::stream(s, indent + "  ", v.trust_motorcycle);
    s << indent << "trust_bicycle: ";
    Printer<double>::stream(s, indent + "  ", v.trust_bicycle);
    s << indent << "trust_pedestrian: ";
    Printer<double>::stream(s, indent + "  ", v.trust_pedestrian);
    s << indent << "trust_stationary: ";
    Printer<double>::stream(s, indent + "  ", v.trust_stationary);
    s << indent << "trust_other: ";
    Printer<double>::stream(s, indent + "  ", v.trust_other);
  }
};

} // namespace message_operations
} // namespace ros

#endif // OBJECT_LIST_MESSAGE_SENSORPROPERTY_H
