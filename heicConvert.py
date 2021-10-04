import tkinter as tk
import sys
import os
from tkinter.constants import ANCHOR
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


def select_file():
    filetypes = (
        ('image files', '*.PNG *.jpg *.jpeg *.HEIC'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/home/nathmart/src',
        filetypes=filetypes)
    print(filename)
    showinfo(
        title='Selected File',
        message=filename
    )


CONVERT = [
    "jpg",
    "HEIC",
    "PNG"
]

window = tk.Tk()

convert_variable = tk.StringVar(window)
convert_variable.set(CONVERT[0])
convert = tk.OptionMenu(window, convert_variable, *CONVERT)

button = tk.Button(
    text="Submit!",
    width=10,
    height=2,
    bg="blue",
    fg="white",
)
l2 = tk.Label(window, text="Filetype to convert to", font=('Aerial 12 bold'))

l2.grid(row=0, column=0, padx=10, pady=5)

convert.grid(row=1, column=0, padx=10, pady=5)

open_button = tk.Button(
    window,
    text='Open a File',
    command=select_file
)

open_button.grid(row=2, column=0, padx=10, pady=5)

button.grid(row=3, column=0, padx=10, pady=5)
window.mainloop()
