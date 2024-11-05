import cv2
imgs = []
for i in range(1, 11):
    img = cv2.imread(f'D:\stuck{i}.png')
    imgs.append(img)