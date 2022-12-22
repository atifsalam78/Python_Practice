from customtkinter import filedialog as fd
import customtkinter
from tkinter import *
from pygame import mixer

def selectFile():
    filename= fd.askopenfilenames(initialdir="sound/",title="Select an Audio File", filetypes=(("mp3 files", "*.mp3"),("mp4 files", "*.mp4"),("wave files", "*.wav")))
    for s in filename:
        s=s.replace("C:/officeup/sound/","")
        songs_list.insert(END,s)    

def musicPlay():
    song = songs_list.get(ACTIVE)    
    song = f"C:/officeup/sound/{song}"
    mixer.music.load(song)
    mixer.music.play()   

def musicPause():
    mixer.music.pause()

def musicStop():
    mixer.music.stop()
    songs_list.select_clear(ACTIVE)

def musicResume():
    mixer.music.unpause()
   
if __name__=="__main__":
    
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")
    
    root = customtkinter.CTk()    
    root.geometry(f"{900}x{600}")
    root.title("Musicon")
    root.iconbitmap("pnglogo.ico")
    root.resizable(0,0)
    root.config(background="tomato3")

    mixer.init()   

    my_menu=Menu(root)
    root.config(menu=my_menu)
    add_song_menu=Menu(my_menu)
    my_menu.add_cascade(label="Menu",menu=add_song_menu)
    add_song_menu.add_command(label="Add songs",command=selectFile)
    add_song_menu.add_command(label="Delete song")
    add_song_menu.add_command(label="Exit", command=root.quit)    

    songs_list=Listbox(root,selectmode=SINGLE,bg="black",fg="white",font=('Helvetica',10, "italic"),height=40,width=15,selectbackground="gray",selectforeground="black")
    songs_list.pack(side=LEFT, fill="both")

    label1 = customtkinter.CTkLabel(master=root, text="Musicon", text_color="black", bg_color="tomato3", font=("Times", 25, "bold"))
    label1.pack(side=TOP)

    # can = customtkinter.CTkCanvas(root)
    # can.pack(side=RIGHT)
    # # can.place(x=20,y=10)

    frameMain= customtkinter.CTkFrame(master=root)
    frameMain.pack(side=BOTTOM)    
         
    button1 = customtkinter.CTkButton(master=frameMain, text="Play", width=80, height=40,font=("Helvetica", 14, "bold"),text_color= ("brown"),fg_color="black", corner_radius=12,command=musicPlay)
    button1.pack(padx=1,side=LEFT)

    button1 = customtkinter.CTkButton(master=frameMain, text="Pause", width=80, height=40,font=("Helvetica", 14, "bold"),text_color= ("brown"),fg_color="black", corner_radius=12, command=musicPause)
    button1.pack(padx=1,side=LEFT)

    button1 = customtkinter.CTkButton(master=frameMain, text="Stop", width=80, height=40,font=("Helvetica", 14, "bold"),text_color= ("brown"),fg_color="black", corner_radius=12, command=musicStop)
    button1.pack(padx=1,side=LEFT)

    button1 = customtkinter.CTkButton(master=frameMain, text="Resume", width=80, height=40,font=("Helvetica", 14, "bold"),text_color= ("brown"),fg_color="black", corner_radius=12, command=musicResume)
    button1.pack(padx=1,side=LEFT)

    button1 = customtkinter.CTkButton(master=frameMain, text="Next", width=80, height=40,font=("Helvetica", 14, "bold"),text_color= ("brown"),fg_color="black", corner_radius=12)
    button1.pack(padx=1,side=LEFT)

    button1 = customtkinter.CTkButton(master=frameMain, text="Previous", width=80, height=40,font=("Helvetica", 14, "bold"),text_color= ("brown"),fg_color="black", corner_radius=12)
    button1.pack(padx=1,side=LEFT)

    # frame1= customtkinter.CTkFrame(master=root)
    # frame1.pack()

    # progressBar = customtkinter.CTkProgressBar(master=frame1, mode="determinate", corner_radius=20)
    # # progressBar.configure(fg_color="red", bg_color="blue")
    # progressBar.start()
    # progressBar.pack()

    

    root.mainloop()



