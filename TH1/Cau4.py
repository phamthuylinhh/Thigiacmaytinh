#Đọc ảnh, cắt một phần tư góc trên trái của ảnh. Phóng 
#ảnh đã cắt gấp 1.5 lần. Lưu lại ảnh kết quả
import cv2
img = cv2.imread(r'C:\Users\phamt\Desktop\python\TH1\anh1.jpg')
h,w = img.shape[:2]
crop = img[0:h//2 , 0:w//2]
rs = cv2.resize(img, None, fx=1.5,fy=1.5)
cv2.imwrite(r'C:\Users\phamt\Desktop\python\TH1\anh3.jpg', rs)
cv2.imshow('anh goc',img)
cv2.imshow('anh moi', crop)
cv2.waitKey(0)
cv2.destroyAllWindows()