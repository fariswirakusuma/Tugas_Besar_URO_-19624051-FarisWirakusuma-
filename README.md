# Tugas_Besar_URO_-19624051-FarisWirakusuma
Video Penjelasan ada di dalam RAR

-- LIST COMMAND PROGRAM:

SOURCING:
source install/setup.bash
source /opt/ros/humble/setup.bash
source ~/ros2_humble_ws/install/setup.bash
source ~/.bashrc
source /usr/share/gazebo/setup.sh

BUILD_PROJEKNYA:
colcon build
colcon build --symlink-install

LAUNCHER:
ros2 launch package_tubes_uro launch_robot_in_rviz.launch.py
ros2 launch package_tubes_uro launch_robot_in_gazebo.launch.py --
