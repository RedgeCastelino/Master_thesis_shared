#include "udp.h"

bool udp_init(SOCKET * s)
{
#ifdef _WIN32
    WSADATA wsa;
    int rc = WSAStartup(MAKEWORD(2,0),&wsa);
    if(rc != 0)
    {
        fprintf(stderr, "Fehler: startWinsock, fehler code: %d\n", rc);
        return false;
    }
#endif
    *s = socket(AF_INET, SOCK_DGRAM, 0);
#ifdef __linux__
    if(*s < 0)
#elif _WIN32
    if(*s == INVALID_SOCKET)
#endif
    {
        int err = ERROR_CODE;
        fprintf(stderr, "Fehler: Der Socket konnte nicht erstellt werden, fehler code: %d\n", err);
        return false;
    }

    return true;
}

bool udp_bind(SOCKET * s, uint16_t port)
{
    struct sockaddr_in addr;
    int rc;
	addr.sin_family = AF_INET;
	addr.sin_addr.s_addr = htonl(INADDR_ANY);
    addr.sin_port = htons(port);
    rc = bind(*s, (struct sockaddr *)&addr, sizeof(addr));
#ifdef __linux__
    if(rc < 0)
#elif _WIN32
    if(rc == SOCKET_ERROR)
#endif
    {
        int err = ERROR_CODE;
        fprintf(stderr, "Fehler: Binden an Port war nicht möglich, fehler code: %d\n", err);
        return false;
    }
    return true;
}

bool udp_send(SOCKET * s, const char * addr, uint16_t port, const uint8_t * data, size_t data_size)
{
    SOCKADDR_IN addr_in;
    addr_in.sin_family = AF_INET;
    addr_in.sin_port = htons(port);
    addr_in.sin_addr.s_addr = inet_addr(addr);
    int rc = sendto (*s, (const char *)data, data_size, 0, (SOCKADDR*)&addr_in, sizeof(SOCKADDR_IN));
#ifdef __linux__
    if(rc < 0)
#elif _WIN32
    if(rc == SOCKET_ERROR)
#endif
    {
        fprintf(stderr, "Fehler: sendto, fehler code: %d\n", ERROR_CODE);
        return false;
    }
    return true;
}

bool udp_recv(SOCKET * s, uint8_t * data, size_t * data_size,
                char * remote_addr, uint16_t * remote_port)
{
    SOCKADDR_IN remoteAddr;
    socklen_t remoteAddrLen = sizeof(SOCKADDR_IN);
    int rc = recvfrom(*s, (char *)data, *data_size, 0, (SOCKADDR*)&remoteAddr, &remoteAddrLen);

#ifdef __linux__
    if(rc < 0)
#elif _WIN32
    if(rc == SOCKET_ERROR)
#endif
    { 
        fprintf(stderr, "Fehler: recvfrom, fehler code: %d\n", ERROR_CODE);
        return false;
    }
    
    if(remote_addr != NULL)
    {
        strcpy(remote_addr, inet_ntoa(remoteAddr.sin_addr));
        *remote_port = ntohs(remoteAddr.sin_port);
    }
    *data_size = rc;
    return true;
}

bool udp_recv_timeout(SOCKET * s, uint8_t * data, size_t * data_size,
                char * remote_addr, uint16_t * remote_port)
{

#ifdef __linux__
    return false;
#elif _WIN32
    struct timeval tv_timeout = { 0, 0 };
    fd_set fdset;
    
    FD_ZERO( &fdset );
    FD_SET( *s, &fdset );
    int rc_select = select( *s+1, &fdset, NULL, NULL, (PTIMEVAL)&tv_timeout );
    if ( rc_select == SOCKET_ERROR )
    {
        fprintf(stderr, "Fehler: select, fehler code: %d\n", ERROR_CODE);
        return false;
    }
    
    
    if ( FD_ISSET( *s, &fdset ) )
    {
        return udp_recv(s, data, data_size, remote_addr, remote_port);
    }
    
    return false;
#endif    
}

bool udp_close(SOCKET * s)
{
#ifdef __linux__
    int rc = close(*s);
     if(rc < 0)
#elif _WIN32
    int rc = closesocket(*s);
    if(rc == SOCKET_ERROR)
#endif
    {
        fprintf(stderr, "Fehler: socketclose, fehler code: %d\n", ERROR_CODE);
        return false;
    }
    return true;
}
