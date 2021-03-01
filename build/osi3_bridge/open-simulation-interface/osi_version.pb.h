// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: osi_version.proto

#ifndef PROTOBUF_osi_5fversion_2eproto__INCLUDED
#define PROTOBUF_osi_5fversion_2eproto__INCLUDED

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
#include <google/protobuf/descriptor.pb.h>
// @@protoc_insertion_point(includes)

namespace osi3 {

// Internal implementation detail -- do not call these.
void protobuf_AddDesc_osi_5fversion_2eproto();
void protobuf_AssignDesc_osi_5fversion_2eproto();
void protobuf_ShutdownFile_osi_5fversion_2eproto();

class InterfaceVersion;

// ===================================================================

class InterfaceVersion : public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:osi3.InterfaceVersion) */ {
 public:
  InterfaceVersion();
  virtual ~InterfaceVersion();

  InterfaceVersion(const InterfaceVersion& from);

  inline InterfaceVersion& operator=(const InterfaceVersion& from) {
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
  static const InterfaceVersion& default_instance();

  void Swap(InterfaceVersion* other);

  // implements Message ----------------------------------------------

  inline InterfaceVersion* New() const { return New(NULL); }

  InterfaceVersion* New(::google::protobuf::Arena* arena) const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const InterfaceVersion& from);
  void MergeFrom(const InterfaceVersion& from);
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
  void InternalSwap(InterfaceVersion* other);
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

  // optional uint32 version_major = 1;
  bool has_version_major() const;
  void clear_version_major();
  static const int kVersionMajorFieldNumber = 1;
  ::google::protobuf::uint32 version_major() const;
  void set_version_major(::google::protobuf::uint32 value);

  // optional uint32 version_minor = 2;
  bool has_version_minor() const;
  void clear_version_minor();
  static const int kVersionMinorFieldNumber = 2;
  ::google::protobuf::uint32 version_minor() const;
  void set_version_minor(::google::protobuf::uint32 value);

  // optional uint32 version_patch = 3;
  bool has_version_patch() const;
  void clear_version_patch();
  static const int kVersionPatchFieldNumber = 3;
  ::google::protobuf::uint32 version_patch() const;
  void set_version_patch(::google::protobuf::uint32 value);

  // @@protoc_insertion_point(class_scope:osi3.InterfaceVersion)
 private:
  inline void set_has_version_major();
  inline void clear_has_version_major();
  inline void set_has_version_minor();
  inline void clear_has_version_minor();
  inline void set_has_version_patch();
  inline void clear_has_version_patch();

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  ::google::protobuf::uint32 _has_bits_[1];
  mutable int _cached_size_;
  ::google::protobuf::uint32 version_major_;
  ::google::protobuf::uint32 version_minor_;
  ::google::protobuf::uint32 version_patch_;
  friend void  protobuf_AddDesc_osi_5fversion_2eproto();
  friend void protobuf_AssignDesc_osi_5fversion_2eproto();
  friend void protobuf_ShutdownFile_osi_5fversion_2eproto();

  void InitAsDefaultInstance();
  static InterfaceVersion* default_instance_;
};
// ===================================================================

static const int kCurrentInterfaceVersionFieldNumber = 81000;
extern ::google::protobuf::internal::ExtensionIdentifier< ::google::protobuf::FileOptions,
    ::google::protobuf::internal::MessageTypeTraits< ::osi3::InterfaceVersion >, 11, false >
  current_interface_version;

// ===================================================================

#if !PROTOBUF_INLINE_NOT_IN_HEADERS
// InterfaceVersion

// optional uint32 version_major = 1;
inline bool InterfaceVersion::has_version_major() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
inline void InterfaceVersion::set_has_version_major() {
  _has_bits_[0] |= 0x00000001u;
}
inline void InterfaceVersion::clear_has_version_major() {
  _has_bits_[0] &= ~0x00000001u;
}
inline void InterfaceVersion::clear_version_major() {
  version_major_ = 0u;
  clear_has_version_major();
}
inline ::google::protobuf::uint32 InterfaceVersion::version_major() const {
  // @@protoc_insertion_point(field_get:osi3.InterfaceVersion.version_major)
  return version_major_;
}
inline void InterfaceVersion::set_version_major(::google::protobuf::uint32 value) {
  set_has_version_major();
  version_major_ = value;
  // @@protoc_insertion_point(field_set:osi3.InterfaceVersion.version_major)
}

// optional uint32 version_minor = 2;
inline bool InterfaceVersion::has_version_minor() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
inline void InterfaceVersion::set_has_version_minor() {
  _has_bits_[0] |= 0x00000002u;
}
inline void InterfaceVersion::clear_has_version_minor() {
  _has_bits_[0] &= ~0x00000002u;
}
inline void InterfaceVersion::clear_version_minor() {
  version_minor_ = 0u;
  clear_has_version_minor();
}
inline ::google::protobuf::uint32 InterfaceVersion::version_minor() const {
  // @@protoc_insertion_point(field_get:osi3.InterfaceVersion.version_minor)
  return version_minor_;
}
inline void InterfaceVersion::set_version_minor(::google::protobuf::uint32 value) {
  set_has_version_minor();
  version_minor_ = value;
  // @@protoc_insertion_point(field_set:osi3.InterfaceVersion.version_minor)
}

// optional uint32 version_patch = 3;
inline bool InterfaceVersion::has_version_patch() const {
  return (_has_bits_[0] & 0x00000004u) != 0;
}
inline void InterfaceVersion::set_has_version_patch() {
  _has_bits_[0] |= 0x00000004u;
}
inline void InterfaceVersion::clear_has_version_patch() {
  _has_bits_[0] &= ~0x00000004u;
}
inline void InterfaceVersion::clear_version_patch() {
  version_patch_ = 0u;
  clear_has_version_patch();
}
inline ::google::protobuf::uint32 InterfaceVersion::version_patch() const {
  // @@protoc_insertion_point(field_get:osi3.InterfaceVersion.version_patch)
  return version_patch_;
}
inline void InterfaceVersion::set_version_patch(::google::protobuf::uint32 value) {
  set_has_version_patch();
  version_patch_ = value;
  // @@protoc_insertion_point(field_set:osi3.InterfaceVersion.version_patch)
}

#endif  // !PROTOBUF_INLINE_NOT_IN_HEADERS

// @@protoc_insertion_point(namespace_scope)

}  // namespace osi3

// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_osi_5fversion_2eproto__INCLUDED
