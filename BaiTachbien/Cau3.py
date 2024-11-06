#Viet chuong trinh tach bien Laplace
import cv2
import numpy as np
img = cv2.imread(r'C:\Users\phamt\Desktop\python\a2.jpg')
laplace = cv2.Laplacian(img, cv2.CV_32F,5)
Result = cv2.convertScaleAbs(laplace)
cv2.imshow('anhtachbien',Result)
cv2.waitKey(0)
cv2.destroyAllWindows()