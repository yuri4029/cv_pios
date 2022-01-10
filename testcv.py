"""


"""
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import cv2
import time
"""
    img = cv2.imread('/home/pi/Desktop/img2.jpg',0)
"""
camera = PiCamera()
rawCapture = PiRGBArray(camera)

time.sleep(0.1)

camera.capture(rawCapture, format="rgb")
image = rawCapture.array

cv2.imshow("Image", image)
cv2.waitKey(0)