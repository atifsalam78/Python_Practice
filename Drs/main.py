"""Decision Review System"""
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import time
import imutils

stream = cv2.VideoCapture("clip.mp4")
flag = True
def play(speed):
    global flag
    print(f"You clicked play. Speed is {speed}")

    # play the video in desired mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
    grabbed, frame =stream.read()
    if not grabbed:
        exit()
    frame = imutils .resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134,26, fill="black", font="Times 26 bold", text="Decision Pending")
    flag = not flag

def pending(decision):
    # 1. Display decision pedning image
    frame = cv2.cvtColor(cv2.imread("pending.png"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame, anchor=tkinter.NW)
    # 2. Wait for 1 second
    time.sleep(1)

    # 3. Display sposor image
    frame = cv2.cvtColor(cv2.imread("sponsor.png"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame, anchor=tkinter.NW)
    # 4. Wait for 1.5 seconds
    time.sleep(1.5)
    # 5. Displat out/not out image
    if decision == "out":
        decisionimg= "out.png"
    else:
        decisionimg = "not_out.png"
    frame = cv2.cvtColor(cv2.imread(decisionimg),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame, anchor=tkinter.NW)


def out():
    thread  = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")

def not_out():
    thread  = threading.Thread(target=pending, args=("not Out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")

# Width and Height of our main screen
SET_WIDTH = 650
SET_HEIGHT = 368

# Tkinter GUI starts here
window = tkinter.Tk()
window.title("Third Umpire DRS System")
cv_img = cv2.cvtColor(cv2.imread("welcome.png"),cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0, anchor=tkinter.NW, image=photo)
canvas.pack()

btn = tkinter.Button(window, text="<< Previous (Fast)", width = 50, command=partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="<< Previous (slow)", width = 50,command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text="Next (Fast) >>", width = 50,command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text="Next (slow) >>", width = 50,command=partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text="Out", width = 50, command=out)
btn.pack()

btn = tkinter.Button(window, text="Not Out", width = 50,command=not_out)
btn.pack()

window.mainloop()

