from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os

def loadImage():        
        for z in listAll:
            yield z    
        

if __name__=="__main__":

    parentPath = "/home/atif/"
    currentWorkingDirectory = os.getcwd()   
    changeDirectory = "PycharmProjects/pythonProject/Tkinter Project/Images/"
    path = os.path.join(parentPath, changeDirectory)
    changePath = os.chdir(path) 
    currentWorkingDirectory = os.getcwd()
    listAll = os.listdir(currentWorkingDirectory)
   
    root = Tk()
    root.geometry("900x600")
    root.title("My Picture Album")

    var = StringVar()
    var.set(" ".join("\n{0}".format(f) for f in listAll))    
    # frameLabelTitle = Frame(master=root).grid(padx=50, column=50)
    labelTitle = Label(text="My Picture Album", font=("Times 16 bold")).grid(column=0)
    # listFrame = Frame(master=root).grid(column=70)     
    label = Label(text="List of files and directories from current path", relief=SUNKEN,textvariable=var).grid(row=1)
     
    x = loadImage()      
    def nextButton():    
        try:
            global img
            global nextValue
            nextValue = next(x)
            img = ImageTk.PhotoImage(Image.open(nextValue))               
            label2 = Label(image=img, width=500, height=350,relief=SUNKEN).grid(padx=100, row=1, column=50)    
        except StopIteration:
            messagebox.showwarning("showinfo", "File Ends")
            
    # frame3 = Frame(master=root, pady=10).grid()    
    btNext = Button(text="Next >>", width=10, height=1, font=("Helvetica 10 bold"),bg="skyblue", command=nextButton).grid(row=2, pady=5)
    btExit = Button(text="Exit", width=10, height=1, font=("Helvetica 10 bold"),bg="pink", command=root.destroy).grid(row=3, pady=5)

    root.mainloop()
