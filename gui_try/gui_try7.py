from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk


root = Tk()
root.title("Prosty kalkulator")
root.geometry("800x800")


logo = Image.open('malpa.jpg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(row=0,column=0)

e = Entry(root, width=50, borderwidth=10, bg="yellow")
e.grid(row=0, column=1, columnspan=3, padx=10, pady=10)


# e.insert(0, "podaj imie")
def button_click():
    return


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda :button_click())
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda :button_click())
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda :button_click())
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda :button_click())
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda :button_click())
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda :button_click())
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda :button_click())
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda :button_click())
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda :button_click())
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda :button_click())
button_add = Button(root, text="+", padx=30, pady=20, command=lambda :button_click())
button_equal = Button(root, text="=", padx=90, pady=20, command=lambda :button_click())
button_clear = Button(root, text="clear", padx=60, pady=20, command=lambda :button_click())

# myButton = Button(root, text="click", command=click)


button_1.grid(row=2, column=1)
button_2.grid(row=2, column=0)
button_3.grid(row=2, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=2)
button_6.grid(row=3, column=1)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0, columnspan=2)
button_clear.grid(row=4, column=1)
button_equal.grid(row=5, column=1, columnspan=2)


root.mainloop()
