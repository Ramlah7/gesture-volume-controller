import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm
import math
wcam,hcam=640,480
import numpy as np

capture=cv2.VideoCapture(0)
capture.set(3,wcam)
capture.set(4,hcam)
prevTime=0
detector=htm.handDetector(detectionCon=0.7)

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities,IAudioEndpointVolume
devices=AudioUtilities.GetSpeakers()
interface=devices.Activate(
    IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
volume=cast(interface,POINTER(IAudioEndpointVolume))
#volume.GetMute()
#volume.GetMasterVolumeLevel()
VolumeRange=volume.GetVolumeRange()
MinVolume=VolumeRange[0]
MAxVolume=VolumeRange[1]
volume.SetMasterVolumeLevel(-20,None)

while True:
    curTime=time.time()
    fps=1/(curTime-prevTime)
    prevTime=curTime
    success,img=capture.read()
    img=detector.findHands(img)
    lmklist=detector.findPosition(img,draw=False)
    if len(lmklist)!=0:
        #print(lmklist[4],lmklist[8])
        x1,y1=lmklist[4][1],lmklist[4][2]
        x2,y2=lmklist[8][1],lmklist[8][2]
        cx,cy=(x1+x2)//2,(y1+y2)//2

        cv2.circle(img,(x1,y1),10,(128,0,0),cv2.FILLED)
        cv2.circle(img,(x2,y2),10,(128,0,0),cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(130,0,75),3)

        length=math.hypot(x2-x1,y2-y1)
        print(length)
        if length<40:
            color=(0,255,0)
        else:
            color=(255,0,111)
        cv2.circle(img, (cx, cy), 7, color, cv2.FILLED)

        vol=np.interp(length,[50,300],[MinVolume,MAxVolume])
        print(f'length = {length} volume = {vol}')
        volume.SetMasterVolumeLevel(vol,None)

        y_center = 380
        x_start = 480
        bars=[20,40,60,80,100]
        for i,threshold in enumerate(bars):
            vols=np.interp(vol,[MinVolume,MAxVolume],[0,100])
            width = 20 + i * 6
            height = 10 + i * 4
            y1 = y_center - height // 2
            x1 = x_start + sum([20 + j * 6 + 5 for j in range(i)])  # stack right with spacing
            x2 = x1 + width
            y2 = y1 + height
            if vols >= threshold:
                color=(34, 34, 178)
            else:
                color=(50,50,50)

            cv2.rectangle(img, (x1, y1), (x2, y2), color, cv2.FILLED)

    cv2.putText(img,f'FPS: {int(fps)}',(40,50),cv2.FONT_HERSHEY_PLAIN,2,(87, 86, 79),2)
    cv2.imshow('image',img)
    cv2.waitKey(1)