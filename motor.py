from RobokitRS.RobokitRS import *
import time as t
rs = RobokitRS()

rs.port_open("COM5")

#(모터 번호,cw-0 ccw-1, speed)

#0번-왼앞 1번-오앞, 2-왼뒤 3-오뒤, 
def forward(speed,tm):
    rs.motor_write(0,1,speed)
    rs.motor_write(1,0,speed)
    rs.motor_write(2,1,speed)
    rs.motor_write(3,0,speed)
    t.sleep(tm)
    stop()

def rightForward(speed,tm):
    rs.motor_write(0,1,speed)
    rs.motor_write(1,0,0)
    rs.motor_write(2,1,0)
    rs.motor_write(3,0,speed)
    t.sleep(tm)
    stop()

def leftForward(speed,tm):
    rs.motor_write(0,1,0)
    rs.motor_write(1,0,speed)
    rs.motor_write(2,1,speed)
    rs.motor_write(3,0,0)
    t.sleep(tm)
    stop()

def backward(speed,tm):
    rs.motor_write(0,0,speed)
    rs.motor_write(1,1,speed)
    rs.motor_write(2,0,speed)
    rs.motor_write(3,1,speed)
    t.sleep(tm)
    stop()

def rightBackward(speed,tm):
    rs.motor_write(0,0,0)
    rs.motor_write(1,1,speed)
    rs.motor_write(2,0,speed)
    rs.motor_write(3,1,0)
    t.sleep(tm)
    stop()

def leftBackward(speed,tm):
    rs.motor_write(0,0,speed)
    rs.motor_write(1,1,0)
    rs.motor_write(2,0,0)
    rs.motor_write(3,1,speed)
    t.sleep(tm)
    stop()

def right(speed,tm):
    rs.motor_write(0,1,speed)
    rs.motor_write(1,1,speed)
    rs.motor_write(2,0,speed)
    rs.motor_write(3,0,speed)
    t.sleep(tm)
    stop()

def left(speed,tm):
    rs.motor_write(0,0,speed)
    rs.motor_write(1,0,speed)
    rs.motor_write(2,1,speed)
    rs.motor_write(3,1,speed)
    t.sleep(tm)
    stop()

def uTurnL(speed,tm):
    rs.motor_write(0,0,speed)
    rs.motor_write(1,0,speed)
    rs.motor_write(2,0,speed)
    rs.motor_write(3,0,speed)
    t.sleep(tm)
    stop()

def uTurnR(speed,tm):
    rs.motor_write(0,1,speed)
    rs.motor_write(1,1,speed)
    rs.motor_write(2,1,speed)
    rs.motor_write(3,1,speed)
    t.sleep(tm)
    stop()

def stop():
    rs.motor_stop(0)
    rs.motor_stop(1)
    rs.motor_stop(2)
    rs.motor_stop(3)

if __name__=="__main__":
    speed = 15
    tm = 2

    
    
    forward(speed,tm)
    leftForward(speed,tm)
    forward(speed,tm-0.5)
    left(speed,tm+2)
    backward(speed,tm)
    rightBackward(speed,tm)
    backward(speed,tm-1.5)
    uTurnR(speed,tm-1.5)
    rightForward(speed,1)


   
