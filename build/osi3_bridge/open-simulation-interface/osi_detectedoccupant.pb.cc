// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: osi_detectedoccupant.proto

#define INTERNAL_SUPPRESS_PROTOBUF_FIELD_DEPRECATION
#include "osi_detectedoccupant.pb.h"

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

const ::google::protobuf::Descriptor* DetectedOccupant_descriptor_ = NULL;
const ::google::protobuf::internal::GeneratedMessageReflection*
  DetectedOccupant_reflection_ = NULL;
const ::google::protobuf::Descriptor* DetectedOccupant_CandidateOccupant_descriptor_ = NULL;
const ::google::protobuf::internal::GeneratedMessageReflection*
  DetectedOccupant_CandidateOccupant_reflection_ = NULL;

}  // namespace


void protobuf_AssignDesc_osi_5fdetectedoccupant_2eproto() GOOGLE_ATTRIBUTE_COLD;
void protobuf_AssignDesc_osi_5fdetectedoccupant_2eproto() {
  protobuf_AddDesc_osi_5fdetectedoccupant_2eproto();
  const ::google::protobuf::FileDescriptor* file =
    ::google::protobuf::DescriptorPool::generated_pool()->FindFileByName(
      "osi_detectedoccupant.proto");
  GOOGLE_CHECK(file != NULL);
  DetectedOccupant_descriptor_ = file->message_type(0);
  static const int DetectedOccupant_offsets_[2] = {
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(DetectedOccupant, header_),
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(DetectedOccupant, candidate_),
  };
  DetectedOccupant_reflection_ =
    ::google::protobuf::internal::GeneratedMessageReflection::NewGeneratedMessageReflection(
      DetectedOccupant_descriptor_,
      DetectedOccupant::default_instance_,
      DetectedOccupant_offsets_,
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(DetectedOccupant, _has_bits_[0]),
      -1,
      -1,
      sizeof(DetectedOccupant),
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(DetectedOccupant, _internal_metadata_),
      -1);
  DetectedOccupant_CandidateOccupant_descriptor_ = DetectedOccupant_descriptor_->nested_type(0);
  static const int DetectedOccupant_CandidateOccupant_offsets_[2] = {
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(DetectedOccupant_CandidateOccupant, probability_),
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(DetectedOccupant_CandidateOccupant, classification_),
  };
  DetectedOccupant_CandidateOccupant_reflection_ =
    ::google::protobuf::internal::GeneratedMessageReflection::NewGeneratedMessageReflection(
      DetectedOccupant_CandidateOccupant_descriptor_,
      DetectedOccupant_CandidateOccupant::default_instance_,
      DetectedOccupant_CandidateOccupant_offsets_,
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(DetectedOccupant_CandidateOccupant, _has_bits_[0]),
      -1,
      -1,
      sizeof(DetectedOccupant_CandidateOccupant),
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(DetectedOccupant_CandidateOccupant, _internal_metadata_),
      -1);
}

namespace {

GOOGLE_PROTOBUF_DECLARE_ONCE(protobuf_AssignDescriptors_once_);
inline void protobuf_AssignDescriptorsOnce() {
  ::google::protobuf::GoogleOnceInit(&protobuf_AssignDescriptors_once_,
                 &protobuf_AssignDesc_osi_5fdetectedoccupant_2eproto);
}

void protobuf_RegisterTypes(const ::std::string&) GOOGLE_ATTRIBUTE_COLD;
void protobuf_RegisterTypes(const ::std::string&) {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedMessage(
      DetectedOccupant_descriptor_, &DetectedOccupant::default_instance());
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedMessage(
      DetectedOccupant_CandidateOccupant_descriptor_, &DetectedOccupant_CandidateOccupant::default_instance());
}

}  // namespace

void protobuf_ShutdownFile_osi_5fdetectedoccupant_2eproto() {
  delete DetectedOccupant::default_instance_;
  delete DetectedOccupant_reflection_;
  delete DetectedOccupant_CandidateOccupant::default_instance_;
  delete DetectedOccupant_CandidateOccupant_reflection_;
}

