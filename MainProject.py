import numpy as np
import cv2

vidCap = cv2.VideoCapture(0)
ret, frame = vidCap.read()
height, width, sss = frame.shape
print(height, width, sss)

while True:
    ret, frame = vidCap.read()
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #frame = cv2.line(frame, (0,0), (100, 100),(255,0,0),5)
    frame = cv2.circle(frame, (int(width/2), int(height/2)), int(height/2), (255,0,0),5)
    #frame = cv2.rectangle(frame, (10, 10), (30, 30), (0,255,0), 10)
    frame = cv2.flip(frame, 1)
    cv2.imshow('Circle', frame)

    if cv2.waitKey(20) == 27:
        break

vidCap.release()
cv2.destroyAllWindows()
