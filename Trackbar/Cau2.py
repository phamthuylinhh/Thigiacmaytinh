#Viet chuong trinh doc anh, doi anh sang xamn, doi anhxam sang anh am ban. Hien 3 anh
import cv2
img = cv2.imread(r'C:\Users\phamt\source\repos\Doan\wwwroot\assets1\images\product-7.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
neg_img = cv2.bitwise_not(gray)
cv2.imshow('anhgoc', img)
cv2.imshow('anhxam', gray)
cv2.imshow('anhamban', neg_img)
cv2.waitKey(0)
cv2.destroyAllWindows
