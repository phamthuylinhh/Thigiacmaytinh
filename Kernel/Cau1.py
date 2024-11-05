#Tao trackar lay kich thuoc kernel cho bo loc trung loc trung binh.Luu lai anh khi an phim s
import cv2
import numpy as np
img = cv2.imread(r'C:\Users\phamt\Desktop\python\a2.jpg')
def get_value(pos):
    pass
cv2.namedWindow('Window')
cv2.createTrackbar('TrackbarWindow','Window',1,50, get_value)
while (True):
    ksize = cv2.getTrackbarPos('TrackbarWindow','Window')
    if ksize %2 == 0: 
        ksize+=1

    f = cv2.blur(img,(ksize,ksize))
    cv2.imshow('Window', f)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('linh.jpg',f)
        break
   
cv2.destroyAllWindows()

