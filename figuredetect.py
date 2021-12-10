
import cv2


img = cv2.imread('qqq.jpg')
imgContour = img.copy()
img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
canny = cv2.Canny(img, 150, 200)  #取輪廓
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)  #取輪廓外型

for cnt in contours :
    cv2.drawContours(imgContour, cnt, -1, (0,0,0),4)
    # print(cv2.contourArea(cnt))
    # print(cv2.arcLength(cnt, True))

    area = cv2.contourArea(cnt)
    if area > 500:
        peri = cv2.arcLength(cnt,True)  #邊長
        vertices = cv2.approxPolyDP(cnt, peri*0.02, True)  #取多邊形的頂點
        corners = len(vertices)  #求出圖形的邊有幾個
        x,y,w,h = cv2.boundingRect(vertices)
        cv2.rectangle(imgContour,(x,y),(x+w,y+h), (0,255,0), 4)

        if corners == 3:
            cv2.putText(imgContour,'Triangle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
        elif corners == 4:
            cv2.putText(imgContour, 'Rectangle', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        elif corners == 5:
            cv2.putText(imgContour, 'Pentangon', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        elif corners >= 6:
            cv2.putText(imgContour, 'Circle', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)



cv2.imshow('img',img)
cv2.imshow('canny', canny)
cv2.imshow('imgcontour', imgContour)
cv2.waitKey(0)
