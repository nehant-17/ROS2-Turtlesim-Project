# ROS 2 Turtlesim Project

A ROS 2 turtlesim project demonstrating custom messages, custom services, turtle spawning, and automatic turtle control.

## Features

- Custom ROS 2 messages
- Custom ROS 2 service
- Automatic turtle spawning
- Turtle controller
- Closest-turtle-first behavior
- Launch file for the complete system
- YAML configuration

## Requirements

- Ubuntu 24.04
- ROS 2 Jazzy
- Python 3
- turtlesim

## Project Structure

myturtlesim_ws/
└── src/
    ├── my_turtlesim_interfaces/
    │   ├── msg/
    │   │   ├── Turtle.msg
    │   │   └── TurtleArray.msg
    │   └── srv/
    │       └── CatchTurtle.srv
    │
    ├── my_turtlesim_pkg/
    │   └── my_turtlesim_pkg/
    │       ├── turtle_controller.py
    │       └── turtle_spawner.py
    │
    └── my_turtlesim_bringup/
        ├── launch/
        │   └── turtlesim_catch_them_all.launch.xml
        └── config/
            └── catch_them_all_config.yaml

## Installation

Clone the repository:

```bash
git clone https://github.com/nehant-17/ROS2-Turtlesim-Project.git
cd ROS2-Turtlesim-Project

