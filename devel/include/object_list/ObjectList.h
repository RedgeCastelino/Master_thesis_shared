// Generated by gencpp from file object_list/ObjectList.msg
// DO NOT EDIT!


#ifndef OBJECT_LIST_MESSAGE_OBJECTLIST_H
#define OBJECT_LIST_MESSAGE_OBJECTLIST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <object_list/Geometric.h>
#include <object_list/Dimension.h>
#include <object_list/Classification.h>
#include <object_list/Features.h>

namespace object_list
{
template <class ContainerAllocator>
struct ObjectList_
{
  typedef ObjectList_<ContainerAllocator> Type;

  ObjectList_()
    : obj_id(0)
    , time(0.0)
    , geometric()
    , covariance()
    , dimension()
    , prop_existence(0.0)
    , prop_nonexistence(0.0)
    , prop_persistance(0.0)
    , prop_mov(0.0)
    , classification()
    , classification_mass()
    , features()
    , sensors_fused()  {
      covariance.assign(0.0);

      classification_mass.assign(0.0);
  }
  ObjectList_(const ContainerAllocator& _alloc)
    : obj_id(0)
    , time(0.0)
    , geometric(_alloc)
    , covariance()
    , dimension(_alloc)
    , prop_existence(0.0)
    , prop_nonexistence(0.0)
    , prop_persistance(0.0)
    , prop_mov(0.0)
    , classification(_alloc)
    , classification_mass()
    , features(_alloc)
    , sensors_fused(_alloc)  {
  (void)_alloc;
      covariance.assign(0.0);

      classification_mass.assign(0.0);
  }



   typedef int32_t _obj_id_type;
  _obj_id_type obj_id;

   typedef double _time_type;
  _time_type time;

   typedef  ::object_list::Geometric_<ContainerAllocator>  _geometric_type;
  _geometric_type geometric;

   typedef boost::array<double, 36>  _covariance_type;
  _covariance_type covariance;

   typedef  ::object_list::Dimension_<ContainerAllocator>  _dimension_type;
  _dimension_type dimension;

   typedef double _prop_existence_type;
  _prop_existence_type prop_existence;

   typedef double _prop_nonexistence_type;
  _prop_nonexistence_type prop_nonexistence;

   typedef double _prop_persistance_type;
  _prop_persistance_type prop_persistance;

   typedef double _prop_mov_type;
  _prop_mov_type prop_mov;

   typedef  ::object_list::Classification_<ContainerAllocator>  _classification_type;
  _classification_type classification;

   typedef boost::array<double, 12>  _classification_mass_type;
  _classification_mass_type classification_mass;

   typedef  ::object_list::Features_<ContainerAllocator>  _features_type;
  _features_type features;

   typedef std::vector<int64_t, typename ContainerAllocator::template rebind<int64_t>::other >  _sensors_fused_type;
  _sensors_fused_type sensors_fused;





  typedef boost::shared_ptr< ::object_list::ObjectList_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::object_list::ObjectList_<ContainerAllocator> const> ConstPtr;

}; // struct ObjectList_

typedef ::object_list::ObjectList_<std::allocator<void> > ObjectList;

typedef boost::shared_ptr< ::object_list::ObjectList > ObjectListPtr;
typedef boost::shared_ptr< ::object_list::ObjectList const> ObjectListConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::object_list::ObjectList_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::object_list::ObjectList_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::object_list::ObjectList_<ContainerAllocator1> & lhs, const ::object_list::ObjectList_<ContainerAllocator2> & rhs)
{
  return lhs.obj_id == rhs.obj_id &&
    lhs.time == rhs.time &&
    lhs.geometric == rhs.geometric &&
    lhs.covariance == rhs.covariance &&
    lhs.dimension == rhs.dimension &&
    lhs.prop_existence == rhs.prop_existence &&
    lhs.prop_nonexistence == rhs.prop_nonexistence &&
    lhs.prop_persistance == rhs.prop_persistance &&
    lhs.prop_mov == rhs.prop_mov &&
    lhs.classification == rhs.classification &&
    lhs.classification_mass == rhs.classification_mass &&
    lhs.features == rhs.features &&
    lhs.sensors_fused == rhs.sensors_fused;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::object_list::ObjectList_<ContainerAllocator1> & lhs, const ::object_list::ObjectList_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace object_list

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::object_list::ObjectList_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::object_list::ObjectList_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::object_list::ObjectList_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::object_list::ObjectList_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::object_list::ObjectList_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::object_list::ObjectList_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::object_list::ObjectList_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d5793b04b71b063f6fee4d02602a19de";
  }

  static const char* value(const ::object_list::ObjectList_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd5793b04b71b063fULL;
  static const uint64_t static_value2 = 0x6fee4d02602a19deULL;
};

