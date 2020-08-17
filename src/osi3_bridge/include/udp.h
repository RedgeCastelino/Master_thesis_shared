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
 * Plattformunabhängige (Windows und Linux) UDP Funktionen
 *
 */

#ifndef UDP_CLIENT_HEADER
#define UDP_CLIENT_HEADER

#ifdef __linux__
    #include <sys/types.h>
    #include <sys/socket.h>
    #include <netinet/in.h>
    #include <arpa/inet.h>
    #include <netdb.h>
    #include <stdio.h>
    #include <unistd.h>
    #include <string.h>
    #include <stdlib.h>
    #include <sys/time.h>
    #include <errno.h>

    typedef struct sockaddr_in SOCKADDR_IN;
    typedef struct sockaddr SOCKADDR;
    typedef int SOCKET;
    #define ERROR_CODE (errno)
#elif _WIN32
    #include <winsock2.h>
    #include <windows.h>
    #define ERROR_CODE (WSAGetLastError())
    typedef int socklen_t;
#else
    #error "OS not supported!"
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>

/**
 * Initialisierungsfunktion
 *
 * Initialisiert einen UDP-Socket
 *
 * @param s Socket, der initialisiert wird
 * @return Erfolg der Initialisierung
 */
bool udp_init(SOCKET * s);

/**
 * Bindefunktion
 *
 * @param s Socket, der initialisiert wird
 * @param port Port, an den der Socket gebunden wird
 * @return Erfolg des Binde
 */
bool udp_bind(SOCKET * s, uint16_t port);

/**
 * Sendefunktion
 *
 * @param s Socket, der initialisiert wird
 * @param addr Zieladdresse
 * @param port Zielport
 * @param data Daten, die versendet werden sollen
 * @param data_size Größe der Daten
 * @return Erfolg des Senden
 */
bool udp_send(SOCKET * s, const char * addr, uint16_t port, 
                const uint8_t * data, size_t data_size);

/**
 * Empfangsfunktion
 *
 * @param s Socket, der initialisiert wird
 * @param remote_addr Quelladresse (oder NULL, falls nicht von Intresse)
 * @param remote_port Quellport
 * @param data Daten, die empfangen wurden
 * @param[inout] data_size Maximale größe (in), empfangene Größe (out)
 * @return Erfolg des Empfangen
 */
bool udp_recv(SOCKET * s, uint8_t * data, size_t * data_size,
                char * remote_addr, uint16_t * remote_port);

/**
 * Empfangsfunktion mit Timeout
 *
 * @param s Socket, der initialisiert wird
 * @param remote_addr Quelladresse (oder NULL, falls nicht von Intresse)
 * @param remote_port Quellport
 * @param data Daten, die empfangen wurden
 * @param[inout] data_size Maximale größe (in), empfangene Größe (out)
 * @return Erfolg des Empfangen
 */
bool udp_recv_timeout(SOCKET * s, uint8_t * data, size_t * data_size,
                char * remote_addr, uint16_t * remote_port);
                
/**
 * Deinitialiserungsfunktion
 *
 * @param s Socket, der deinitialisert wird
 * @return Erfolg der Deinitialiserung
 */
bool udp_close(SOCKET * s);

#endif
