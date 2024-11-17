import HandTrackingModule as htm
import cv2
import numpy as np
cap = cv2.VideoCapture(0)
detector = htm.HandDetector()
def isOpen(fingerTip,lmList):
    p1 = lmList[0][1:]
    p2 = lmList[fingerTip-2][1:]
    p3 = lmList[fingerTip][1:]
    line1_point1 = np.array(p1)
    line1_point2 = np.array(p2)
    line2_point1 = np.array(p2)
    line2_point2 = np.array(p3)
    vector1 = line1_point2 - line1_point1 
    vector2 = line2_point2 - line2_point1 
    dot_product = np.dot(vector1, vector2)
    magnitude_vector1 = np.linalg.norm(vector1)
    magnitude_vector2 = np.linalg.norm(vector2)
    cos_angle = dot_product / (magnitude_vector1 * magnitude_vector2)
    angle_rad = np.arccos(np.clip(cos_angle, -1.0, 1.0)) 
    angle_deg = np.degrees(angle_rad)
    if fingerTip == 4:
        return angle_deg < 60

    return angle_deg<90
while True:
    success,img = cap.read()
    w,h,c = img.shape
    img = cv2.flip(img,1)
    if not success or cv2.waitKey(1)&0xFF == ord('q'):
        break
    lmList = detector.findPosition(img,draw=False)
    fingerCount = 0
    if lmList:
        if isOpen(4,lmList):#Thumb finger is Open
            fingerCount += 1
        if isOpen(8,lmList):#Index finger is Open
            fingerCount += 1
        if isOpen(12,lmList):#Middle finger is Open
            fingerCount += 1
        if isOpen(16,lmList):#Ring finger is Open
            fingerCount += 1
        if isOpen(20,lmList):#Pinky finger is Open
            fingerCount += 1
    cv2.putText(img,"FingersCount: "+str(fingerCount),(20,70),2,2,(255,0,0),2)
    cv2.imshow("Image",img)
