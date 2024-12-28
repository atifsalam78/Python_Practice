from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root=Tk()
root.title("My Picture Album")
# root.iconbitmap("C:/Users/atif.salam/PycharmProjects/pythonProject1/pnglogo.ico")
# root.attributes('-alpha',0.95)

# img = ImageTk.PhotoImage(Image.open("C:/officeup/sprites/message3.png"))

# set resizing to false
# root.resizable(width=FALSE, height=FALSE)

# set size of window
root.geometry('1200x700')
# root.config(bg="#26242f")

#Set Main Menu
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About")

#Set Frames
leftFrame = Frame(root, bg="grey20")
leftFrame.pack(side=LEFT, fill="y")

rightFrame = Frame(root,bg="grey20")
rightFrame.pack(side=RIGHT, fill="y")

bottomFrame = Frame(root, relief=RAISED, bg="grey20")
bottomFrame.pack(side=BOTTOM, fill="x")

topFrame = Frame(root, bg="grey20")
topFrame.pack(side=TOP, fill="x")

centreFrame = Frame(root, width=600, height=400, borderwidth=2, relief=GROOVE)
centreFrame.pack(side=LEFT, fill=BOTH, expand=TRUE)

label1 = Label(leftFrame, width=25, text="Left column",fg="white", bg="grey20")
label1.pack()

b1 = Button(bottomFrame, width=10, height=1, font="Helvetica 10 bold", fg="darkblue", bg="grey20",text="Next>>").pack(side=LEFT)
b2 = Button(bottomFrame, width=10, height=1, font="Helvetica 10 bold", fg="darkblue", bg="grey20",text="Stop").pack(side=LEFT)
b3 = Button(bottomFrame, width=10, height=1, font="Helvetica 10 bold", fg="darkblue", bg="grey20",text="<<Previous").pack(side=LEFT)
b4 = Button(bottomFrame, width=10, height=1, font="Helvetica 10 bold", fg="darkblue", bg="grey20",text="Exit", command=root.destroy).pack(side=LEFT)

label2 = Label(rightFrame, text="Right column",fg="white",bg="grey20")
label2.pack()

label4 = Label(topFrame, text="My Picture Album", font=("Times 16 bold"), fg="white", bg="grey20")
label4.pack()

label5 = Label(centreFrame, image=img, width=1100, height=400,text="Pictures", font=("Times 16 bold"))
label5.pack(fill=BOTH)

# set an infinite loop so window stays in view
root.mainloop()