#Tách biên ảnh bằng phương pháp Canny, Laplace. Hiện ảnh gốc, các ảnh sau khi tách biên lên matplotlib. 
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r'C:\Users\phamt\Desktop\python\TH1\anh1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
Result = cv2.Canny(gray, 100,200)

laplace = cv2.Laplacian(gray, cv2.CV_32F,5)
Laplace= cv2.convertScaleAbs(laplace)

plt.figure(figsize=(12,12))
plt.subplot(1,3,1)
plt.imshow(img)
plt.title('anh goc')
plt.subplot(1,3,2)
plt.imshow(Result)
plt.title('Canny')
plt.subplot(1,3,3)
plt.imshow(Laplace)
plt.title('Laplace')

plt.show()