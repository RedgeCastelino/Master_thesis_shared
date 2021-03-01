// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: osi_sensorspecific.proto

#define INTERNAL_SUPPRESS_PROTOBUF_FIELD_DEPRECATION
#include "osi_sensorspecific.pb.h"

#include <algorithm>

#include <google/protobuf/stubs/common.h>
#include <google/protobuf/stubs/port.h>
#include <google/protobuf/stubs/once.h>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/wire_format_lite_inl.h>
#include <google/protobuf/descriptor.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/reflection_ops.h>
#include <google/protobuf/wire_format.h>
// @@protoc_insertion_point(includes)

namespace osi3 {

namespace {

const ::google::protobuf::Descriptor* RadarSpecificObjectData_descriptor_ = NULL;
const ::google::protobuf::internal::GeneratedMessageReflection*
  RadarSpecificObjectData_reflection_ = NULL;
const ::google::protobuf::Descriptor* LidarSpecificObjectData_descriptor_ = NULL;
const ::google::protobuf::internal::GeneratedMessageReflection*
  LidarSpecificObjectData_reflection_ = NULL;
const ::google::protobuf::Descriptor* CameraSpecificObjectData_descriptor_ = NULL;
const ::google::protobuf::internal::GeneratedMessageReflection*
  CameraSpecificObjectData_reflection_ = NULL;
const ::google::protobuf::Descriptor* UltrasonicSpecificObjectData_descriptor_ = NULL;
const ::google::protobuf::internal::GeneratedMessageReflection*
  UltrasonicSpecificObjectData_reflection_ = NULL;

}  // namespace


void protobuf_AssignDesc_osi_5fsensorspecific_2eproto() GOOGLE_ATTRIBUTE_COLD;
void protobuf_AssignDesc_osi_5fsensorspecific_2eproto() {
  protobuf_AddDesc_osi_5fsensorspecific_2eproto();
  const ::google::protobuf::FileDescriptor* file =
    ::google::protobuf::DescriptorPool::generated_pool()->FindFileByName(
      "osi_sensorspecific.proto");
  GOOGLE_CHECK(file != NULL);
  RadarSpecificObjectData_descriptor_ = file->message_type(0);
  static const int RadarSpecificObjectData_offsets_[1] = {
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(RadarSpecificObjectData, rcs_),
  };
  RadarSpecificObjectData_reflection_ =
    ::google::protobuf::internal::GeneratedMessageReflection::NewGeneratedMessageReflection(
      RadarSpecificObjectData_descriptor_,
      RadarSpecificObjectData::default_instance_,
      RadarSpecificObjectData_offsets_,
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(RadarSpecificObjectData, _has_bits_[0]),
      -1,
      -1,
      sizeof(RadarSpecificObjectData),
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(RadarSpecificObjectData, _internal_metadata_),
      -1);
  LidarSpecificObjectData_descriptor_ = file->message_type(1);
  static const int LidarSpecificObjectData_offsets_[1] = {
  };
  LidarSpecificObjectData_reflection_ =
    ::google::protobuf::internal::GeneratedMessageReflection::NewGeneratedMessageReflection(
      LidarSpecificObjectData_descriptor_,
      LidarSpecificObjectData::default_instance_,
      LidarSpecificObjectData_offsets_,
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(LidarSpecificObjectData, _has_bits_[0]),
      -1,
      -1,
      sizeof(LidarSpecificObjectData),
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(LidarSpecificObjectData, _internal_metadata_),
      -1);
  CameraSpecificObjectData_descriptor_ = file->message_type(2);
  static const int CameraSpecificObjectData_offsets_[1] = {
  };
  CameraSpecificObjectData_reflection_ =
    ::google::protobuf::internal::GeneratedMessageReflection::NewGeneratedMessageReflection(
      CameraSpecificObjectData_descriptor_,
      CameraSpecificObjectData::default_instance_,
      CameraSpecificObjectData_offsets_,
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(CameraSpecificObjectData, _has_bits_[0]),
      -1,
      -1,
      sizeof(CameraSpecificObjectData),
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(CameraSpecificObjectData, _internal_metadata_),
      -1);
  UltrasonicSpecificObjectData_descriptor_ = file->message_type(3);
  static const int UltrasonicSpecificObjectData_offsets_[1] = {
  };
  UltrasonicSpecificObjectData_reflection_ =
    ::google::protobuf::internal::GeneratedMessageReflection::NewGeneratedMessageReflection(
      UltrasonicSpecificObjectData_descriptor_,
      UltrasonicSpecificObjectData::default_instance_,
      UltrasonicSpecificObjectData_offsets_,
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(UltrasonicSpecificObjectData, _has_bits_[0]),
      -1,
      -1,
      sizeof(UltrasonicSpecificObjectData),
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(UltrasonicSpecificObjectData, _internal_metadata_),
      -1);
}

namespace {

GOOGLE_PROTOBUF_DECLARE_ONCE(protobuf_AssignDescriptors_once_);
inline void protobuf_AssignDescriptorsOnce() {
  ::google::protobuf::GoogleOnceInit(&protobuf_AssignDescriptors_once_,
                 &protobuf_AssignDesc_osi_5fsensorspecific_2eproto);
}

void protobuf_RegisterTypes(const ::std::string&) GOOGLE_ATTRIBUTE_COLD;
void protobuf_RegisterTypes(const ::std::string&) {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedMessage(
      RadarSpecificObjectData_descriptor_, &RadarSpecificObjectData::default_instance());
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedMessage(
      LidarSpecificObjectData_descriptor_, &LidarSpecificObjectData::default_instance());
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedMessage(
      CameraSpecificObjectData_descriptor_, &CameraSpecificObjectData::default_instance());
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedMessage(
      UltrasonicSpecificObjectData_descriptor_, &UltrasonicSpecificObjectData::default_instance());
}

}  // namespace

void protobuf_ShutdownFile_osi_5fsensorspecific_2eproto() {
  delete RadarSpecificObjectData::default_instance_;
  delete RadarSpecificObjectData_reflection_;
  delete LidarSpecificObjectData::default_instance_;
  delete LidarSpecificObjectData_reflection_;
  delete CameraSpecificObjectData::default_instance_;
  delete CameraSpecificObjectData_reflection_;
  delete UltrasonicSpecificObjectData::default_instance_;
  delete UltrasonicSpecificObjectData_reflection_;
}

void protobuf_AddDesc_osi_5fsensorspecific_2eproto() GOOGLE_ATTRIBUTE_COLD;
void protobuf_AddDesc_osi_5fsensorspecific_2eproto() {
  static bool already_here = false;
  if (already_here) return;
  already_here = true;
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  ::google::protobuf::DescriptorPool::InternalAddGeneratedFile(
    "\n\030osi_sensorspecific.proto\022\004osi3\"&\n\027Rada"
    "rSpecificObjectData\022\013\n\003rcs\030\001 \001(\001\"\031\n\027Lida"
    "rSpecificObjectData\"\032\n\030CameraSpecificObj"
    "ectData\"\036\n\034UltrasonicSpecificObjectDataB"
    "\002H\001", 163);
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedFile(
    "osi_sensorspecific.proto", &protobuf_RegisterTypes);
  RadarSpecificObjectData::default_instance_ = new RadarSpecificObjectData();
  LidarSpecificObjectData::default_instance_ = new LidarSpecificObjectData();
  CameraSpecificObjectData::default_instance_ = new CameraSpecificObjectData();
  UltrasonicSpecificObjectData::default_instance_ = new UltrasonicSpecificObjectData();
  RadarSpecificObjectData::default_instance_->InitAsDefaultInstance();
  LidarSpecificObjectData::default_instance_->InitAsDefaultInstance();
  CameraSpecificObjectData::default_instance_->InitAsDefaultInstance();
  UltrasonicSpecificObjectData::default_instance_->InitAsDefaultInstance();
  ::google::protobuf::internal::OnShutdown(&protobuf_ShutdownFile_osi_5fsensorspecific_2eproto);
}

// Force AddDescriptors() to be called at static initialization time.
struct StaticDescriptorInitializer_osi_5fsensorspecific_2eproto {
  StaticDescriptorInitializer_osi_5fsensorspecific_2eproto() {
    protobuf_AddDesc_osi_5fsensorspecific_2eproto();
  }
} static_descriptor_initializer_osi_5fsensorspecific_2eproto_;

// ===================================================================

#if !defined(_MSC_VER) || _MSC_VER >= 1900
const int RadarSpecificObjectData::kRcsFieldNumber;
#endif  // !defined(_MSC_VER) || _MSC_VER >= 1900

RadarSpecificObjectData::RadarSpecificObjectData()
  : ::google::protobuf::Message(), _internal_metadata_(NULL) {
  SharedCtor();
  // @@protoc_insertion_point(constructor:osi3.RadarSpecificObjectData)
}

void RadarSpecificObjectData::InitAsDefaultInstance() {
}

RadarSpecificObjectData::RadarSpecificObjectData(const RadarSpecificObjectData& from)
  : ::google::protobuf::Message(),
    _internal_metadata_(NULL) {
  SharedCtor();
  MergeFrom(from);
  // @@protoc_insertion_point(copy_constructor:osi3.RadarSpecificObjectData)
}

void RadarSpecificObjectData::SharedCtor() {
  _cached_size_ = 0;
  rcs_ = 0;
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
}

RadarSpecificObjectData::~RadarSpecificObjectData() {
  // @@protoc_insertion_point(destructor:osi3.RadarSpecificObjectData)
  SharedDtor();
}

void RadarSpecificObjectData::SharedDtor() {
  if (this != default_instance_) {
  }
}

void RadarSpecificObjectData::SetCachedSize(int size) const {
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
}
const ::google::protobuf::Descriptor* RadarSpecificObjectData::descriptor() {
  protobuf_AssignDescriptorsOnce();
  return RadarSpecificObjectData_descriptor_;
}

const RadarSpecificObjectData& RadarSpecificObjectData::default_instance() {
  if (default_instance_ == NULL) protobuf_AddDesc_osi_5fsensorspecific_2eproto();
  return *default_instance_;
}

RadarSpecificObjectData* RadarSpecificObjectData::default_instance_ = NULL;

RadarSpecificObjectData* RadarSpecificObjectData::New(::google::protobuf::Arena* arena) const {
  RadarSpecificObjectData* n = new RadarSpecificObjectData;
  if (arena != NULL) {
    arena->Own(n);
  }
  return n;
}

void RadarSpecificObjectData::Clear() {
// @@protoc_insertion_point(message_clear_start:osi3.RadarSpecificObjectData)
  rcs_ = 0;
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
  if (_internal_metadata_.have_unknown_fields()) {
    mutable_unknown_fields()->Clear();
  }
}

bool RadarSpecificObjectData::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!GOOGLE_PREDICT_TRUE(EXPRESSION)) goto failure
  ::google::protobuf::uint32 tag;
  // @@protoc_insertion_point(parse_start:osi3.RadarSpecificObjectData)
  for (;;) {
    ::std::pair< ::google::protobuf::uint32, bool> p = input->ReadTagWithCutoff(127);
    tag = p.first;
    if (!p.second) goto handle_unusual;
    switch (::google::protobuf::internal::WireFormatLite::GetTagFieldNumber(tag)) {
      // optional double rcs = 1;
      case 1: {
        if (tag == 9) {
          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   double, ::google::protobuf::internal::WireFormatLite::TYPE_DOUBLE>(
                 input, &rcs_)));
          set_has_rcs();
        } else {
          goto handle_unusual;
        }
        if (input->ExpectAtEnd()) goto success;
        break;
      }

      default: {
      handle_unusual:
        if (tag == 0 ||
            ::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_END_GROUP) {
          goto success;
        }
        DO_(::google::protobuf::internal::WireFormat::SkipField(
              input, tag, mutable_unknown_fields()));
        break;
      }
    }
  }
