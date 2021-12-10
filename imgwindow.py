import  cv2
import numpy as np

img=np.zeros((600,600),np.uint8)

cv2.imshow('img',img)
cv2.waitKey(0)