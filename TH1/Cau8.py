# Xoay ảnh 1 góc tùy ý lấy từ trackbar
import cv2
img = cv2.imread(r'C:\Users\phamt\Desktop\python\TH1\anh1.jpg')
h,w= img.shape[:2]
cv2.namedWindow("Window")
r = 0
def xoay(pos):
    global r
    r =pos
cv2.createTrackbar("Goc xoay",'Window',0,360,xoay)
while(True):
    m = cv2.getRotationMatrix2D((h//2,w//2),r,0.5)
    new = cv2.warpAffine(img,m,(h,w))
    cv2.imshow('anh goc', img)
    cv2.imshow('anh xoay', new)
    if cv2.waitKey(20) == ord('q'):break
cv2.destroyAllWindows()
