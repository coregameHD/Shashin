from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageEnhance, ImageDraw, ImageFont, ImagePalette, ImageFilter, ImageChops

import backend

class ShashinImageEditor:
    stickerVar = 0
    frameVar = 0
    brightnessVar = 0
    contrastVar = 0
    filterVar = (0,0,0,0)
    tintVar = (0,0,0,0)

    '''
    CHANGE STATE
    change the value of global variable
    '''
    def changeStickerValue(self, val):
        self.stickerVar = val
        print('sticker = ', end="")
        print(self.stickerVar)
        return

    def changeFrameValue(self, val):
        self.frameVar = val
        print('frame = ', end="")
        print(self.frameVar)
        return

    def changeBrightnessValue(self, val):
        self.brightnessVar = val
        print('brightness = ', end="")
        print(self.brightnessVar)
        return

    def changeContrastValue(self, val):
        self.contrastVar = val
        print('contrast = ', end="")
        print(self.contrastVar)
        return

    '''
    DIALOG
    function to handle all pop-up dialog
    '''
    def stickerDialog(self):
        stickerWindow = Toplevel()
        stickerWindow.resizable(width=False, height=False)
        stickerWindow.minsize(width=600, height=600)
        stickerWindow.title("Select sticker")
        stickerCanvas = Canvas(stickerWindow, width = 600, height = 400, bg = "gray")
        stickerCanvas.grid(row=0, column=0, columnspan=2)
        
        var = IntVar()
        var.set(0)
        for i in range(8):
            b = Radiobutton(stickerWindow, text="Sticker " + str(i+1), variable=var, value=i)
            if i < 4:
                b.grid(row=(i%4)+1, column=0)
            else:
                b.grid(row=(i%4)+1, column=1)
            b.select()
        stickerOKButton = Button(stickerWindow, width = 14, height = 2,
                                  background="pink",
                                  text = "OK", command=lambda : self.changeStickerValue(var.get()))
        stickerOKButton.grid(columnspan=2)

    def frameDialog(self):
        frameWindow = Toplevel()
        frameWindow.resizable(width=False, height=False)
        frameWindow.minsize(width=600, height=600)
        frameWindow.title("Select frame")
        frameCanvas = Canvas(frameWindow, width = 600, height = 400, bg = "gray")
        gif2 = PhotoImage(file='small_globe.gif')
        frameCanvas.create_image(10, 50, image=gif2, anchor=NW)
        frameCanvas.grid(row=0, column=0, columnspan=2)
        
        var = IntVar()
        var.set(0)
        for i in range(8):
            b = Radiobutton(frameWindow, text="frame " + str(i+1), variable=var, value=i)
            if i < 4:
                b.grid(row=(i%4)+1, column=0)
            else:
                b.grid(row=(i%4)+1, column=1)
            b.select()
        frameOKButton = Button(frameWindow, width = 14, height = 2,
                                  background="pink",
                                  text = "OK", command=lambda : self.changeFrameValue(var.get()))
        frameOKButton.grid(columnspan=2)

    def brightnessDialog(self):
        brightnessWindow = Toplevel()
        brightnessWindow.resizable(width=False, height=False)
        brightnessWindow.minsize(width=400, height=120)
        brightnessWindow.title("Adjust Brightness")
        brightnessScale = Scale(brightnessWindow, from_=-100, to=100,
                             length=300, tickinterval=10,
                             troughcolor="red",
                             orient=HORIZONTAL)
        brightnessScale.set(0)
        brightnessScale.pack()
        brightnessOKButton = Button(brightnessWindow,
                                  background="red",
                                  foreground="white",
                                  text = "OK",
                                  command = lambda : self.changeBrightnessValue(brightnessScale.get()))
        brightnessOKButton.pack()
        brightnessWindow.mainloop()

    def closeBrightnessDialog(self):
        self.destroy()

    def contrastDialog(self):
        contrastWindow = Toplevel()
        contrastWindow.resizable(width=False, height=False)
        contrastWindow.minsize(width=400, height=120)
        contrastWindow.title("Adjust Contrast")
        contrastScale = Scale(contrastWindow, from_=-100, to=100,
                             length=300, tickinterval=10,
                             troughcolor="pink",
                             orient=HORIZONTAL)
        contrastScale.set(0)
        contrastScale.pack()
        contrastOKButton = Button(contrastWindow,
                                  background="pink",
                                  text = "OK",
                                  command = lambda : self.changeContrastValue(contrastScale.get()))
        contrastOKButton.pack()
        contrastWindow.mainloop()
        
    def closeContrastDialog(self):
        self.destroy()
        #print(contrastScale.get())
        #selection = "Value = " + str(contrastScale.get())
        #label1.config(text = selection)

        
        #canvas.destroy()
        #self.destroy()
        #return w.contrastScale.get()


    def filterDialog(self):
        mycolor = colorchooser.askcolor()
        colorRGBA = tuple(map(int, mycolor[0])) + (0,)
        print(colorRGBA)
        backend.imgColourFilter(colorRGBA)
        return

    # @todo driver function of tint (from backend)
    def tintDialog(self):
        mycolor = colorchooser.askcolor()
        colorRGBA = tuple(map(int, mycolor[0])) + (0,)
        print(colorRGBA)
        backend.imgColourFilter(colorRGBA)
        return
    

    

   
    '''
    HELPER
    helper function
    '''
    def displayImageOnCanvas(self, canvas):
        #gif1 = PhotoImage(file='small_globe.gif')
        #canvas.create_image(150, 100, image=gif1, anchor=NW)
        gif1 = PhotoImage(file='small_globe.gif')
        canvas.create_image(150, 100, image=gif1, anchor=NW)

    def aboutDialog(self):
        messagebox.showinfo("About", "Built with Love")
        return

    def buttonFrame(self):
        backend.imgFrame()
        return

    '''
    __INIT__
    App Initialization
    '''
    def appInitHelper(self, root, canvas):
        self.buttonPaneInit(root, canvas)
        self.menuBarInit(root, canvas)
        self.displayImageOnCanvas(canvas)
        canvas.pack()
        #canvas.pack(side = RIGHT, expand=YES, fill=BOTH)

    def buttonPaneInit(self, root, canvas):
        # Buttons
        buttonBGColor = "pink"
        buttonWidth = 14
        buttonHeight = 2
        buttonFrame = Frame(root)

        #icon = PhotoImage(file='camera_icon.png')

        logoLabelEng = Label(buttonFrame, text="Shashin")
        logoLabelEng.config(font=("Courier", 16))
        logoLabelEng.grid(row=1, column=1, sticky="N")
        
        logoLabelJap = Label(buttonFrame, text="写真")
        logoLabelJap.config(font=("Courier", 32))
        logoLabelJap.grid(row=2, column=1, sticky="N")

        # 1-click beauty
        oneClickBeautyButton = Button(buttonFrame,
                     background = "White",
                     text = "One-Click Beauty",
                     width=buttonWidth,
                     height=buttonHeight).grid(row = 3, column = 1)

        # sticker/frame
        stickerButton = Button(buttonFrame,
                     background = buttonBGColor,
                     text = "Sticker",
                     width=buttonWidth,
                     height=buttonHeight,
                     command=self.stickerDialog).grid(row = 4, column = 1)
        frameButton = Button(buttonFrame,
                     background = buttonBGColor,
                     text = "Frame",
                     width=buttonWidth,
                     height=buttonHeight,
                     command = self.buttonFrame).grid(row = 5, column = 1)

        # brightness/contrast
        brightnessButton = Button(buttonFrame,
                     background = buttonBGColor,
                     text = "Brightness",
                     width=buttonWidth,
                     height=buttonHeight,
                     command = self.brightnessDialog).grid(row = 6, column = 1)
        contrastButton = Button(buttonFrame,
                     background = buttonBGColor,
                     text = "Contrast",
                     width=buttonWidth,
                     height=buttonHeight,
                     command = self.contrastDialog).grid(row = 7, column = 1)

        # filter/tint
        filterButton = Button(buttonFrame,
                     background = buttonBGColor,
                     text = "Filter",
                     width=buttonWidth,
                     height=buttonHeight,
                     command = self.filterDialog).grid(row = 8, column = 1)
        tintButton = Button(buttonFrame,
                     background = buttonBGColor,
                     text = "Tint",
                     width=buttonWidth,
                     height=buttonHeight,
                     command = self.tintDialog).grid(row = 9, column = 1)

        # just-in-case (can be removed)
        dummyButton = Button(buttonFrame,
                     background = buttonBGColor,
                     text = "______",
                     width=buttonWidth,
                     height=buttonHeight).grid(row = 10, column = 1)

        # reset
        resetButton = Button(buttonFrame,
                     background = "red",
                     foreground = "white",
                     width=buttonWidth,
                     height=buttonHeight,
                     text = "Reset").grid(row = 11, column = 1, sticky="SW")

        buttonFrame.pack(side = LEFT)

    def menuBarInit(self, root, canvas):
        # Menu Bar
        menubar = Menu(root)

        commandmenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "Command", menu = commandmenu)
        commandmenu.add_command(label = "Generate")
        commandmenu.add_command(label = "Copy to Clipboard")
        commandmenu.add_separator()
        commandmenu.add_command(label = "Exit", command = root.quit)
        root.config(menu = menubar)

        aboutmenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "About", menu = aboutmenu)
        aboutmenu.add_command(label = "Github")
        aboutmenu.add_separator()
        aboutmenu.add_command(label = "About", command = self.aboutDialog)

        root.config(menu = menubar)

    def __init__(self):
        # Root window
        root = Tk()
        root.resizable(width=False, height=False)
        root.minsize(width=800, height=600)
        root.title("Shashin Image Editor")
        canvas = Canvas(root, width = 700, height = 600, bg = "gray")

        self.appInitHelper(root, canvas)
        gif1 = PhotoImage(file='small_globe.gif')
        canvas.create_image(150, 100, image=gif1, anchor=NW)

        root.mainloop()

ShashinImageEditor()
