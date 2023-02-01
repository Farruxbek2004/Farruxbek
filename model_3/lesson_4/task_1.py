# Yoshni hisoblaydigan dastur tuzing, bunda foydalanuvchi tugilgan yili
# kiritiladi, shunga mos yoshini qaytaring


from tkinter import *
from datetime import date
from tkinter import Entry, Label, Button

window = Tk()
window.title("Age calculator")
window.geometry("300x400")


def age():
    value = date.today()
    year = int(year_entry.get())
    if year <= 0 or year >= 2023:
        year_label['text'] == "Xato"
    else:
        info = value.year - year
        Label['text'] == str(info)


year_label = Label(window, text="Birth year:")
year_label.place(x=0, y=15)
year_entry = Entry(window, width=20, borderwidth=3)
year_entry.place(x=60, y=15)
year_button = Button(text="Age", command=age)
year_button.place(x=100, y=35)
window.mainloop()
