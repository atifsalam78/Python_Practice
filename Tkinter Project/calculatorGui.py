import tkinter as tk
from tkinter import *
import customtkinter

expression = ""

def buttonPress(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalPress():
    try:
        global expression
        character_limit(expression)
        total = str(eval(expression))
        equation.trace("w", lambda *args: character_limit(expression))
        equation.set(total)        

    except:
        equation.set("Invalid Syntax")
        expression = ""

def clear():
    global expression
    expression = ""   
    equation.set("")

def returnExp():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def character_limit(expression):
    if len(equation.get()) >= 16:
        equation.set(equation.get()[:-1])
        
if __name__=="__main__":    

    # customtkinter.set_appearance_mode("dark")
    # customtkinter.set_default_color_theme("dark-blue")

    # customtkinter.set_theme("dark-blue")

    root = tk.Tk()
    # root = customtkinter
    # root.title("Calculator")
    # root.geometry(f"{331}x{325}")
    # root.resizable(0,0)
             
    equation = StringVar()      
    expressionLabel = customtkinter.CTkEntry(master=root, justify=tk.CENTER, width=2700, height=60, corner_radius=5, textvariable=equation,font=('Times', 40), fg_color="black")
    expressionLabel.configure(state="disabled")   
    expressionLabel.pack()
    equation.trace("w", lambda *args: character_limit(expression))
        
    # First Frame
    frame1 = customtkinter.CTkFrame(master=root, width=50, height=27)
    frame1.pack(pady=4, padx=6,  expand=False)

    buttonClear = customtkinter.CTkButton(master=frame1, text="C", text_color="black",width=60, height=30, command=lambda:clear(),corner_radius=5, font=('Times', 30))
    buttonClear.pack(padx=2, pady=2, side=LEFT)
    root.bind("<Escape>",lambda event:clear())
    
    buttonDiv = customtkinter.CTkButton(master=frame1, text="÷", text_color="black",width=60, height=30, command=lambda:buttonPress("/"),corner_radius=5, font=('Times', 30))
    buttonDiv.pack(padx=2, pady=2, side=LEFT)
    root.bind("/",lambda event:buttonPress("/"))

    buttonMul = customtkinter.CTkButton(master=frame1, text="×", text_color="black",width=60, height=30, command=lambda:buttonPress("*"),corner_radius=5, font=('Times', 30))
    buttonMul.pack(padx=2, pady=2, side=LEFT)
    root.bind("*",lambda event:buttonPress("*"))

    buttonMin = customtkinter.CTkButton(master=frame1, text="−", text_color="black",width=60, height=30, command=lambda:buttonPress("-"),corner_radius=5, font=('Times', 30))
    buttonMin.pack(padx=2, pady=2, side=LEFT)
    root.bind("-",lambda event:buttonPress("-"))

    buttonPlus = customtkinter.CTkButton(master=frame1, text="+", text_color="black",width=60, height=30, command=lambda:buttonPress("+"),corner_radius=5, font=('Times', 30))
    buttonPlus.pack(padx=2, pady=2, side=LEFT)
    root.bind("+",lambda event:buttonPress("+"))

    #Second Frame
    frame1 = customtkinter.CTkFrame(master=root, width=50, height=27)
    frame1.pack(pady=4, padx=6,  expand=False)

    button7 = customtkinter.CTkButton(master=frame1, text="7", text_color="black",width=60, height=30, command=lambda:buttonPress("7"), border_width=0,corner_radius=5, font=('Times', 30,"bold"))
    button7.pack(padx=2, pady=2, side=LEFT)
    root.bind("7",lambda event:buttonPress("7"))

    button8 = customtkinter.CTkButton(master=frame1, text="8", text_color="black",width=60, height=30, command=lambda:buttonPress("8"),corner_radius=5, font=('Times', 30,"bold"))
    button8.pack(padx=2, pady=2, side=LEFT)
    root.bind("8",lambda event:buttonPress("8"))

    button9 = customtkinter.CTkButton(master=frame1, text="9", text_color="black",width=60, height=30, command=lambda:buttonPress("9"),corner_radius=5, font=('Times', 30,"bold"))
    button9.pack(padx=2, pady=2, side=LEFT)
    root.bind("9",lambda event:buttonPress("9"))

    buttonRoot = customtkinter.CTkButton(master=frame1, text="√", text_color="black",width=60, height=30, command=lambda:buttonPress("**0.5"),corner_radius=5, font=('Times', 30))
    buttonRoot.pack(padx=2, pady=2, side=LEFT)  

    buttonSqr = customtkinter.CTkButton(master=frame1, text="sqr", text_color="black",width=60, height=30, command=lambda:buttonPress("**2"),corner_radius=5, font=('Times', 30))
    buttonSqr.pack(padx=2, pady=2, side=LEFT)

    # Third Frame

    frame1 = customtkinter.CTkFrame(master=root, width=50, height=27)
    frame1.pack(pady=4, padx=6,  expand=False)

    button4 = customtkinter.CTkButton(master=frame1, text="4", text_color="black",width=60, height=30, command=lambda:buttonPress("4"), border_width=0,corner_radius=5, font=('Times', 30,"bold"))
    button4.pack(padx=2, pady=2, side=LEFT)
    root.bind("4",lambda event:buttonPress("4")) 

    button5 = customtkinter.CTkButton(master=frame1, text="5", text_color="black",width=60, height=30, command=lambda:buttonPress("5"),corner_radius=5, font=('Times', 30,"bold"))
    button5.pack(padx=2, pady=2, side=LEFT)
    root.bind("5",lambda event:buttonPress("5"))

    button6 = customtkinter.CTkButton(master=frame1, text="6", text_color="black",width=60, height=30, command=lambda:buttonPress("6"),corner_radius=5, font=('Times', 30,"bold"))
    button6.pack(padx=2, pady=2, side=LEFT)
    root.bind("6",lambda event:buttonPress("6"))

    buttonPlusMinus = customtkinter.CTkButton(master=frame1, text="<<", text_color="black",width=60, height=30, command=lambda:returnExp(), border_width=0,corner_radius=5, font=('Times', 30))
    buttonPlusMinus.pack(padx=2, pady=2, side=LEFT)
    root.bind("<BackSpace>",lambda event:returnExp())

    buttonPer = customtkinter.CTkButton(master=frame1, text="%", text_color="black",width=60, height=30, command=lambda:buttonPress("/100"), border_width=0,corner_radius=5, font=('Times', 30))
    buttonPer.pack(padx=2, pady=2, side=LEFT)
    root.bind("%",lambda event:buttonPress("%"))

    # Fourth Frame
    frame1 = customtkinter.CTkFrame(master=root, width=50, height=27)
    frame1.pack(pady=4, padx=6,  expand=False)

    button1 = customtkinter.CTkButton(master=frame1, text="1", text_color="black",width=60, height=30, command=lambda:buttonPress("1"), border_width=0,corner_radius=5, font=('Times', 30,"bold"))
    button1.pack(padx=2, pady=2, side=LEFT)
    root.bind("1",lambda event:buttonPress("1"))

    button2 = customtkinter.CTkButton(master=frame1, text="2", text_color="black",width=60, height=30, command=lambda:buttonPress("2"),corner_radius=5, font=('Times', 30,"bold"))
    button2.pack(padx=2, pady=2, side=LEFT)
    root.bind("2",lambda event:buttonPress("2"))

    button3 = customtkinter.CTkButton(master=frame1, text="3", text_color="black",width=60, height=30, command=lambda:buttonPress("3"),corner_radius=5, font=('Times', 30,"bold"))
    button3.pack(padx=2, pady=2, side=LEFT)
    root.bind("3",lambda event:buttonPress("3"))

    button0 = customtkinter.CTkButton(master=frame1, text="0", text_color="black",width=60, height=30, command=lambda:buttonPress("0"),corner_radius=5, font=('Times', 30,"bold"))
    button0.pack(padx=2, pady=2, side=LEFT)
    root.bind("0",lambda event:buttonPress("0"))

    buttonDec = customtkinter.CTkButton(master=frame1, text=".", text_color="black",width=60, height=30, command=lambda:buttonPress("."),corner_radius=5, font=('Times', 30))
    buttonDec.pack(padx=2, pady=2, side=LEFT)
    root.bind(".",lambda event:buttonPress("."))
    
    # Fifth Frame
    frame1 = customtkinter.CTkFrame(master=root)
    frame1.pack(pady=4, padx=5)

    buttonEqual = customtkinter.CTkButton(master=frame1, text="=", text_color="black",width=100, height=50, command=lambda:equalPress(),corner_radius=5, font=('Times', 30))
    buttonEqual.pack(padx=2, pady=2, side=RIGHT)
    root.bind("<Return>",lambda event:equalPress())
   
    root.mainloop()
