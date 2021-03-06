import tkinter as tk
import random as rnd
import PIL.Image as image
import PIL.ImageTk as imageTk
import PIL.ImageFile as imageF
import PIL.ImageDraw as imageD
import time

class OutputFrame(tk.Frame):
    directory = ""
    name = "maze"
    img = None
    buttons = []

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        #self.createButtonField(20, 20)
        #self.createWidgets()
    
    def generatePicture(self, mazeSize, bitmap, directory, filename):
        timeAm = time.clock()
        im = image.new("1", mazeSize)
        pixels = im.load()
        
        timeA = time.clock()
        for i in range (mazeSize[0]):
            for j in range (mazeSize[1]):
                pixels[i, j] = bitmap[i][j]
        timeB = time.clock()

        im.save(directory + "\\" + filename + ".png", "PNG")
        self.img = im
        self.directory = directory + "\\" + filename + ".png"
        timeC = time.clock()

        print("time: ", timeA-timeAm, " AB - ", timeB-timeA, " BC - ", timeC-timeB)
        print("total: ", timeC-timeA)

        #im.show()
        self.createWidgets()

    def createButtonField(self, rows, columns):
        for i in range(rows):
            buttons = []
            for j in range(columns):
                button = self.createButton("", "", i, j, bg = "black")
                buttons.append(button)
            self.buttons.append(buttons)

        (self.buttons[4][0])["bg"] = "white"
        (self.buttons[18][19])["bg"] = "white"

        for i in range(1, 19):
            for j in range(1, 19):
                colors = ['white'] * 60 + ['black'] * 40
                color = rnd.choice(colors)
                (self.buttons[i][j])["bg"] = color
    
    def createWidgets(self):
        img = image.open(self.directory)
        size = (self.img.size[0]*2, self.img.size[1]*2)
        img = img.resize(size)
        self.img = imageTk.PhotoImage(img)
        self.createImageField(0, 0)
        
    def createImageField(self, row, column):
        #self.img = self.img.thumbnail(size)
        self.image = tk.Label(self, image=self.img)
        self.pack()
        self.image.grid(column = column, row = row)

    def createButton(self, text, command, row, column, bg = None, columnSpan = 1):
            self.button = tk.Button(self)
            self.button["text"] = text
            self.button["bg"] = bg
            self.button["command"] = command
            self.button.config(width = 1, height = 1)
            self.button.grid(column=column, row=row, columnspan=columnSpan, sticky="NSEW")
            return self.button