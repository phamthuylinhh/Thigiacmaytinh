#Viet chuong trinh doc anh, ap dung bo loc song phuong. Sau do thay doi do sang va do tuong phan cua anh
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r'C:\Users\phamt\Desktop\python\a2.jpg')
b = cv2.bilateralFilter(img,9,75,75)
alpha= 1.5
beta = 50
a = cv2.convertScaleAbs(b, alpha=alpha, beta=beta)
plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))
plt.title('Anh sau khi ap dung bo loc song phuong')

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(a,cv2.COLOR_BGR2RGB))
plt.title('Anh sau khi thay doi do sang va do tuong phan')

plt.show()
