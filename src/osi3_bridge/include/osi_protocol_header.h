/**
 * @file
 * @author  Georg Seifert <georg.seifert@thi.de>
 * @version 1
 *
 * @section LICENSE
 *
 * For internal use only
 *
 * @section BESCHREIBUNG
 * 
 * Das "osi network protocol" definiert einen statischen Header, der vor das OSI 
 * gesetzt wird um die dynamische Größe zu kodieren.
 *
 * \latexonly
 * \begin{bytefield}[bitwidth=0.8em]{32}
 * 	\bitheader{0,15,16,23,24,31} \\
 * 	\begin{rightwordgroup}{Header}
 * 		\wordbox{2}{Magic ID} \\
 * 		\wordbox{1}{Protokoll Version} \\
 * 		\begin{leftwordgroup}{OSI Version}
 * 			\bitbox{16}{Major} & \bitbox{8}{Minor} & \bitbox{8}{Patch}
 * 		\end{leftwordgroup} \\
 * 		\wordbox{1}{Payload Größe} \\
 * 		\wordbox{1}{Payload Typ}
 * 	\end{rightwordgroup}\\
 * 	\begin{rightwordgroup}{Payload}
 * 	\wordbox[lrt]{1}{OSI Daten} \\
 * 	\skippedwords \\
 * 	\wordbox[lrb]{1}{}
 * 	\end{rightwordgroup}
 * \end{bytefield}
 * \endlatexonly
 * 
 * Hierbei ist zu beachten, dass die versendeten Werte als Network/Big Endian
 * abgelegt werden. Um dies sicher zu stellen werden für den Zugriff auf die 
 * Datenstruktur Getter und Setter bereitgestellt, die die Codierung intern 
 * übernehmen.
 *
 */

#ifndef OSI_NETWORK_PROTOCOL_HEADER
#define OSI_NETWORK_PROTOCOL_HEADER