success:
  // @@protoc_insertion_point(parse_success:osi3.RadarSpecificObjectData)
  return true;
failure:
  // @@protoc_insertion_point(parse_failure:osi3.RadarSpecificObjectData)
  return false;
#undef DO_
}

void RadarSpecificObjectData::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // @@protoc_insertion_point(serialize_start:osi3.RadarSpecificObjectData)
  // optional double rcs = 1;
  if (has_rcs()) {
    ::google::protobuf::internal::WireFormatLite::WriteDouble(1, this->rcs(), output);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        unknown_fields(), output);
  }
  // @@protoc_insertion_point(serialize_end:osi3.RadarSpecificObjectData)
}

::google::protobuf::uint8* RadarSpecificObjectData::InternalSerializeWithCachedSizesToArray(
    bool deterministic, ::google::protobuf::uint8* target) const {
  // @@protoc_insertion_point(serialize_to_array_start:osi3.RadarSpecificObjectData)
  // optional double rcs = 1;
  if (has_rcs()) {
    target = ::google::protobuf::internal::WireFormatLite::WriteDoubleToArray(1, this->rcs(), target);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        unknown_fields(), target);
  }
  // @@protoc_insertion_point(serialize_to_array_end:osi3.RadarSpecificObjectData)
  return target;
}