void protobuf_AddDesc_osi_5fdetectedoccupant_2eproto() GOOGLE_ATTRIBUTE_COLD;
void protobuf_AddDesc_osi_5fdetectedoccupant_2eproto() {
  static bool already_here = false;
  if (already_here) return;
  already_here = true;
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  ::osi3::protobuf_AddDesc_osi_5foccupant_2eproto();
  ::osi3::protobuf_AddDesc_osi_5fdetectedobject_2eproto();
  ::google::protobuf::DescriptorPool::InternalAddGeneratedFile(
    "\n\032osi_detectedoccupant.proto\022\004osi3\032\022osi_"
    "occupant.proto\032\030osi_detectedobject.proto"
    "\"\332\001\n\020DetectedOccupant\022(\n\006header\030\001 \001(\0132\030."
    "osi3.DetectedItemHeader\022;\n\tcandidate\030\002 \003"
    "(\0132(.osi3.DetectedOccupant.CandidateOccu"
    "pant\032_\n\021CandidateOccupant\022\023\n\013probability"
    "\030\001 \001(\001\0225\n\016classification\030\002 \001(\0132\035.osi3.Oc"
    "cupant.ClassificationB\002H\001", 305);
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedFile(
    "osi_detectedoccupant.proto", &protobuf_RegisterTypes);
  DetectedOccupant::default_instance_ = new DetectedOccupant();
  DetectedOccupant_CandidateOccupant::default_instance_ = new DetectedOccupant_CandidateOccupant();
  DetectedOccupant::default_instance_->InitAsDefaultInstance();
  DetectedOccupant_CandidateOccupant::default_instance_->InitAsDefaultInstance();
  ::google::protobuf::internal::OnShutdown(&protobuf_ShutdownFile_osi_5fdetectedoccupant_2eproto);
}

// Force AddDescriptors() to be called at static initialization time.
struct StaticDescriptorInitializer_osi_5fdetectedoccupant_2eproto {
  StaticDescriptorInitializer_osi_5fdetectedoccupant_2eproto() {
    protobuf_AddDesc_osi_5fdetectedoccupant_2eproto();
  }
} static_descriptor_initializer_osi_5fdetectedoccupant_2eproto_;

// ===================================================================

#if !defined(_MSC_VER) || _MSC_VER >= 1900
const int DetectedOccupant_CandidateOccupant::kProbabilityFieldNumber;
const int DetectedOccupant_CandidateOccupant::kClassificationFieldNumber;
#endif  // !defined(_MSC_VER) || _MSC_VER >= 1900

DetectedOccupant_CandidateOccupant::DetectedOccupant_CandidateOccupant()
  : ::google::protobuf::Message(), _internal_metadata_(NULL) {
  SharedCtor();
  // @@protoc_insertion_point(constructor:osi3.DetectedOccupant.CandidateOccupant)
}

void DetectedOccupant_CandidateOccupant::InitAsDefaultInstance() {
  classification_ = const_cast< ::osi3::Occupant_Classification*>(&::osi3::Occupant_Classification::default_instance());
}

DetectedOccupant_CandidateOccupant::DetectedOccupant_CandidateOccupant(const DetectedOccupant_CandidateOccupant& from)
  : ::google::protobuf::Message(),
    _internal_metadata_(NULL) {
  SharedCtor();
  MergeFrom(from);
  // @@protoc_insertion_point(copy_constructor:osi3.DetectedOccupant.CandidateOccupant)
}

void DetectedOccupant_CandidateOccupant::SharedCtor() {
  _cached_size_ = 0;
  probability_ = 0;
  classification_ = NULL;
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
}

DetectedOccupant_CandidateOccupant::~DetectedOccupant_CandidateOccupant() {
  // @@protoc_insertion_point(destructor:osi3.DetectedOccupant.CandidateOccupant)
  SharedDtor();
}

