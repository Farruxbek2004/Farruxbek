from tkinter import *
from transliterate import *


def translate():
    la = to_cyrillic(var1.get())
    var2.set(la)


def swappp():
    lan1.set('Cryil')
    lan2.set('Latin')


def clouse():
    target.destroy()


target = Tk()
target.title('Translate ')
target['background'] = 'yellow'

main = Frame(target)
main.grid(column=0, row=0, sticky=(N, W, E, S))
main.columnconfigure(0, weight=4)
main.rowconfigure(0, weight=1)
main.pack(pady=50, padx=90)

lan1 = StringVar(target)
lan2 = StringVar(target)

chose = {'Latin', 'Cryil'}

lan1main = OptionMenu(main, lan1, *chose).grid(row=1, column=3)
lan1.set('Latin')
lan2main = OptionMenu(main, lan2, *chose).grid(row=1, column=1)
lan2.set('Cryil')


Label(main, text='enter text :').grid(row=2, column=0)
var1 = StringVar()
enterr = Entry(main, textvariable=var1).grid(row=2, column=1)


Label(main, text='out pout').grid(row=2, column=2)
var2 = StringVar()
enter = Entry(main, textvariable=var2).grid(row=2, column=3)


value = Button(main, text='Translate ', command=translate).grid(row=3, column=1, columnspan=3)
result = Button(main, text='Exit', command=clouse).grid(row=5, column=12, columnspan=5)
res = Button(main, text='↔️', command=swappp).grid(row=1, column=2)


target.mainloop()
