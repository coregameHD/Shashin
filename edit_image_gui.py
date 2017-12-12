from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
from PIL import Image, ImageEnhance, ImageDraw, ImageFont, ImagePalette, ImageFilter, ImageChops

import backend

class ShashinImageEditor:
    def about_dialog(self):
        messagebox.showinfo("About", "Built with Love")
        return

    def buttonFilter(self):
        mycolor = colorchooser.askcolor()
        colorRGBA = tuple(map(int, mycolor[0])) + (0,)
        print(colorRGBA)
        backend.imgColourFilter(colorRGBA)
        return

    def buttonFrame(self):
        backend.imgFrame()
        return


    def __init__(self):
        # Root window
        window = Tk()
        window.resizable(width=False, height=False)
        window.minsize(width=800, height=600)
        window.title("Shashin Image Editor")


        # Menu Bar
        menubar = Menu(window)
        window.config(menu = menubar)

        commandmenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "Command", menu = commandmenu)
        commandmenu.add_command(label = "Generate")
        commandmenu.add_command(label = "Copy to Clipboard")
        commandmenu.add_separator()
        commandmenu.add_command(label = "Exit", command = window.quit)

        aboutmenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "About", menu = aboutmenu)
        aboutmenu.add_command(label = "Github")
        aboutmenu.add_separator()
        aboutmenu.add_command(label = "About", command = self.about_dialog)


        # Main Program
        buttonFrame = Frame(window)
        buttonFrame.pack(side = LEFT)
        buttonBGColor = "pink"
        buttonWidth = 14
        buttonHeight = 2

        icon = PhotoImage(file='camera_icon.png')
        tempLb = Label(buttonFrame, image=icon).grid(row=1, column=1)

        bt1 = Button(buttonFrame,
                     background = "White",
                     text = "One-Click Beauty",
                     width=buttonWidth,
                     height=buttonHeight).grid(row = 2, column = 1)
        bt2 = Button(buttonFrame,
                     background = buttonBGColor,
                     text = "Sticker",
                     width=buttonWidth,
                     height=buttonHeight).grid(row = 3, column = 1)
        bt3 = Button(buttonFrame,
                     background = buttonBGColor,
                     text = "Effect",
                     width=buttonWidth,
                     height=buttonHeight).grid(row = 4, column = 1)
        bt4 = Button(buttonFrame,
                     background = buttonBGColor,
                     text = "Filter",
                     width=buttonWidth,
                     height=buttonHeight,
                     command = self.buttonFilter).grid(row = 5, column = 1)
        bt5 = Button(buttonFrame,
                     background = buttonBGColor,
                     text = "Frame",
                     width=buttonWidth,
                     height=buttonHeight,
                     command = self.buttonFrame).grid(row = 6, column = 1)
        bt6 = Button(buttonFrame,
                     background = buttonBGColor,
                     text = "Contrast",
                     width=buttonWidth,
                     height=buttonHeight).grid(row = 7, column = 1)
        bt7 = Button(buttonFrame,
                     background = buttonBGColor,
                     text = "Brightness",
                     width=buttonWidth,
                     height=buttonHeight).grid(row = 8, column = 1)
        bt8 = Button(buttonFrame,
                     background = buttonBGColor,
                     text = "Flip",
                     width=buttonWidth,
                     height=buttonHeight).grid(row = 9, column = 1)
        
        canvas = Canvas(window, width = 700, height = 600, bg = "white")
        canvas.pack(side = RIGHT, expand=YES, fill=BOTH)
        gif1 = PhotoImage(file='small_globe.gif')
        # pic's upper left corner (NW) on the canvas is at x=50 y=10
        canvas.create_image(150, 100, image=gif1, anchor=NW)
            
        window.mainloop()

ShashinImageEditor()
