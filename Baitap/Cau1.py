# Viet chuong trinh thay doi kich thuoc cua anh gap 1.8 lan so vs kich thuoc ban dau

import cv2
img = cv2.imread(r'C:\Users\phamt\Pictures\Screenshots\Screenshot 2024-08-15 134429.png')
h,w = img.shape[:2]
height = int(h*1.8)
weight = int(w*1.8)
img = cv2.resize(img,(height,weight))
cv2.imshow('anhmoi', img)
cv2.waitKey(0)
cv2.destroyAllWindows()