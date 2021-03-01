# Install script for directory: /home/student/Desktop/Redge_Thesis/vil/src/osi3_bridge/open-simulation-interface

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/student/Desktop/Redge_Thesis/vil/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xlibx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/osi3" TYPE STATIC_LIBRARY FILES "/home/student/Desktop/Redge_Thesis/vil/devel/lib/libopen_simulation_interface_static.a")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xlibx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/osi3" TYPE STATIC_LIBRARY FILES "/home/student/Desktop/Redge_Thesis/vil/devel/lib/libopen_simulation_interface_pic.a")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xlibx" OR NOT CMAKE_INSTALL_COMPONENT)
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/osi3/libopen_simulation_interface.so.3.0.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/osi3/libopen_simulation_interface.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/osi3" TYPE SHARED_LIBRARY FILES
    "/home/student/Desktop/Redge_Thesis/vil/devel/lib/libopen_simulation_interface.so.3.0.1"
    "/home/student/Desktop/Redge_Thesis/vil/devel/lib/libopen_simulation_interface.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/osi3/libopen_simulation_interface.so.3.0.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/osi3/libopen_simulation_interface.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xdevx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/open_simulation_interface-3" TYPE FILE FILES
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/CMakeFiles/open_simulation_interface-config.cmake"
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/open_simulation_interface-config-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/osi3" TYPE FILE FILES
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/osi_version.pb.h"
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/osi_common.pb.h"
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/osi_datarecording.pb.h"
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/osi_detectedtrafficsign.pb.h"
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/osi_detectedtrafficlight.pb.h"
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/osi_detectedroadmarking.pb.h"
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/osi_detectedlane.pb.h"
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/osi_detectedobject.pb.h"
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/osi_detectedoccupant.pb.h"
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/osi_environment.pb.h"
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/osi_groundtruth.pb.h"
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/osi_hostvehicledata.pb.h"
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/osi_trafficsign.pb.h"
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/osi_trafficlight.pb.h"
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/osi_roadmarking.pb.h"
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/osi_lane.pb.h"
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/osi_featuredata.pb.h"
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/osi_object.pb.h"
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/osi_occupant.pb.h"
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/osi_sensordata.pb.h"
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/osi_sensorviewconfiguration.pb.h"
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/osi_sensorspecific.pb.h"
    "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/osi_sensorview.pb.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xdevx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/open_simulation_interface-3/open_simulation_interface_targets.cmake")
    file(DIFFERENT EXPORT_FILE_CHANGED FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/open_simulation_interface-3/open_simulation_interface_targets.cmake"
         "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/CMakeFiles/Export/lib/cmake/open_simulation_interface-3/open_simulation_interface_targets.cmake")
    if(EXPORT_FILE_CHANGED)
      file(GLOB OLD_CONFIG_FILES "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/open_simulation_interface-3/open_simulation_interface_targets-*.cmake")
      if(OLD_CONFIG_FILES)
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/open_simulation_interface-3/open_simulation_interface_targets.cmake\" will be replaced.  Removing files [${OLD_CONFIG_FILES}].")
        file(REMOVE ${OLD_CONFIG_FILES})
      endif()
    endif()
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/open_simulation_interface-3" TYPE FILE FILES "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/CMakeFiles/Export/lib/cmake/open_simulation_interface-3/open_simulation_interface_targets.cmake")
  if("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/open_simulation_interface-3" TYPE FILE FILES "/home/student/Desktop/Redge_Thesis/vil/build/osi3_bridge/open-simulation-interface/CMakeFiles/Export/lib/cmake/open_simulation_interface-3/open_simulation_interface_targets-release.cmake")
  endif()
endif()

