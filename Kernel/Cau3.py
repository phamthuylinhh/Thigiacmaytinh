#tao trackbar lay kich thuoc kernel cho bo loc trung vi, luu lai anh khi nhan phim s
import cv2
import numpy as np
img = cv2.imread(r'C:\Users\phamt\Desktop\python\a2.jpg')
def get_value(pos):
    pass
cv2.namedWindow('Window')
cv2.createTrackbar('TrackbarWindow','Window',0,50,get_value)
while(True):
    ksize = cv2.getTrackbarPos('TrackbarWindow','Window')
    if ksize %2 == 0: 
        ksize+=1

    m = cv2.medianBlur(img,ksize)
    cv2.imshow('Window',m)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        cv2.imwrite('linh3.jpg',m)
        break
cv2.destroyAllWindows()