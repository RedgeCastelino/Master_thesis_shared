// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: osi_detectedroadmarking.proto

#ifndef PROTOBUF_osi_5fdetectedroadmarking_2eproto__INCLUDED
#define PROTOBUF_osi_5fdetectedroadmarking_2eproto__INCLUDED

#include <string>

#include <google/protobuf/stubs/common.h>

#if GOOGLE_PROTOBUF_VERSION < 3000000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please update
#error your headers.
#endif
#if 3000000 < GOOGLE_PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/metadata.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>
#include <google/protobuf/extension_set.h>
#include <google/protobuf/unknown_field_set.h>
#include "osi_common.pb.h"
#include "osi_roadmarking.pb.h"
#include "osi_detectedobject.pb.h"
// @@protoc_insertion_point(includes)

namespace osi3 {

// Internal implementation detail -- do not call these.
void protobuf_AddDesc_osi_5fdetectedroadmarking_2eproto();
void protobuf_AssignDesc_osi_5fdetectedroadmarking_2eproto();
void protobuf_ShutdownFile_osi_5fdetectedroadmarking_2eproto();

class DetectedRoadMarking;
class DetectedRoadMarking_CandidateRoadMarking;

// ===================================================================

class DetectedRoadMarking_CandidateRoadMarking : public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:osi3.DetectedRoadMarking.CandidateRoadMarking) */ {
 public:
  DetectedRoadMarking_CandidateRoadMarking();
  virtual ~DetectedRoadMarking_CandidateRoadMarking();

  DetectedRoadMarking_CandidateRoadMarking(const DetectedRoadMarking_CandidateRoadMarking& from);

  inline DetectedRoadMarking_CandidateRoadMarking& operator=(const DetectedRoadMarking_CandidateRoadMarking& from) {
    CopyFrom(from);
    return *this;
  }

  inline const ::google::protobuf::UnknownFieldSet& unknown_fields() const {
    return _internal_metadata_.unknown_fields();
  }

  inline ::google::protobuf::UnknownFieldSet* mutable_unknown_fields() {
    return _internal_metadata_.mutable_unknown_fields();
  }

  static const ::google::protobuf::Descriptor* descriptor();
  static const DetectedRoadMarking_CandidateRoadMarking& default_instance();

  void Swap(DetectedRoadMarking_CandidateRoadMarking* other);

  // implements Message ----------------------------------------------

  inline DetectedRoadMarking_CandidateRoadMarking* New() const { return New(NULL); }

  DetectedRoadMarking_CandidateRoadMarking* New(::google::protobuf::Arena* arena) const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const DetectedRoadMarking_CandidateRoadMarking& from);
  void MergeFrom(const DetectedRoadMarking_CandidateRoadMarking& from);
  void Clear();
  bool IsInitialized() const;

  int ByteSize() const;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input);
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      bool deterministic, ::google::protobuf::uint8* output) const;
  ::google::protobuf::uint8* SerializeWithCachedSizesToArray(::google::protobuf::uint8* output) const {
    return InternalSerializeWithCachedSizesToArray(false, output);
  }
  int GetCachedSize() const { return _cached_size_; }
  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const;
  void InternalSwap(DetectedRoadMarking_CandidateRoadMarking* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return _internal_metadata_.arena();
  }
  inline void* MaybeArenaPtr() const {
    return _internal_metadata_.raw_arena_ptr();
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // optional double probability = 1;
  bool has_probability() const;
  void clear_probability();
  static const int kProbabilityFieldNumber = 1;
  double probability() const;
  void set_probability(double value);

  // optional .osi3.RoadMarking.Classification classification = 2;
  bool has_classification() const;
  void clear_classification();
  static const int kClassificationFieldNumber = 2;
  const ::osi3::RoadMarking_Classification& classification() const;
  ::osi3::RoadMarking_Classification* mutable_classification();
  ::osi3::RoadMarking_Classification* release_classification();
  void set_allocated_classification(::osi3::RoadMarking_Classification* classification);

  // @@protoc_insertion_point(class_scope:osi3.DetectedRoadMarking.CandidateRoadMarking)
 private:
  inline void set_has_probability();
  inline void clear_has_probability();
  inline void set_has_classification();
  inline void clear_has_classification();

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  ::google::protobuf::uint32 _has_bits_[1];
  mutable int _cached_size_;
  double probability_;
  ::osi3::RoadMarking_Classification* classification_;
  friend void  protobuf_AddDesc_osi_5fdetectedroadmarking_2eproto();
  friend void protobuf_AssignDesc_osi_5fdetectedroadmarking_2eproto();
  friend void protobuf_ShutdownFile_osi_5fdetectedroadmarking_2eproto();

  void InitAsDefaultInstance();
  static DetectedRoadMarking_CandidateRoadMarking* default_instance_;
};
// -------------------------------------------------------------------

