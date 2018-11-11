import tkinter as tk
import tkinter.filedialog as fdialog
import tkinter.messagebox as msgbox
import output_frame as outf
import validator
import random as rnd
import maze_generator_depth_first_search as maze_generator

class InputFrame(tk.Frame):
    mazeSizeX = None
    mazeSizeY = None
    minMazeSize = (4, 4)
    multiplePaths = False
    startPosX = None
    startPosY = None
    endPosX = None
    endPosY = None
    directory = ""
    filename = ""
    pic = None

    def __init__(self, picture, master=None):
        tk.Frame.__init__(self, master)
        self.pic = picture
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.createLabel("Maze size", 0, 0)
        self.mazeSizeX = self.createTextField(0, 1, tk.IntVar(self))
        self.mazeSizeY = self.createTextField(0, 2, tk.IntVar(self))

        self.createLabel("Multiple Paths?", 1, 0)
        self.multiplePaths = self.createCheckbox(1, 1, True, False, tk.BooleanVar(self))

        self.createLabel("Start position", 2, 0)
        self.startPosX = self.createTextField(2, 1, tk.IntVar(self))
        self.startPosY = self.createTextField(2, 2, tk.IntVar(self))

        self.createLabel("End position", 3, 0)
        self.endPosX = self.createTextField(3, 1, tk.IntVar(self))
        self.endPosY = self.createTextField(3, 2, tk.IntVar(self))

        self.createLabel("Maze Location", 4, 0)
        self.createFileDialog("...", 4, 1, command = self.loadDirectory, columnSpan = 2)
        
        self.createLabel("Maze filename", 5, 0)
        self.filename = self.createTextField(5, 1, tk.StringVar(self), columnSpan = 2)

        self.createButton("GENERATE", self.generate, 6, 0, columnSpan = 2)

        self.createButton("QUIT", self.quit, 6, 2, "red") #root.destroy


    def createButton(self, text, command, row, column, fg = None, columnSpan = 1):
        self.button = tk.Button(self)
        self.button["text"] = text
        self.button["fg"] = fg
        self.button["command"] = command
        self.button.grid(column=column, row=row, columnspan=columnSpan, sticky="NSEW")

    def createLabel(self, text, row, column):
        self.label = tk.Label(self)
        self.label["text"] = text
        self.label.grid(column=column, row=row)

    def createCheckbox(self, row, column, onValue, offValue, variable, columnSpan = 1):
        self.checkbox = tk.Checkbutton(self)
        self.checkbox["variable"] = variable
        self.checkbox["onvalue"] = onValue
        self.checkbox["offvalue"] = offValue
        self.checkbox.grid(column=column, row=row, columnspan = columnSpan)
        return variable

    def createFileDialog(self, text, row, column, command, columnSpan = 1):
        self.fileDialog = tk.Button(self)
        self.fileDialog["text"] = text
        self.fileDialog["command"] = command
        self.fileDialog.grid(column = column, row = row, columnspan = columnSpan, sticky="NSEW")

    def loadDirectory(self):
        self.directory = fdialog.askdirectory()

    def createTextField(self, row, column, variable, columnSpan = 1):
        self.textField = tk.Entry(self)
        self.textField["textvariable"] = variable
        self.textField.grid(column = column, row = row, columnspan = columnSpan, sticky = "NSEW")
        return variable

    #def createImageField(self, location, row, column, rowspan = 1):
    #    self.image = tk.Label(self, image=self.img)
    #    self.image.grid(column = column, row = row, rowspan = rowspan)

    def generate(self):
        mazeSize = (self.mazeSizeX.get(), self.mazeSizeY.get())
        print ("Maze size - ", mazeSize)

        multiplePaths = self.multiplePaths.get()
        print ("Multiple paths - ", multiplePaths)
        
        startPos = (self.startPosX.get() - 1, self.startPosY.get() - 1)
        print ("Start Position - ", startPos)
        
        endPos = (self.endPosX.get() - 1, self.endPosY.get() - 1)
        print ("End Position - ", endPos)
        
        directory = self.directory
        print ("Directory - ", self.directory)

        filename = self.filename.get()
        print ("Filename - ", filename)

        print("Validating...")
        val_obj = validator.Validator()
        result = val_obj.validateInput(self.minMazeSize, mazeSize, startPos, endPos, directory, filename)
        
        if not(result is None):
            msgbox.showerror(title="Error!", message=result)
        else:
            print("Success!!!")
            self.generateMaze(mazeSize, startPos, endPos, directory, filename)

    def generateMaze(self, mazeSize, startPos, endPos, directory, filename):
        bitmap = maze_generator.generate_maze(mazeSize)
        print(bitmap)
        self.pic.generatePicture(mazeSize, bitmap, directory, filename)
