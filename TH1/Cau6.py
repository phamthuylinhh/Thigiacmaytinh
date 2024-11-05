#Tạo trackbar để thay đổi độ sáng và độ tương phản của ảnh
import cv2
x = 1
y = 0
def dosang(pos):
    global x
    x=pos
def dotuongphan(pos):
    global y
    y = pos
img = cv2.imread(r'C:\Users\phamt\Desktop\python\TH1\anh1.jpg')
cv2.namedWindow('TrackbarWindow')
cv2.createTrackbar('Dosang', 'TrackbarWindow', 0,255, dosang)
cv2.createTrackbar('Do tuong phan', 'TrackbarWindow', 0,255,dotuongphan)
while(True):
    new = cv2.convertScaleAbs(img, alpha=x, beta=y)
    cv2.imshow('TrackbarWindow', new)
    if cv2.waitKey(20) == ord('q'):break
cv2.destroyAllWindows()