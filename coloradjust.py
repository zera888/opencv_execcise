import  cv2
import numpy as np

def empty(v):
    pass

img=cv2.imread('789.jpg')
img=cv2.resize(img,(0,0),fx=0.8, fy=0.8)

cv2.namedWindow('TrackBar')
cv2.resizeWindow('TrackBar',640,320)

cv2.createTrackbar('Hue min', 'TrackBar', 0, 179, empty)
cv2.createTrackbar('Hue max', 'TrackBar', 179, 179, empty)
cv2.createTrackbar('Sat min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Sat max', 'TrackBar', 255, 255, empty)
cv2.createTrackbar('Val min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Val max', 'TrackBar', 255, 255, empty)

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

while True:
    h_min = cv2.getTrackbarPos('Hue min', 'TrackBar')
    h_max = cv2.getTrackbarPos('Hue max', 'TrackBar')
    s_min = cv2.getTrackbarPos('Sat min', 'TrackBar')
    s_max = cv2.getTrackbarPos('Sat max', 'TrackBar')
    v_min = cv2.getTrackbarPos('Val min', 'TrackBar')
    v_max = cv2.getTrackbarPos('Val max', 'TrackBar')
    print(h_min,h_max,s_min,s_max,v_min,v_max)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    mask = cv2.inRange(hsv,lower,upper)
    result = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow('img', img)
    cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('result',result)
    cv2.waitKey(1)

