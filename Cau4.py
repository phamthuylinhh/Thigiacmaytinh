#Viet chuong trinh dung 3 cach tach bien, hien thi anh ket qua tren matplotlib
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r'C:\Users\phamt\Desktop\python\a2.jpg')
Result = cv2.Canny(img, 100,200)

x = cv2.Sobel(img, cv2.CV_64F,1,0,ksize=3)
y = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
Sobel = np.sqrt(x**2 +y**2)
Sobel =cv2.convertScaleAbs(Sobel)

laplace = cv2.Laplacian(img, cv2.CV_32F,5)
Laplace= cv2.convertScaleAbs(laplace)

plt.figure(figsize=(12,12))
plt.subplot(1,3,1)
plt.imshow(Result)
plt.title('Canny')
plt.subplot(1,3,2)
plt.imshow(Sobel)
plt.title('Sobel')
plt.subplot(1,3,3)
plt.imshow(Laplace)
plt.title('Laplace')

plt.show()