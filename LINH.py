import cv2
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import easyocr

easyocr_reader = easyocr.Reader(['vi','en'])
cap = cv2.VideoCapture(1)
root = Tk()
root.geometry('1300x770')
root.title("TRich xuat")
root.configure(background='white')
