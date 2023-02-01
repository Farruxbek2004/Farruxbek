# Yoshni hisoblaydigan dastur tuzing, bunda foydalanuvchi tugilgan yili
# kiritiladi, shunga mos yoshini qaytaring


from tkinter import *

window = Tk()
window.title("Age calculator")
window.geometry("300x400")
year_label = Label(window, text="Birth year:")
year_label.place(x=0, y=15)
year_entry = Entry(window, width=20, borderwidth=3)
year_entry.place(x=60, y=15)


def func():
    my_button.config(text="your name: 23")


my_button = Button(window, text="OK", command=func)
my_button.place(x=55, y=50)
window.mainloop()
