from RobokitRS.RobokitRS import *
import time as t

rs = RobokitRS()

rs.port_open("COM5")

#set led red, led on
rs.set_rgb_led_red(7)
rs.set_rgb_led_on(7)

rs.sonar_begin(13)

while 1:
    SONAR = rs.sonar_read(13)
    t.sleep(0.2)
    if(SONAR < 20):
        break
rs.set_rgb_led_off(7)

