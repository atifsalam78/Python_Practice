from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("500x500")

list1 = ["1.png", "2.png","3.png","4.png","5.png", "6.png","7.png", "8.png", "9.png", "0.png"]

def getImage(val):
    indexValue = 0    
    print("Opening %s" % val)
    if val == "next":
        if indexValue == len(list1) - 1:
            indexValue = 0
        else:
            indexValue  += 1
            zoo = list1[indexValue]

    elif val == "prev":
        if indexValue == 0:
            indexValue = len(list1) - 1
        else:
            indexValue -= 1    
            zoo = list1[indexValue]


    img = ImageTk.PhotoImage(Image.open(zoo))
    labelImage = Label(image=img, relief=SUNKEN).grid(row=0,column=5)
    return
     

# def nextAction():
#     global indexValue
#     global zoo
#     global img
#     if indexValue == len(list1) - 1:
#         indexValue = 0
#     else:
#         indexValue  += 1
#         zoo = list1[indexValue]   
#     img = ImageTk.PhotoImage(Image.open(zoo))
#     labelImage = Label(image=img, relief=SUNKEN).grid(row=0,column=5)
    
# def previousAction():
#     global indexValue
#     global zoo
#     global img
#     if indexValue == 0:
#         indexValue = len(list1) - 1
#     else:
#         indexValue -= 1    
#         zoo = list1[indexValue]        
#         img = ImageTk.PhotoImage(Image.open(zoo))
#         labelImage = Label(image=img, relief=SUNKEN).grid(row=0,column=5)

nextButton = Button(text="Next", command=lambda val="next": getImage(val)).grid()
prevButton = Button(text="Previous",command=lambda val="prev": getImage(val)).grid()

root.mainloop()