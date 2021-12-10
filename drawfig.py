import  cv2
import numpy as np

img=np.zeros((600,600,3),np.uint8)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,0,0),2)
cv2.rectangle(img,(50,300),(250,500),(0,255,0),2)
cv2.rectangle(img,(300,450),(400,550),(0,0,255),cv2.FILLED)
cv2.circle(img,(100,200),50,(0,255,255),3)
cv2.putText(img,'Hello',(300,300),cv2.FONT_ITALIC,2,(255,0,255),2)


cv2.imshow('img',img)
cv2.waitKey(0)