int RadarSpecificObjectData::ByteSize() const {
// @@protoc_insertion_point(message_byte_size_start:osi3.RadarSpecificObjectData)
  int total_size = 0;

  // optional double rcs = 1;
  if (has_rcs()) {
    total_size += 1 + 8;
  }

  if (_internal_metadata_.have_unknown_fields()) {
    total_size +=
      ::google::protobuf::internal::WireFormat::ComputeUnknownFieldsSize(
        unknown_fields());
  }
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = total_size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
  return total_size;
}

void RadarSpecificObjectData::MergeFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:osi3.RadarSpecificObjectData)
  if (GOOGLE_PREDICT_FALSE(&from == this)) {
    ::google::protobuf::internal::MergeFromFail(__FILE__, __LINE__);
  }
  const RadarSpecificObjectData* source = 
      ::google::protobuf::internal::DynamicCastToGenerated<const RadarSpecificObjectData>(
          &from);
  if (source == NULL) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:osi3.RadarSpecificObjectData)
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:osi3.RadarSpecificObjectData)
    MergeFrom(*source);
  }
}

void RadarSpecificObjectData::MergeFrom(const RadarSpecificObjectData& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:osi3.RadarSpecificObjectData)
  if (GOOGLE_PREDICT_FALSE(&from == this)) {
    ::google::protobuf::internal::MergeFromFail(__FILE__, __LINE__);
  }
  if (from._has_bits_[0 / 32] & (0xffu << (0 % 32))) {
    if (from.has_rcs()) {
      set_rcs(from.rcs());
    }
  }
  if (from._internal_metadata_.have_unknown_fields()) {
    mutable_unknown_fields()->MergeFrom(from.unknown_fields());
  }
}

