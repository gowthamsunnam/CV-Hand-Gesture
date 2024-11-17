import mediapipe as mp
import cv2
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
myhands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
while True:
    success,frame = cap.read()
    RGB_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = myhands.process(RGB_frame)
    if results.multi_hand_landmarks:
        for each_hand in  results.multi_hand_landmarks:
            for id,landmark in  enumerate(each_hand.landmark):
                h,w,c = frame.shape
                cx,cy = int(landmark.x*w),int(landmark.y*h)
                print(id,cx,cy)
                if id == 8:
                    cv2.circle(frame,(cx,cy),20,(255,255,255),cv2.FILLED)
            mpDraw.draw_landmarks(frame,each_hand,mpHands.HAND_CONNECTIONS)
    cv2.imshow("Image",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

