import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview, Style
from tkinter import messagebox

def fixed_map(option):
    # Fix for setting text colour for Tkinter 8.6.9
    #
    # Returns the style map for 'option' with any styles starting with
    # ('!disabled', '!selected', ...) filtered out.
    #
    # style.map() returns an empty list for missing options, so this
    # should be future-safe.
    return [elm for elm in style.map('Treeview', query_opt=option) if elm[:2] != ('!disabled', '!selected')]

# Function to get data from url
def get_refresh_data():        
        try:
            # Fetch data from web and convert it into pandas data frame
            url = 'https://www.forex.com.pk/open_market_rates.asp'
            data = pd.read_html(url)
            currency_data = data[11]
            currency_data = currency_data.rename(columns={0: "Currency", 1: "Buying", 2: "Selling"})
            currency_data["Date"] = datetime.today().strftime("%d-%m-%Y %H:%M")
            currency_data["Date"] = pd.to_datetime(currency_data.Date)
            # currency_usd = currency_data.loc[currency_data["Currency"] == "US Dollar"]
            # print("\n", currency_data)
            currency_data.to_csv("currency_data.csv", index=False)
            df = pd.read_csv("currency_data.csv")
            for i in tree.get_children():
                tree.delete(i)
            for i, row in df.iterrows():
                tree.insert('', 'end', values=list(row))            

        except Exception as e:
            
            msg = "Unable to fetch data from website or server down"
            # print("\nUnable to fetch data from website or server down --", e)
            messagebox.showerror("Error 404",msg, icon="error")

df = pd.read_csv("currency_data.csv")

if __name__=="__main__":

    root = tk.Tk()
    
    # Title
    root.title("Currency Rate Extractor")

    # Canvas
    canvas = Canvas(root, width=400, height=200)
    canvas.pack()

    # Canvas Line
    # canvas_height = 20
    # canvas_width = 600
    # # y = int(canvas_height / 2)
    # # canvas.create_line(0, y, canvas_width, y) 

    # Label
    label = Label(canvas, text="Currency Rate Extractor", font=("Arial", 25))
    label.pack()

    # Tree View----------- Starts Here

    # Get style
    style = ttk.Style()
    # Required to get heading colour to work
    style.theme_use('clam')
    # Required to get .tag_configure('colour', background='PaleGreen2') to work
    style.map('Treeview', foreground=fixed_map('foreground'),  background=fixed_map('background'))

    # Create a Treeview widget
    tree = ttk.Treeview(canvas)
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"

    # Add columns to the Treeview
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    # Insert data into the Treeview
    for i, row in df.iterrows():
        tree.insert('', 'end', values=list(row))

    # Display the Treeview
    tree.pack(padx=10, pady=10)

    # Tree View----------- Ends Here
       

    # Button to trigger getting data from web and refresh data
    button_get_data = Button(canvas, text="Refresh", width=25, command=get_refresh_data)
    button_get_data.pack(padx=150,side=tk.LEFT)

    # Button
    button_exit = Button(canvas, text="Exit", width=25, command=root.destroy)
    button_exit.pack(pady=10, side=tk.LEFT)

    label_footer = Label(root, text="https://www.forex.com.pk", font=("Arial", 10))
    label_footer.pack()

    root.mainloop()
  




