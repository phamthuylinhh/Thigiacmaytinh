import cv2

def mouse_callback(event, x, y, flags, param):
    global selected_objects

    if event == cv2.EVENT_LBUTTONDOWN:
        for cnt in contours:
            x_obj, y_obj, w_obj, h_obj = cv2.boundingRect(cnt)
            if x_obj <= x <= x_obj + w_obj and y_obj <= y <= y_obj + h_obj:
                selected_objects.append((x_obj, y_obj, w_obj, h_obj))
                break

cv2.namedWindow('Camera')
cv2.setMouseCallback('Camera', mouse_callback)

cap = cv2.VideoCapture(0)

selected_objects = []

while True:
    ret, frame = cap.read()

    # Chuyển ảnh sang ảnh đen trắng
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Áp dụng ngưỡng nhị phân
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Tìm contour
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    for (x_obj, y_obj, w_obj, h_obj) in selected_objects:
        cv2.rectangle(frame, (x_obj, y_obj), (x_obj+w_obj, y_obj+h_obj), (0, 0, 255), 2)
        width_mm = w_obj * 10  # Giả sử mỗi pixel tương ứng với 1mm
        height_mm = h_obj * 10  # Giả sử mỗi pixel tương ứng với 1mm
        cv2.putText(frame, f"Width: {width_mm:.2f} mm, Height: {height_mm:.2f} mm", (x_obj, y_obj - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow('Camera', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        if selected_objects:
            for i, (x_obj, y_obj, w_obj, h_obj) in enumerate(selected_objects):
                object_img = frame[y_obj:y_obj+h_obj, x_obj:x_obj+w_obj]
                cv2.imshow(f"Object {i}", object_img)

cap.release()
cv2.destroyAllWindows()
