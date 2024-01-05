from RoboCam.robocam import *
import time as t

rCam = RoboCam()

rCam.CameraStreamInit()
rCam.CameraStream()
rCam.SketchDetectorInit()
rCam.SketchDetectorStart()

rCam.TrainSketchData("C:/Temp/fd")

while(1):
    rCam.GetSketchNames()
    
    # rCam.SketchCapture('Right', captureCount=100,path="c:/Temp/right")
    #  
# rCam.TrainSketchData("C:/Temp/stop")

# rCam.GetSketchNames()