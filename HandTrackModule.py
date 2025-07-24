import cv2
import mediapipe as mp
import time
class handDetector():
    def __init__(self,mode=False,maxHands=2,detectionCon=0.5,trackCon=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.trackCon=trackCon
        self.mpHands=mp.solutions.hands
        self.hands=self.mpHands.Hands()
        self.mpDraw=mp.solutions.drawing_utils
    def findHands(self,img,draw=True):
        imgRgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.result=self.hands.process(imgRgb)
        if self.result.multi_hand_landmarks:
            for handlmk in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handlmk, self.mpHands.HAND_CONNECTIONS)
        return img
    def findPosition(self,img,handNo=0,draw=True):
        lmList=[]
        if self.result.multi_hand_landmarks:
            myHand=self.result.multi_hand_landmarks[handNo]
            for id, lmk in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int((lmk.x * w)), int((lmk.y * h))
                lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx, cy), 25, (255, 255, 0), cv2.FILLED)
        return lmList
    def drawCircle(self,img,lmk):
        lmList = []
        if self.result.multi_hand_landmarks:
            for handlmk in self.result.multi_hand_landmarks:
                for id, lmk in enumerate(handlmk.landmark):
                    h, w, c = img.shape
                    cx, cy = int((lmk.x * w)), int((lmk.y * h))
                    lmList.append([id, cx, cy])
                    if id==lmk:
                        cv2.circle(img, (cx, cy), 25, (255, 255, 0), cv2.FILLED)

def main():
    capture = cv2.VideoCapture(0)
    prevTime = 0
    cTime=0
    detector=handDetector()
    while True:
        success,img=capture.read()
        img=detector.findHands(img)
        lmkList=detector.findPosition(img,0)
        if len(lmkList) !=0:
            print(lmkList[4])
        cTime = time.time()
        fps=1/(cTime-prevTime)
        prevTime=cTime
        cv2.putText(img,str(int(fps)),(100,140),cv2.FONT_HERSHEY_SIMPLEX,3,(255,0,255),3)
        cv2.imshow('image', img)
        cv2.waitKey(1)
if __name__ == "__main__":
    main()