#Ghi văn bản, vẽ các hình đơn giản lên ảnh: đường thẳng, mũi tên, hình tròn, elip, hình chữ nhật, đa giác
import cv2
import numpy as np
img = cv2.imread(r'C:\Users\phamt\Desktop\python\TH1\anh1.jpg')
#Duong thang
cv2.line(img,[200,80],[450,80],(255,255,0), thickness=3)
#mui ten
cv2.arrowedLine(img,[50,100],[450,100],(0,255,0),5)
#Hinh tron
cv2.circle(img,[415,190],100,(0,0, 255), thickness=3, lineType=cv2.LINE_AA)
#Elip
cv2.ellipse(img,[315,190],[100,50],0,0,360,(255,0,0),thickness=3)
cv2.ellipse(img,[315,190],[125,50],90,0,360,(0,0,255), thickness=3)
#Hinh chu nhat
cv2.rectangle(img,[200,115],[400,425],(0,0,255),thickness=3,lineType=cv2.LINE_8)
#Da giac
pts = np.array([[100, 300], [200, 400], [300, 350], [400, 400], [450, 300]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], isClosed=True, color=(0, 255, 255), thickness=2)
#Ghi van ban
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Pham Thuy Linh', (50, 470), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.imshow('Anh da chinh sua', img)
cv2.waitKey(0)
cv2.destroyAllWindows()