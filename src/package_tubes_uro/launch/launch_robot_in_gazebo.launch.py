from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, LogInfo
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition, UnlessCondition
from ament_index_python.packages import get_package_share_directory
import xacro
import os

def generate_launch_description():
    # Declare GUI argument
    gui = LaunchConfiguration('gui', default='false')

    # Robot spawn coordinates
    spawn_x_val = '0.0'
    spawn_y_val = '0.0'
    spawn_z_val = '0.0'
    spawn_yaw_val = '0.00'
    
    robotXacroName = 'robot_tubes_uro'
    name_package = 'package_tubes_uro'
    
    # URDF and world file paths
    urdf_file_relative_path = 'urdf/robot_tubes_uro_gazebo.urdf.xacro'
    world_path_relative_path = 'worlds/empty.world'
    
    urdf_path = os.path.join(get_package_share_directory(name_package), urdf_file_relative_path)
    world_path = os.path.join(get_package_share_directory(name_package), world_path_relative_path)

    # Process XACRO to URDF
    robot_description = xacro.process_file(urdf_path).toxml()

    # Gazebo launch file (gzserver + gzclient)
    gazebo_ros_launch = PythonLaunchDescriptionSource(
        os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
    )
    gazebo_launch = IncludeLaunchDescription(gazebo_ros_launch, launch_arguments={'world': world_path}.items())

    # Spawn model node
    spawn_model_node = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', robotXacroName, '-topic', 'robot_description',
                   '-x', spawn_x_val, '-y', spawn_y_val, '-z', spawn_z_val, '-Y', spawn_yaw_val],
        output='screen'
    )

    # Robot state publisher node
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description, 'use_sim_time': True}],
        output='screen'
    )

    # Joint state publisher node
    start_joint_state_publisher_cmd = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        condition=UnlessCondition(gui),
    )

    # Create the LaunchDescription
    launch_description = LaunchDescription()

    # Add actions to the launch description
    launch_description.add_action(gazebo_launch)  # Include Gazebo
    launch_description.add_action(spawn_model_node)
    launch_description.add_action(robot_state_publisher_node)
    launch_description.add_action(start_joint_state_publisher_cmd)

    # Return the LaunchDescription
    return launch_description
