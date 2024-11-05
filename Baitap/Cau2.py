#Viet chuong trinh tao 2 trackbar de dich anh
import cv2
import numpy as np
img = cv2.imread(r'C:\Users\phamt\Pictures\Screenshots\Screenshot 2024-09-30 223705.png')
cv2.namedWindow('Dichanh')
x= 1
y=1
def traiphai (pos):
    global x
    x=pos
def lenxuong (pos):
    global y
    y = pos
cv2.createTrackbar("traiphai",'Dichanh',0,200,traiphai)
cv2.createTrackbar("lenxuong",'Dichanh',0,200,lenxuong)
h,w =img.shape[:2]
while(True):
    M= np.float32([[1,0,x],[0,1,y]])
    new = cv2.warpAffine(img,M,(w,h))
    cv2.imshow('anh moi', new)
    cv2.imshow('anh goc', img)
    if cv2.waitKey(20)== ord('q'):break
cv2.destroyAllWindows()