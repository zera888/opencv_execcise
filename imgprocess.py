import random

import cv2
import numpy as np
import random

img=cv2.imread('47514.jpg')
#img=np.empty((300,300,3),np.uint8)
newimg=img[100:320,100:500]

#for row in range(300):
#    for col in range(300) :
#        img[row][col]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))

cv2.imshow('img',img)
cv2.imshow('newimg',newimg)
cv2.waitKey(0)