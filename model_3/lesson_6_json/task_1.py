import csv
import tkinter as tk
from tkinter import ttk
from model_3.exceptions import exceptins_func
import requests


KEY = 'gKOeS2ZI3wK4zTeGcKeZ8dgBp9psidFl1ntV2cAR'
url = f"https://api.freecurrencyapi.com/v1/latest?apikey={KEY}"
resp = requests.get(url)

window = tk.Tk()
window.title("Currency Converter")
window.geometry("300x400")
file_path = "exchange.csv"


def add():
    try:
        with open(file_path, "a", newline="\n") as f:
            file = csv.writer(f)
            file.writerow([combo_usd.get(), combo_eur.get()])
            file.writerow([main_money.get(), next_money.get()])
    except FileNotFoundError as e:
        exceptins_func(e)


def clear():
    main_money.delete(0, tk.END),
    next_money.delete(0, tk.END)


main_money = tk.Entry(window, width=18, fg="red")
main_money.place(x=10, y=20)

next_money = tk.Entry(window, width=18, fg="red")
next_money.place(x=180, y=20)

value = tk.Label(window, padx=20, pady=10)
value.place(x=118, y=65)

window_btn = tk.Button(window, text="⇆", padx=7, pady=2, bg="green")
window_btn.place(x=135, y=15)

combo_usd = ttk.Combobox(window, width=15, )
combo_usd["values"] = ["USD", "EUR"]
combo_usd.current(0)
combo_usd.place(x=10, y=80)

combo_eur = ttk.Combobox(window, width=15)
combo_eur["values"] = ["EUR", "USD"]
combo_eur.current(0)
combo_eur.place(x=180, y=80)

# Clear
clear_batten = tk.Button(window, text="Clear", padx=10, pady=10, command=clear, bg="green")
clear_batten.place(x=175, y=120)
# Add
add_batten = tk.Button(window, text="Add", padx=10, pady=10, command=add, bg="green")
add_batten.place(x=70, y=120)
if __name__ == "__main__":
    window.mainloop()