void RadarSpecificObjectData::CopyFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:osi3.RadarSpecificObjectData)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void RadarSpecificObjectData::CopyFrom(const RadarSpecificObjectData& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:osi3.RadarSpecificObjectData)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool RadarSpecificObjectData::IsInitialized() const {

  return true;
}

void RadarSpecificObjectData::Swap(RadarSpecificObjectData* other) {
  if (other == this) return;
  InternalSwap(other);
}
void RadarSpecificObjectData::InternalSwap(RadarSpecificObjectData* other) {
  std::swap(rcs_, other->rcs_);
  std::swap(_has_bits_[0], other->_has_bits_[0]);
  _internal_metadata_.Swap(&other->_internal_metadata_);
  std::swap(_cached_size_, other->_cached_size_);
}

::google::protobuf::Metadata RadarSpecificObjectData::GetMetadata() const {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::Metadata metadata;
  metadata.descriptor = RadarSpecificObjectData_descriptor_;
  metadata.reflection = RadarSpecificObjectData_reflection_;
  return metadata;
}

#if PROTOBUF_INLINE_NOT_IN_HEADERS
// RadarSpecificObjectData

// optional double rcs = 1;
bool RadarSpecificObjectData::has_rcs() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
void RadarSpecificObjectData::set_has_rcs() {
  _has_bits_[0] |= 0x00000001u;
}
void RadarSpecificObjectData::clear_has_rcs() {
  _has_bits_[0] &= ~0x00000001u;
}
void RadarSpecificObjectData::clear_rcs() {
  rcs_ = 0;
  clear_has_rcs();
}
 double RadarSpecificObjectData::rcs() const {
  // @@protoc_insertion_point(field_get:osi3.RadarSpecificObjectData.rcs)
  return rcs_;
}
 void RadarSpecificObjectData::set_rcs(double value) {
  set_has_rcs();
  rcs_ = value;
  // @@protoc_insertion_point(field_set:osi3.RadarSpecificObjectData.rcs)
}

#endif  // PROTOBUF_INLINE_NOT_IN_HEADERS

// ===================================================================

#if !defined(_MSC_VER) || _MSC_VER >= 1900
#endif  // !defined(_MSC_VER) || _MSC_VER >= 1900

LidarSpecificObjectData::LidarSpecificObjectData()
  : ::google::protobuf::Message(), _internal_metadata_(NULL) {
  SharedCtor();
  // @@protoc_insertion_point(constructor:osi3.LidarSpecificObjectData)
}

void LidarSpecificObjectData::InitAsDefaultInstance() {
}

LidarSpecificObjectData::LidarSpecificObjectData(const LidarSpecificObjectData& from)
  : ::google::protobuf::Message(),
    _internal_metadata_(NULL) {
  SharedCtor();
  MergeFrom(from);
  // @@protoc_insertion_point(copy_constructor:osi3.LidarSpecificObjectData)
}

void LidarSpecificObjectData::SharedCtor() {
  _cached_size_ = 0;
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
}

LidarSpecificObjectData::~LidarSpecificObjectData() {
  // @@protoc_insertion_point(destructor:osi3.LidarSpecificObjectData)
  SharedDtor();
}

void LidarSpecificObjectData::SharedDtor() {
  if (this != default_instance_) {
  }
}

void LidarSpecificObjectData::SetCachedSize(int size) const {
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
}
const ::google::protobuf::Descriptor* LidarSpecificObjectData::descriptor() {
  protobuf_AssignDescriptorsOnce();
  return LidarSpecificObjectData_descriptor_;
}

const LidarSpecificObjectData& LidarSpecificObjectData::default_instance() {
  if (default_instance_ == NULL) protobuf_AddDesc_osi_5fsensorspecific_2eproto();
  return *default_instance_;
}

LidarSpecificObjectData* LidarSpecificObjectData::default_instance_ = NULL;

