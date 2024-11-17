import cv2
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow("Image",frame)
    if not ret or( cv2.waitKey(1) & 0xFF == ord('q')):
        break