void DetectedOccupant_CandidateOccupant::SharedDtor() {
  if (this != default_instance_) {
    delete classification_;
  }
}

void DetectedOccupant_CandidateOccupant::SetCachedSize(int size) const {
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
}
const ::google::protobuf::Descriptor* DetectedOccupant_CandidateOccupant::descriptor() {
  protobuf_AssignDescriptorsOnce();
  return DetectedOccupant_CandidateOccupant_descriptor_;
}

const DetectedOccupant_CandidateOccupant& DetectedOccupant_CandidateOccupant::default_instance() {
  if (default_instance_ == NULL) protobuf_AddDesc_osi_5fdetectedoccupant_2eproto();
  return *default_instance_;
}

DetectedOccupant_CandidateOccupant* DetectedOccupant_CandidateOccupant::default_instance_ = NULL;

DetectedOccupant_CandidateOccupant* DetectedOccupant_CandidateOccupant::New(::google::protobuf::Arena* arena) const {
  DetectedOccupant_CandidateOccupant* n = new DetectedOccupant_CandidateOccupant;
  if (arena != NULL) {
    arena->Own(n);
  }
  return n;
}

void DetectedOccupant_CandidateOccupant::Clear() {
// @@protoc_insertion_point(message_clear_start:osi3.DetectedOccupant.CandidateOccupant)
  if (_has_bits_[0 / 32] & 3u) {
    probability_ = 0;
    if (has_classification()) {
      if (classification_ != NULL) classification_->::osi3::Occupant_Classification::Clear();
    }
  }
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
  if (_internal_metadata_.have_unknown_fields()) {
    mutable_unknown_fields()->Clear();
  }
}

bool DetectedOccupant_CandidateOccupant::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!GOOGLE_PREDICT_TRUE(EXPRESSION)) goto failure
  ::google::protobuf::uint32 tag;
  // @@protoc_insertion_point(parse_start:osi3.DetectedOccupant.CandidateOccupant)
  for (;;) {
    ::std::pair< ::google::protobuf::uint32, bool> p = input->ReadTagWithCutoff(127);
    tag = p.first;
    if (!p.second) goto handle_unusual;
    switch (::google::protobuf::internal::WireFormatLite::GetTagFieldNumber(tag)) {
      // optional double probability = 1;
      case 1: {
        if (tag == 9) {
          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   double, ::google::protobuf::internal::WireFormatLite::TYPE_DOUBLE>(
                 input, &probability_)));
          set_has_probability();
        } else {
          goto handle_unusual;
        }
        if (input->ExpectTag(18)) goto parse_classification;
        break;
      }

      // optional .osi3.Occupant.Classification classification = 2;
      case 2: {
        if (tag == 18) {
         parse_classification:
          DO_(::google::protobuf::internal::WireFormatLite::ReadMessageNoVirtual(
               input, mutable_classification()));
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
  // @@protoc_insertion_point(parse_success:osi3.DetectedOccupant.CandidateOccupant)
  return true;
failure:
  // @@protoc_insertion_point(parse_failure:osi3.DetectedOccupant.CandidateOccupant)
  return false;
#undef DO_
}

void DetectedOccupant_CandidateOccupant::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // @@protoc_insertion_point(serialize_start:osi3.DetectedOccupant.CandidateOccupant)
  // optional double probability = 1;
  if (has_probability()) {
    ::google::protobuf::internal::WireFormatLite::WriteDouble(1, this->probability(), output);
  }

  // optional .osi3.Occupant.Classification classification = 2;
  if (has_classification()) {
    ::google::protobuf::internal::WireFormatLite::WriteMessageMaybeToArray(
      2, *this->classification_, output);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        unknown_fields(), output);
  }
  // @@protoc_insertion_point(serialize_end:osi3.DetectedOccupant.CandidateOccupant)
}

