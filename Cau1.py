
import cv2;
img = cv2.imread(R'C:\Users\phamt\source\repos\Doan\wwwroot\images\a2.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Anh goc', img)
cv2.imshow('Anh xam', gray)
h, w = img.shape[:2]
print('Chieu cao la:', h)
print('Chieu rong la:', w)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('a2.jpg', img)