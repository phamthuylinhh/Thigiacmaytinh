#Thu phóng ảnh với tỉ lệ nhập vào từ bàn phím
import cv2
img = cv2.imread(r'C:\Users\phamt\Desktop\python\TH1\anh1.jpg')
factor = float(input("Nhâp ti le thu phong:"))
rs = cv2.resize(img,None,fx=factor, fy= factor)
cv2.imshow('anh goc', img)
cv2.imshow('anh thu phong', rs)
cv2.waitKey(0)
cv2.destroyAllWindows()