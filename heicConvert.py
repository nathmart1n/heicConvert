import tkinter as tk
import sys
import os
from PIL import Image, ExifTags
from tkinter.constants import ANCHOR
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


class Convert():
    def __init__(self):
        self.convertType = 'jpg'
        self.filePath = '/'

    def UpdateConvertType(self, newType):
        self.convertType = newType
        print(self.convertType)

    def UpdateFilePath(self):
        filetypes = (
            ('image files', '*.png *.jpg *.jpeg *.HEIC'),
            ('All files', '*.*')
        )

        self.filePath = fd.askopenfilename(
            title='Open a file',
            initialdir='/home/nathmart/src/heicConvert',
            filetypes=filetypes)

    def ConvertImage(self):
        im = Image.open(self.filePath)
        if im._getexif():
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break
            exif = dict(im._getexif().items())

            if exif[orientation] == 3:
                im = im.rotate(180, expand=True)
            elif exif[orientation] == 6:
                im = im.rotate(270, expand=True)
            elif exif[orientation] == 8:
                im = im.rotate(90, expand=True)
        im.save('test.' + self.convertType)

        showinfo(
            title='File Converted!',
            message='File Converted! The new image is in the same location as the old one.'
        )


def callback(selection):
    convertType = selection
    print(convertType)


newConvert = Convert()

CONVERT = [
    "jpg",
    "heic",
    "png"
]

window = tk.Tk()

convert_variable = tk.StringVar(window)
convert_variable.set(CONVERT[0])
convert = tk.OptionMenu(window, convert_variable, *CONVERT, command=newConvert.UpdateConvertType)

l2 = tk.Label(window, text="Filetype to convert to", font=('Aerial 12 bold'))

l2.grid(row=0, column=0, padx=10, pady=5)

convert.grid(row=1, column=0, padx=10, pady=5)

open_button = tk.Button(
    window,
    text='Select File',
    command=newConvert.UpdateFilePath
)

open_button.grid(row=2, column=0, padx=10, pady=5)

submit_button = tk.Button(
    window,
    width=10,
    height=2,
    bg="blue",
    fg="white",
    text='Submit!',
    command=newConvert.ConvertImage
)

submit_button.grid(row=3, column=0, padx=10, pady=5)

window.mainloop()
