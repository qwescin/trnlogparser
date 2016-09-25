#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Roman'

from tkinter import *
from tkinter import ttk
from tkinter import filedialog


def calculate(*args):
    pass


def openfile():                             # диалог открытия файла
    filename = filedialog.askopenfilename()
    file_path.set(filename)


def search_in_file():                       # поиск номера телефона в файле и выделение блоков его вхождения
    block =''
    flag = True
    count = 0
    with open(str(file_path.get()), 'r') as f:
        for string in f:
            block += string
            if string.startswith('\n'):
                if str(phone_number.get()) in block:
                    text.insert('end', block)
                    count += 1
                block = ''
                continue

    print(count)




root = Tk()
root.title("TRN log parser")
root.geometry('1000x550+500+300')
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(3, weight=1)


file_path = StringVar()
phone_number = StringVar()

ttk.Button(mainframe, text="open file", command=openfile).grid(column=1, row=1, sticky=(N, W, E), padx=5, pady=5)
file_route = ttk.Entry(mainframe, width=40, textvariable=file_path)
file_route.grid(column=0, row=1, sticky=(N, W, E), padx=5, pady=5)

ttk.Button(mainframe, text="search", command=search_in_file).grid(column=1, row=2, sticky=(N, W, E), padx=5, pady=5)
search_phone = ttk.Entry(mainframe, width=40, textvariable=phone_number)
search_phone.grid(column=0, row=2, sticky=(N, W, E), padx=5, pady=5)

text = Text(mainframe, wrap=NONE)
text.grid(column=0, row=3, columnspan=2, sticky=(N, S, E, W), padx=(5, 0), pady=(5, 0))
yscroll = ttk.Scrollbar(mainframe, orient=VERTICAL, command=text.yview)
yscroll.grid(column=2, row=3, sticky=(N, S), padx=0, pady=5)
xscroll = ttk.Scrollbar(mainframe, orient=HORIZONTAL, command=text.xview)
xscroll.grid(column=0, row=4, columnspan=2, sticky=(W, E), padx=5, pady=0)
text.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)

#ttk.Sizegrip(mainframe).grid(column=4, row=4)

# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)






#root.bind('<Return>', calculate)

root.mainloop()
