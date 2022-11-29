from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
root = Tk()

logo = Image.open('malpa.jpg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.pack()

e= Entry(root, width=50, borderwidth=5, bg="yellow")
e.pack()
e.insert(0, "podaj imie")

def click():
    hello = "Hello" + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root,text="click", command=click)
myButton.pack()


root.mainloop()