#Tách biên ảnh bằng phương pháp Sobel, lưu lại ảnh sau khi tách biên. 
import cv2
import numpy as np
img = cv2.imread(r'C:\Users\phamt\Desktop\python\TH1\anh1.jpg')
x = cv2.Sobel(img, cv2.CV_64F,1,0,3)
y = cv2.Sobel(img,cv2.CV_64F,0,1,3)
Sobel = np.sqrt(x**2 +y**2)
Sobel =cv2.convertScaleAbs(Sobel)
cv2.imshow('anh moi', Sobel)
cv2.imwrite('sobel.jpg',Sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()