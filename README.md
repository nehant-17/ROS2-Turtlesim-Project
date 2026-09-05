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

```text
myturtlesim_ws/
└── src/
    ├── my_turtlesim_interfaces/
    │   ├── msg/
    │   │   ├── Turtle.msg
    │   │   └── TurtleArray.msg
    │   ├── srv/
    │   │   └── CatchTurtle.srv
    │   ├── CMakeLists.txt
    │   └── package.xml
    │
    ├── my_turtlesim_pkg/
    │   ├── my_turtlesim_pkg/
    │   │   ├── __init__.py
    │   │   ├── turtle_controller.py
    │   │   └── turtle_spawner.py
    │   ├── setup.py
    │   ├── setup.cfg
    │   └── package.xml
    │
    └── my_turtlesim_bringup/
        ├── launch/
        │   └── turtlesim_catch_them_all.launch.xml
        ├── config/
        │   └── catch_them_all_config.yaml
        ├── CMakeLists.txt
        └── package.xml
```
## Installation

Clone the repository:

```bash
git clone https://github.com/nehant-17/ROS2-Turtlesim-Project.git
cd ROS2-Turtlesim-Project
```

Source ROS 2 Jazzy:

```bash
source /opt/ros/jazzy/setup.bash
```

Install dependencies:

```bash
rosdep install --from-paths src --ignore-src -r -y
```

Build the workspace:

```bash
colcon build
```

Source the workspace:

```bash
source install/setup.bash
```

## Run the Project

Launch the complete turtlesim system:

```bash
ros2 launch my_turtlesim_bringup turtlesim_catch_them_all.launch.xml
```
