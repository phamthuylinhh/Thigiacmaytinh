# Tạo trackbar lấy ngưỡng dưới cho tách biên Canny, ngưỡng trên gấp đôi ngưỡng dưới
import cv2
import numpy as np
img = cv2.imread(r'C:\Users\phamt\Desktop\python\a2.jpg') 
def get_value(pos):
    pass
cv2.namedWindow('Window')
cv2.createTrackbar('TrackbarWindow','Window', 0,255,get_value)
while(True):
    lower = cv2.getTrackbarPos('TrackbarWindow','Window')
    up = lower*2
    result= cv2.Canny(img,lower,up)
    cv2.imshow('Window', result)
    if cv2.waitKey(1) & 0xFF == ord('q'):break
cv2.destroyAllWindows()