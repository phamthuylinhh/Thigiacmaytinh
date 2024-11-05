import cv2
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'D:\\Applications\\ORC\\tesseract.exe'

cap = cv2.VideoCapture(1)

root = Tk()
root.geometry('1300x770')
root.resizable(width=False, height=False)
root.title("TRÍCH XUẤT THÔNG TIN TỪ THẺ SINH VIÊN")
root.configure(bg='white')

tentruong = Label(root, text="TRƯỜNG ĐẠI HỌC VINH", bg='white',font=('Time 25 bold'), fg='blue')
tentruong.pack(side=TOP)
a = Label(root, text="      ", bg='white',font=('Time 5 bold'))
a.pack(side=TOP)
khoa = Label(root, text="HỌC PHẦN THỊ GIÁC MÁY TÍNH", bg='white',font=('Time 22 bold'))
khoa.pack(side=TOP)
c = Label(root, text="    ", bg='white',font=('Time 10 bold'))
c.pack(side=TOP)
doan = Label(root, text="ĐỒ ÁN", bg='white', fg='red',font=('Time 25 bold'))
doan.pack(side=TOP)
detai = Label(root, text="TRÍCH XUẤT THÔNG TIN TỪ THẺ SINH VIÊN", bg='white', fg='red', font=('Time 25 bold'))
detai.pack(side=TOP)
thoigian = Label(root, text="Vui lòng kiểm tra thông tin", bg='white', fg='blue', font=('Time 25 bold'))
thoigian.place(x= 740, y= 250)

gd_hoten = Label(root, text="Họ và tên:", bg='white', fg='black', font=('Time 18 bold'))
gd_hoten.place(x= 745, y= 300)

gd_ngaysinh = Label(root, text="Ngành:", bg='white', fg='black', font=('Time 18 bold'))
gd_ngaysinh.place(x= 745, y= 335)

gd_nganh = Label(root, text="Khoa:", bg='white', fg='black', font=('Time 18 bold'))
gd_nganh.place(x= 745, y= 370)

gd_khoa = Label(root, text="Khóa:", bg='white', fg='black', font=('Time 18 bold'))
gd_khoa.place(x= 745, y= 405)

gd_mssv = Label(root, text="MSSV:", bg='white', fg='black', font=('Time 18 bold'))
gd_mssv.place(x= 745, y= 440)

logo = cv2.imread('logodhv.jpg')
logo = cv2.resize(logo, (200, 200))
logo = cv2.cvtColor(logo, cv2.COLOR_BGR2RGB)
img = Image.fromarray(logo)
img = ImageTk.PhotoImage(image=img)
imglabel = Label(root, image=img)
imglabel.place(x=0, y=0)
logo1 = cv2.imread('logodhv.jpg')
logo1 = cv2.resize(logo1, (195, 195))
logo1 = cv2.cvtColor(logo1, cv2.COLOR_BGR2RGB)
img1 = Image.fromarray(logo1)
img1 = ImageTk.PhotoImage(image=img1)
img1label = Label(root, image=img1)
img1label.place(x=1095, y=0)

canvas = Canvas(root, width= 320, height= 240, bg= "white")
canvas.place(x= 50, y= 250)


cut_tsv = Canvas(root, width= 320, height= 240, bg= "white")
# cut_tsv = Canvas(root, width= 300, height= 350, bg= "white")
cut_tsv.place(x= 400, y= 250)

global roi_resized

