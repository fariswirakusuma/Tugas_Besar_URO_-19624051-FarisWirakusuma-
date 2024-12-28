cmake_minimum_required(VERSION 3.5)
project(package_tubes_uro)

# Find dependencies
set(ament_cmake_DIR "/opt/ros/humble/share/ament_cmake/cmake")
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(urdf REQUIRED) 
#find_package(xacro REQUIRED)  # If you want to process xacro files

# Add executable for your C++ file
add_executable(urdf_example_node src/urdf_example_node.cpp)

# Link libraries
ament_target_dependencies(urdf_example_node rclcpp urdf)

# Install executables
install(TARGETS
  urdf_example_node
  DESTINATION lib/${PROJECT_NAME}
)

install(
  DIRECTORY launch urdf worlds
  DESTINATION share/${PROJECT_NAME}
)


ament_package()
