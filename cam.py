from RoboCam.robocam import*
import time as t

rCam = RoboCam()

#무선카메라
# rCam.CameraStreamInit()
# rCam.FacedetectorInit()

# while(1):
#     rCam.CameraStream()
#     rCam.FacedetectorStart()

    #faceCapture
    #rCam.FaceCapture("lee",5,"c:/Temp/face")
    

#노트북 카메라
rCam.WebcamStreamInit()
rCam.FacedetectorInit()
rCam.ArucoDetectorInit()
while(1):
    rCam.ArucoDetectorStart()
    rCam.WebcamStream()
    # rCam.FacedetectorStart()
    #image capture
#     rCam.FaceCapture("lee",5,"c:/Temp/face")
    rCam.GetFaceNames()

#image train
# rCam.TrainFaceData(facePath="c:/Temp/face")
