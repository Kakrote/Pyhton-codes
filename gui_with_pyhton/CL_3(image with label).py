from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("1200x1000")
x="test_img.jpg"
img = Image.open(x)
imag = ImageTk.PhotoImage(img)
label = Label(image=imag)
label.pack()

root.mainloop()
