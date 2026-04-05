# 🚗 Omni3WD Robot (ROS2 + Gazebo)

A simulation and control project for a **3-Wheel Omnidirectional Mobile Robot (Omni3WD)** using **ROS2** and **Gazebo**.

This robot uses three omni wheels placed at **120°** to achieve full omnidirectional motion (x, y, rotation).

---

## 📌 Features

- 🧭 Omnidirectional motion (Holonomic drive)
- 🤖 ROS2-based architecture
- 🌍 Gazebo simulation support
- 📡 Sensor integration (LiDAR / Camera /Imu)
- 🗺️ Compatible with SLAM & Navigation (Nav2)
- 🎮 Teleoperation support

---

## 🧱 System Architecture
    +----------------------+
    |   ROS2 Nodes         |
    |----------------------|
    | cmd_vel (geometry)   |
    | odometry             |
    | sensors              |
    +----------+-----------+
               |
               v
    +----------------------+
    | Omni Kinematics Node |
    +----------------------+
               |
               v
    +----------------------+
    |  Wheel Controllers   |
    +----------------------+
               |
               v
    +----------------------+
    |   Gazebo Simulation  |
    +----------------------+

---

## ⚙️ Requirements

- Ubuntu 24.04
- ROS2 (Humble / Jazzy)
- Gazebo (Fortress / Harmonic)
- colcon build tools

Install ROS2:
```bash
sudo apt update
sudo apt install ros-jazzy-desktop
# Create workspace
mkdir -p ~/omni_ws/src
cd ~/omni_ws/src

# Clone repo
git clone https://github.com/mohmedatwa/Omni3WD.git

# Build
cd ~/omni_ws
colcon build

# Source workspace
source install/setup.bash
