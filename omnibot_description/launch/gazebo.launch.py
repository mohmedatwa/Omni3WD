#!/usr/bin env python3
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.parameter_descriptions import ParameterValue
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory
import os


def generate_launch_description():
    omnibot_description_dir = get_package_share_directory("omnibot_description")
    model_arg = DeclareLaunchArgument(
        name="model",
        default_value= os.path.join(omnibot_description_dir,"urdf","omnibot.xacro"),
        description="Path to robot urdf file"
    )
    robot_description =ParameterValue(Command(["xacro ", LaunchConfiguration("model")]),value_type=str)

    robot_state_pub_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description":robot_description}]
    )
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory("ros_gz_sim"), "launch"), "/gz_sim.launch.py"]),
                launch_arguments=[
                    ("gz_args", [" -v 4", " -r", " empty.sdf"]
                    )
                ]
             )
    gz_spawn_entity = Node(
        package="ros_gz_sim",
        executable="create",
        output="screen",
        arguments=["-topic", "robot_description",
                   "-name", "omnibot"],
    )

    gz_bridge = Node(
    package="ros_gz_bridge",
    executable="parameter_bridge",
    parameters=[{"config_file": os.path.join(omnibot_description_dir,"config","ros_gz_bridge.yaml")}],
    output="screen"
        
    )

    rviz_node = Node(

        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=("-d",os.path.join(omnibot_description_dir,"rviz", "display.rviz"))
    )

    return LaunchDescription([
        model_arg,
        robot_state_pub_node,
        gazebo,
        gz_spawn_entity,
        gz_bridge,
        rviz_node,
        
    ])