# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_package_tubes_uro_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED package_tubes_uro_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(package_tubes_uro_FOUND FALSE)
  elseif(NOT package_tubes_uro_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(package_tubes_uro_FOUND FALSE)
  endif()
  return()
endif()
set(_package_tubes_uro_CONFIG_INCLUDED TRUE)

# output package information
if(NOT package_tubes_uro_FIND_QUIETLY)
  message(STATUS "Found package_tubes_uro: 0.0.0 (${package_tubes_uro_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'package_tubes_uro' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${package_tubes_uro_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(package_tubes_uro_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${package_tubes_uro_DIR}/${_extra}")
endforeach()
