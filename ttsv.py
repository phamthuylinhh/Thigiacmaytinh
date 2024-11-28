import cv2
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import easyocr
from datetime import datetime

easyocr_reader = easyocr.Reader(['vi', 'en'])
cap = cv2.VideoCapture(1)

root = Tk()
root.geometry('1300x770')
root.title("TRÍCH XUẤT THÔNG TIN TỪ THẺ SINH VIÊN")
root.configure(bg='white')

Label(root, text="TRƯỜNG ĐẠI HỌC VINH", 
          bg='white', font=('Times', 25, 'bold'), fg='blue').pack(side=TOP)
Label(root, text="HỌC PHẦN THỊ GIÁC MÁY TÍNH", 
          bg='white', font=('Times', 22, 'bold')).pack(side=TOP)
Label(root, text="ĐỒ ÁN", 
          bg='white', fg='red', font=('Times', 25, 'bold')).pack(side=TOP)
Label(root, text="TRÍCH XUẤT THÔNG TIN TỪ THẺ SINH VIÊN", 
          bg='white', fg='red', font=('Times', 25, 'bold')).pack(side=TOP)

Label(root, text="Camera Input", bg='white', font=('Times', 20, 'bold'), fg='black').place(x=25, y=200)
Label(root, text="Ảnh Chụp", bg='white', font=('Times', 20, 'bold'), fg='black').place(x=515, y=200)
Label(root, text="Thông Tin Trích Xuất", bg='white', font=('Times', 20, 'bold'), fg='black').place(x=850, y=200)

fields = {
    'hoten': "Họ và tên:", 'nganh': "Ngành:", 'khoa': "Khoa:",
    'khoas': "Khóa:", 'msv': "MSSV:"
}
labels = {}
y_pos = 300
for key, text in fields.items():
    labels[key] = Label(root, text=text, bg='white', fg='black', font=('Times', 18, 'bold'))
    labels[key].place(x=850, y=y_pos)
    y_pos += 35

canvas = Canvas(root, width=480, height=360, bg="white")
canvas.place(x=25, y=250)
cut_tsv = Canvas(root, width=320, height=240, bg="white")
cut_tsv.place(x=515, y=250)

imgGetText = None
image1 = None
image2 = None

def save_to_file(info_dict):
  
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    try:
        with open('ttsv.txt', 'a', encoding='utf-8') as f:
            f.write(f"\n--- Thông tin trích xuất lúc {timestamp} ---\n")
            for key, value in info_dict.items():
                f.write(f"{value}\n")
            f.write("-" * 50 + "\n")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể lưu file: {str(e)}")


def display():

    global imgGetText, image1, image2

    ret, frame = cap.read()
    if not ret:
        print("Không thể truy cập camera")
        return

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image1 = ImageTk.PhotoImage(image=Image.fromarray(frame_rgb))
    canvas.create_image(0, 0, image=image1, anchor=NW)
    canvas.image = image1 

    blurred = cv2.GaussianBlur(frame, (5, 5), 0)
    edges = cv2.Canny(blurred, 75, 150)
    contours, _ = cv2.findContours(edges, cv2.chRETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w > 100 and h > 100:
            imgGetText = cv2.resize(frame_rgb[y:y+h, x:x+w], (800, 600))
            roi_resized = cv2.resize(frame_rgb[y:y+h, x:x+w], (320, 240))
            image2 = ImageTk.PhotoImage(image=Image.fromarray(roi_resized))
            cut_tsv.create_image(0, 0, image=image2, anchor=NW)
            cut_tsv.image = image2 
            break
    root.after(10, display)

def extract_info():
   
    if imgGetText is None:
        messagebox.showerror("Error", "Không tìm thấy ảnh sinh viên để nhận diện.")
        return
    cv2.imwrite("oopp.jpg", cv2.cvtColor(imgGetText, cv2.COLOR_RGB2BGR))

    extracted_info = {}

    regions = {
        "HOTEN": (100, 127, 99, 212), "NGANH": (127, 145, 120, 231),
        "KHOA": (144, 166, 76, 233), "KHOAS": (166, 188, 130, 214),
        "MSV": (520, 580, 543, 790) 
    }

    for key, (y1, y2, x1, x2) in regions.items():

        if key != "MSV":
            y1, y2, x1, x2 = map(lambda v: int(v * 2.5), (y1, y2, x1, x2))
        if y2 <= imgGetText.shape[0] and x2 <= imgGetText.shape[1]:
            region = imgGetText[y1:y2, x1:x2]
            results = easyocr_reader.readtext(region)
            text = ' '.join([result[1] for result in results]) if results else "Không xác định"
            if key == "MSV" and len(text) > 4:
                text = text[4:]
            labels[key.lower()].config(text=f"{fields[key.lower()]} {text}")
            label_text = f"{fields[key.lower()]} {text}"
            extracted_info[key.lower()] = label_text
        else:
            print(f"Vùng {key} vượt quá giới hạn ảnh. Bỏ qua.")
    save_to_file(extracted_info)

Button(root, text='Trích xuất thông tin', bg='green', fg='white', font=('Times', 15, 'bold'), command=extract_info).place(x=500, y=650)


display()
root.protocol("WM_DELETE_WINDOW", lambda: (cap.release(), root.destroy()))
root.mainloop()
