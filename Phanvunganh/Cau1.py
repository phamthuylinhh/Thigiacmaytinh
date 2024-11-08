# cv2.adaptive Threshould
# import cv2
# img = cv2.imread(r'C:\Users\phamt\Desktop\python\a2.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# thresh_img = cv2.adaptiveThreshold(gray, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
# cv2.imshow("Anh ban dau", img)
# cv2.imshow("Anh ket qua", thresh_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.otsu Thresholding
# import cv2
# img = cv2.imread('C:\\Users\\phamt\\Desktop\\python\\a2.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, thresh_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# cv2.imshow("Anh goc", img)
# cv2.imshow("Anh Ket Qua", thresh_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
img = cv2.imread(r'C:\Users\phamt\Desktop\python\a2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
cv2.imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()