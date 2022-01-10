import time
import picamera

with picamera.PiCamera() as camera :
    
    
    '''
    image
    
    camera.resolution = (1024,768)
    camera.start_preview()
    time.sleep(2)
    camera.capture ('/home/pi/cv_/img2.jpg',0)
    '''
    
    camera.resolution = (640,480)
    camera.start_recording('/home/pi/cv_/minh1.h264')
    camera.wait_recording(60)
    camera.stop_recording()