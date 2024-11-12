#Phân ngưỡng ảnh bằng phân ngưỡng nhị phân, phân ngưỡng thích nghi, phân ngưỡng tối ưu. Hiện ảnh gốc và các ảnh phân ngưỡng lên matplotlib.
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Users\phamt\Desktop\python\a2.jpg', cv2.IMREAD_GRAYSCALE)
ret, binary_thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
adaptive_thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
ret, otsu_thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
plt.figure(figsize=(12, 6))

plt.subplot(1, 4, 1)
plt.imshow(img, cmap='gray')
plt.title('anh goc')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(binary_thresh, cmap='gray')
plt.title('phân ngưỡng nhị phân')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(adaptive_thresh, cmap='gray')
plt.title('phân ngưỡng thích nghi')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.imshow(otsu_thresh, cmap='gray')
plt.title("phân ngưỡng tối ưu")
plt.axis('off')

plt.show()