::google::protobuf::uint8* DetectedOccupant_CandidateOccupant::InternalSerializeWithCachedSizesToArray(
    bool deterministic, ::google::protobuf::uint8* target) const {
  // @@protoc_insertion_point(serialize_to_array_start:osi3.DetectedOccupant.CandidateOccupant)
  // optional double probability = 1;
  if (has_probability()) {
    target = ::google::protobuf::internal::WireFormatLite::WriteDoubleToArray(1, this->probability(), target);
  }

  // optional .osi3.Occupant.Classification classification = 2;
  if (has_classification()) {
    target = ::google::protobuf::internal::WireFormatLite::
      InternalWriteMessageNoVirtualToArray(
        2, *this->classification_, false, target);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        unknown_fields(), target);
  }
  // @@protoc_insertion_point(serialize_to_array_end:osi3.DetectedOccupant.CandidateOccupant)
  return target;
}

int DetectedOccupant_CandidateOccupant::ByteSize() const {
// @@protoc_insertion_point(message_byte_size_start:osi3.DetectedOccupant.CandidateOccupant)
  int total_size = 0;

  if (_has_bits_[0 / 32] & 3u) {
    // optional double probability = 1;
    if (has_probability()) {
      total_size += 1 + 8;
    }

    // optional .osi3.Occupant.Classification classification = 2;
    if (has_classification()) {
      total_size += 1 +
        ::google::protobuf::internal::WireFormatLite::MessageSizeNoVirtual(
          *this->classification_);
    }

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

void DetectedOccupant_CandidateOccupant::MergeFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:osi3.DetectedOccupant.CandidateOccupant)
  if (GOOGLE_PREDICT_FALSE(&from == this)) {
    ::google::protobuf::internal::MergeFromFail(__FILE__, __LINE__);
  }
  const DetectedOccupant_CandidateOccupant* source = 
      ::google::protobuf::internal::DynamicCastToGenerated<const DetectedOccupant_CandidateOccupant>(
          &from);
  if (source == NULL) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:osi3.DetectedOccupant.CandidateOccupant)
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:osi3.DetectedOccupant.CandidateOccupant)
    MergeFrom(*source);
  }
}

void DetectedOccupant_CandidateOccupant::MergeFrom(const DetectedOccupant_CandidateOccupant& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:osi3.DetectedOccupant.CandidateOccupant)
  if (GOOGLE_PREDICT_FALSE(&from == this)) {
    ::google::protobuf::internal::MergeFromFail(__FILE__, __LINE__);
  }
  if (from._has_bits_[0 / 32] & (0xffu << (0 % 32))) {
    if (from.has_probability()) {
      set_probability(from.probability());
    }
    if (from.has_classification()) {
      mutable_classification()->::osi3::Occupant_Classification::MergeFrom(from.classification());
    }
  }
  if (from._internal_metadata_.have_unknown_fields()) {
    mutable_unknown_fields()->MergeFrom(from.unknown_fields());
  }
}

void DetectedOccupant_CandidateOccupant::CopyFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:osi3.DetectedOccupant.CandidateOccupant)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void DetectedOccupant_CandidateOccupant::CopyFrom(const DetectedOccupant_CandidateOccupant& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:osi3.DetectedOccupant.CandidateOccupant)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool DetectedOccupant_CandidateOccupant::IsInitialized() const {

  return true;
}

void DetectedOccupant_CandidateOccupant::Swap(DetectedOccupant_CandidateOccupant* other) {
  if (other == this) return;
  InternalSwap(other);
}
void DetectedOccupant_CandidateOccupant::InternalSwap(DetectedOccupant_CandidateOccupant* other) {
  std::swap(probability_, other->probability_);
  std::swap(classification_, other->classification_);
  std::swap(_has_bits_[0], other->_has_bits_[0]);
  _internal_metadata_.Swap(&other->_internal_metadata_);
  std::swap(_cached_size_, other->_cached_size_);
}

