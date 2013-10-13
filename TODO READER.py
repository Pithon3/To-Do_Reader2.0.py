#-------------------------------------------#
# TODO Reader 2.0 - Aidan S (Idea by Erik D)#
#-------------------------------------------#
# Version 2.0 Details:                      #
#     New GUI look                          #
#     Multiple Lists                        #
#     Structured classes                    # 
#-------------------------------------------#

#Import Declarations
from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()

        self.Buttons = []

        file = open("ToDoMainfile.txt", "a")
        file.close()

        tempfile = open("ToDoMainfile.txt", "r")
        self.filenames = tempfile.readlines()
        tempfile.close()

        index = 0
        for name in self.filenames:
            self.filenames[index] = name.replace("\n", "")
            index += 1
        
        self.files = []
        for filename in self.filenames:
            file = open(filename, "a+")
            self.files.append(file)
            file.close()

        self.startlayout()

    def startlayout(self):
        WelcomeL = Label(self, text = "                             Welcome to the To-Do Reader 2.0!                             ")
        WelcomeL.grid(columnspan = 6)

        nwrow = 2
        
        if self.files:
            YesFileLabel = Label(self, text = "Your todo lists:")
            YesFileLabel.grid()

            for filename in self.filenames:
                NewButton(filename)
                nwrow += 1
                
        else:
            NoFileL = Label(self, text = "You curently have no todo lists.")
            NoFileL.grid(columnspan = 2)

        Spacer1 = Label(self, text = "")
        Spacer1.grid(row = nwrow)
        AddFileL = Label(self, text = "Add a file:")
        AddFileL.grid(row = nwrow, sticky = W)

        self.AddFile_ent = Entry(self)
        self.AddFile_ent.grid(row = nwrow, column = 1)
        self.AddFile_ent.insert(0, "TODO")

        AddFileB = Button(self, text = "  OK  ", command = self.addfile)
        AddFileB.grid(row = nwrow, column = 2, sticky = W)

    def addfile(self):
        filename = self.AddFile_ent.get() + ".txt"
        file = open(filename, "a+")
        self.files.append(file)
        file.close()
        self.filenames.append(filename)
        self.RefreshMainfile()

    def RefreshMainfile(self):
        clearfile = open("ToDoMainfile.txt", "w")
        clearfile.close()

        file = open("ToDoMainfile.txt", "a")
        for filename in self.filenames:
            file.write(filename)
            file.write("\n")

    def list(self):
        found = False

        while not found:
            pass

    def NewButton(self, ButtonName):
        self.Buttons.append(Button(self, text = ButtonName.replace(".txt", " >")))

root = Tk()
root.title("To-Do Reader 2.0")
root.geometry("400x300")
app = Application(root)
root.mainloop()
