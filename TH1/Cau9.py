#Biến đổi phối cảnh ảnh
import cv2
import numpy as np
img = cv2.imread(r'C:\Users\phamt\Desktop\python\TH1\anh1.jpg')
h = 300
w = 500
M = np.float32([[244,502],[419,509],[414,890],[232,889]])
M2 = np.float32([[0,0],[w,0],[w,h],[0,h]])
img1 = cv2.getPerspectiveTransform(M,M2)
warp = cv2.warpPerspective(img, img1,(w,h))
cv2.imshow('anh bien doi phoi canh',warp)
cv2.waitKey(0)
