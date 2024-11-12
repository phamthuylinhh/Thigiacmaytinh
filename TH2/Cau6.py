#Tìm contours của ảnh, vẽ contours bằng màu đỏ 
import cv2
img = cv2.imread(r'C:\Users\phamt\Desktop\python\TH1\anh1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
cv2.imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()