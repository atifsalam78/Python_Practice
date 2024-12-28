import tkinter as tk
from PIL import ImageTk
from tkinter import *
import currency_gui_treeview
from tkinter import ttk

bg_color = "#dab600"

def load_frame1():
	frame1.pack_propagate(False)
	# Logo Widget
	logo_img = ImageTk.PhotoImage(file="assets/currency_logo_small.png")
	logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.pack()

	# Label Widget
	tk.Label(frame1, text="Ready to extract currency data from the web", 
		bg=bg_color,
		fg="black",
		font=("TkMenuFont", 14)).pack()

	# Button Widget
	tk.Button(frame1,
		text="Start Extracting",
		font=("TkHeadingFont", 20),
		bg="#a98600",
		fg="black",
		cursor="hand2",
		activebackground="#f8ed62",
		activeforeground="black",
		command = lambda:load_frame2()).pack(pady=20)

def OpenMarket():
	currency_gui_treeview.currency_open_rates()

def InterBank():
	currency_gui_treeview.currency_inter_bank_rates()

def ForeignExchange():
	currency_gui_treeview.foreign_exchange_rates()

def about():
	# Initializing App
	root = tk.Tk()
	root.title('About')
	# Place our window to the centre of the screen 
	# root.eval("tk::PlaceWindow . center")
	x = root.winfo_screenwidth()//2
	y = int(root.winfo_screenheight()*0.1)
	root.geometry('300x150+' + str(x) + '+' + str(y))

	# Creating Frame Widget
	frame1 = tk.Frame(root, width=300, height=150, bg=bg_color)
	frame1.grid(row=0, column=0)
	frame1.pack_propagate(False)
	# Label Widget

	tk.Label(frame1, text="Copyright © 2024 Atif Salam\nVersion 1.0", 
		bg=bg_color,
		fg="black",
		font=("TkMenuFont", 14)).pack()

	root.mainloop()

def license():
	# Initializing App
	root = tk.Tk()
	root.title('License')
	# Place our window to the centre of the screen 
	# root.eval("tk::PlaceWindow . center")
	x = root.winfo_screenwidth()//4
	y = int(root.winfo_screenheight()*0.1)
	root.geometry('500x600+' + str(x) + '+' + str(y))

	# Creating Frame Widget
	frame1 = tk.Frame(root, width=500, height=600, bg=bg_color)
	frame1.grid(row=0, column=0)
	frame1.pack_propagate(False)
	# Label Widget
	encodings = ['utf-8', 'latin-1']
	for encoding in encodings:
		with open("license.txt", "rb") as file:
			file_content = file.read().decode(encoding)
	
	tk.Label(frame1, text=file_content,
		bg=bg_color,
		fg="black",
		font=("TkMenuFont", 10), wraplength=400).pack()

	root.mainloop()

if __name__=="__main__":
	# Initializing App
	root = tk.Tk()
	root.title('Currency Extractor')

	style = ttk.Style()
	style.theme_use('clam')  # Change the theme here (e.g., 'clam', 'alt', 'default', 'classic')

	# Place our window to the centre of the screen 
	# root.eval("tk::PlaceWindow . center")
	x = root.winfo_screenwidth()//3
	y = int(root.winfo_screenheight()*0.1)
	root.geometry('500x600+' + str(x) + '+' + str(y))

	# Creating Frame Widget
	frame1 = tk.Frame(root, width= 500, height=600, bg=bg_color)
	frame1.grid(row=0, column=0)

	load_frame1()

	# Menu Bar
	menu_bar = tk.Menu(root)	

	# Currency Menu
	currency_menu = tk.Menu(menu_bar, tearoff=0)
	menu_bar.add_cascade(label="Currency", menu=currency_menu)
	currency_menu.add_command(label="Open Market Rates", command=OpenMarket)
	currency_menu.add_command(label="Inter Bank Rates", command=InterBank)
	currency_menu.add_command(label="Foreign Exchange Rates", command=ForeignExchange)
	currency_menu.add_separator()
	currency_menu.add_command(label="Exit", command=root.destroy)

	# Gold Menu
	gold_menu = tk.Menu(menu_bar, tearoff=0)
	menu_bar.add_cascade(label="Gold", menu=gold_menu)
	gold_menu.add_command(label="Gold Price(Pak)", command=OpenMarket)
	gold_menu.add_command(label="Gold Price(Others)", command=InterBank)
	
	gold_menu.entryconfig("Gold Price(Pak)", state="disabled")
	gold_menu.entryconfig("Gold Price(Others)", state="disabled")

	# Help Menu
	help_menu = tk.Menu(menu_bar, tearoff=0)
	menu_bar.add_cascade(label="Help", menu=help_menu)
	help_menu.add_command(label="Setting", command=InterBank)
	help_menu.add_command(label="License", command=license)
	help_menu.add_command(label="About", command=about)

	help_menu.entryconfig("Setting", state="disabled")

	root.config(menu=menu_bar)
	root.mainloop()