::google::protobuf::Metadata DetectedOccupant_CandidateOccupant::GetMetadata() const {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::Metadata metadata;
  metadata.descriptor = DetectedOccupant_CandidateOccupant_descriptor_;
  metadata.reflection = DetectedOccupant_CandidateOccupant_reflection_;
  return metadata;
}


// -------------------------------------------------------------------

#if !defined(_MSC_VER) || _MSC_VER >= 1900
const int DetectedOccupant::kHeaderFieldNumber;
const int DetectedOccupant::kCandidateFieldNumber;
#endif  // !defined(_MSC_VER) || _MSC_VER >= 1900

DetectedOccupant::DetectedOccupant()
  : ::google::protobuf::Message(), _internal_metadata_(NULL) {
  SharedCtor();
  // @@protoc_insertion_point(constructor:osi3.DetectedOccupant)
}

void DetectedOccupant::InitAsDefaultInstance() {
  header_ = const_cast< ::osi3::DetectedItemHeader*>(&::osi3::DetectedItemHeader::default_instance());
}

DetectedOccupant::DetectedOccupant(const DetectedOccupant& from)
  : ::google::protobuf::Message(),
    _internal_metadata_(NULL) {
  SharedCtor();
  MergeFrom(from);
  // @@protoc_insertion_point(copy_constructor:osi3.DetectedOccupant)
}

void DetectedOccupant::SharedCtor() {
  _cached_size_ = 0;
  header_ = NULL;
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
}

DetectedOccupant::~DetectedOccupant() {
  // @@protoc_insertion_point(destructor:osi3.DetectedOccupant)
  SharedDtor();
}

void DetectedOccupant::SharedDtor() {
  if (this != default_instance_) {
    delete header_;
  }
}

void DetectedOccupant::SetCachedSize(int size) const {
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
}
const ::google::protobuf::Descriptor* DetectedOccupant::descriptor() {
  protobuf_AssignDescriptorsOnce();
  return DetectedOccupant_descriptor_;
}

const DetectedOccupant& DetectedOccupant::default_instance() {
  if (default_instance_ == NULL) protobuf_AddDesc_osi_5fdetectedoccupant_2eproto();
  return *default_instance_;
}

DetectedOccupant* DetectedOccupant::default_instance_ = NULL;

DetectedOccupant* DetectedOccupant::New(::google::protobuf::Arena* arena) const {
  DetectedOccupant* n = new DetectedOccupant;
  if (arena != NULL) {
    arena->Own(n);
  }
  return n;
}

void DetectedOccupant::Clear() {
// @@protoc_insertion_point(message_clear_start:osi3.DetectedOccupant)
  if (has_header()) {
    if (header_ != NULL) header_->::osi3::DetectedItemHeader::Clear();
  }
  candidate_.Clear();
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
  if (_internal_metadata_.have_unknown_fields()) {
    mutable_unknown_fields()->Clear();
  }
}