class DetectedRoadMarking : public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:osi3.DetectedRoadMarking) */ {
 public:
  DetectedRoadMarking();
  virtual ~DetectedRoadMarking();

  DetectedRoadMarking(const DetectedRoadMarking& from);

  inline DetectedRoadMarking& operator=(const DetectedRoadMarking& from) {
    CopyFrom(from);
    return *this;
  }

  inline const ::google::protobuf::UnknownFieldSet& unknown_fields() const {
    return _internal_metadata_.unknown_fields();
  }

  inline ::google::protobuf::UnknownFieldSet* mutable_unknown_fields() {
    return _internal_metadata_.mutable_unknown_fields();
  }

  static const ::google::protobuf::Descriptor* descriptor();
  static const DetectedRoadMarking& default_instance();

  void Swap(DetectedRoadMarking* other);

  // implements Message ----------------------------------------------

  inline DetectedRoadMarking* New() const { return New(NULL); }

  DetectedRoadMarking* New(::google::protobuf::Arena* arena) const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const DetectedRoadMarking& from);
  void MergeFrom(const DetectedRoadMarking& from);
  void Clear();
  bool IsInitialized() const;

  int ByteSize() const;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input);
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      bool deterministic, ::google::protobuf::uint8* output) const;
  ::google::protobuf::uint8* SerializeWithCachedSizesToArray(::google::protobuf::uint8* output) const {
    return InternalSerializeWithCachedSizesToArray(false, output);
  }
  int GetCachedSize() const { return _cached_size_; }
  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const;
  void InternalSwap(DetectedRoadMarking* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return _internal_metadata_.arena();
  }
  inline void* MaybeArenaPtr() const {
    return _internal_metadata_.raw_arena_ptr();
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const;

  // nested types ----------------------------------------------------

  typedef DetectedRoadMarking_CandidateRoadMarking CandidateRoadMarking;

  // accessors -------------------------------------------------------

  // optional .osi3.DetectedItemHeader header = 1;
  bool has_header() const;
  void clear_header();
  static const int kHeaderFieldNumber = 1;
  const ::osi3::DetectedItemHeader& header() const;
  ::osi3::DetectedItemHeader* mutable_header();
  ::osi3::DetectedItemHeader* release_header();
  void set_allocated_header(::osi3::DetectedItemHeader* header);

  // optional .osi3.BaseStationary base = 2;
  bool has_base() const;
  void clear_base();
  static const int kBaseFieldNumber = 2;
  const ::osi3::BaseStationary& base() const;
  ::osi3::BaseStationary* mutable_base();
  ::osi3::BaseStationary* release_base();
  void set_allocated_base(::osi3::BaseStationary* base);

  // optional .osi3.BaseStationary base_rmse = 3;
  bool has_base_rmse() const;
  void clear_base_rmse();
  static const int kBaseRmseFieldNumber = 3;
  const ::osi3::BaseStationary& base_rmse() const;
  ::osi3::BaseStationary* mutable_base_rmse();
  ::osi3::BaseStationary* release_base_rmse();
  void set_allocated_base_rmse(::osi3::BaseStationary* base_rmse);

  // repeated .osi3.DetectedRoadMarking.CandidateRoadMarking candidate = 4;
  int candidate_size() const;
  void clear_candidate();
  static const int kCandidateFieldNumber = 4;
  const ::osi3::DetectedRoadMarking_CandidateRoadMarking& candidate(int index) const;
  ::osi3::DetectedRoadMarking_CandidateRoadMarking* mutable_candidate(int index);
  ::osi3::DetectedRoadMarking_CandidateRoadMarking* add_candidate();
  ::google::protobuf::RepeatedPtrField< ::osi3::DetectedRoadMarking_CandidateRoadMarking >*
      mutable_candidate();
  const ::google::protobuf::RepeatedPtrField< ::osi3::DetectedRoadMarking_CandidateRoadMarking >&
      candidate() const;

  // @@protoc_insertion_point(class_scope:osi3.DetectedRoadMarking)
 private:
  inline void set_has_header();
  inline void clear_has_header();
  inline void set_has_base();
  inline void clear_has_base();
  inline void set_has_base_rmse();
  inline void clear_has_base_rmse();

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  ::google::protobuf::uint32 _has_bits_[1];
  mutable int _cached_size_;
  ::osi3::DetectedItemHeader* header_;
  ::osi3::BaseStationary* base_;
  ::osi3::BaseStationary* base_rmse_;
  ::google::protobuf::RepeatedPtrField< ::osi3::DetectedRoadMarking_CandidateRoadMarking > candidate_;
  friend void  protobuf_AddDesc_osi_5fdetectedroadmarking_2eproto();
  friend void protobuf_AssignDesc_osi_5fdetectedroadmarking_2eproto();
  friend void protobuf_ShutdownFile_osi_5fdetectedroadmarking_2eproto();

  void InitAsDefaultInstance();
  static DetectedRoadMarking* default_instance_;
};
// ===================================================================


