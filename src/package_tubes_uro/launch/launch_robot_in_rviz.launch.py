import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
import os

def generate_launch_description():
    # Define launch configurations
    gui_arg = LaunchConfiguration('gui')
    model_arg = LaunchConfiguration('model')

    # Find package share directory
    pkg_share = FindPackageShare(package='package_tubes_uro').find('package_tubes_uro')

    # Specify the default URDF file path
    default_urdf_path = os.path.join(pkg_share, 'urdf', 'robot_tubes_uro.urdf')

    # Read the URDF file (with error handling)
    try:
        with open(default_urdf_path, 'r') as urdf_file:
            robot_desc = urdf_file.read()
    except FileNotFoundError:
        raise RuntimeError(f"URDF file not found at {default_urdf_path}")

    # Define parameters
    params = {'robot_description': robot_desc}

    # Create Nodes
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params]
    )

    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        parameters=[params],
        condition=UnlessCondition(gui_arg)
    )

    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        output='screen',
        condition=IfCondition(gui_arg)
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )

    # Return Launch Description
    return LaunchDescription([
        DeclareLaunchArgument(
            name='gui',
            default_value='true',
            description='Flag to enable joint_state_publisher_gui'
        ),
        DeclareLaunchArgument(
            name='model',
            default_value=default_urdf_path,
            description='Path to the URDF model file'
        ),
        robot_state_publisher_node,
        joint_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz_node
    ])