bool DetectedOccupant::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!GOOGLE_PREDICT_TRUE(EXPRESSION)) goto failure
  ::google::protobuf::uint32 tag;
  // @@protoc_insertion_point(parse_start:osi3.DetectedOccupant)
  for (;;) {
    ::std::pair< ::google::protobuf::uint32, bool> p = input->ReadTagWithCutoff(127);
    tag = p.first;
    if (!p.second) goto handle_unusual;
    switch (::google::protobuf::internal::WireFormatLite::GetTagFieldNumber(tag)) {
      // optional .osi3.DetectedItemHeader header = 1;
      case 1: {
        if (tag == 10) {
          DO_(::google::protobuf::internal::WireFormatLite::ReadMessageNoVirtual(
               input, mutable_header()));
        } else {
          goto handle_unusual;
        }
        if (input->ExpectTag(18)) goto parse_candidate;
        break;
      }

      // repeated .osi3.DetectedOccupant.CandidateOccupant candidate = 2;
      case 2: {
        if (tag == 18) {
         parse_candidate:
          DO_(input->IncrementRecursionDepth());
         parse_loop_candidate:
          DO_(::google::protobuf::internal::WireFormatLite::ReadMessageNoVirtualNoRecursionDepth(
                input, add_candidate()));
        } else {
          goto handle_unusual;
        }
        if (input->ExpectTag(18)) goto parse_loop_candidate;
        input->UnsafeDecrementRecursionDepth();
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
  // @@protoc_insertion_point(parse_success:osi3.DetectedOccupant)
  return true;
failure:
  // @@protoc_insertion_point(parse_failure:osi3.DetectedOccupant)
  return false;
#undef DO_
}

void DetectedOccupant::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // @@protoc_insertion_point(serialize_start:osi3.DetectedOccupant)
  // optional .osi3.DetectedItemHeader header = 1;
  if (has_header()) {
    ::google::protobuf::internal::WireFormatLite::WriteMessageMaybeToArray(
      1, *this->header_, output);
  }

  // repeated .osi3.DetectedOccupant.CandidateOccupant candidate = 2;
  for (unsigned int i = 0, n = this->candidate_size(); i < n; i++) {
    ::google::protobuf::internal::WireFormatLite::WriteMessageMaybeToArray(
      2, this->candidate(i), output);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        unknown_fields(), output);
  }
  // @@protoc_insertion_point(serialize_end:osi3.DetectedOccupant)
}

::google::protobuf::uint8* DetectedOccupant::InternalSerializeWithCachedSizesToArray(
    bool deterministic, ::google::protobuf::uint8* target) const {
  // @@protoc_insertion_point(serialize_to_array_start:osi3.DetectedOccupant)
  // optional .osi3.DetectedItemHeader header = 1;
  if (has_header()) {
    target = ::google::protobuf::internal::WireFormatLite::
      InternalWriteMessageNoVirtualToArray(
        1, *this->header_, false, target);
  }

  // repeated .osi3.DetectedOccupant.CandidateOccupant candidate = 2;
  for (unsigned int i = 0, n = this->candidate_size(); i < n; i++) {
    target = ::google::protobuf::internal::WireFormatLite::
      InternalWriteMessageNoVirtualToArray(
        2, this->candidate(i), false, target);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        unknown_fields(), target);
  }
  // @@protoc_insertion_point(serialize_to_array_end:osi3.DetectedOccupant)
  return target;
}

int DetectedOccupant::ByteSize() const {
// @@protoc_insertion_point(message_byte_size_start:osi3.DetectedOccupant)
  int total_size = 0;

  // optional .osi3.DetectedItemHeader header = 1;
  if (has_header()) {
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::MessageSizeNoVirtual(
        *this->header_);
  }

  // repeated .osi3.DetectedOccupant.CandidateOccupant candidate = 2;
  total_size += 1 * this->candidate_size();
  for (int i = 0; i < this->candidate_size(); i++) {
    total_size +=
      ::google::protobuf::internal::WireFormatLite::MessageSizeNoVirtual(
        this->candidate(i));
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

void DetectedOccupant::MergeFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:osi3.DetectedOccupant)
  if (GOOGLE_PREDICT_FALSE(&from == this)) {
    ::google::protobuf::internal::MergeFromFail(__FILE__, __LINE__);
  }
  const DetectedOccupant* source = 
      ::google::protobuf::internal::DynamicCastToGenerated<const DetectedOccupant>(
          &from);
  if (source == NULL) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:osi3.DetectedOccupant)
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:osi3.DetectedOccupant)
    MergeFrom(*source);
  }
}

