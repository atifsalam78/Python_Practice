from customtkinter import filedialog as fd
import customtkinter
from tkinter import StringVar
from tkinter import *
import tkinter as tk
import time

# def selectFolder():
#     global folderPath
#     filename = fd.askdirectory()
#     folderPath.set(filename)
#     print(filename)


def selectFile():
    
    filename= fd.askopenfilename(initialdir="/",
    title="Select an Audio File",filetypes = (("Wave file","*.wav"),("mp3 files", "*.mp3"),("mp4 files", "*.mp4"),("all files", "*.*")))
    
    # filename = fd.askopenfile()
    folderPath.set(filename)
    # print(filename)
    musicPlay(filename)
   
    

def musicPlay(filename):    
    from pygame import mixer
    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()
    
    # while mixer.music.get_busy(): # wait for music to finish playing
    #     time.sleep(1)

def musicPause():    
    from pygame import mixer
    mixer.init()
    # mixer.music.load(filename)
    mixer.music.pause()

def musicStop():    
    from pygame import mixer
    mixer.init()
    mixer.music.stop()
           

   
if __name__=="__main__":
    
    customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("blue")

    root = customtkinter.CTk()
    root.title("Simple Music Player")
    root.geometry(f"{300}x{200}")
    root.resizable(0,0)

    folderPath = StringVar()
    
    label1 = customtkinter.CTkLabel(master=root, text="Simple Music Player", font=("Times", 20, "bold"))
    label1.pack()

    # label2 = customtkinter.CTkLabel(master=frameMain)
    # label2.pack(pady=20)   

    frameMain= customtkinter.CTkFrame(master=root)
    frameMain.pack(pady=60)    
         
    button1 = customtkinter.CTkButton(master=frameMain, text="Play", border_width=1,width=60, height=40,font=("Times", 20, "bold"),text_color= ("brown"),fg_color="black", corner_radius=12,command=selectFile)
    button1.pack(padx=1,side=LEFT)

    button1 = customtkinter.CTkButton(master=frameMain, text="Pause", border_width=1,width=60, height=40,font=("Times", 20, "bold"),text_color= ("brown"),fg_color="black", corner_radius=12, command=musicPause)
    button1.pack(padx=1,side=LEFT)

    button1 = customtkinter.CTkButton(master=frameMain, text="Stop", border_width=1,width=60, height=40,font=("Times", 20, "bold"),text_color= ("brown"),fg_color="black", corner_radius=12, command=musicStop)
    button1.pack(padx=1,side=LEFT)

    button1 = customtkinter.CTkButton(master=frameMain, text="Exit", border_width=1,width=60, height=40,font=("Times", 20, "bold"),text_color= ("brown"),fg_color="black", corner_radius=12, command=root.destroy)
    button1.pack(padx=1,side=LEFT)

    frame1= customtkinter.CTkFrame(master=root)
    frame1.pack()

    progressBar = customtkinter.CTkProgressBar(master=frame1, mode="determinate", corner_radius=20)
    # progressBar.configure(fg_color="red", bg_color="blue")
    progressBar.start()
    progressBar.pack()


    root.mainloop()



