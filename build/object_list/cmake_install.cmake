# Install script for directory: /home/student/Desktop/Redge_Thesis/vil/src/object_list

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

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/object_list/msg" TYPE FILE FILES
    "/home/student/Desktop/Redge_Thesis/vil/src/object_list/msg/Classification.msg"
    "/home/student/Desktop/Redge_Thesis/vil/src/object_list/msg/Dimension.msg"
    "/home/student/Desktop/Redge_Thesis/vil/src/object_list/msg/Features.msg"
    "/home/student/Desktop/Redge_Thesis/vil/src/object_list/msg/Geometric.msg"
    "/home/student/Desktop/Redge_Thesis/vil/src/object_list/msg/ObjectList.msg"
    "/home/student/Desktop/Redge_Thesis/vil/src/object_list/msg/ObjectsList.msg"
    "/home/student/Desktop/Redge_Thesis/vil/src/object_list/msg/EgoData.msg"
    "/home/student/Desktop/Redge_Thesis/vil/src/object_list/msg/SensorProperty.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/object_list/cmake" TYPE FILE FILES "/home/student/Desktop/Redge_Thesis/vil/build/object_list/catkin_generated/installspace/object_list-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/student/Desktop/Redge_Thesis/vil/devel/include/object_list")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/student/Desktop/Redge_Thesis/vil/devel/share/roseus/ros/object_list")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/student/Desktop/Redge_Thesis/vil/devel/share/common-lisp/ros/object_list")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/student/Desktop/Redge_Thesis/vil/devel/share/gennodejs/ros/object_list")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/student/Desktop/Redge_Thesis/vil/devel/lib/python2.7/dist-packages/object_list")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/student/Desktop/Redge_Thesis/vil/devel/lib/python2.7/dist-packages/object_list")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/student/Desktop/Redge_Thesis/vil/build/object_list/catkin_generated/installspace/object_list.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/object_list/cmake" TYPE FILE FILES "/home/student/Desktop/Redge_Thesis/vil/build/object_list/catkin_generated/installspace/object_list-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/object_list/cmake" TYPE FILE FILES
    "/home/student/Desktop/Redge_Thesis/vil/build/object_list/catkin_generated/installspace/object_listConfig.cmake"
    "/home/student/Desktop/Redge_Thesis/vil/build/object_list/catkin_generated/installspace/object_listConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/object_list" TYPE FILE FILES "/home/student/Desktop/Redge_Thesis/vil/src/object_list/package.xml")
endif()