void DetectedOccupant::MergeFrom(const DetectedOccupant& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:osi3.DetectedOccupant)
  if (GOOGLE_PREDICT_FALSE(&from == this)) {
    ::google::protobuf::internal::MergeFromFail(__FILE__, __LINE__);
  }
  candidate_.MergeFrom(from.candidate_);
  if (from._has_bits_[0 / 32] & (0xffu << (0 % 32))) {
    if (from.has_header()) {
      mutable_header()->::osi3::DetectedItemHeader::MergeFrom(from.header());
    }
  }
  if (from._internal_metadata_.have_unknown_fields()) {
    mutable_unknown_fields()->MergeFrom(from.unknown_fields());
  }
}

void DetectedOccupant::CopyFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:osi3.DetectedOccupant)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void DetectedOccupant::CopyFrom(const DetectedOccupant& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:osi3.DetectedOccupant)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool DetectedOccupant::IsInitialized() const {

  return true;
}

void DetectedOccupant::Swap(DetectedOccupant* other) {
  if (other == this) return;
  InternalSwap(other);
}
void DetectedOccupant::InternalSwap(DetectedOccupant* other) {
  std::swap(header_, other->header_);
  candidate_.UnsafeArenaSwap(&other->candidate_);
  std::swap(_has_bits_[0], other->_has_bits_[0]);
  _internal_metadata_.Swap(&other->_internal_metadata_);
  std::swap(_cached_size_, other->_cached_size_);
}

::google::protobuf::Metadata DetectedOccupant::GetMetadata() const {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::Metadata metadata;
  metadata.descriptor = DetectedOccupant_descriptor_;
  metadata.reflection = DetectedOccupant_reflection_;
  return metadata;
}

#if PROTOBUF_INLINE_NOT_IN_HEADERS
// DetectedOccupant_CandidateOccupant

// optional double probability = 1;
bool DetectedOccupant_CandidateOccupant::has_probability() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
void DetectedOccupant_CandidateOccupant::set_has_probability() {
  _has_bits_[0] |= 0x00000001u;
}
void DetectedOccupant_CandidateOccupant::clear_has_probability() {
  _has_bits_[0] &= ~0x00000001u;
}
void DetectedOccupant_CandidateOccupant::clear_probability() {
  probability_ = 0;
  clear_has_probability();
}
 double DetectedOccupant_CandidateOccupant::probability() const {
  // @@protoc_insertion_point(field_get:osi3.DetectedOccupant.CandidateOccupant.probability)
  return probability_;
}
 void DetectedOccupant_CandidateOccupant::set_probability(double value) {
  set_has_probability();
  probability_ = value;
  // @@protoc_insertion_point(field_set:osi3.DetectedOccupant.CandidateOccupant.probability)
}

// optional .osi3.Occupant.Classification classification = 2;
bool DetectedOccupant_CandidateOccupant::has_classification() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
void DetectedOccupant_CandidateOccupant::set_has_classification() {
  _has_bits_[0] |= 0x00000002u;
}
void DetectedOccupant_CandidateOccupant::clear_has_classification() {
  _has_bits_[0] &= ~0x00000002u;
}
void DetectedOccupant_CandidateOccupant::clear_classification() {
  if (classification_ != NULL) classification_->::osi3::Occupant_Classification::Clear();
  clear_has_classification();
}
const ::osi3::Occupant_Classification& DetectedOccupant_CandidateOccupant::classification() const {
  // @@protoc_insertion_point(field_get:osi3.DetectedOccupant.CandidateOccupant.classification)
  return classification_ != NULL ? *classification_ : *default_instance_->classification_;
}
::osi3::Occupant_Classification* DetectedOccupant_CandidateOccupant::mutable_classification() {
  set_has_classification();
  if (classification_ == NULL) {
    classification_ = new ::osi3::Occupant_Classification;
  }
  // @@protoc_insertion_point(field_mutable:osi3.DetectedOccupant.CandidateOccupant.classification)
  return classification_;
}
::osi3::Occupant_Classification* DetectedOccupant_CandidateOccupant::release_classification() {
  // @@protoc_insertion_point(field_release:osi3.DetectedOccupant.CandidateOccupant.classification)
  clear_has_classification();
  ::osi3::Occupant_Classification* temp = classification_;
  classification_ = NULL;
  return temp;
}
void DetectedOccupant_CandidateOccupant::set_allocated_classification(::osi3::Occupant_Classification* classification) {
  delete classification_;
  classification_ = classification;
  if (classification) {
    set_has_classification();
  } else {
    clear_has_classification();
  }
  // @@protoc_insertion_point(field_set_allocated:osi3.DetectedOccupant.CandidateOccupant.classification)
}

