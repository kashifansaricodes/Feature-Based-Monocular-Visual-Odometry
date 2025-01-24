# Feature-based-Monocular-Visual-Odometry

# Visual Odometry with KITTI Dataset

## Overview
This Visual Odometry project implements a computer vision technique for estimating camera trajectory by tracking feature points across consecutive image frames from the KITTI dataset. Using OpenCV's advanced image processing algorithms, the system detects and tracks visual features, computes camera pose changes through essential matrix decomposition, and reconstructs 3D motion with ground truth scale integration, providing real-time visualization of camera movement through a scene.

![Screenshot from 2025-01-24 11-51-01](https://github.com/user-attachments/assets/43821acc-a6ff-48c7-abba-1674fd124742)

![Screenshot from 2025-01-24 11-49-24](https://github.com/user-attachments/assets/8000836d-f17a-4002-8a6e-0878fb28952d)

## Video Demonstration <<<
[Watch Project Demonstration](https://drive.google.com/file/d/17V9M7m_ldSC8W2JBr6J97VvN86amLDRw/view?usp=sharing)

## Prerequisites
- OpenCV
- CMake
- C++17 compatible compiler

## Camera Coordinate System
Detailed information about camera coordinate systems can be found at:
https://de.mathworks.com/help/vision/gs/coordinate-systems.html

## Steps

### Dataset Preparation
- Download KITTI grayscale dataset
- Place dataset inside `kitti_dataset` directory
- Dataset sources:
  - Image dataset: [KITTI Grayscale Dataset](https://www.cvlibs.net/datasets/kitti/eval_odometry.php)
  - Ground truth: KITTI odometry ground truth poses

### Compilation and Execution
```bash
mkdir build && cd build
cmake ..
make
./visual_odometry
```

## Algorithm Workflow

![Screenshot from 2025-01-24 10-31-00](https://github.com/user-attachments/assets/65931d54-9c5b-40e2-8b75-5452f4af04d4)


1. Feature Detection (FAST algorithm)
2. Feature Tracking (Optical Flow)
3. Essential Matrix Computation
4. Camera Pose Recovery
5. Trajectory Estimation

## Dependencies
- OpenCV
- Standard C++ Filesystem Library

## Output
- Real-time camera trajectory visualization
- Current camera coordinates display

## Acknowledgments
- KITTI Dataset
- OpenCV Library
