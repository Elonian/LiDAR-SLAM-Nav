import numpy as np
import os
import constants as const
from collections import defaultdict


def load_data(dataset: int = 20) -> defaultdict:
    data = defaultdict(dict)
    data["dataset"] = dataset

    # Load Encoders
    encoder_file = const.ENCODER.FILE_TEMPLATE % dataset
    if os.path.exists(encoder_file):
        with np.load(encoder_file) as enc_data:
            data["encoder"] = {
                "encoder_counts": enc_data[const.ENCODER.COUNTS],      # 4 x n encoder counts
                "encoder_stamps": enc_data[const.ENCODER.STAMPS]    # encoder time stamps
            }
    else:
        print(f"File {encoder_file} not found.")

    # Load Lidar
    lidar_file = const.LIDAR.FILE_TEMPLATE % dataset
    if os.path.exists(lidar_file):
        with np.load(lidar_file) as lidar_data:
            data["lidar"] = {
                "lidar_angle_min": lidar_data[const.LIDAR.ANGLE_MIN],            # start angle of the scan [rad]
                "lidar_angle_max": lidar_data[const.LIDAR.ANGLE_MAX],            # end angle of the scan [rad]
                "lidar_angle_increment": lidar_data[const.LIDAR.ANGLE_INCREMENT],# angular distance between measurements [rad]
                "lidar_range_min": lidar_data[const.LIDAR.RANGE_MIN],            # minimum range value [m]
                "lidar_range_max": lidar_data[const.LIDAR.RANGE_MAX],            # maximum range value [m]
                "lidar_ranges": lidar_data[const.LIDAR.RANGES],                  # range data [m]
                "lidar_stamps": lidar_data[const.LIDAR.STAMPS]              # acquisition times of the lidar scans
            }
    else:
        print(f"File {lidar_file} not found.")

    # Load IMU
    imu_file = const.IMU.FILE_TEMPLATE % dataset
    if os.path.exists(imu_file):
        with np.load(imu_file) as imu_data:
            data["imu"] = {
                "imu_angular_velocity": imu_data[const.IMU.ANGULAR_VELOCITY],      # angular velocity in rad/sec
                "imu_linear_acceleration": imu_data[const.IMU.LINEAR_ACCELERATION],# accelerations in gs
                "imu_stamps": imu_data[const.IMU.STAMPS]                      # acquisition times of the imu measurements
            }
    else:
        print(f"File {imu_file} not found.")

    # Load Kinect
    kinect_file = const.KINECT.FILE_TEMPLATE % dataset
    if os.path.exists(kinect_file):
        with np.load(kinect_file) as kinect_data:
            data["kinect"] = {
                "disp_stamps": kinect_data[const.KINECT.DISP_STAMPS], # acquisition times of the disparity images
                "rgb_stamps": kinect_data[const.KINECT.RGB_STAMPS]         # acquisition times of the rgb images
            }
    else:
        print(f"File {kinect_file} not found.")

    return data