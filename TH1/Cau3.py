#Viết chương trình đọc video với các yêu cầu sau:
# #In ra các thông tin của video gồm số khung hình trên 
#giây, tổng số khung hình. 
# #Xem video với màu xám
#Ghi lại hình khi ấn phím s, thoát khi ấn phím q
import cv2
video = cv2.VideoCapture(r'C:\Users\phamt\Desktop\python\TH1\video.mp4')
while(True):
    ret, frame = video.read()
    if not ret:
        break
    fps = video.get(cv2.CAP_PROP_FPS)
    total_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    # Xem video voi mau xam
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print("Số khung hình trên giây (FPS):",fps)
    print("Tổng số khung hình: ", total_frames)
    cv2.imshow('Xemvideo', gray)
    key = cv2.waitKey(25)
    if key == ord('s'):
        cv2.imwrite('frame.png', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):break
video.release()
cv2.destroyAllWindows()

