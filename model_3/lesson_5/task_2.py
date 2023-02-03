# translate package orqali tarjimon app qilish, har bir tarjima qilingan sozlarni
# istoriya sifatida csv faylga saqlab borish sana va soati bilan birga. Tarjima da
# ishlatiladigan tillar kodini bu yerdan olish mumkin


import csv
import tkinter as tk
from model_3.exceptions import exceptins_func
from tkinter import ttk
from tkinter.messagebox import showinfo
from translate import Translator

window = tk.Tk()
window.title("Translation")
window.geometry("300x400")

file_path = "translation.csv"


# Add function
def add():
    try:
        with open(file_path, "a", newline="\n") as f:
            file = csv.writer(f)
            file.writerow(["Translation", "The word you entered"])
            file.writerow([translation_entry.get(), translate_entry.get()])
    except FileNotFoundError as e:
        exceptins_func(e)


# Clear function
def clear():
    translate_entry.delete(0, tk.END),
    translation_entry.delete(0, tk.END)


# Translate function
def translate_func():
    try:
        translate_entry.get()
        translator = Translator(to_lang=combo.get())
        translation = translator.translate(translate_entry.get())
        text.set(translation)
    except:
        showinfo(("Erorr"), "\nError")


translate_label = tk.Label(window, padx=20, pady=10, text="Write here", fg="green")
translate_label.grid(row=0, column=0)
translate_entry = tk.Entry(window, width=30, borderwidth=3)
translate_entry.grid(row=0, column=1)

combo = ttk.Combobox(window, width=25)
combo["values"] = ["ru", "zu", "zh", "yo", "ur", "uz", "uk", "en", "tr", "tk", "tg", "tt", "sr", "sq",
                   "pt", "no", "mk", "la", "lg", "ko", "kk", "kn", "ja", "it", "hi", "de", "fr", "ar", "az", "af"]
combo.current(0)
combo.place(x=100, y=120)

# Add
add_btn = tk.Button(window, text="Add", padx=15, pady=10, fg="green", command=add)
add_btn.place(x=25, y=120)

# Clear
clear_btn = tk.Button(window, text="Clear", padx=15, pady=10, fg="green", command=clear)
clear_btn.place(x=25, y=170)

translation_label = tk.Label(window, padx=20, pady=10, text="Translations", fg="green")
translation_label.place(x=5, y=70)

text = tk.StringVar()
translation_entry = tk.Entry(window, textvariable=text, width=30, borderwidth=3)
translation_entry.place(x=100, y=80)

translate_btn = tk.Button(text="Translation", padx=20, pady=3, width=20, bg="green", command=translate_func)
translate_btn.grid(row=5, column=1)

if __name__ == "__main__":
    window.mainloop()
