import cv2
import numpy as np
import pylab as pl


def read(filename):

    capture = cv2.VideoCapture(filename)

    while(True):
        success, frame = capture.read()
        
	pl.figure(1)
	pl.title("red")
	pl.hist(frame[:,:,0])	

	pl.figure(2)
	pl.title("green")
	pl.hist(frame[:,:,1])	
	
	pl.figure(3)
	pl.title("blue")
	pl.hist(frame[:,:,2])	
	
	pl.figure(4)
	pl.imshow(frame, interpolation="nearest")
	pl.show()
	


read("./data/legostein.mp4")




 
