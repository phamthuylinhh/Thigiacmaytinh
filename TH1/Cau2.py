#Viết chương trình đổi ảnh màu sang ảnh xám, ảnh âm bản. 
#Hiển thị 3 ảnh trên matplotlib

import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r'C:\Users\phamt\Desktop\python\TH1\anh1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
neg = 255 -img

plt.figure(figsize=(12,6))
plt.subplot(1,3,1)
plt.imshow(img)
plt.title("Ảnh gốc")
plt.subplot(1,3,2)
plt.imshow(gray,cmap='gray')
plt.title("Ảnh xám")
plt.subplot (1,3,3)
plt.imshow(neg)
plt.title("Ảnh âm bản")
plt.tight_layout()
plt.show()