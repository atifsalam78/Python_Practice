from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os

root = Tk()
root.geometry("500x600")


def loadImage():        
        for z in listAll:
            yield z

x = loadImage()      
def nextButton():
    try:
        global img
        global nextValue
        nextValue = next(x)
        img = ImageTk.PhotoImage(Image.open(nextValue))
        # frame1 = Frame(master=root).grid(row=0, column=10) 
        label2 = Label(image=img).grid(row=5, column=50)
    except StopIteration:
        messagebox.showwarning("showinfo", "File Ends")       
        

if __name__=="__main__":

    parentPath = "C:/"
    currentWorkingDirectory = os.getcwd()   
    changeDirectory = "officeup/sprites"
    path = os.path.join(parentPath, changeDirectory)
    changePath = os.chdir(path) 
    currentWorkingDirectory = os.getcwd()
    listAll = os.listdir(currentWorkingDirectory)
    # print(listAll)

    var = StringVar()
    var.set(" ".join("\n{0}".format(f) for f in listAll))  
    listFrame = Frame(master=root).grid(row=0, column=1)     
    label = Label(master=listFrame, text="List of files and directories from current path", relief=SUNKEN,textvariable=var).grid(row=0, column=1)
    # frame2 = Frame(master=root).grid(row=0, column=25)
    # label = Label(master=frame2, text="Image", font=("Times 16 bold"),relief=SUNKEN).grid()
    
    frame3 = Frame(master=root).grid(row=2, column=5)     
    bt = Button(text="Next >>", command=nextButton).grid()



    root.mainloop()
