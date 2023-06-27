# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import ttk
import os

root=Tk()
root.title("Image Viewer")
root.geometry("666x666")
root.configure(bg="medium orchid")

label_img = Label(root, bg="white", highlightthickness=5)
label_img.place(relx=0.5, rely=0.5, anchor=CENTER)

img_path = ""

def openImg():
    global img_path
    img_path = filedialog.askopenfilename(title = "Open Image File", filetypes = [{"Image File", "*.jpg *.gif *.png *.jpeg"}])
    print(img_path)
    image = Image.open(img_path)
    img = ImageTk.PhotoImage(image)
    name = os.path.basename(img_path)
    formatted_name = name.split('.')[0]
    root.title(formatted_name)
    label_img["image"] = img
    img.close()

open_btn = Button(root, text="Open Image", bg="Grey", fg="white", font={"Times New Roman", 15, "bold"}, padx=15, pady=10, relief=SOLID, command=openImg)

root.mainloop()