// ===================================================================

#if !PROTOBUF_INLINE_NOT_IN_HEADERS
// DetectedRoadMarking_CandidateRoadMarking

// optional double probability = 1;
inline bool DetectedRoadMarking_CandidateRoadMarking::has_probability() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
inline void DetectedRoadMarking_CandidateRoadMarking::set_has_probability() {
  _has_bits_[0] |= 0x00000001u;
}
inline void DetectedRoadMarking_CandidateRoadMarking::clear_has_probability() {
  _has_bits_[0] &= ~0x00000001u;
}
inline void DetectedRoadMarking_CandidateRoadMarking::clear_probability() {
  probability_ = 0;
  clear_has_probability();
}
inline double DetectedRoadMarking_CandidateRoadMarking::probability() const {
  // @@protoc_insertion_point(field_get:osi3.DetectedRoadMarking.CandidateRoadMarking.probability)
  return probability_;
}
inline void DetectedRoadMarking_CandidateRoadMarking::set_probability(double value) {
  set_has_probability();
  probability_ = value;
  // @@protoc_insertion_point(field_set:osi3.DetectedRoadMarking.CandidateRoadMarking.probability)
}

// optional .osi3.RoadMarking.Classification classification = 2;
inline bool DetectedRoadMarking_CandidateRoadMarking::has_classification() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
inline void DetectedRoadMarking_CandidateRoadMarking::set_has_classification() {
  _has_bits_[0] |= 0x00000002u;
}
inline void DetectedRoadMarking_CandidateRoadMarking::clear_has_classification() {
  _has_bits_[0] &= ~0x00000002u;
}
inline void DetectedRoadMarking_CandidateRoadMarking::clear_classification() {
  if (classification_ != NULL) classification_->::osi3::RoadMarking_Classification::Clear();
  clear_has_classification();
}
inline const ::osi3::RoadMarking_Classification& DetectedRoadMarking_CandidateRoadMarking::classification() const {
  // @@protoc_insertion_point(field_get:osi3.DetectedRoadMarking.CandidateRoadMarking.classification)
  return classification_ != NULL ? *classification_ : *default_instance_->classification_;
}
inline ::osi3::RoadMarking_Classification* DetectedRoadMarking_CandidateRoadMarking::mutable_classification() {
  set_has_classification();
  if (classification_ == NULL) {
    classification_ = new ::osi3::RoadMarking_Classification;
  }
  // @@protoc_insertion_point(field_mutable:osi3.DetectedRoadMarking.CandidateRoadMarking.classification)
  return classification_;
}
inline ::osi3::RoadMarking_Classification* DetectedRoadMarking_CandidateRoadMarking::release_classification() {
  // @@protoc_insertion_point(field_release:osi3.DetectedRoadMarking.CandidateRoadMarking.classification)
  clear_has_classification();
  ::osi3::RoadMarking_Classification* temp = classification_;
  classification_ = NULL;
  return temp;
}
inline void DetectedRoadMarking_CandidateRoadMarking::set_allocated_classification(::osi3::RoadMarking_Classification* classification) {
  delete classification_;
  classification_ = classification;
  if (classification) {
    set_has_classification();
  } else {
    clear_has_classification();
  }
  // @@protoc_insertion_point(field_set_allocated:osi3.DetectedRoadMarking.CandidateRoadMarking.classification)
}