LidarSpecificObjectData* LidarSpecificObjectData::New(::google::protobuf::Arena* arena) const {
  LidarSpecificObjectData* n = new LidarSpecificObjectData;
  if (arena != NULL) {
    arena->Own(n);
  }
  return n;
}

void LidarSpecificObjectData::Clear() {
// @@protoc_insertion_point(message_clear_start:osi3.LidarSpecificObjectData)
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
  if (_internal_metadata_.have_unknown_fields()) {
    mutable_unknown_fields()->Clear();
  }
}

bool LidarSpecificObjectData::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!GOOGLE_PREDICT_TRUE(EXPRESSION)) goto failure
  ::google::protobuf::uint32 tag;
  // @@protoc_insertion_point(parse_start:osi3.LidarSpecificObjectData)
  for (;;) {
    ::std::pair< ::google::protobuf::uint32, bool> p = input->ReadTagWithCutoff(127);
    tag = p.first;
    if (!p.second) goto handle_unusual;
  handle_unusual:
    if (tag == 0 ||
        ::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
        ::google::protobuf::internal::WireFormatLite::WIRETYPE_END_GROUP) {
      goto success;
    }
    DO_(::google::protobuf::internal::WireFormat::SkipField(
          input, tag, mutable_unknown_fields()));
  }
success:
  // @@protoc_insertion_point(parse_success:osi3.LidarSpecificObjectData)
  return true;
failure:
  // @@protoc_insertion_point(parse_failure:osi3.LidarSpecificObjectData)
  return false;
#undef DO_
}

void LidarSpecificObjectData::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // @@protoc_insertion_point(serialize_start:osi3.LidarSpecificObjectData)
  if (_internal_metadata_.have_unknown_fields()) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        unknown_fields(), output);
  }
  // @@protoc_insertion_point(serialize_end:osi3.LidarSpecificObjectData)
}

::google::protobuf::uint8* LidarSpecificObjectData::InternalSerializeWithCachedSizesToArray(
    bool deterministic, ::google::protobuf::uint8* target) const {
  // @@protoc_insertion_point(serialize_to_array_start:osi3.LidarSpecificObjectData)
  if (_internal_metadata_.have_unknown_fields()) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        unknown_fields(), target);
  }
  // @@protoc_insertion_point(serialize_to_array_end:osi3.LidarSpecificObjectData)
  return target;
}

int LidarSpecificObjectData::ByteSize() const {
// @@protoc_insertion_point(message_byte_size_start:osi3.LidarSpecificObjectData)
  int total_size = 0;

  if (_internal_metadata_.have_unknown_fields()) {
    total_size +=
      ::google::protobuf::internal::WireFormat::ComputeUnknownFieldsSize(
        unknown_fields());
  }
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = total_size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
  return total_size;
}

void LidarSpecificObjectData::MergeFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:osi3.LidarSpecificObjectData)
  if (GOOGLE_PREDICT_FALSE(&from == this)) {
    ::google::protobuf::internal::MergeFromFail(__FILE__, __LINE__);
  }
  const LidarSpecificObjectData* source = 
      ::google::protobuf::internal::DynamicCastToGenerated<const LidarSpecificObjectData>(
          &from);
  if (source == NULL) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:osi3.LidarSpecificObjectData)
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:osi3.LidarSpecificObjectData)
    MergeFrom(*source);
  }
}

void LidarSpecificObjectData::MergeFrom(const LidarSpecificObjectData& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:osi3.LidarSpecificObjectData)
  if (GOOGLE_PREDICT_FALSE(&from == this)) {
    ::google::protobuf::internal::MergeFromFail(__FILE__, __LINE__);
  }
  if (from._internal_metadata_.have_unknown_fields()) {
    mutable_unknown_fields()->MergeFrom(from.unknown_fields());
  }
}

void LidarSpecificObjectData::CopyFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:osi3.LidarSpecificObjectData)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void LidarSpecificObjectData::CopyFrom(const LidarSpecificObjectData& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:osi3.LidarSpecificObjectData)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool LidarSpecificObjectData::IsInitialized() const {

  return true;
}

void LidarSpecificObjectData::Swap(LidarSpecificObjectData* other) {
  if (other == this) return;
  InternalSwap(other);
}
void LidarSpecificObjectData::InternalSwap(LidarSpecificObjectData* other) {
  _internal_metadata_.Swap(&other->_internal_metadata_);
  std::swap(_cached_size_, other->_cached_size_);
}

::google::protobuf::Metadata LidarSpecificObjectData::GetMetadata() const {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::Metadata metadata;
  metadata.descriptor = LidarSpecificObjectData_descriptor_;
  metadata.reflection = LidarSpecificObjectData_reflection_;
  return metadata;
}

