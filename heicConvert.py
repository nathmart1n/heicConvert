import tkinter as tk
import sys
import os
from tkinter.constants import ANCHOR
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )


SOURCE = [
    "HEIC",
    "PNG",
    "JPG"
]

CONVERT = [
    "JPG",
    "HEIC",
    "PNG"
]

window = tk.Tk()
window.geometry("350x200")
source_variable = tk.StringVar(window)
source_variable.set(SOURCE[0])
source = tk.OptionMenu(window, source_variable, *SOURCE)

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
l1 = tk.Label(window, text="Source Filetype", font=('Aerial 12 bold'))
l2 = tk.Label(window, text="Converted Filetype", font=('Aerial 12 bold'))

l1.grid(row=0, column=0, padx=10, pady=5)
l2.grid(row=0, column=1, padx=3, pady=5)

source.grid(row=1, column=0, padx=10, pady=5)
convert.grid(row=1, column=1, padx=10, pady=5)

open_button = tk.Button(
    window,
    text='Open a File',
    command=select_file
)

open_button.grid(row=2, columnspan=2)

button.grid(row=3, columnspan=2)
window.mainloop()