// -------------------------------------------------------------------

// DetectedRoadMarking

// optional .osi3.DetectedItemHeader header = 1;
inline bool DetectedRoadMarking::has_header() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
inline void DetectedRoadMarking::set_has_header() {
  _has_bits_[0] |= 0x00000001u;
}
inline void DetectedRoadMarking::clear_has_header() {
  _has_bits_[0] &= ~0x00000001u;
}
inline void DetectedRoadMarking::clear_header() {
  if (header_ != NULL) header_->::osi3::DetectedItemHeader::Clear();
  clear_has_header();
}
inline const ::osi3::DetectedItemHeader& DetectedRoadMarking::header() const {
  // @@protoc_insertion_point(field_get:osi3.DetectedRoadMarking.header)
  return header_ != NULL ? *header_ : *default_instance_->header_;
}
inline ::osi3::DetectedItemHeader* DetectedRoadMarking::mutable_header() {
  set_has_header();
  if (header_ == NULL) {
    header_ = new ::osi3::DetectedItemHeader;
  }
  // @@protoc_insertion_point(field_mutable:osi3.DetectedRoadMarking.header)
  return header_;
}
inline ::osi3::DetectedItemHeader* DetectedRoadMarking::release_header() {
  // @@protoc_insertion_point(field_release:osi3.DetectedRoadMarking.header)
  clear_has_header();
  ::osi3::DetectedItemHeader* temp = header_;
  header_ = NULL;
  return temp;
}
inline void DetectedRoadMarking::set_allocated_header(::osi3::DetectedItemHeader* header) {
  delete header_;
  header_ = header;
  if (header) {
    set_has_header();
  } else {
    clear_has_header();
  }
  // @@protoc_insertion_point(field_set_allocated:osi3.DetectedRoadMarking.header)
}

// optional .osi3.BaseStationary base = 2;
inline bool DetectedRoadMarking::has_base() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
inline void DetectedRoadMarking::set_has_base() {
  _has_bits_[0] |= 0x00000002u;
}
inline void DetectedRoadMarking::clear_has_base() {
  _has_bits_[0] &= ~0x00000002u;
}
inline void DetectedRoadMarking::clear_base() {
  if (base_ != NULL) base_->::osi3::BaseStationary::Clear();
  clear_has_base();
}
inline const ::osi3::BaseStationary& DetectedRoadMarking::base() const {
  // @@protoc_insertion_point(field_get:osi3.DetectedRoadMarking.base)
  return base_ != NULL ? *base_ : *default_instance_->base_;
}
inline ::osi3::BaseStationary* DetectedRoadMarking::mutable_base() {
  set_has_base();
  if (base_ == NULL) {
    base_ = new ::osi3::BaseStationary;
  }
  // @@protoc_insertion_point(field_mutable:osi3.DetectedRoadMarking.base)
  return base_;
}
inline ::osi3::BaseStationary* DetectedRoadMarking::release_base() {
  // @@protoc_insertion_point(field_release:osi3.DetectedRoadMarking.base)
  clear_has_base();
  ::osi3::BaseStationary* temp = base_;
  base_ = NULL;
  return temp;
}
inline void DetectedRoadMarking::set_allocated_base(::osi3::BaseStationary* base) {
  delete base_;
  base_ = base;
  if (base) {
    set_has_base();
  } else {
    clear_has_base();
  }
  // @@protoc_insertion_point(field_set_allocated:osi3.DetectedRoadMarking.base)
}

