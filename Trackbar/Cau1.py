# Viet chuong trinh tao trackbar de thay doi do sang cua anh
import cv2
x= 1
def get_value(pos):
    global x
    x= pos
img = cv2.imread(r'C:\Users\phamt\source\repos\Doan\wwwroot\assets1\images\product-7.jpg')
cv2.namedWindow('TrackbarWindow')
cv2.createTrackbar('Thaydoi', 'TrackbarWindow', 0,255, get_value)

while(True):
    new = cv2.convertScaleAbs(img, alpha=1, beta = x)
    cv2.imshow('TrackbarWindow', new)
    if cv2.waitKey(20)== ord('q'):break
cv2.destroyWindow()