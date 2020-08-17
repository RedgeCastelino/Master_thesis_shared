#include "osi_protocol_header.h"

size_t osiph_get_header_size()
{
    return sizeof(osi_protocol_header);
}

void osiph_set_magic_id(void * header)
{
    ((osi_protocol_header*)header)->magic_id = SWAP_64(OSI_PROTOCOL_HEADER_MAGIC_ID);
}

bool osiph_check_magic_id(void * header)
{
    return SWAP_64(((osi_protocol_header*)header)->magic_id) == OSI_PROTOCOL_HEADER_MAGIC_ID;
}

void osiph_set_protocol_version(void * header)
{
    ((osi_protocol_header*)header)->protocol_version = SWAP_32(OSI_PROTOCOL_HEADER_VERSION);
}

uint32_t osiph_get_protocol_version(void * header)
{
    return SWAP_32(((osi_protocol_header*)header)->protocol_version);
}

bool osiph_check_protocol_version(void * header)
{
    return SWAP_32(((osi_protocol_header*)header)->protocol_version) == OSI_PROTOCOL_HEADER_VERSION;
}

void osiph_set_osi_version(void * header, uint16_t major, uint8_t minor, uint8_t patch)
{
    ((osi_protocol_header*)header)->osi_version_major = SWAP_16(major);
    ((osi_protocol_header*)header)->osi_version_minor = minor;
    ((osi_protocol_header*)header)->osi_version_patch = patch;
}

uint16_t osiph_get_osi_version_major(void * header)
{
    return SWAP_16(((osi_protocol_header*)header)->osi_version_major);
}

uint8_t osiph_get_osi_version_minor(void * header)
{
    return ((osi_protocol_header*)header)->osi_version_minor;
}

uint8_t osiph_get_osi_version_patch(void * header)
{
    return ((osi_protocol_header*)header)->osi_version_patch;
}

void osiph_set_payload_size(void * header, uint32_t size)
{
    ((osi_protocol_header*)header)->payload_size = SWAP_32(size);
}

uint32_t osiph_get_payload_size(void * header)
{
    return SWAP_32(((osi_protocol_header*)header)->payload_size);
}

void osiph_set_payload_type(void * header, uint32_t type)
{
    ((osi_protocol_header*)header)->payload_type = SWAP_32(type);
}

uint32_t osiph_get_payload_type(void * header)
{
    return SWAP_32(((osi_protocol_header*)header)->payload_type);
}

void * osiph_get_payload(void * header)
{
    return (void *)(((uintptr_t) header) + sizeof(osi_protocol_header));
}
