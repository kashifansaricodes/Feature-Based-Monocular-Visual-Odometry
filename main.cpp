/**
 * @file main.cpp
 * @brief Entry point for the monocular visual odometry application.
 *
 * This file contains the main function which initializes and runs the visual odometry algorithm.
 */

#include "vo.h"
#include <filesystem>

/**
 * @brief Main function to run the visual odometry algorithm.
 *
 * This function sets up the dataset path and initializes the VisualOdometry object.
 * It then runs the visual odometry algorithm on the specified image set.
 *
 * @param argc Number of command-line arguments.
 * @param argv Array of command-line arguments.
 * @return int Returns 0 on successful execution, or an error code otherwise.
 */
int main(int argc, char **argv)
{
  // Initialize the VisualOdometry object
  VisualOdometry vo;

  // Define the path to the dataset
  std::filesystem::path dataset_path = std::filesystem::current_path() / "../kitti_dataset" / "data_odometry_gray";
  std::filesystem::path imageset_path = dataset_path / "dataset/sequences/00/";

  // Run the visual odometry algorithm on the specified image set
  int ret = vo.run(imageset_path.string());

  // Return the result of the visual odometry algorithm
  return ret;
}
