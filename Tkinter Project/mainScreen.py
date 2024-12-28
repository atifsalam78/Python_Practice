from tkinter import *
from PIL import Image, ImageTk
root = Tk()

root.geometry("733x434")
root.minsize(650,250)
root.title("Welcome to PyCharm")

# Only for PNG image files
# photo = PhotoImage(file="2.png")


# For other than PNG files

image = Image.open("2.png")
photo = ImageTk.PhotoImage(image)

Photolabel = Label(image=photo)
Photolabel.grid()

labelOne = Label(text="PyCharm Community Edition", font=("Cascadia", 30))
labelOne.grid(padx=100)

labelOne = Label(text="Version 2022")
labelOne.grid(padx=140)

labelOne = Label(text="Create New Project")
labelOne.grid(padx=140)

labelOne = Label(text="Open")
labelOne.grid(padx=140)

labelOne = Label(text="Check out from Version Control")
labelOne.grid(padx=140)

root.mainloop()