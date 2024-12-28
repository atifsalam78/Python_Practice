from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def user_login():
    email = email_input.get()
    password = password_input.get()

    if email == "atif.salam@gmail.com" and password == "1234":
        messagebox.showinfo("hurray", "Login Successfull")
    else:
        messagebox.showerror("Error","Login Failed")

root = Tk()
root.title("Login Window")
root.iconbitmap("favicon.ico")
# root.minsize(400,400)
# root.maxsize(700, 700)
root.geometry('350x500')
root.config(background='#000000')

img = Image.open("my_logo2.jpg")
resized_img = img.resize((70,70))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(root, image=img)
img_label.pack(pady=(10,10)) # This is a geometry manager like interior designer

text_label = Label(root, text="Linguist", fg="yellow", bg="#000000")
text_label.pack()
text_label.config(font=("verdana", 24))


email_label = Label(root, text="Enter Email", fg="yellow", bg="#000000")
email_label.pack(pady=(20,5))
email_label.config(font=("verdana", 12))

email_input = Entry(root, width=50)
email_input.pack(ipady=6, pady=(1,15))

password_label = Label(root, text="Enter Password", fg="yellow", bg="#000000")
password_label.pack(pady=(20,5))
password_label.config(font=("verdana", 12))

password_input = Entry(root, width=50)
password_input.pack(ipady=6, pady=(1,15))

login_button = Button(root, text="Login Button", fg="black", bg="yellow", width=20, height=2, command=user_login)
login_button.pack(pady=(10,20))
login_button.config(font=("verdana", 10))





root.mainloop()