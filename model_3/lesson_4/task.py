# import tkinter as tk
#
# window = tk.Tk()
# window.title("Tkinter")
# window.configure(background="red")
# window.geometry("250x300")
# my_label = tk.Label(window, text="Salom", width=40, height=5, bg="blue")
# my_label.grid(row=0, column=1)
#
#
# def funk1():
#     my_label.config(text="Hello")
#
#
# my_button = tk.Button(window, width=10, bg = "Yellow", text = "Tarjimasi", command = funk1)
# my_button.grid(row=2, column=1)
# window.mainloop()
import csv
from tkinter import *
from tkinter import ttk

#
# app = Tk()
# res = StringVar()
# soz = Label(textvariable=res, bg="red",fg="blue",  font=("Algerian", 15), cursor="dot", underline=0)
# soz.pack()
# res.set("Salom:")
# app.mainloop()
# bg="red" - > rang berish
# fg="blue" = > sozlarning ranggini ozgartirish
# font=("Algerian", 15) - > yozuv turini aniqlash
# cursor="dot" - > sichqoncha turini aniqlash
#  underline=6 - > so'zlarni tagiga chiziq chizish
# def tugma_():
#     tugma.config(text="Tugma ishladi")
#
#
# dastur = Tk()
# soz = Label(text="Salom")
# dastur.geometry("300x400")
# tugma = Button(text="Ok", command=tugma_)
# tugma.pack()
# dastur.mainloop()

win = Tk()
win.title("Student Record")
win.geometry("500x600")


def write():
    with open("students.csv", "w", newline="") as f:
        file = csv.writer(f, delimiter=',')
        name = var1.get()
        file.writerow(["Name"])
        file.writerow([name])

Label(win, text="Name").grid(row=1, column=1, columnspan=2)
var1 = StringVar()
Entry(win, textvariable=var1).grid(row=2, column=2)
combo = ttk.Combobox(win, width=17)
combo["values"] = ["Select", "India", "America", "Japan", "Russia", "CHina"]
combo.current(0)
combo.grid(row=2, columnspan=1)
Button(win, text="Add", command=write).grid(row=6, column=1, columnspan=2)
win.mainloop()
