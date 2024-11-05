#Viet chuong trinh tao trackbar de lay goc xoay cua anh
import cv2
import numpy as np
img = cv2.imread(r'C:\Users\phamt\Pictures\Screenshots\Screenshot 2024-08-15 144304.png')
cv2.imshow('img',img)
cv2.namedWindow('TrackbarWindow')
h,w= img.shape[:2]
x =0
def value(pos):
    global x
    x=pos
cv2.createTrackbar('value',"TrackbarWindow",0)
