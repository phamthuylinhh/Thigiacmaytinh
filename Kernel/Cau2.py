#Tạo trackbar để lấy kích thước kernel cho bộ lọc Baus, ấn phím c để chuyển sang ảnh xám, ấn phím s để lưu ảnh
import cv2
import numpy as np
img = cv2.imread(r'C:\Users\phamt\Desktop\python\a2.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
def get_value(pos):
    pass
cv2.namedWindow('Window')
cv2.createTrackbar('TrackbarWindow','Window',1,50,get_value)
while(True):
    ksize = cv2.getTrackbarPos('TrackbarWindow','Window')
    ksize +=1
    f= cv2.blur(img,(ksize,ksize),0)
    cv2.imshow('Window',f)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
     cv2.imshow('Window',gray)
    elif key == ord('s'):
        cv2.imwrite('linh1.jpg', f)
        break
cv2.destroyAllWindows()
    
