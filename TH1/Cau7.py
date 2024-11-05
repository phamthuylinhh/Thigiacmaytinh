#Dịch chuyển ảnh với khoảng cách trục x, trục y thay đổi lấy từ trackbar
import cv2
import numpy as np
img = cv2.imread(r'C:\Users\phamt\Desktop\python\TH1\anh1.jpg')
cv2.namedWindow('TrackbarWindow')
x = 0
y = 0
def get_x (pos):
    global x
    x = pos
def get_y(pos):
    global y
    y = pos
cv2.createTrackbar("x",'TrackbarWindow',100,150,get_x)
cv2.createTrackbar("y",'TrackbarWindow',100,150,get_y)
h,w = img.shape[:2]
while(True):
    M = np.float32([[1,0,x],[0,1,y]])
    new = cv2.warpAffine(img, M,(w,h))
    cv2.imshow('anh moi', new)
    cv2.imshow('anh goc', img)
    if cv2.waitKey(20) ==ord('q'):break
cv2.destroyAllWindows()
