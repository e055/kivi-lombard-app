from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Learn frame")



frame = LabelFrame(root, text="This is my frame", pady=20, padx=20)
frame.pack(pady=100,padx=100)
b = Button(frame, text="click")
b.pack(padx=30,pady=10)


root.mainloop()