#Creating an application that allows screen recording and screenshots

#importing following packages:
import datetime
#Allows for inclusion of current date
import cv2
#Allows for image capturing
from PIL import ImageGrab
#Allows for screenshot
import numpy as np
import cv2
from win32api import GetSystemMetrics

print("User can type something here to be displayed on recording or image"[::-1])
#Allows user to print on recording, I added this

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
#Creates even size for recording

timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
filename =  f'{timestamp}.mp4'
print(timestamp)
#This saves the recorded video with a timestamp of time of recording, including time in hours, minutes and seconds

Screen_Size = (2000, 1000)
fourcc = cv2.VideoWriter_fourcc("m","p","4","v")
Captured_video = cv2.VideoWriter_fourcc("oputput.mp4", fourcc, 20.0,(width,height))
fps = 30
#this allows for 30 frames per second during the recording and also gives the size of the recording screen

webcam=cv2.VideoCapture(0)
#this allows for the vidoe capture to include webcam

print(width,height)

while True:
    image =ImageGrab(bbox=(0,0,width,height ))
    imgnp=np.array(image)
    imagefinal=cv2.cvtColor(imgnp, cv2.COLOR_BG2RGB)
    _, frame = webcam.read()
    frheight, frwidth, _, = frame.shape
    imagefinal[0: frheight, 0:frwidth,:] = frame [0:frheight, 0:frwidth, :]
    cv2.imageshow("Capture",imgnp)
    cv2.imageshow('webcam', frame)
    captured_video.write(imagefinal)
    if cv2.waitKey(10)==ord("q"):
        break
        #this allows user to press q key to stop recording

cv2.destroyAllWindows()
captured_video.release()
