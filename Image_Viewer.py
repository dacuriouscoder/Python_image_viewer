import tkinter as tk
from tkinter import *

from PIL import ImageTk,Image

window = tk.Tk()
window.title("UTK Image Viewer")
window.iconbitmap("icon11.ico")
window.geometry("300x400")

Im1 = ImageTk.PhotoImage(Image.open("icon1.ico"))
Im2 = ImageTk.PhotoImage(Image.open("icon2.ico"))
Im3 = ImageTk.PhotoImage(Image.open("icon3.ico"))
Im4 = ImageTk.PhotoImage(Image.open("icon4.ico"))

Imagelist = [Im1, Im2, Im3, Im4]

label1 = Label(image = Im1)
label1.grid(row=0, column=0, columnspan=3)

status = tk.Label(window, text="Image "+ str(1) + " of " + str(len(Imagelist)), bd= 1, relief=SUNKEN, anchor = E)
status.grid (row =2, column=0, columnspan = 3, pady = 20, sticky = E+W)

def back(image_num):
    global label1
    global button_forward
    global button_back

    label1.grid_forget()
    label1 = Label(image=Imagelist[image_num - 1])
    label1.grid(row=0, column=0, columnspan=3)
    button_back = tk.Button(window, text="<<", command=lambda: back(image_num - 1 ))
    button_forward = tk.Button(window, text=">>", command=lambda: forward(image_num + 1))
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status = tk.Label(window, text="Image " + str(image_num) + " of " + str(len(Imagelist)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, pady=20, sticky=E + W)



def forward(image_num):
    global label1
    global button_forward
    global button_back

    label1.grid_forget()
    label1 = Label(image=Imagelist[image_num - 1])
    label1.grid(row=0, column=0, columnspan=3)
    if image_num == 3:
        button_forward = tk.Button(window, text=">>", state = DISABLED)
    button_back = tk.Button(window, text="<<", command=lambda: back(image_num - 1))
    button_forward = tk.Button(window, text=">>", command=lambda: forward(image_num + 1))
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status = tk.Label(window, text="Image " + str(image_num) + " of " + str(len(Imagelist)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, pady=20, sticky=E + W)

button_back = tk.Button(window, text="<<", command=lambda:back)
button_exit = tk.Button(window, text="EXIT", command=window.quit)
button_forward = tk.Button(window, text=">>", command=lambda:forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)



window.mainloop()







