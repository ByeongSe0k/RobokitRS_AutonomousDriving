from RobokitRS.RobokitRS import *
import time as t

rs = RobokitRS()
rs.port_open("COM5")

rs.set_pin_mode(13,Modes.INPUT)

def btn():
    while(1):
        btn = rs.digital_read(13)

def main():
    btn()

if(__name__=="__main__"):
    main()