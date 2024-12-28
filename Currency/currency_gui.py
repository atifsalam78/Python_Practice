import pandas as pd
from datetime import datetime
import time
import tkinter as tk
from tkinter import *
root = tk.Tk()
import json

# Function to get the value of the Spinbox widget
def get_spinbox_value():
    spinbox_value = int(spin_box.get())
    print("Spinbox value:", spinbox_value)
    data = {
        "spinbox_value": spinbox_value
    }
    # Specify the file path where you want to save the JSON file
    file_path = "config.json"

    # Write the data dictionary to a JSON file
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)

    print("Spinbox value saved to JSON file.")

# Function to get data from url
def get_data():        
        try:
            # Get Data from config
            with open("config.json", 'r') as value:
                params = json.load(value)

            value_seconds = params["spinbox_value"]

            # Fetch data from web and convert it into pandas data frame
            url = 'https://www.forex.com.pk/open_market_rates.asp'
            data = pd.read_html(url)
            currency_data = data[11]
            currency_data = currency_data.rename(columns={0: "Currency", 1: "Buying", 2: "Selling"})
            currency_data["Date"] = datetime.today().strftime("%d-%m-%Y %H:%M")
            currency_data["Date"] = pd.to_datetime(currency_data.Date)
            # currency_usd = currency_data.loc[currency_data["Currency"] == "US Dollar"]
            print("\n", currency_data)
            currency_data.to_csv("currency_data.csv", index=False)           
            
        except Exception as e:
            print("\nUnable to fetch data from website Or server down --", e)

class Table:
    def __init__(self, root):
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width = 20, fg="black", 
                                font=("Arial", 10))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

df = pd.read_csv("currency_data.csv")
lst = df.values.tolist()

# find total numnbers of rows
# columns in lst
total_rows= len(lst)
total_columns = len(lst[0])

    

if __name__=="__main__":

    # Title
    root.title("Currency Rate Extractor")

    t = Table(root)

    # Label
    label = Label(root, text="Currency Rate Extractor")
    label.grid()
    # Spin Box
    spin_box = Spinbox(root, from_=0, to=12)
    spin_box.grid()    

    # Button to trigger getting the Spinbox value
    button_spin = Button(root, text="Set Spinbox Value", command=get_spinbox_value)
    button_spin.grid()

    # Button to trigger getting the Spinbox value
    button_get_data = Button(root, text="Get Data", command=get_data)
    button_get_data.grid()       

    # Canvas
    canvas = Canvas(root, width=400, height=200)
    canvas.grid()

    # Canvas Line
    # canvas_height = 20
    # canvas_width = 600
    # # y = int(canvas_height / 2)
    # # canvas.create_line(0, y, canvas_width, y)    

    # Button
    button = tk.Button(root, text="Exit", width=25, command=root.destroy)
    button.grid()


    root.mainloop()




