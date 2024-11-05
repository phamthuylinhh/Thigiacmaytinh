#xoay anh sang phai 1 goc 60 do voi tam xoay la o giua anh
import cv2
img = cv2.imread(r'C:\Users\phamt\Pictures\Screenshots\Screenshot 2024-08-25 210109.png')
cv2.namedWindow('xoayanh')
x=1
def xoay (pos):
    global x
    x= pos
cv2.createTrackbar('xoay','xoayanh',0,360,xoay)
h,w = img.shape[:2]
while(True):
    m = cv2.getRotationMatrix2D((h//2,w//2),x,0.5)
    new= cv2.warpAffine(img,m,(h,w))
    cv2.imshow('anh goc', img)
    cv2.imshow('anh xoay', new)
    if cv2.waitKey(20) == ord ('q') :break
cv2.destroyAllWindows()