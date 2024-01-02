from RobokitRS.RobokitRS import *
import time as t
rs = RobokitRS()

rs.port_open("COM5")

#RGB LED set Color
rs.set_rgb_led_color(7,100,100,100)
rs.set_rgb_led_on(7)
t.sleep(1)
rs.set_rgb_led_off(7)

colors = ['red', 'navy', 'random']

for color in colors:
    if color == 'red':
        rs.set_rgb_led_red(7)
        rs.set_rgb_led_on(7)

    elif color == 'navy':
        rs.set_rgb_led_navy(7)
        rs.set_rgb_led_on(7)

    elif color == 'random':
        rs.set_rgb_led_random(7)
        rs.set_rgb_led_on(7)

    else:
        rs.set_rgb_led_off(7)

t.sleep(1)
rs.set_rgb_led_off(7)
