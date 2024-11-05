import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh
image_path = r'C:\Users\phamt\Desktop\python\a2.jpg'
image = cv2.imread(image_path)

if image is None:
    print(f"Không thể đọc ảnh từ đường dẫn: {image_path}")
else:
    # Áp dụng bộ lọc trung bình
    blur = cv2.blur(image, (5, 5))

    # Áp dụng bộ lọc Gauss
    gaussian = cv2.GaussianBlur(image, (5, 5), 0)

    # Áp dụng bộ lọc trung vị
    median = cv2.medianBlur(image, 5)

    # Áp dụng bộ lọc sóng phương
    bilateral = cv2.bilateralFilter(image, 9, 75, 75)

    # Hiển thị 4 ảnh đã lọc
    plt.figure(figsize=(12, 12))

    plt.subplot(221), plt.imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)), plt.title('Bộ lọc trung bình')
    plt.subplot(222), plt.imshow(cv2.cvtColor(gaussian, cv2.COLOR_BGR2RGB)), plt.title('Bộ lọc Gauss')
    plt.subplot(223), plt.imshow(cv2.cvtColor(median, cv2.COLOR_BGR2RGB)), plt.title('Bộ lọc trung vị')
    plt.subplot(224), plt.imshow(cv2.cvtColor(bilateral, cv2.COLOR_BGR2RGB)), plt.title('Bộ lọc sóng phương')

    plt.show()