// -------------------------------------------------------------------

// DetectedOccupant

// optional .osi3.DetectedItemHeader header = 1;
bool DetectedOccupant::has_header() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
void DetectedOccupant::set_has_header() {
  _has_bits_[0] |= 0x00000001u;
}
void DetectedOccupant::clear_has_header() {
  _has_bits_[0] &= ~0x00000001u;
}
void DetectedOccupant::clear_header() {
  if (header_ != NULL) header_->::osi3::DetectedItemHeader::Clear();
  clear_has_header();
}
const ::osi3::DetectedItemHeader& DetectedOccupant::header() const {
  // @@protoc_insertion_point(field_get:osi3.DetectedOccupant.header)
  return header_ != NULL ? *header_ : *default_instance_->header_;
}
::osi3::DetectedItemHeader* DetectedOccupant::mutable_header() {
  set_has_header();
  if (header_ == NULL) {
    header_ = new ::osi3::DetectedItemHeader;
  }
  // @@protoc_insertion_point(field_mutable:osi3.DetectedOccupant.header)
  return header_;
}
::osi3::DetectedItemHeader* DetectedOccupant::release_header() {
  // @@protoc_insertion_point(field_release:osi3.DetectedOccupant.header)
  clear_has_header();
  ::osi3::DetectedItemHeader* temp = header_;
  header_ = NULL;
  return temp;
}
void DetectedOccupant::set_allocated_header(::osi3::DetectedItemHeader* header) {
  delete header_;
  header_ = header;
  if (header) {
    set_has_header();
  } else {
    clear_has_header();
  }
  // @@protoc_insertion_point(field_set_allocated:osi3.DetectedOccupant.header)
}

// repeated .osi3.DetectedOccupant.CandidateOccupant candidate = 2;
int DetectedOccupant::candidate_size() const {
  return candidate_.size();
}
void DetectedOccupant::clear_candidate() {
  candidate_.Clear();
}
const ::osi3::DetectedOccupant_CandidateOccupant& DetectedOccupant::candidate(int index) const {
  // @@protoc_insertion_point(field_get:osi3.DetectedOccupant.candidate)
  return candidate_.Get(index);
}
::osi3::DetectedOccupant_CandidateOccupant* DetectedOccupant::mutable_candidate(int index) {
  // @@protoc_insertion_point(field_mutable:osi3.DetectedOccupant.candidate)
  return candidate_.Mutable(index);
}
::osi3::DetectedOccupant_CandidateOccupant* DetectedOccupant::add_candidate() {
  // @@protoc_insertion_point(field_add:osi3.DetectedOccupant.candidate)
  return candidate_.Add();
}
::google::protobuf::RepeatedPtrField< ::osi3::DetectedOccupant_CandidateOccupant >*
DetectedOccupant::mutable_candidate() {
  // @@protoc_insertion_point(field_mutable_list:osi3.DetectedOccupant.candidate)
  return &candidate_;
}
const ::google::protobuf::RepeatedPtrField< ::osi3::DetectedOccupant_CandidateOccupant >&
DetectedOccupant::candidate() const {
  // @@protoc_insertion_point(field_list:osi3.DetectedOccupant.candidate)
  return candidate_;
}

#endif  // PROTOBUF_INLINE_NOT_IN_HEADERS

// @@protoc_insertion_point(namespace_scope)

}  // namespace osi3

// @@protoc_insertion_point(global_scope)