// optional .osi3.BaseStationary base_rmse = 3;
inline bool DetectedRoadMarking::has_base_rmse() const {
  return (_has_bits_[0] & 0x00000004u) != 0;
}
inline void DetectedRoadMarking::set_has_base_rmse() {
  _has_bits_[0] |= 0x00000004u;
}
inline void DetectedRoadMarking::clear_has_base_rmse() {
  _has_bits_[0] &= ~0x00000004u;
}
inline void DetectedRoadMarking::clear_base_rmse() {
  if (base_rmse_ != NULL) base_rmse_->::osi3::BaseStationary::Clear();
  clear_has_base_rmse();
}
inline const ::osi3::BaseStationary& DetectedRoadMarking::base_rmse() const {
  // @@protoc_insertion_point(field_get:osi3.DetectedRoadMarking.base_rmse)
  return base_rmse_ != NULL ? *base_rmse_ : *default_instance_->base_rmse_;
}
inline ::osi3::BaseStationary* DetectedRoadMarking::mutable_base_rmse() {
  set_has_base_rmse();
  if (base_rmse_ == NULL) {
    base_rmse_ = new ::osi3::BaseStationary;
  }
  // @@protoc_insertion_point(field_mutable:osi3.DetectedRoadMarking.base_rmse)
  return base_rmse_;
}
inline ::osi3::BaseStationary* DetectedRoadMarking::release_base_rmse() {
  // @@protoc_insertion_point(field_release:osi3.DetectedRoadMarking.base_rmse)
  clear_has_base_rmse();
  ::osi3::BaseStationary* temp = base_rmse_;
  base_rmse_ = NULL;
  return temp;
}
inline void DetectedRoadMarking::set_allocated_base_rmse(::osi3::BaseStationary* base_rmse) {
  delete base_rmse_;
  base_rmse_ = base_rmse;
  if (base_rmse) {
    set_has_base_rmse();
  } else {
    clear_has_base_rmse();
  }
  // @@protoc_insertion_point(field_set_allocated:osi3.DetectedRoadMarking.base_rmse)
}

// repeated .osi3.DetectedRoadMarking.CandidateRoadMarking candidate = 4;
inline int DetectedRoadMarking::candidate_size() const {
  return candidate_.size();
}
inline void DetectedRoadMarking::clear_candidate() {
  candidate_.Clear();
}
inline const ::osi3::DetectedRoadMarking_CandidateRoadMarking& DetectedRoadMarking::candidate(int index) const {
  // @@protoc_insertion_point(field_get:osi3.DetectedRoadMarking.candidate)
  return candidate_.Get(index);
}
inline ::osi3::DetectedRoadMarking_CandidateRoadMarking* DetectedRoadMarking::mutable_candidate(int index) {
  // @@protoc_insertion_point(field_mutable:osi3.DetectedRoadMarking.candidate)
  return candidate_.Mutable(index);
}
inline ::osi3::DetectedRoadMarking_CandidateRoadMarking* DetectedRoadMarking::add_candidate() {
  // @@protoc_insertion_point(field_add:osi3.DetectedRoadMarking.candidate)
  return candidate_.Add();
}
inline ::google::protobuf::RepeatedPtrField< ::osi3::DetectedRoadMarking_CandidateRoadMarking >*
DetectedRoadMarking::mutable_candidate() {
  // @@protoc_insertion_point(field_mutable_list:osi3.DetectedRoadMarking.candidate)
  return &candidate_;
}
inline const ::google::protobuf::RepeatedPtrField< ::osi3::DetectedRoadMarking_CandidateRoadMarking >&
DetectedRoadMarking::candidate() const {
  // @@protoc_insertion_point(field_list:osi3.DetectedRoadMarking.candidate)
  return candidate_;
}

#endif  // !PROTOBUF_INLINE_NOT_IN_HEADERS
// -------------------------------------------------------------------


// @@protoc_insertion_point(namespace_scope)

}  // namespace osi3

// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_osi_5fdetectedroadmarking_2eproto__INCLUDED
