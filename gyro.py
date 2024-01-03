from RobokitRS.RobokitRS import *
import time as t

rs = RobokitRS()

rs.port_open("COM5")

rs.gyro_begin()
rs.set_gyro_default_position(0)


while(1):
    angleX = rs.gyro_read(GyroDataType.ANGLE_X)
    angleY = rs.gyro_read(GyroDataType.ANGLE_Y)
    angleZ = rs.gyro_read(GyroDataType.ANGLE_Z)
    gyroX = rs.gyro_read(GyroDataType.GYRO_X)
    gyroY = rs.gyro_read(GyroDataType.GYRO_Y)
    gyroZ = rs.gyro_read(GyroDataType.GYRO_Z)
    shake = rs.gyro_read(GyroDataType.SHAKE)
    t.sleep(0.02)

    

    print("(",angleX, angleY, angleZ,")","(",gyroX, gyroY, gyroZ,")","(",shake,")")
