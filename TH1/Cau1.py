#Đọc và hiển thị ảnh. In ra giá trị màu tại điểm ảnh có 
#tọa độ nhập vào.
import cv2
img = cv2.imread(r'C:\Users\phamt\Desktop\python\TH1\anh1.jpg')
x= int(input('Nhap toa do x: '))
y= int(input('Nhap toa do y: '))
(B,G,R) = img[y,x]
cv2.imshow('anhmoi', img)
cv2.waitKey(0)
print('B={},G={},R={}'.format(B,G,R))
cv2.destroyAllWindows()