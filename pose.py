import cv2 as cv
import numpy as np
import mediapipe-rp4 as mp

cap = cv.VideoCapture(0)

mp_pose = mp.solutions.pose
mpDraw = mp.solutions.drawing_utils
pose = mp_pose.Pose()

while True :
    ret, frame = cap.read()
    flipped = cv.flip(frame,flipCode = -1)
    frame1 = cv.resize(flipped,(640,480))
    cv.imshow('Frame',frame1)
    
cap.release()
cv.destroyAllWindows()