#Đọc ảnh, áp dụng các bộ lọc trung bình, trung vị, gauss, song phương. Hiện các ảnh lên matplotlib
import cv2
import numpy as np
import matplotlib.pyplot as plt

img= cv2.imread(r'C:\Users\phamt\Desktop\python\TH1\anh1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
while(True):
    blur = cv2.blur(gray, (5, 5))
    gaussian = cv2.GaussianBlur(img, (5, 5), 0)
    median = cv2.medianBlur(img, 5)
    bilateral = cv2.bilateralFilter(img, 9, 75, 75)
    plt.figure(figsize=(12, 12))
    plt.subplot(221), plt.imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)), plt.title('Bộ lọc trung bình')
    plt.subplot(222), plt.imshow(cv2.cvtColor(gaussian, cv2.COLOR_BGR2RGB)), plt.title('Bộ lọc Gauss')
    plt.subplot(223), plt.imshow(cv2.cvtColor(median, cv2.COLOR_BGR2RGB)), plt.title('Bộ lọc trung vị')
    plt.subplot(224), plt.imshow(cv2.cvtColor(bilateral, cv2.COLOR_BGR2RGB)), plt.title('Bộ lọc sóng phương')

    plt.show()
    plt.close()