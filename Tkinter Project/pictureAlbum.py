from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import filedialog as fd

parentPath = "/home/atif/"
currentWorkingDirectory = os.getcwd()   
changeDirectory = "C:/Users/atif/Dropbox/Python Tutorial/Tkinter Project/Images"
path = os.path.join(parentPath, changeDirectory)
changePath = os.chdir(path) 
currentWorkingDirectory = os.getcwd()
listAll = os.listdir(currentWorkingDirectory)

def selectFile():    
    filename= fd.askopenfilename(initialdir="/",
    title="Select an Audio File",filetypes = (("Jpeg file","*.jpeg"),("JPG files", "*.jpg"),
                                              ("PNG files", "*.png"),("ICO files", "*.ico"),
                                              ("SVG files", "*.svg"), ("TIF files", "*.tif")))       
    # folderPath.set(filename)
    openImage(filename)
    
def openImage(zoo):           
    titleVar = StringVar()
    titleVar = currentWorkingDirectory+"\\"+zoo+" - My Picture Album"
    root.title(titleVar)    
    masterimg = Image.open(zoo)
    masterimg.thumbnail((1100,1000))
    img = ImageTk.PhotoImage(masterimg)        
    labelImage = Label(centreFrame, image=img, width=1100, height=400)
    labelImage.pack(fill=BOTH)
    labelImage.place(x=1,y=1)

indexValue = 0
def nextAction():
    global indexValue   
    global img
    global zoo    
    if indexValue == len(listAll) - 1:
        indexValue = 0
    else:
        indexValue  += 1
    zoo = listAll[indexValue]
    # openImage(listAll[indexValue])
    titleVar = StringVar()
    titleVar = currentWorkingDirectory+"\\"+zoo+" - My Picture Album"
    root.title(titleVar)    
    masterimg = Image.open(zoo)
    masterimg.thumbnail((1000,1000))
    img = ImageTk.PhotoImage(masterimg)        
    labelImage = Label(centreFrame, image=img, width=1100, height=800)
    labelImage.pack(fill=BOTH)
    labelImage.place(x=0,y=1)
    
def previousAction():
    global indexValue
    global zoo
    global img
    if indexValue == 0:
        indexValue = len(listAll) - 1
    else:
        indexValue -= 1    
    zoo = listAll[indexValue]
    # openImage(zoo)
    titleVar = StringVar()
    titleVar = currentWorkingDirectory+"\\"+zoo+" - My Picture Album"
    root.title(titleVar)    
    masterimg = Image.open(zoo)
    masterimg.thumbnail((1000,1000))
    img = ImageTk.PhotoImage(masterimg)    
    labelImage = Label(centreFrame, image=img, width=1100, height=800)
    labelImage.pack(fill=BOTH)
    labelImage.place(x=0,y=1)

def helpWindow():
    root2 = Tk()
    root2.geometry('500x250')
    root2.resizable(0,0)
    # root2.iconbitmap("/home/atif/PycharmProjects/pythonProject/Tkinter Project/Images/admin.svg")
    root2.title("About us")
    root2.configure(bg="#4B4B00")    
    helpLabel1=Label(root2, text="My Picture Album",font="Helvetica 14 bold", fg="black",bg="#4B4B00").pack(side=TOP)
    helpLabel2=Label(root2, text="About",font="Helvetica 12 bold", fg="black",bg="#4B4B00").pack(side=TOP)
    helpLabel3=Label(root2, text="Created only for educational purpose",font="Helvetica 10", fg="black",bg="#4B4B00").pack(side=TOP)    
    helpLabel4=Label(root2, text="Version 1.01",font="Helvetica 12 bold", fg="black",bg="#4B4B00").pack(side=TOP)
    helpLabel5=Label(root2, text="Copyright - 2022 Atif Salam",font="Helvetica 10", fg="black",bg="#4B4B00").pack(side=BOTTOM)    