#if PROTOBUF_INLINE_NOT_IN_HEADERS
// LidarSpecificObjectData

#endif  // PROTOBUF_INLINE_NOT_IN_HEADERS

// ===================================================================

#if !defined(_MSC_VER) || _MSC_VER >= 1900
#endif  // !defined(_MSC_VER) || _MSC_VER >= 1900

CameraSpecificObjectData::CameraSpecificObjectData()
  : ::google::protobuf::Message(), _internal_metadata_(NULL) {
  SharedCtor();
  // @@protoc_insertion_point(constructor:osi3.CameraSpecificObjectData)
}

void CameraSpecificObjectData::InitAsDefaultInstance() {
}

CameraSpecificObjectData::CameraSpecificObjectData(const CameraSpecificObjectData& from)
  : ::google::protobuf::Message(),
    _internal_metadata_(NULL) {
  SharedCtor();
  MergeFrom(from);
  // @@protoc_insertion_point(copy_constructor:osi3.CameraSpecificObjectData)
}

void CameraSpecificObjectData::SharedCtor() {
  _cached_size_ = 0;
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
}

CameraSpecificObjectData::~CameraSpecificObjectData() {
  // @@protoc_insertion_point(destructor:osi3.CameraSpecificObjectData)
  SharedDtor();
}

void CameraSpecificObjectData::SharedDtor() {
  if (this != default_instance_) {
  }
}

void CameraSpecificObjectData::SetCachedSize(int size) const {
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
}
const ::google::protobuf::Descriptor* CameraSpecificObjectData::descriptor() {
  protobuf_AssignDescriptorsOnce();
  return CameraSpecificObjectData_descriptor_;
}

const CameraSpecificObjectData& CameraSpecificObjectData::default_instance() {
  if (default_instance_ == NULL) protobuf_AddDesc_osi_5fsensorspecific_2eproto();
  return *default_instance_;
}

CameraSpecificObjectData* CameraSpecificObjectData::default_instance_ = NULL;

CameraSpecificObjectData* CameraSpecificObjectData::New(::google::protobuf::Arena* arena) const {
  CameraSpecificObjectData* n = new CameraSpecificObjectData;
  if (arena != NULL) {
    arena->Own(n);
  }
  return n;
}

void CameraSpecificObjectData::Clear() {
// @@protoc_insertion_point(message_clear_start:osi3.CameraSpecificObjectData)
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
  if (_internal_metadata_.have_unknown_fields()) {
    mutable_unknown_fields()->Clear();
  }
}

bool CameraSpecificObjectData::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!GOOGLE_PREDICT_TRUE(EXPRESSION)) goto failure
  ::google::protobuf::uint32 tag;
  // @@protoc_insertion_point(parse_start:osi3.CameraSpecificObjectData)
  for (;;) {
    ::std::pair< ::google::protobuf::uint32, bool> p = input->ReadTagWithCutoff(127);
    tag = p.first;
    if (!p.second) goto handle_unusual;
  handle_unusual:
    if (tag == 0 ||
        ::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
        ::google::protobuf::internal::WireFormatLite::WIRETYPE_END_GROUP) {
      goto success;
    }
    DO_(::google::protobuf::internal::WireFormat::SkipField(
          input, tag, mutable_unknown_fields()));
  }
success:
  // @@protoc_insertion_point(parse_success:osi3.CameraSpecificObjectData)
  return true;
failure:
  // @@protoc_insertion_point(parse_failure:osi3.CameraSpecificObjectData)
  return false;
#undef DO_
}

void CameraSpecificObjectData::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // @@protoc_insertion_point(serialize_start:osi3.CameraSpecificObjectData)
  if (_internal_metadata_.have_unknown_fields()) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        unknown_fields(), output);
  }
  // @@protoc_insertion_point(serialize_end:osi3.CameraSpecificObjectData)
}

::google::protobuf::uint8* CameraSpecificObjectData::InternalSerializeWithCachedSizesToArray(
    bool deterministic, ::google::protobuf::uint8* target) const {
  // @@protoc_insertion_point(serialize_to_array_start:osi3.CameraSpecificObjectData)
  if (_internal_metadata_.have_unknown_fields()) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        unknown_fields(), target);
  }
  // @@protoc_insertion_point(serialize_to_array_end:osi3.CameraSpecificObjectData)
  return target;
}

int CameraSpecificObjectData::ByteSize() const {
// @@protoc_insertion_point(message_byte_size_start:osi3.CameraSpecificObjectData)
  int total_size = 0;

  if (_internal_metadata_.have_unknown_fields()) {
    total_size +=
      ::google::protobuf::internal::WireFormat::ComputeUnknownFieldsSize(
        unknown_fields());
  }
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = total_size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
  return total_size;
}

