import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from body import *
from tkinter.messagebox import showinfo
from tkinter import Entry



root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

logo = Image.open('malpa.jpg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

instructions = tk.Label(root, text="Wybierz plik na komputerze ")
instructions.grid(columnspan=3, column=0, row=1)


def popup_window():
    window = tk.Canvas(root, width=600, height=300)
    window.grid(columnspan=3, rowspan=3)

    label = tk.Label(window, text="Hello World!")
    label.pack(fill='x', padx=350, pady=350)


    button_close = tk.Button(window, text="Close", command=window.destroy)
    button_close.pack(fill='x')




def open_file():
    browser_text.set("loading...")
    ad_person()


browser_text = tk.StringVar()
browser_btn = tk.Button(root, textvariable=browser_text, command=lambda: open_file(), background="#00FFCE")
browser_text.set("Browse")
browser_btn.grid(column=1, row=2)

button_bonus = tk.Button(root, text="Window", command=popup_window)
button_bonus.grid(column=1, row=3)


canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3)

root.mainloop()
