import cv2
import  numpy as np

cap = cv2.VideoCapture(0)

# Blue, Green, yellow  red
penColorHSV = [[112,123,92,162,255,255],
               [28,116,100,179,255,255],
               [20,80,127,155,255,255],
               [0,130,134,179,220,248]]

penColorBGR = [[255, 0, 0],
               [0, 255, 0],
               [0, 255, 255],
               [0,0,255]]

#{x,y,colorid}
drawpoints = []

def findpen(img):
    ret,img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    for i in range (len(penColorHSV)):
        lower = np.array(penColorHSV[i][:3])
        upper = np.array(penColorHSV[i][3:6])

        mask = cv2.inRange(hsv,lower,upper)
        result = cv2.bitwise_and(img,img,mask=mask)
        penx,peny = findcontour(mask)
        cv2.circle(imgContour,(penx,peny), 10, penColorBGR[i], cv2.FILLED)
        if peny != -1 :
            drawpoints.append([penx,peny,i])
        # cv2.imshow('result',result)

def findcontour(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 取輪廓外型
    x,y,w,h = -1,-1,-1,-1
    for cnt in contours:
        #cv2.drawContours(imgContour, cnt, -1, (255, 255, 255), 4)
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt, True)  # 邊長
            vertices = cv2.approxPolyDP(cnt, peri * 0.02, True)  # 取多邊形的頂點
            x, y, w, h = cv2.boundingRect(vertices)
    return x+w//2,y

def draw(drawpoints):
    for point in drawpoints :
        cv2.circle(imgContour, (point[0], point[1]), 10, penColorBGR[point[2]], cv2.FILLED)

cap=cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    if ret:
        imgContour = frame.copy()
        cv2.imshow('Video',frame)
        findpen(frame)
        draw(drawpoints)
        cv2.imshow('contour',imgContour)
    else:
        break
    if cv2.waitKey(1) == ord('q'):
        break

        cv2.w