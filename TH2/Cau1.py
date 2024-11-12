#Tạo trackbar lấy kích thước cho bộ lọc trung vị để lọc anh.
import cv2
import numpy as np
img = cv2.imread(r'C:\Users\phamt\Desktop\python\TH1\anh1.jpg')
def get_value(pos):
    pass
cv2.namedWindow('Window')
cv2.createTrackbar('TrackbarWindow', 'Window', 0,50,get_value)
while(True):
    ksize = cv2.getTrackbarPos('TrackbarWindow','Window')
    if ksize %2 == 0: 
        ksize+=1

    m = cv2.medianBlur(img,ksize)
    cv2.imshow('Window',m)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()

