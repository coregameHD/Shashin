from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageEnhance, ImageDraw, ImageFont, ImagePalette, ImageFilter, ImageChops
import backend
import os
import subprocess

class ShashinImageEditor:
    '''
    INSTANT VARIABLES
    global variables for internal use
    '''
    stickerVar = 0
    frameVar = 0
    brightnessVar = 0
    contrastVar = 0
    filterVar = (0,0,0,0)
    tintVar = (0,0,0,0)

    x = 0
    y = 0

    root = Tk()
    canvas = Canvas(root, width = 800, height = 600, bg = "gray")
    gif1 = PhotoImage(file="temp.png")
    canvas_img = canvas.create_image(0, 0, image=gif1, anchor=NW)

    sticker_dict = {x: os.path.dirname(os.path.abspath(__file__))+\
                    "/stickers/sticker"+str(x)+".png"\
                    for x in range(8)}
    frame_dict = {x: os.path.dirname(os.path.abspath(__file__))+\
                    "/frames/frame"+str(x)+".png"\
                    for x in range(8)}
    
    '''
    SETTER FUNCTIONS
    change the value of global variable
    '''
    def beautify(self):
        backend.imgBeauty()
        self.updateCanvas()
        return
    
    def changeStickerValue(self, val, top):
        self.stickerVar = val
        print('sticker = ', end="")
        print(self.stickerVar)
        top.destroy()

        self.canvas.bind('<Button-1>', lambda e: "break")
        backend.imgSticker(self.sticker_dict[self.stickerVar], (self.x - 80, self.y - 80)) 
        self.updateCanvas()
        return

    def changeFrameValue(self, val, top):
        self.frameVar = val
        print('frame = ', end="")
        print(self.frameVar)
        top.destroy()

        backend.imgFrame(self.frame_dict[self.frameVar])
        self.updateCanvas()
        return

    def changeBrightnessValue(self, val, top):
        self.brightnessVar = val
        print('brightness = ', end="")
        print(self.brightnessVar)
        top.destroy()

        backend.imgBrightness((self.brightnessVar / 100.0) + 1)
        self.updateCanvas()
        return

    def changeContrastValue(self, val, top):
        self.contrastVar = val
        print('contrast = ', end="")
        print(self.contrastVar)
        top.destroy()

        backend.imgContrast((self.contrastVar / 100.0) + 1)
        self.updateCanvas()
        return

    '''
    HELPER
    helper functions / utility functions
    '''
    def updateCanvas(self):
        self.gif1.configure(file="temp.png")

    def on_click(self, event):
        self.x, self.y = event.x, event.y
        userPosition = (self.x, self.y)
        print(userPosition)

    def reset(self):
        self.reload()
        self.updateCanvas()

    def aboutDialog(self):
        messagebox.showinfo("About", "Built with Love")
        return

    def buttonFrame(self):
        backend.imgFrame()
        return

    '''
    DIALOG
    function to handle all pop-up dialog
    '''
    def stickerDialog(self):
        self.canvas.bind('<Button-1>', self.on_click)
        stickerWindow = Toplevel()
        stickerWindow.resizable(width=False, height=False)
        stickerWindow.minsize(width=600, height=600)
        stickerWindow.title("Select sticker")
        stickerCanvas = Canvas(stickerWindow, width = 600, height = 400, bg = "gray")
        stickerCanvas.grid(row=0, column=0, columnspan=2)
        previewImg = PhotoImage(file=os.path.dirname(os.path.abspath(__file__))+\
                    "/stickers/stickers.png")
        stickerCanvas.create_image(0, 0, image=previewImg, anchor=NW)
        stickerCanvas.canvas = previewImg
        
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
                                  text = "OK", command=lambda : self.changeStickerValue(var.get(), stickerWindow))
        stickerOKButton.grid(columnspan=2)

        infoLabel = Label(stickerWindow, text="** Please select position on the image **", fg = "red").grid(columnspan = 2)

    def frameDialog(self):
        frameWindow = Toplevel()
        frameWindow.resizable(width=False, height=False)
        frameWindow.minsize(width=600, height=600)
        frameWindow.title("Select frame")
        frameCanvas = Canvas(frameWindow, width = 600, height = 400, bg = "gray")
        frameCanvas.grid(row=0, column=0, columnspan=2)
        previewImg = PhotoImage(file=os.path.dirname(os.path.abspath(__file__))+\
                    "/frames/frames.png")
        frameCanvas.create_image(0, 0, image=previewImg, anchor=NW)
        frameCanvas.canvas = previewImg
        
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
                                  text = "OK", command=lambda : self.changeFrameValue(var.get(), frameWindow))
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
                                  command = lambda : self.changeBrightnessValue(brightnessScale.get(), brightnessWindow))
        brightnessOKButton.pack()
        brightnessWindow.mainloop()

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
                                  command = lambda : self.changeContrastValue(contrastScale.get(), contrastWindow))
        contrastOKButton.pack()
        contrastWindow.mainloop()
        
    def filterDialog(self):
        mycolor = colorchooser.askcolor()
        colorRGBA = tuple(map(int, mycolor[0])) + (0,)
        print(colorRGBA)
        backend.imgColourFilter(colorRGBA)

        self.updateCanvas()
        return

    def tintDialog(self):
        mycolor = colorchooser.askcolor()
        colorRGBA = tuple(map(int, mycolor[0])) + (0,)
        print(colorRGBA)
        backend.imgTint(colorRGBA)

        self.updateCanvas()
        return
   
    '''
    __INIT__
    App Initialization
    '''
    def appInitHelper(self, root, canvas):
        self.buttonPaneInit(root, canvas)
        self.menuBarInit(root, canvas)
        canvas.pack()

    def buttonPaneInit(self, root, canvas):
        # Button init
        buttonBGColor = "pink"
        buttonWidth = 14
        buttonHeight = 2
        buttonFrame = Frame(root)

        # App name
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
                     width = buttonWidth,
                     height = buttonHeight,
                     command=self.beautify).grid(row = 3, column = 1)

        # sticker/frame
        stickerButton = Button(buttonFrame,
                     background = buttonBGColor,
                     text = "Sticker",
                     width = buttonWidth,
                     height = buttonHeight,
                     command=self.stickerDialog).grid(row = 4, column = 1)
        frameButton = Button(buttonFrame,
                     background = buttonBGColor,
                     text = "Frame",
                     width = buttonWidth,
                     height = buttonHeight,
                     command = self.frameDialog).grid(row = 5, column = 1)

        # brightness/contrast
        brightnessButton = Button(buttonFrame,
                     background = buttonBGColor,
                     text = "Brightness",
                     width = buttonWidth,
                     height = buttonHeight,
                     command = self.brightnessDialog).grid(row = 6, column = 1)
        contrastButton = Button(buttonFrame,
                     background = buttonBGColor,
                     text = "Contrast",
                     width = buttonWidth,
                     height = buttonHeight,
                     command = self.contrastDialog).grid(row = 7, column = 1)

        # filter/tint
        filterButton = Button(buttonFrame,
                     background = buttonBGColor,
                     text = "Filter",
                     width = buttonWidth,
                     height = buttonHeight,
                     command = self.filterDialog).grid(row = 8, column = 1)
        tintButton = Button(buttonFrame,
                     background = buttonBGColor,
                     text = "Tint",
                     width = buttonWidth,
                     height = buttonHeight,
                     command = self.tintDialog).grid(row = 9, column = 1)
        # save
        saveButton = Button(buttonFrame,
                     background = "green",
                     foreground = "white",
                     width = buttonWidth,
                     height = buttonHeight,
                     text = "Save",
                     command = self.saveToDisk).grid(row = 10, column = 1, sticky="SW")
        # reset
        resetButton = Button(buttonFrame,
                     background = "red",
                     foreground = "white",
                     width = buttonWidth,
                     height = buttonHeight,
                     text = "Reset",
                     command = self.reset).grid(row = 11, column = 1, sticky="SW")
        buttonFrame.pack(side = LEFT)
        
    def menuBarInit(self, root, canvas):
        menubar = Menu(root)
        
        # Command
        commandmenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "Command", menu = commandmenu)
        commandmenu.add_command(label = "Exit", command = root.destroy)
        root.config(menu = menubar)

        # About
        aboutmenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "About", menu = aboutmenu)
        aboutmenu.add_command(label = "Github")
        aboutmenu.add_separator()
        aboutmenu.add_command(label = "About", command = self.aboutDialog)

        root.config(menu = menubar)

    def reload(self):
        original = Image.open("input.png").convert('RGBA')
        original = original.resize((800,600))
        original.save("./temp.png")

    def saveToDisk(self):
        original = Image.open("temp.png").convert('RGBA')
        original.save("./output.png")

        # For printing process
        # lpr =  subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
        # lpr.stdin.write(your_data_here)
    
    def __init__(self):
        # Root window
        self.root.resizable(width=False, height=False)
        self.root.minsize(width=800, height=600)
        
        self.root.title("Shashin Image Editor")
        self.appInitHelper(self.root, self.canvas)
        self.reload()
        self.updateCanvas()
        self.root.mainloop()
