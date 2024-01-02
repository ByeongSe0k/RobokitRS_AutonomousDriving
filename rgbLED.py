from RobokitRS.RobokitRS import *
import time as t

rs = RobokitRS()

rs.port_open("COM5")

#RGB LED set Color
rs.set_rgb_led_color(12,100,100,100)
rs.set_rgb_led_on(7)
