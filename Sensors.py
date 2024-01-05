from RobokitRS.RobokitRS import *
import time as t

rs = RobokitRS()

rs.port_open("COM5")

def sonar():
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


class Motor():
    #(모터 번호,cw-0 ccw-1, speed)
    #0번-왼앞 1번-오앞, 2-왼뒤 3-오뒤,
    def stop(self):
        rs.motor_stop(0)
        rs.motor_stop(1)
        rs.motor_stop(2)
        rs.motor_stop(3)
     
    def forward(self,speed,tm):
        rs.motor_write(0,1,speed)
        rs.motor_write(1,0,speed)
        rs.motor_write(2,1,speed)
        rs.motor_write(3,0,speed)
        t.sleep(tm)
        self.stop()

    def rightForward(self,speed,tm):
        rs.motor_write(0,1,speed)
        rs.motor_write(1,0,0)
        rs.motor_write(2,1,0)
        rs.motor_write(3,0,speed)
        t.sleep(tm)
        self.stop()

    def leftForward(self,speed,tm):
        rs.motor_write(0,1,0)
        rs.motor_write(1,0,speed)
        rs.motor_write(2,1,speed)
        rs.motor_write(3,0,0)
        t.sleep(tm)
        self.stop()

    def backward(self,speed,tm):
        rs.motor_write(0,0,speed)
        rs.motor_write(1,1,speed)
        rs.motor_write(2,0,speed)
        rs.motor_write(3,1,speed)
        t.sleep(tm)
        self.stop()

    def rightBackward(self,speed,tm):
        rs.motor_write(0,0,0)
        rs.motor_write(1,1,speed)
        rs.motor_write(2,0,speed)
        rs.motor_write(3,1,0)
        t.sleep(tm)
        self.stop()

    def leftBackward(self,speed,tm):
        rs.motor_write(0,0,speed)
        rs.motor_write(1,1,0)
        rs.motor_write(2,0,0)
        rs.motor_write(3,1,speed)
        t.sleep(tm)
        self.stop()

    def right(self,speed,tm):
        rs.motor_write(0,1,speed)
        rs.motor_write(1,1,speed)
        rs.motor_write(2,0,speed)
        rs.motor_write(3,0,speed)
        t.sleep(tm)
        self.stop()

    def left(self,speed,tm):
        rs.motor_write(0,0,speed)
        rs.motor_write(1,0,speed)
        rs.motor_write(2,1,speed)
        rs.motor_write(3,1,speed)
        t.sleep(tm)
        self.stop()

    def uTurnL(self,speed,tm):
        rs.motor_write(0,0,speed)
        rs.motor_write(1,0,speed)
        rs.motor_write(2,0,speed)
        rs.motor_write(3,0,speed)
        t.sleep(tm)
        self.stop()

    def uTurnR(self,speed,tm):
        rs.motor_write(0,1,speed)
        rs.motor_write(1,1,speed)
        rs.motor_write(2,1,speed)
        rs.motor_write(3,1,speed)
        t.sleep(tm)
        self.stop()


def btn():
    rs.set_pin_mode(13,Modes.INPUT)

    while(1):
        btn = rs.digital_read(13)


def gyro():
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
    

def infrared():
    while(1):
        sensor1 = rs.analog_read(0)
        sensor3 = rs.analog_read(1)
        print(sensor1, sensor3)
        t.sleep(0.1)

