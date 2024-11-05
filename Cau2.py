
import cv2,time
video = cv2.VideoCapture(R'c:\Users\maiqu\Downloads\An_gf1RDg8JLsPMQCsZLkHFlwaPZh79VXBEsai_rzZDi0plf-1RX6hy4ZXrdZnQs8_ZwLsmQXEgIRxQXNvLvjOoo.mp4')
prev_time = 0
while True:
    ret, frame = video.read()
    if not ret:
        break
    # Lấy số khung hình trên giây (FPS) của video, không phải đang phát
    fps = video.get(cv2.CAP_PROP_FPS)
    # Lấy tổng số khung hình
    total_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    # Lấy tốc độ phát (bitrate)
    bitrate = video.get(cv2.CAP_PROP_BITRATE)
    cv2.putText(frame, f'FPS: {fps}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, f'Total frames: {total_frames}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, f'Bitrate: {bitrate}kbps', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow('video', frame)
    time.sleep(1/(fps))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break