#ifdef __cplusplus
extern "C"
{
#endif

#include <stddef.h>
#include <stdint.h>
#include <stdbool.h>
#include "win_dll_export.h"

#if __BYTE_ORDER__ == __ORDER_LITTLE_ENDIAN__
    /// 16-Bit Swap Function
    #define SWAP_16(x) \
         ((((x) >> 8) & 0xffu) | (((x) & 0xffu) << 8))

    /// 32-Bit Swap Function
    #define SWAP_32(x) \
         ((((x) & 0xff000000u) >> 24) | (((x) & 0x00ff0000u) >>  8) |   \
          (((x) & 0x0000ff00u) <<  8) | (((x) & 0x000000ffu) << 24))

    /// 64-Bit Swap Function
    #define SWAP_64(x) \
         ((((x) & 0xff00000000000000ull) >> 56) |   \
          (((x) & 0x00ff000000000000ull) >> 40) |   \
          (((x) & 0x0000ff0000000000ull) >> 24) |   \
          (((x) & 0x000000ff00000000ull) >> 8)  |   \
          (((x) & 0x00000000ff000000ull) << 8)  |   \
          (((x) & 0x0000000000ff0000ull) << 24) |   \
          (((x) & 0x000000000000ff00ull) << 40) |   \
          (((x) & 0x00000000000000ffull) << 56))

#elif __BYTE_ORDER__ == __ORDER_BIG_ENDIAN__
    #define SWAP_16(x) (x)
    #define SWAP_32(x) (x)
    #define SWAP_64(x) (x)
#else
    #error Byteorder ("__ORDER_BIG_ENDIAN__" or "__ORDER_LITTLE_ENDIAN__") has to be defined
#endif

/// Magic ID um das Protokoll zu erkennen
#define OSI_PROTOCOL_HEADER_MAGIC_ID (4846245148911422785lu)
/// Aktuelle verwendete Version des Protokolls
#define OSI_PROTOCOL_HEADER_VERSION  (1u)

/// OSI Datenpaket Typ
enum osi_payloadDataType
{
    osi_GroundTruth = 0,    /**<  OSI Paket ist vom Typ: Ground Truth */
    osi_SensorData  = 1,    /**<  OSI Paket ist vom Typ: Sensor Data */
    osi_SensorView  = 2,    /**<  OSI Paket ist vom Typ: Sensor View */
    osi_FeatureData = 3     /**<  OSI Paket ist vom Typ: Feature Data */
};

/**
 * Struktur des Statischen Headers
 *
 * Die Struktur beschreibt die einzelnen Elemente des "network protocol".
 * Bei änderungen im Protokoll ist zu beachten, dass das das Alignment von
 * von 64-Bit eingehalten wird, und wenn nötig mit spare-Variablen gefüllt wird,
 * um Kompilerspezifika zu umgehen.
 *
 * @note Daten werden als Network bzw. Big Endian über das Netzwerk verschickt
 */
typedef struct _osi_protocol_header
{
    uint64_t magic_id;              /**< 64-Bit ID um das Protokoll zu erkennen */
    uint32_t protocol_version;      /**< 32-Bit Aktuelle Version des Protokolls */
    uint16_t osi_version_major;     /**< 16-Bit OSI Major Version */
    uint8_t  osi_version_minor;     /**< 8-Bit OSI Minor Version */
    uint8_t  osi_version_patch;     /**< 8-Bit OSI Patch Version */
    uint32_t payload_size;          /**< 32-Bit Größe des Nachfolgenden OSI-Pakets */
    uint32_t payload_type;          /**< 32-Bit OSI Typ @see enum payloadDataType */
} osi_protocol_header;

/**
 * Liefert die Größe der internen Struktur zurück
 *
 * @return Größe der Header-Struktur
 */
MODULE_API size_t osiph_get_header_size();

/**
 * Setter für Magic ID
 *
 * @param header Header, bei dem sie Magic ID gesetzt wird
 */
MODULE_API void osiph_set_magic_id(void * header);

/**
 * Überprüfen der Magic ID
 *
 * @param header Header, bei dem die Magic ID überprüft wird
 * @return Ergebnis der Überprüfung
 */
MODULE_API bool osiph_check_magic_id(void * header);

/**
 * Setter der Version
 *
 * @param header Header, bei dem die Version gesetzt wird
 */
MODULE_API void osiph_set_protocol_version(void * header);

/**
 * Getter der Version
 *
 * @param header Header, bei dem die Version zurückgeliefert wird
 * @return Version des Headers
 */
MODULE_API uint32_t osiph_get_protocol_version(void * header);

/**
 * Überprüfen der Magic ID
 *
 * @param header Header, bei dem sie Version geprüft wird
 * @return Ergebnis der Überprüfung
 */
MODULE_API bool osiph_check_protocol_version(void * header);

/**
 * Setter der OSI Version
 *
 * Versionierung siehe:
 * https://github.com/OpenSimulationInterface/open-simulation-interface/blob/master/README.md
 *
 * @param header Header, bei dem sie OSI Version gesetzt wird
 * @param major OSI Major-Version
 * @param minor OSI Minor-Version
 * @param patch OSI Patch-Version
 */
MODULE_API void osiph_set_osi_version(void * header, uint16_t major, uint8_t minor, uint8_t patch);

/**
 * Getter der OSI Major-Version
 *
 * Versionierung siehe:
 * https://github.com/OpenSimulationInterface/open-simulation-interface/blob/master/README.md
 *
 * @param header Header, bei dem die Version zurückgeliefert wird
 * @return OSI Major-Version des Headers
 */
MODULE_API uint16_t osiph_get_osi_version_major(void * header);

/**
 * Getter der OSI Minor-Version
 *
 * Versionierung siehe:
 * https://github.com/OpenSimulationInterface/open-simulation-interface/blob/master/README.md
 *
 * @param header Header, bei dem die Version zurückgeliefert wird
 * @return OSI Minor-Version des Headers
 */
MODULE_API uint8_t osiph_get_osi_version_minor(void * header);

/**
 * Getter der OSI Patch-Version
 *
 * Versionierung siehe:
 * https://github.com/OpenSimulationInterface/open-simulation-interface/blob/master/README.md
 *
 * @param header Header, bei dem die Version zurückgeliefert wird
 * @return OSI Patch-Version des Headers
 */
MODULE_API uint8_t osiph_get_osi_version_patch(void * header);

/**
 * Setter für OSI Payload Size
 *
 * @param header Header, bei dem die Version zurückgeliefert wird
 * @param size Payload Size
 */
MODULE_API void osiph_set_payload_size(void * header, uint32_t size);

/**
 * Getter für OSI Payload Size
 *
 * @param header Header, bei dem die Version zurückgeliefert wird
 * @return Payload Size
 */
MODULE_API uint32_t osiph_get_payload_size(void * header);

/**
 * Setter für OSI Payload Type
 *
 * @param header Header, bei dem die Version zurückgeliefert wird
 * @param type Payload Type
 */
MODULE_API void osiph_set_payload_type(void * header, uint32_t type);

/**
 * Getter für OSI Payload Type
 *
 * @param header Header, bei dem die Version zurückgeliefert wird
 * @return Payload Type
 */
MODULE_API uint32_t osiph_get_payload_type(void * header);

/**
 * Getter für OSI Payload
 *
 * @param header Header, bei dem die Version zurückgeliefert wird
 * @return Pointer auf OSI Payload
 */
MODULE_API void * osiph_get_payload(void * header);

#ifdef __cplusplus
}
#endif

#endif // NETWORK_PROTOCOL_HEADER