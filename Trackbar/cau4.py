#Viet chuong trinh doc anh, doi anh sang xamn, doi anhxam sang anh am ban. Hien 3 anh tren matplotlib
import cv2
import matplotlib.pyplot as plt

# Đọc ảnh từ đường dẫn
img = cv2.imread(r'C:\Users\phamt\source\repos\Doan\wwwroot\assets1\images\product-7.jpg')

# Chuyển đổi ảnh sang xám
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Tạo ảnh âm bản bằng cách sử dụng bitwise_not
neg_img = cv2.bitwise_not(gray)

# Hiển thị các ảnh
plt.figure(figsize=(12, 6))

# Ảnh gốc
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Chuyển đổi từ BGR sang RGB
plt.title('Ảnh gốc')
plt.axis('off')

# Ảnh xám
plt.subplot(1, 3, 2)
plt.imshow(gray, cmap='gray')  # Hiển thị ảnh xám
plt.title('Ảnh xám')
plt.axis('off')

# Ảnh âm bản
plt.subplot(1, 3, 3)
plt.imshow(neg_img, cmap='gray')  # Hiển thị ảnh âm bản
plt.title('Ảnh âm bản')
plt.axis('off')

# Hiển thị biểu đồ
plt.tight_layout()
plt.show()