template<class ContainerAllocator>
struct DataType< ::object_list::ObjectList_<ContainerAllocator> >
{
  static const char* value()
  {
    return "object_list/ObjectList";
  }

  static const char* value(const ::object_list::ObjectList_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::object_list::ObjectList_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 obj_id\n"
"float64 time\n"
"Geometric geometric\n"
"float64[36] covariance\n"
"Dimension dimension\n"
"float64 prop_existence\n"
"float64 prop_nonexistence\n"
"float64 prop_persistance\n"
"float64 prop_mov \n"
"Classification classification\n"
"float64[12] classification_mass\n"
"Features features\n"
"int64[] sensors_fused\n"
"\n"
"================================================================================\n"
"MSG: object_list/Geometric\n"
"float64 x\n"
"float64 y\n"
"float64 vx\n"
"float64 vy\n"
"float64 ax\n"
"float64 ay\n"
"float64 yaw\n"
"float64 yawrate\n"
"\n"
"================================================================================\n"
"MSG: object_list/Dimension\n"
"float64 length\n"
"float64 width\n"
"float64 length_variance\n"
"float64 width_variance\n"
"\n"
"\n"
"================================================================================\n"
"MSG: object_list/Classification\n"
"float32 car\n"
"float32 truck\n"
"float32 motorcycle\n"
"float32 bicycle\n"
"float32 pedestrian\n"
"float32 stacionary\n"
"float32 other\n"
"\n"
"================================================================================\n"
"MSG: object_list/Features\n"
"uint8 FL\n"
"uint8 FM\n"
"uint8 FR\n"
"uint8 MR\n"
"uint8 RR\n"
"uint8 RM\n"
"uint8 RL\n"
"uint8 ML\n"
;
  }

  static const char* value(const ::object_list::ObjectList_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::object_list::ObjectList_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.obj_id);
      stream.next(m.time);
      stream.next(m.geometric);
      stream.next(m.covariance);
      stream.next(m.dimension);
      stream.next(m.prop_existence);
      stream.next(m.prop_nonexistence);
      stream.next(m.prop_persistance);
      stream.next(m.prop_mov);
      stream.next(m.classification);
      stream.next(m.classification_mass);
      stream.next(m.features);
      stream.next(m.sensors_fused);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ObjectList_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::object_list::ObjectList_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::object_list::ObjectList_<ContainerAllocator>& v)
  {
    s << indent << "obj_id: ";
    Printer<int32_t>::stream(s, indent + "  ", v.obj_id);
    s << indent << "time: ";
    Printer<double>::stream(s, indent + "  ", v.time);
    s << indent << "geometric: ";
    s << std::endl;
    Printer< ::object_list::Geometric_<ContainerAllocator> >::stream(s, indent + "  ", v.geometric);
    s << indent << "covariance[]" << std::endl;
    for (size_t i = 0; i < v.covariance.size(); ++i)
    {
      s << indent << "  covariance[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.covariance[i]);
    }
    s << indent << "dimension: ";
    s << std::endl;
    Printer< ::object_list::Dimension_<ContainerAllocator> >::stream(s, indent + "  ", v.dimension);
    s << indent << "prop_existence: ";
    Printer<double>::stream(s, indent + "  ", v.prop_existence);
    s << indent << "prop_nonexistence: ";
    Printer<double>::stream(s, indent + "  ", v.prop_nonexistence);
    s << indent << "prop_persistance: ";
    Printer<double>::stream(s, indent + "  ", v.prop_persistance);
    s << indent << "prop_mov: ";
    Printer<double>::stream(s, indent + "  ", v.prop_mov);
    s << indent << "classification: ";
    s << std::endl;
    Printer< ::object_list::Classification_<ContainerAllocator> >::stream(s, indent + "  ", v.classification);
    s << indent << "classification_mass[]" << std::endl;
    for (size_t i = 0; i < v.classification_mass.size(); ++i)
    {
      s << indent << "  classification_mass[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.classification_mass[i]);
    }
    s << indent << "features: ";
    s << std::endl;
    Printer< ::object_list::Features_<ContainerAllocator> >::stream(s, indent + "  ", v.features);
    s << indent << "sensors_fused[]" << std::endl;
    for (size_t i = 0; i < v.sensors_fused.size(); ++i)
    {
      s << indent << "  sensors_fused[" << i << "]: ";
      Printer<int64_t>::stream(s, indent + "  ", v.sensors_fused[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // OBJECT_LIST_MESSAGE_OBJECTLIST_H
