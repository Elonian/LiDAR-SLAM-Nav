import numpy as np

class ENCODER:
    FILE_TEMPLATE = "data/Encoders%d.npz"
    COUNTS = "counts"
    STAMPS = "time_stamps"

class LIDAR:
    FILE_TEMPLATE = "data/Hokuyo%d.npz"
    ANGLE_MIN = "angle_min"
    ANGLE_MAX = "angle_max"
    ANGLE_INCREMENT = "angle_increment"
    RANGE_MIN = "range_min"
    RANGE_MAX = "range_max"
    RANGES = "ranges"
    STAMPS = "time_stamps"

class IMU:
    FILE_TEMPLATE = "data/Imu%d.npz"
    ANGULAR_VELOCITY = "angular_velocity"
    LINEAR_ACCELERATION = "linear_acceleration"
    STAMPS = "time_stamps"

class KINECT:
    FILE_TEMPLATE = "data/Kinect%d.npz"
    DISP_STAMPS = "disparity_time_stamps"
    RGB_STAMPS = "rgb_time_stamps"

class DDR:
    L = 0.0022

class MAP:
    MIN = np.array([-30, -30])
    MAX =  np.array([30, 30])
    RES = 0.05
    SIZE = np.int32((MAX - MIN) / RES + 1)
    MAP = np.zeros(SIZE)

class MAP2:
    RES = np.array([0.05, 0.05])    
    MIN = np.array([-20.0, -20.0])  
    MAX = np.array([30.0, 30.0])    
    SIZE = np.ceil((MAX - MIN) / RES).astype(int)
    is_even = SIZE % 2 == 0
    SIZE[is_even] += 1
    MAP = np.zeros((SIZE[0], SIZE[1], 3))