void CameraSpecificObjectData::MergeFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:osi3.CameraSpecificObjectData)
  if (GOOGLE_PREDICT_FALSE(&from == this)) {
    ::google::protobuf::internal::MergeFromFail(__FILE__, __LINE__);
  }
  const CameraSpecificObjectData* source = 
      ::google::protobuf::internal::DynamicCastToGenerated<const CameraSpecificObjectData>(
          &from);
  if (source == NULL) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:osi3.CameraSpecificObjectData)
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:osi3.CameraSpecificObjectData)
    MergeFrom(*source);
  }
}

void CameraSpecificObjectData::MergeFrom(const CameraSpecificObjectData& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:osi3.CameraSpecificObjectData)
  if (GOOGLE_PREDICT_FALSE(&from == this)) {
    ::google::protobuf::internal::MergeFromFail(__FILE__, __LINE__);
  }
  if (from._internal_metadata_.have_unknown_fields()) {
    mutable_unknown_fields()->MergeFrom(from.unknown_fields());
  }
}

void CameraSpecificObjectData::CopyFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:osi3.CameraSpecificObjectData)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void CameraSpecificObjectData::CopyFrom(const CameraSpecificObjectData& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:osi3.CameraSpecificObjectData)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool CameraSpecificObjectData::IsInitialized() const {

  return true;
}

void CameraSpecificObjectData::Swap(CameraSpecificObjectData* other) {
  if (other == this) return;
  InternalSwap(other);
}
void CameraSpecificObjectData::InternalSwap(CameraSpecificObjectData* other) {
  _internal_metadata_.Swap(&other->_internal_metadata_);
  std::swap(_cached_size_, other->_cached_size_);
}

::google::protobuf::Metadata CameraSpecificObjectData::GetMetadata() const {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::Metadata metadata;
  metadata.descriptor = CameraSpecificObjectData_descriptor_;
  metadata.reflection = CameraSpecificObjectData_reflection_;
  return metadata;
}

#if PROTOBUF_INLINE_NOT_IN_HEADERS
// CameraSpecificObjectData

#endif  // PROTOBUF_INLINE_NOT_IN_HEADERS

// ===================================================================

#if !defined(_MSC_VER) || _MSC_VER >= 1900
#endif  // !defined(_MSC_VER) || _MSC_VER >= 1900

UltrasonicSpecificObjectData::UltrasonicSpecificObjectData()
  : ::google::protobuf::Message(), _internal_metadata_(NULL) {
  SharedCtor();
  // @@protoc_insertion_point(constructor:osi3.UltrasonicSpecificObjectData)
}

void UltrasonicSpecificObjectData::InitAsDefaultInstance() {
}

UltrasonicSpecificObjectData::UltrasonicSpecificObjectData(const UltrasonicSpecificObjectData& from)
  : ::google::protobuf::Message(),
    _internal_metadata_(NULL) {
  SharedCtor();
  MergeFrom(from);
  // @@protoc_insertion_point(copy_constructor:osi3.UltrasonicSpecificObjectData)
}

void UltrasonicSpecificObjectData::SharedCtor() {
  _cached_size_ = 0;
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
}

UltrasonicSpecificObjectData::~UltrasonicSpecificObjectData() {
  // @@protoc_insertion_point(destructor:osi3.UltrasonicSpecificObjectData)
  SharedDtor();
}

void UltrasonicSpecificObjectData::SharedDtor() {
  if (this != default_instance_) {
  }
}

void UltrasonicSpecificObjectData::SetCachedSize(int size) const {
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
}
const ::google::protobuf::Descriptor* UltrasonicSpecificObjectData::descriptor() {
  protobuf_AssignDescriptorsOnce();
  return UltrasonicSpecificObjectData_descriptor_;
}

const UltrasonicSpecificObjectData& UltrasonicSpecificObjectData::default_instance() {
  if (default_instance_ == NULL) protobuf_AddDesc_osi_5fsensorspecific_2eproto();
  return *default_instance_;
}

UltrasonicSpecificObjectData* UltrasonicSpecificObjectData::default_instance_ = NULL;

UltrasonicSpecificObjectData* UltrasonicSpecificObjectData::New(::google::protobuf::Arena* arena) const {
  UltrasonicSpecificObjectData* n = new UltrasonicSpecificObjectData;
  if (arena != NULL) {
    arena->Own(n);
  }
  return n;
}

void UltrasonicSpecificObjectData::Clear() {
// @@protoc_insertion_point(message_clear_start:osi3.UltrasonicSpecificObjectData)
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
  if (_internal_metadata_.have_unknown_fields()) {
    mutable_unknown_fields()->Clear();
  }
}

