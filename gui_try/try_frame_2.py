from tkinter import *
import tkinter as tk


root = Tk()
root.title('Frame try 2')
root.geometry('800x800')

# my_menu = Menu(root)
# root.config(menu=my_menu)
#
# file_menu = Menu(my_menu)
# my_menu.add_cascade(label='Exit', menu=file_menu)
# file_menu.add_command(label='E X I T', command=root.quit)


def click():
    new_frame.pack(fill="both",expand=3)



button_1 = Button(root, text="click", padx=40, pady=20, command=click)
button_1.pack()

new_frame = Frame(root, width=500, height=600)


tk.Label(root, text="First Name").pack()
tk.Label(new_frame, text="Last Name").grid(row=1)

e1 = tk.Entry(root)
e2 = tk.Entry(new_frame)

e1.pack()
e2.grid(row=1, column=1)


bttn = Button(root, text='enter', command=root.txt_box.get(0, END))
bttn.pack()

root.mainloop()