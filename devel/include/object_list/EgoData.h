// Generated by gencpp from file object_list/EgoData.msg
// DO NOT EDIT!


#ifndef OBJECT_LIST_MESSAGE_EGODATA_H
#define OBJECT_LIST_MESSAGE_EGODATA_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <object_list/Geometric.h>
#include <object_list/Dimension.h>

namespace object_list
{
template <class ContainerAllocator>
struct EgoData_
{
  typedef EgoData_<ContainerAllocator> Type;

  EgoData_()
    : header()
    , geometric()
    , dimension()  {
    }
  EgoData_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , geometric(_alloc)
    , dimension(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef  ::object_list::Geometric_<ContainerAllocator>  _geometric_type;
  _geometric_type geometric;

   typedef  ::object_list::Dimension_<ContainerAllocator>  _dimension_type;
  _dimension_type dimension;





  typedef boost::shared_ptr< ::object_list::EgoData_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::object_list::EgoData_<ContainerAllocator> const> ConstPtr;

}; // struct EgoData_

typedef ::object_list::EgoData_<std::allocator<void> > EgoData;

typedef boost::shared_ptr< ::object_list::EgoData > EgoDataPtr;
typedef boost::shared_ptr< ::object_list::EgoData const> EgoDataConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::object_list::EgoData_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::object_list::EgoData_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::object_list::EgoData_<ContainerAllocator1> & lhs, const ::object_list::EgoData_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.geometric == rhs.geometric &&
    lhs.dimension == rhs.dimension;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::object_list::EgoData_<ContainerAllocator1> & lhs, const ::object_list::EgoData_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace object_list

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::object_list::EgoData_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::object_list::EgoData_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::object_list::EgoData_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::object_list::EgoData_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::object_list::EgoData_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::object_list::EgoData_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::object_list::EgoData_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e7e294d9eaab8d77f6809dd7e07899e8";
  }

  static const char* value(const ::object_list::EgoData_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe7e294d9eaab8d77ULL;
  static const uint64_t static_value2 = 0xf6809dd7e07899e8ULL;
};

template<class ContainerAllocator>
struct DataType< ::object_list::EgoData_<ContainerAllocator> >
{
  static const char* value()
  {
    return "object_list/EgoData";
  }

  static const char* value(const ::object_list::EgoData_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::object_list::EgoData_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n"
"object_list/Geometric geometric\n"
"object_list/Dimension dimension\n"
"\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
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
;
  }

  static const char* value(const ::object_list::EgoData_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::object_list::EgoData_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.geometric);
      stream.next(m.dimension);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct EgoData_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::object_list::EgoData_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::object_list::EgoData_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "geometric: ";
    s << std::endl;
    Printer< ::object_list::Geometric_<ContainerAllocator> >::stream(s, indent + "  ", v.geometric);
    s << indent << "dimension: ";
    s << std::endl;
    Printer< ::object_list::Dimension_<ContainerAllocator> >::stream(s, indent + "  ", v.dimension);
  }
};

} // namespace message_operations
} // namespace ros

#endif // OBJECT_LIST_MESSAGE_EGODATA_H
