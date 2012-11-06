import cv2
import numpy as np
import pylab as pl

def hist(image):

    histogram = np.zeros(256, dtype=np.int32)

    for x in xrange(image.shape[0]):
        for y in xrange(image.shape[1]):
            histogram[image[x, y]] += 1
    
    return histogram

def read(filename):

    capture = cv2.VideoCapture(filename)

    images = [cv2.resize(capture.read()[1], (32, 32)) for count in xrange(9)]
    
    print len(images)
    
    for color in xrange(3):
        hists = [hist(images[count][:,:,color]) for count in xrange(9)]
        print hists

read("./data/legostein.mp4")




 
