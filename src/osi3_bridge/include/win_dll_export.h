#ifndef WIN_DLL_EXPORT
#define WIN_DLL_EXPORT

#ifdef _WIN32
#  ifdef MODULE_API_EXPORTS
#    define MODULE_API __declspec(dllexport)
#  elif MODULE_API_IMPORTS
#    define MODULE_API __declspec(dllimport)
#  else 
#    define MODULE_API
#  endif
#else
#  define MODULE_API
#endif

#endif /* WIN_DLL_EXPORT */