def display():
    global image1, image2

    _, frame = cap.read()
    frame = cv2.resize(frame, (480, 350))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image1 = ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.create_image(0, 0, image=image1, anchor=NW)

    blurred = cv2.GaussianBlur(frame, (5, 5), 0)
    img_gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(img_gray, 75, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w > 100 and h > 100:
            global roi_resized
            
            roi = frame[y:y + h, x:x + w]
            roi_resized = cv2.resize(roi, (320, 240))  # Resize vùng cắt
            image2 = ImageTk.PhotoImage(image=Image.fromarray(roi_resized))
            cut_tsv.create_image(0, 0, image=image2, anchor=NW)
            # roi_resized = cv2.cvtColor(roi_resized, cv2.COLOR_BGR2RGB)
            # cv2.imwrite('sv.jpg',roi_resized)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    
    root.after(1, display)

display()


def txtt():
    global roi_resized, textTEN, textNGANH, textKHOA, textKHOAS, textMSV

    HOTEN = img[92:118, 90:214]
    NGANH = img[115:138,118:238]
    KHOA = img[135:158,80:238]
    KHOAS = img[155:176,120:238]
    MSV = img[192:215,239:315]

    HOTEN = cv2.resize(HOTEN, None, fx=2.5, fy=2.5, interpolation=cv2.INTER_CUBIC)
    NGANH = cv2.resize(NGANH, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    KHOA = cv2.resize(KHOA, None, fx=2.5, fy=2.5, interpolation=cv2.INTER_CUBIC)
    KHOAS = cv2.resize(KHOAS, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    MSV = cv2.resize(MSV, None, fx=2.5, fy=2, interpolation=cv2.INTER_CUBIC)

    # cv2.imshow('a', HOTEN)
    # cv2.imshow('b', NGANH)
    # cv2.imshow('c', KHOA)
    # cv2.imshow('d', KHOAS)
    grayTEN = cv2.cvtColor(HOTEN, cv2.COLOR_BGR2GRAY)
    grayNGANH = cv2.cvtColor(NGANH, cv2.COLOR_BGR2GRAY)
    grayKHOA = cv2.cvtColor(KHOA, cv2.COLOR_BGR2GRAY)
    grayKHOAS = cv2.cvtColor(KHOAS, cv2.COLOR_BGR2GRAY)
    grayMSV = cv2.cvtColor(MSV, cv2.COLOR_BGR2GRAY)

    thresTEN = cv2.adaptiveThreshold(grayTEN,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,4)
    thresNGANH = cv2.adaptiveThreshold(grayNGANH,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,4)
    thresKHOA = cv2.adaptiveThreshold(grayKHOA,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,4)
    thresKHOAS = cv2.adaptiveThreshold(grayKHOAS,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,4)
    threshMSV = cv2.adaptiveThreshold(grayMSV,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,4)

    kernel = np.array((15,15))

    imDialTEN = cv2.erode(thresTEN, kernel, iterations=1)
    imDialNGANH = cv2.erode(thresNGANH, kernel, iterations=1)
    imDialKHOA = cv2.erode(thresKHOA, kernel, iterations=1)
    imDialKHOAS = cv2.erode(thresKHOAS, kernel, iterations=1)
    imDialMSV = cv2.dilate(threshMSV, kernel, iterations=1)

    imCloseMSV = cv2.morphologyEx(imDialMSV, cv2.MORPH_CLOSE, kernel)
    imCloseNGANH = cv2.morphologyEx(imDialNGANH, cv2.MORPH_CLOSE, kernel)
    imCloseKHOA = cv2.morphologyEx(imDialKHOA, cv2.MORPH_CLOSE, kernel)
    imCloseKHOAS = cv2.morphologyEx(imDialKHOAS, cv2.MORPH_CLOSE, kernel)
    imCloseTEN = cv2.morphologyEx(imDialTEN, cv2.MORPH_CLOSE, kernel)

    textTEN = pytesseract.image_to_string((imCloseTEN), lang='vie')
    textNGANH = pytesseract.image_to_string((imCloseNGANH), lang='vie')
    textKHOA = pytesseract.image_to_string((imDialKHOA), lang='vie')
    textKHOAS = pytesseract.image_to_string((imDialKHOAS), lang='vie')
    textMSV = pytesseract.image_to_string((imCloseMSV), lang='vie')

    print(textTEN)
    print(textNGANH)
    print(textKHOA)
    print(textKHOAS)
    print(textMSV)

    
    ht_TEN = Label(root, text=textTEN, height=2, bg='white', font=('Time 18 bold'))
    ht_TEN.place(x=915, y=300)

    ht_NGANH = Label(root, text=textNGANH, height=2, bg='white', font=('Time 18 bold'))
    ht_NGANH.place(x=930, y=335)

    ht_KHOA = Label(root, text=textKHOA, height=2, bg='white', font=('Time 18 bold'),justify='left')
    ht_KHOA.place(x=915, y=370)
    ht_KHOAS = Label(root, text=textKHOAS, height=2, bg='white', font=('Time 18 bold'))
    ht_KHOAS.place(x=855, y=405)

    ht_MSV = Label(root, text=textMSV, bg='white', fg='black', font=('Time 18 bold'))
    ht_MSV.place(x= 855, y= 440)


#Nút nhấn trích xuất dữ liệu
btn_txtt = Button(root, text='Trích xuất thông tin', bg='green', fg='white', font=('Time 15 bold'))
btn_txtt.config(command=txtt)
btn_txtt.place(x=400, y=560)

#Kết thúc chương trình
root.mainloop()