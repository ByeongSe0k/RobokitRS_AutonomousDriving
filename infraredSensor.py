from RobokitRS.RobokitRS import *
import time as t

rs = RobokitRS()

rs.port_open("COM5")

while(1):
    sensor1 = rs.analog_read(0)
    sensor3 = rs.analog_read(1)
    print(sensor1, sensor3)
    t.sleep(0.2)