if __name__=="__main__":

    root = Tk()
    root.geometry('1200x700')
    # root.iconbitmap("/home/atif/PycharmProjects/pythonProject/Tkinter Project/Images/admin.svg")  
    root.title("My Picture Album")

    folderPath = StringVar()
    var = StringVar()
    var.set(" ".join("\n{0}".format(f) for f in listAll))        

    #Set Main Menu
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New")
    filemenu.add_command(label="Open", command=selectFile)
    filemenu.add_command(label="Save", command=selectFile)
    filemenu.add_command(label="Save As", command=selectFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About", command=helpWindow)

    #Set Frame
    leftFrame = Frame(root, bg="#4B4B00")
    leftFrame.pack(side=LEFT, fill="y")
    rightFrame = Frame(root,bg="#4B4B00")
    rightFrame.pack(side=RIGHT, fill="y")
    bottomFrame = Frame(root, relief=RAISED, bg="#4B4B00")
    bottomFrame.pack(side=BOTTOM, fill="x")
    topFrame = Frame(root, bg="#4B4B00")
    topFrame.pack(side=TOP, fill="x")
    centreFrame = Frame(root, width=600, height=400, borderwidth=2, relief=RIDGE)
    centreFrame.pack(side=LEFT, fill=BOTH, expand=TRUE)

    #Set Buttons
    b1 = Button(bottomFrame, width=10, height=1, font="Helvetica 10 bold", fg="white", bg="#4B4B00",text="Next>>", command=nextAction)
    b1.pack(side=LEFT)
    b2 = Button(bottomFrame, width=10, height=1, font="Helvetica 10 bold", fg="white", bg="#4B4B00",text="Stop")
    b2.pack(side=LEFT)
    b3 = Button(bottomFrame, width=10, height=1, font="Helvetica 10 bold", fg="white", bg="#4B4B00",text="<<Previous", command=previousAction)
    b3.pack(side=LEFT)
    b4 = Button(bottomFrame, width=10, height=1, font="Helvetica 10 bold", fg="white", bg="#4B4B00",text="Exit", command=root.destroy)
    b4.pack(side=LEFT)
    b5 = Button(bottomFrame, width=10, height=1, font="Helvetica 10 bold", fg="white", bg="#4B4B00",text="Zoom (In)")
    b5.pack(side=LEFT)
    b6 = Button(bottomFrame, width=10, height=1, font="Helvetica 10 bold", fg="white", bg="#4B4B00",text="Zoom (Out)")
    b6.pack(side=LEFT)
    b7 = Button(bottomFrame, width=10, height=1, font="Helvetica 10 bold", fg="white", bg="#4B4B00",text="Slide Show >")
    b7.pack(side=LEFT)
    b8 = Button(bottomFrame, width=10, height=1, font="Helvetica 10 bold", fg="white", bg="#4B4B00",text="< Slide Show")
    b8.pack(side=LEFT)

    #Set Labels
    mainLabel = Label(leftFrame,text="List of Files",fg="white", bg="#4B4B00",font="Times 12 italic")
    mainLabel.pack(side=TOP)
    label1 = Label(leftFrame, width=25, text="List of files",fg="white", bg="#4B4B00", textvariable=var)
    label1.pack(side=TOP)
    label2 = Label(rightFrame, text="Setting Options",fg="white",bg="#4B4B00")
    label2.pack()    
    label4 = Label(topFrame, text="My Picture Album", font=("Times 16 bold"), fg="white", bg="#4B4B00")
    label4.pack()

    #Set Radio Buttons
    rd1 = Radiobutton(rightFrame, text="Option 1", fg="white",bg="#4B4B00").pack(side=TOP)
    rd2 = Radiobutton(rightFrame, text="Option 2", fg="white",bg="#4B4B00").pack(side=TOP)
    rd3 = Radiobutton(rightFrame, text="Option 3", fg="white",bg="#4B4B00").pack(side=TOP)
    rd4 = Radiobutton(rightFrame, text="Option 4", fg="white",bg="#4B4B00").pack(side=TOP)

    #Set Check Buttons
    Cb1 = Checkbutton(rightFrame, text = "Check 1", onvalue = 1, offvalue = 0, fg="white", bg="#4B4B00").pack()
    Cb2 = Checkbutton(rightFrame, text = "Check 2", onvalue = 1, offvalue = 0, fg="white", bg="#4B4B00").pack()
    Cb3 = Checkbutton(rightFrame, text = "Check 3", onvalue = 1, offvalue = 0, fg="white", bg="#4B4B00").pack()
    Cb4 = Checkbutton(rightFrame, text = "Check 4", onvalue = 1, offvalue = 0, fg="white", bg="#4B4B00").pack()

    root.mainloop()