// Generated by gencpp from file rosserial_mbed/Adc.msg
// DO NOT EDIT!


#ifndef ROSSERIAL_MBED_MESSAGE_ADC_H
#define ROSSERIAL_MBED_MESSAGE_ADC_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace rosserial_mbed
{
template <class ContainerAllocator>
struct Adc_
{
  typedef Adc_<ContainerAllocator> Type;

  Adc_()
    : adc0(0)
    , adc1(0)
    , adc2(0)
    , adc3(0)
    , adc4(0)
    , adc5(0)  {
    }
  Adc_(const ContainerAllocator& _alloc)
    : adc0(0)
    , adc1(0)
    , adc2(0)
    , adc3(0)
    , adc4(0)
    , adc5(0)  {
  (void)_alloc;
    }



   typedef uint16_t _adc0_type;
  _adc0_type adc0;

   typedef uint16_t _adc1_type;
  _adc1_type adc1;

   typedef uint16_t _adc2_type;
  _adc2_type adc2;

   typedef uint16_t _adc3_type;
  _adc3_type adc3;

   typedef uint16_t _adc4_type;
  _adc4_type adc4;

   typedef uint16_t _adc5_type;
  _adc5_type adc5;





  typedef boost::shared_ptr< ::rosserial_mbed::Adc_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rosserial_mbed::Adc_<ContainerAllocator> const> ConstPtr;

}; // struct Adc_

typedef ::rosserial_mbed::Adc_<std::allocator<void> > Adc;

typedef boost::shared_ptr< ::rosserial_mbed::Adc > AdcPtr;
typedef boost::shared_ptr< ::rosserial_mbed::Adc const> AdcConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rosserial_mbed::Adc_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rosserial_mbed::Adc_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::rosserial_mbed::Adc_<ContainerAllocator1> & lhs, const ::rosserial_mbed::Adc_<ContainerAllocator2> & rhs)
{
  return lhs.adc0 == rhs.adc0 &&
    lhs.adc1 == rhs.adc1 &&
    lhs.adc2 == rhs.adc2 &&
    lhs.adc3 == rhs.adc3 &&
    lhs.adc4 == rhs.adc4 &&
    lhs.adc5 == rhs.adc5;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::rosserial_mbed::Adc_<ContainerAllocator1> & lhs, const ::rosserial_mbed::Adc_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace rosserial_mbed

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::rosserial_mbed::Adc_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rosserial_mbed::Adc_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rosserial_mbed::Adc_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rosserial_mbed::Adc_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rosserial_mbed::Adc_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rosserial_mbed::Adc_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rosserial_mbed::Adc_<ContainerAllocator> >
{
  static const char* value()
  {
    return "6d7853a614e2e821319068311f2af25b";
  }

  static const char* value(const ::rosserial_mbed::Adc_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x6d7853a614e2e821ULL;
  static const uint64_t static_value2 = 0x319068311f2af25bULL;
};

template<class ContainerAllocator>
struct DataType< ::rosserial_mbed::Adc_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rosserial_mbed/Adc";
  }

  static const char* value(const ::rosserial_mbed::Adc_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rosserial_mbed::Adc_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint16 adc0\n"
"uint16 adc1\n"
"uint16 adc2\n"
"uint16 adc3\n"
"uint16 adc4\n"
"uint16 adc5\n"
;
  }

  static const char* value(const ::rosserial_mbed::Adc_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rosserial_mbed::Adc_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.adc0);
      stream.next(m.adc1);
      stream.next(m.adc2);
      stream.next(m.adc3);
      stream.next(m.adc4);
      stream.next(m.adc5);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Adc_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rosserial_mbed::Adc_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rosserial_mbed::Adc_<ContainerAllocator>& v)
  {
    s << indent << "adc0: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.adc0);
    s << indent << "adc1: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.adc1);
    s << indent << "adc2: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.adc2);
    s << indent << "adc3: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.adc3);
    s << indent << "adc4: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.adc4);
    s << indent << "adc5: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.adc5);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROSSERIAL_MBED_MESSAGE_ADC_H
