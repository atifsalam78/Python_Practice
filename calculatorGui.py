import tkinter as tk
from tkinter import *

expression = ""

def buttonPress(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalPress():
    try:
        global expression

        total = str(eval(expression))
        equation.set(total)


    except:
        equation.set("error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__=="__main__":

    mainWindow = tk.Tk()
    mainWindow.title("Calculator")
    mainWindow.geometry("370x300")

    equation = StringVar()

    expression_field = Entry(mainWindow, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=130)

    btns_frame = Frame(mainWindow, width=312, height=272.5, bg="black")
    btns_frame.grid()



    percentButton = Button(btns_frame, text="%", width=3, bd=0, command=lambda: buttonPress("%"), activebackground="#CDCDC5", font = "Helvetica 12 bold")
    percentButton.grid(row = 1, column = 0)
    
    rootButton = Button(btns_frame, text="√", width = 3, bd=0, command=lambda: buttonPress("√"), activebackground="#CDCDC5", font = "Helvetica 12 bold")
    rootButton.grid(row = 1, column = 3, columnspan = 3, padx = 1, pady = 1)

    # sqrButton = Button(frame1, text="x2", width=8,activebackground="#CDCDC5", font = "Helvetica 12 bold")
    # sqrButton.pack(side=LEFT)

    # fracButton = Button(frame1, text="1/x", width=8,activebackground="#CDCDC5", font = "Helvetica 12 bold")
    # fracButton.pack(side=LEFT)

    # # Second Frame

    # frame2 = Frame(mainWindow)
    # frame2.pack()

    # bottomFrame2 = Frame(mainWindow)
    # bottomFrame2.pack(side=BOTTOM)

    # percentButton = Button(frame2, text="CE", width=8,activebackground="#CDCDC5", font = "Helvetica 12 bold")
    # percentButton.pack(side=LEFT)

    # rootButton = Button(frame2, text="C", width=8,activebackground="#CDCDC5", font = "Helvetica 12 bold")
    # rootButton.pack(side=LEFT)

    # sqrButton = Button(frame2, text="<+>", width=8,activebackground="#CDCDC5", font = "Helvetica 12 bold")
    # sqrButton.pack(side=LEFT)

    # fracButton = Button(frame2, text="/", width=8,activebackground="#CDCDC5", font = "Helvetica 12 bold")
    # fracButton.pack(side=LEFT)


    # # Third Frame

    # frame3 = Frame(mainWindow)
    # frame3.pack()

    # bottomFrame3 = Frame(mainWindow)
    # bottomFrame3.pack(side=BOTTOM)

    # percentButton = Button(frame3, text="7", width=8,activebackground="#CDCDC5", font = "Helvetica 12 bold")
    # percentButton.pack(side=LEFT)

    # rootButton = Button(frame3, text="8", width=8,activebackground="#CDCDC5", font = "Helvetica 12 bold")
    # rootButton.pack(side=LEFT)

    # sqrButton = Button(frame3, text="9", width=8,activebackground="#CDCDC5", font = "Helvetica 12 bold")
    # sqrButton.pack(side=LEFT)

    # fracButton = Button(frame3, text="X", width=8,activebackground="#CDCDC5", font = "Helvetica 12 bold")
    # fracButton.pack(side=LEFT)

    # # Fourth Frame

    # frame4 = Frame(mainWindow)
    # frame4.pack()

    # bottomFrame4 = Frame(mainWindow)
    # bottomFrame4.pack(side=BOTTOM)

    # percentButton = Button(frame4, text="4", width=8,activebackground="#CDCDC5", font = "Helvetica 12 bold")
    # percentButton.pack(side=LEFT)

    # rootButton = Button(frame4, text="5", width=8,activebackground="#CDCDC5", font = "Helvetica 12 bold")
    # rootButton.pack(side=LEFT)

    # sqrButton = Button(frame4, text="6", width=8,activebackground="#CDCDC5", font = "Helvetica 12 bold")
    # sqrButton.pack(side=LEFT)

    # fracButton = Button(frame4, text="-", width=8,activebackground="#CDCDC5", font = "Helvetica 12 bold")
    # fracButton.pack(side=LEFT)

    # # Fifth Frame

    # frame5 = Frame(mainWindow)
    # frame5.pack()

    # bottomFrame5 = Frame(mainWindow)
    # bottomFrame5.pack(side=BOTTOM)

    # percentButton = Button(frame5, text="1", width=8,activebackground="#CDCDC5", font = "Helvetica 12 bold")
    # percentButton.pack(side=LEFT)

    # rootButton = Button(frame5, text="2", width=8,activebackground="#CDCDC5", font = "Helvetica 12 bold")
    # rootButton.pack(side=LEFT)

    # sqrButton = Button(frame5, text="3", width=8,activebackground="#CDCDC5", font = "Helvetica 12 bold")
    # sqrButton.pack(side=LEFT)

    # fracButton = Button(frame5, text="+", width=8,activebackground="#CDCDC5", font = "Helvetica 12 bold")
    # fracButton.pack(side=LEFT)

    # # Sixth Frame

    # frame6 = Frame(mainWindow)
    # frame6.pack()

    # bottomFrame6 = Frame(mainWindow)
    # bottomFrame6.pack(side=BOTTOM)

    # percentButton = Button(frame6, text="+/-", width=8,activebackground="#CDCDC5", font = "Helvetica 12 bold")
    # percentButton.pack(side=LEFT)

    # rootButton = Button(frame6, text="0", width=8,activebackground="#CDCDC5", font = "Helvetica 12 bold")
    # rootButton.pack(side=LEFT)

    # sqrButton = Button(frame6, text=".", width=8,activebackground="#CDCDC5", font = "Helvetica 12 bold")
    # sqrButton.pack(side=LEFT)

    # fracButton = Button(frame6, text="=", width=8,activebackground="#CDCDC5", font = "Helvetica 12 bold")
    # fracButton.pack(side=LEFT)

    # button = tk.Button(mainWindow, text="Exit", width=25, activebackground="red4",command=mainWindow.destroy)
    # button.pack()



    # Main loop used when your application is ready to run
    mainWindow.mainloop()





