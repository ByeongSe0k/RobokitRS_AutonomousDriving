from RobokitRS.RobokitRS import *
import time as t

rs = RobokitRS()

rs.port_open("COM5")

#set led red, led on
rs.set_rgb_led_red(7)
rs.set_rgb_led_on(7)


rs.sonar_begin(12)

while 1:
    t.sleep(0.2)
    SONAR = rs.sonar_read(12)

    if(SONAR == 0 or SONAR == 508): 
        print(SONAR)
        continue
    
    if(5 <= SONAR < 25):
        rs.set_rgb_led_red(7)

    elif(25 < SONAR < 100):
        rs.set_rgb_led_orange(7)
    
    elif(SONAR >=100):
        rs.set_rgb_led_green(7)

rs.set_rgb_led_off(7)

