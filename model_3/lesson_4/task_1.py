import tkinter
from tkinter import *
from datetime import datetime
from tkinter.messagebox import showerror

age = Tk()
age.title('P10-Age Calculator')
age.resizable(width=False, height=False)
age.configure(background="green")
name = Frame(age, height=400, width=400, bg='white', )
name.grid(row=0, column=1)
age_name = Label(age, text="Age calculator", foreground="red", font=30)
age_name.place(x=150, y=10)
label_data = Label(age, text="Day: ", bg='green', font=25)
label_data.place(x=70, y=40)
day_entry = Entry(age, width=5, font=(None, 10, 'bold'))
day_entry.place(x=150, y=40)

label_month = Label(age, text="Month: ", bg='green', font=25)
label_month.place(x=70, y=80)
month_entry = Entry(age, width=5)
month_entry.place(x=150, y=80)

label_year = Label(age, text="Year: ", bg='green', font=25)
label_year.place(x=70, y=120)
year_entry = Entry(age, width=5)
year_entry.place(x=150, y=120)
calculator_age = Label(age, text="Calculate age ->", foreground="green", font=25)
calculator_age.place(x=20, y=170)

label_name = Label(age, text="Your age: ", bg='green', font=50)
label_name.place(x=50, y=250)


def year_calculator():
    try:
        year_entry.get()
        current_year = datetime.now().year
        your_age = current_year - int(year_entry.get())
        your_age = str(your_age)
        text.set(your_age)
    except:
        showerror(("Error"),
                  "\nError fayl")


text = tkinter.StringVar()
age_entry = Entry(age, textvariable=text, width=6, font=50)
age_entry.place(x=150, y=250)

buttton = Button(age, text="Enter", padx=20, pady=10, bg="green", command=year_calculator)
buttton.place(x=160, y=160)

age.mainloop()
