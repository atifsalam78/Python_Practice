
from customtkinter import filedialog as fd
import customtkinter
from tkinter import *
from pygame import mixer
import pygame
import audio_metadata
from io import BytesIO
from PIL import Image, ImageTk
import os
import mutagen
from mutagen.mp3 import MP3


def selectFile():
    filename= fd.askopenfilenames(initialdir="/home/atif/Music/",title="Select an Audio File", filetypes=(("mp3 files", "*.mp3"),("mp4 files", "*.mp4"),("wave files", "*.wav")))
    for s in filename:
        s = s.replace("/home/atif/Music/","")
        songs_list.insert(END,s)

def volumeUp():
    level=mixer.music.get_volume()
    level +=0.1
    level = round(level,1)
    if level >= 1.0:
        level = 1.0        
        mixer.music.set_volume(level)        
        print("Maximum")
    else:
        mixer.music.set_volume(level)
        print(level)

def volumeDown():    
    level = mixer.music.get_volume()
    level -= 0.1
    level = round(level,1)
    if level <= 0.1:
        level = 0        
        mixer.music.set_volume(level)
        print("Minimum")
    else:        
        mixer.music.set_volume(level)
        print(level)

def musicPlay():    
    song = songs_list.get(ACTIVE)    
    song = os.path.join("/home/atif/Music/",song)        
    # song = f"C:/officeup/sound/{song}"
    mixer.init()    
    mixer.music.load(song)    
    mixer.music.get_volume()
    mixer.music.play()
    # mixer.music.get_busy()   
    audio_file = MP3(song)
    if "APIC:" in audio_file:
        cover = audio_file["APIC:"].data
        stream = BytesIO(cover)           
        thumImage = Image.open(stream)
        
    else:
        thumImage = Image.open("/home/atif/Music/cover2.png")

    thumImage.thumbnail((300, 300))        
    img = ImageTk.PhotoImage(thumImage)
    canvas = Canvas(master=root, width = 300, height = 300)
    canvas.pack()    
    canvas.create_image(0, 0, anchor=NW, image=img)       
    
    root.mainloop()    

def musicPause():
    mixer.music.pause()

def musicStop():    
    mixer.music.fadeout(2000)
    songs_list.select_clear(ACTIVE)

def musicResume():
    mixer.music.unpause()
   
if __name__=="__main__":    
    
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")
    
    root = customtkinter.CTk()    
    root.geometry(f"{900}x{400}")
    root.title("Musicon")
    # root.iconbitmap("pnglogo.ico")
    root.resizable(0,0)
    root.config(background="tomato3")   

    my_menu=Menu(root)
    root.config(menu=my_menu)
    add_song_menu=Menu(my_menu)
    my_menu.add_cascade(label="Menu",menu=add_song_menu)
    add_song_menu.add_command(label="Add songs",command=selectFile)
    add_song_menu.add_command(label="Delete song")
    add_song_menu.add_command(label="Exit", command=root.quit)     

    songs_list=Listbox(root,selectmode=SINGLE,bg="tomato4",fg="white",font=('Helvetica',10, "italic"),height=40,width=25,selectbackground="gray",selectforeground="black")
    songs_list.pack(side=LEFT, fill="both")

    label1 = customtkinter.CTkLabel(master=root, text="Musicon", text_color="black", bg_color="tomato3", font=("Times", 25, "bold"))
    label1.pack(side=TOP)     
    
    frameMain= customtkinter.CTkFrame(master=root, border_color="tomato3", fg_color="tomato3")
    frameMain.pack(side=BOTTOM)    
         
    button1 = customtkinter.CTkButton(master=frameMain, text="Play", width=80, height=40,font=("Helvetica", 14, "bold"),text_color= ("tomato3"),fg_color="black", corner_radius=12,command=musicPlay)
    button1.pack(padx=1,side=LEFT)

    button1 = customtkinter.CTkButton(master=frameMain, text="Pause", width=80, height=40,font=("Helvetica", 14, "bold"),text_color= ("tomato3"),fg_color="black", corner_radius=12, command=musicPause)
    button1.pack(padx=1,side=LEFT)

    button1 = customtkinter.CTkButton(master=frameMain, text="Stop", width=80, height=40,font=("Helvetica", 14, "bold"),text_color= ("tomato3"),fg_color="black", corner_radius=12, command=musicStop)
    button1.pack(padx=1,side=LEFT)

    button1 = customtkinter.CTkButton(master=frameMain, text="Resume", width=80, height=40,font=("Helvetica", 14, "bold"),text_color= ("tomato3"),fg_color="black", corner_radius=12, command=musicResume)
    button1.pack(padx=1,side=LEFT)

    button1 = customtkinter.CTkButton(master=frameMain, text="Next", width=80, height=40,font=("Helvetica", 14, "bold"),text_color= ("tomato3"),fg_color="black", corner_radius=12)
    button1.pack(padx=1,side=LEFT)

    button1 = customtkinter.CTkButton(master=frameMain, text="Previous", width=80, height=40,font=("Helvetica", 14, "bold"),text_color= ("tomato3"),fg_color="black", corner_radius=12)
    button1.pack(padx=1,side=LEFT)

    button1 = customtkinter.CTkButton(master=frameMain, text="Vol +", width=80, height=40,font=("Helvetica", 14, "bold"),text_color= ("tomato3"),fg_color="black", corner_radius=12, command=volumeUp)
    button1.pack(padx=1,side=LEFT)


    button1 = customtkinter.CTkButton(master=frameMain, text="Vol -", width=80, height=40,font=("Helvetica", 14, "bold"),text_color= ("tomato3"),fg_color="black", corner_radius=12, command=volumeDown)
    button1.pack(padx=1,side=LEFT)

    # frame1= customtkinter.CTkFrame(master=root)
    # frame1.pack()

    # progressBar = customtkinter.CTkProgressBar(master=frame1, mode="determinate", corner_radius=20)
    # # progressBar.configure(fg_color="red", bg_color="blue")
    # progressBar.start()
    # progressBar.pack()    

    root.mainloop()

    # def musicPlay():   
    # song = songs_list.get(ACTIVE)    
    # song = f"/home/atif/Music/{song}"    
    # mixer.music.load(song)   
    # mixer.music.get_volume()
    # audioMetaData = audio_metadata.load(song)
    # audioPicture = audioMetaData.pictures[0].data
    # stream = BytesIO(audioPicture)
    # thumImage = Image.open(stream)
    # thumImage.thumbnail((300, 300))
    # img = ImageTk.PhotoImage(thumImage)
    # canvas = Canvas(master=root, width = 300, height = 300)
    # canvas.pack()
    # canvas.create_image(0, 0, anchor=NW, image=img) 
    # mixer.music.play()
    # mixer.music.get_busy()
    # root.mainloop()
   