bool UltrasonicSpecificObjectData::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!GOOGLE_PREDICT_TRUE(EXPRESSION)) goto failure
  ::google::protobuf::uint32 tag;
  // @@protoc_insertion_point(parse_start:osi3.UltrasonicSpecificObjectData)
  for (;;) {
    ::std::pair< ::google::protobuf::uint32, bool> p = input->ReadTagWithCutoff(127);
    tag = p.first;
    if (!p.second) goto handle_unusual;
  handle_unusual:
    if (tag == 0 ||
        ::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
        ::google::protobuf::internal::WireFormatLite::WIRETYPE_END_GROUP) {
      goto success;
    }
    DO_(::google::protobuf::internal::WireFormat::SkipField(
          input, tag, mutable_unknown_fields()));
  }
success:
  // @@protoc_insertion_point(parse_success:osi3.UltrasonicSpecificObjectData)
  return true;
failure:
  // @@protoc_insertion_point(parse_failure:osi3.UltrasonicSpecificObjectData)
  return false;
#undef DO_
}

void UltrasonicSpecificObjectData::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // @@protoc_insertion_point(serialize_start:osi3.UltrasonicSpecificObjectData)
  if (_internal_metadata_.have_unknown_fields()) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        unknown_fields(), output);
  }
  // @@protoc_insertion_point(serialize_end:osi3.UltrasonicSpecificObjectData)
}

::google::protobuf::uint8* UltrasonicSpecificObjectData::InternalSerializeWithCachedSizesToArray(
    bool deterministic, ::google::protobuf::uint8* target) const {
  // @@protoc_insertion_point(serialize_to_array_start:osi3.UltrasonicSpecificObjectData)
  if (_internal_metadata_.have_unknown_fields()) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        unknown_fields(), target);
  }
  // @@protoc_insertion_point(serialize_to_array_end:osi3.UltrasonicSpecificObjectData)
  return target;
}

int UltrasonicSpecificObjectData::ByteSize() const {
// @@protoc_insertion_point(message_byte_size_start:osi3.UltrasonicSpecificObjectData)
  int total_size = 0;

  if (_internal_metadata_.have_unknown_fields()) {
    total_size +=
      ::google::protobuf::internal::WireFormat::ComputeUnknownFieldsSize(
        unknown_fields());
  }
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = total_size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
  return total_size;
}

void UltrasonicSpecificObjectData::MergeFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:osi3.UltrasonicSpecificObjectData)
  if (GOOGLE_PREDICT_FALSE(&from == this)) {
    ::google::protobuf::internal::MergeFromFail(__FILE__, __LINE__);
  }
  const UltrasonicSpecificObjectData* source = 
      ::google::protobuf::internal::DynamicCastToGenerated<const UltrasonicSpecificObjectData>(
          &from);
  if (source == NULL) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:osi3.UltrasonicSpecificObjectData)
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:osi3.UltrasonicSpecificObjectData)
    MergeFrom(*source);
  }
}

void UltrasonicSpecificObjectData::MergeFrom(const UltrasonicSpecificObjectData& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:osi3.UltrasonicSpecificObjectData)
  if (GOOGLE_PREDICT_FALSE(&from == this)) {
    ::google::protobuf::internal::MergeFromFail(__FILE__, __LINE__);
  }
  if (from._internal_metadata_.have_unknown_fields()) {
    mutable_unknown_fields()->MergeFrom(from.unknown_fields());
  }
}

void UltrasonicSpecificObjectData::CopyFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:osi3.UltrasonicSpecificObjectData)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void UltrasonicSpecificObjectData::CopyFrom(const UltrasonicSpecificObjectData& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:osi3.UltrasonicSpecificObjectData)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool UltrasonicSpecificObjectData::IsInitialized() const {

  return true;
}

void UltrasonicSpecificObjectData::Swap(UltrasonicSpecificObjectData* other) {
  if (other == this) return;
  InternalSwap(other);
}
void UltrasonicSpecificObjectData::InternalSwap(UltrasonicSpecificObjectData* other) {
  _internal_metadata_.Swap(&other->_internal_metadata_);
  std::swap(_cached_size_, other->_cached_size_);
}

::google::protobuf::Metadata UltrasonicSpecificObjectData::GetMetadata() const {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::Metadata metadata;
  metadata.descriptor = UltrasonicSpecificObjectData_descriptor_;
  metadata.reflection = UltrasonicSpecificObjectData_reflection_;
  return metadata;
}

#if PROTOBUF_INLINE_NOT_IN_HEADERS
// UltrasonicSpecificObjectData

#endif  // PROTOBUF_INLINE_NOT_IN_HEADERS

// @@protoc_insertion_point(namespace_scope)

}  // namespace osi3

// @@protoc_insertion_point(global_scope)