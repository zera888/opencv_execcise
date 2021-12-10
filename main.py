import  cv2

img = cv2.imread('lenna.jpg')
img = cv2.resize(img,(0,0), fx=0.4, fy=0.4)
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
faceCascade = cv2.CascadeClassifier('facedetect.xml')
faceRect = faceCascade.detectMultiScale(gray, 1.1, 3)
print(len(faceRect))

for (x,y,w,h) in faceRect :
    cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),2)

cv2.imshow('img',img)
cv2.imshow('gray',gray)
cv2.waitKey(0)
