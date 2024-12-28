from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import customtkinter as ctk

def user_login():
    email = email_input.get()
    password = password_input.get()

    if email == "atif.salam@gmail.com" and password == "1234":
        messagebox.showinfo("hurray", "Login Successfull")
    else:
        messagebox.showerror("Error","Login Failed")


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

appWidth, appHeight = 600, 700


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Linguist")
        self.geometry(f"{appWidth}x{appHeight}")

        #Name Label
        self.nameLabel = ctk.CTkLabel(self, text="Enter Name")
        self.nameLabel.grid(row=0, column=0, pady=20, padx=20, sticky="ew")

        #Name Entry
        self.nameEntry = ctk.CTkEntry(self, placeholder_text="Enter your name")
        self.nameEntry.grid(row=0, column=0, columnspan=3, padx=20, pady=20, stick="ew") 


if __name__ == "__main__":
    app = App()
    app.mainloop()

