# Mehmonxona registratsiya tizimini ishlab chiqing, bunda uning ismi, yoshi,
# qayerdan ekanligi va necha kun qolishligi, qancha pul tolash kerak ekanligini royxatga
# oling, malumotlarni csv faylga saqlab boring.


import csv
from model_3.exceptions import exceptins_func
from tkinter import messagebox, END, Tk, Label, Entry, Button
from tkinter import ttk
from hotel import Hotel

window = Tk()
window.title("Student Registration")
window.geometry("450x350")
window.configure(background="green")
hotels = []


def add():
    hotel = Hotel(
        fullname_entry.get(),
        age_entry.get(),
        address_entry.get(),
        length_of_stay_entry.get(),
        summa_entry.get(),
        country.get()
    )
    hotels.append(hotel.get_attrs(as_dict=True))
    messagebox.showinfo("Information", "The data has been added successfully")


def write():
    try:
        with open("hotelt_info.csv", "a", newline="\n") as f:
            file = csv.writer(f)
            file.writerow(["Fullname", "Age", "Address", "Length of stay", "Summa", "Country"])
            file.writerow(
                [fullname_entry.get(), age_entry.get(), address_entry.get(), length_of_stay_entry.get(),
                 summa_entry.get(),
                 country.get()])
    except FileNotFoundError as e:
        exceptins_func(e)


def clear():
    fullname_entry.delete(0, END)
    age_entry.delete(0, END)
    address_entry.delete(0, END)
    length_of_stay_entry.delete(0, END)
    summa_entry.delete(0, END)


# Fullname
fullname_label = Label(window, text="Fullname: ", padx=20, pady=10, font=("Algerian", 11), fg="blue")
fullname_label.grid(row=0, column=0)
fullname_entry = Entry(window, width=30, borderwidth=3)
fullname_entry.grid(row=0, column=1)

# Age
age_label = Label(window, text="Age: ", padx=20, pady=10, font=("Algerian", 11), fg="blue")
age_label.grid(row=1, column=0)
age_entry = Entry(window, width=30, borderwidth=3)
age_entry.grid(row=1, column=1)

# address
address_label = Label(window, text="Address: ", padx=20, pady=10, font=("Algerian", 11), fg="blue")
address_label.grid(row=2, column=0)
address_entry = Entry(window, width=30, borderwidth=3)
address_entry.grid(row=2, column=1)

# Length of stay
length_of_stay_label = Label(window, text="Length of stay: ", padx=20, pady=10, font=("Algerian", 11), fg="blue")
length_of_stay_label.grid(row=4, column=0)
length_of_stay_entry = Entry(window, width=30, borderwidth=3)
length_of_stay_entry.grid(row=4, column=1)

# Summa
summa_label = Label(window, text="Summa: ", padx=20, pady=10, font=("Algerian", 11), fg="blue")
summa_label.grid(row=6, column=0)
summa_entry = Entry(window, width=30, borderwidth=3)
summa_entry.grid(row=6, column=1)

# Country
country = ttk.Combobox(window, width=15)
country["values"] = ["Select a Country", "India", "America", "Japan", "Russia", "China", "Uzbekistan", "Ukrain",
                     "Argentina", "Qozog'iston"]
country.current(0)
country.grid(row=7, columnspan=1)

# Save button
save_btn = Button(window, text="Save", padx=15, pady=10, command=write, font=("Algerian", 9), cursor="dot", fg="green")
save_btn.place(x=60, y=250)

# Add button
add_btn = Button(window, text="Add", padx=15, pady=10, command=add, font=("Algerian", 9), cursor="dot", fg="green")
add_btn.place(x=140, y=250)

# Clear button
clear_btn = Button(window, text="Clear", padx=15, pady=10, command=clear, font=("Algerian", 9), cursor="dot",
                   fg="green")
clear_btn.place(x=210, y=250)

# Exit button
exit_btn = Button(window, text="Exit", padx=15, pady=10, command=window.quit, font=("Algerian", 9), cursor="dot",
                  fg="green")
exit_btn.place(x=295, y=250)

if __name__ == "__main__":
    window.mainloop()
