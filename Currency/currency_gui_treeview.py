import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview, Style
from tkinter import messagebox

def display_rates(title, url, columns, filename, data_index, column_range, row_location=0):
    def fixed_map(option):
        return [elm for elm in style.map('Treeview', query_opt=option) if elm[:2] != ('!disabled', '!selected')]

    def fetch_rates():
        try:
            data = pd.read_html(url)
            currency_data = data[int(data_index)]
            currency_data = currency_data[column_range]
            currency_data = currency_data.rename(columns=columns)
            currency_data = currency_data.iloc[int(row_location)::]
            currency_data["Date"] = datetime.today().strftime("%d-%m-%Y %H:%M")
            currency_data["Date"] = pd.to_datetime(currency_data["Date"], format='%d-%m-%Y %H:%M', dayfirst=True)
            
            try:
                currency_data.to_csv(filename, index=False)
            except Exception as e:
                msg = "Permission Denied\nClose open file"
                messagebox.showerror(f"Permission Denied", msg, icon="error")            

            df = pd.read_csv(filename)
            for i in tree.get_children():
                tree.delete(i)
            for i, row in df.iterrows():
                tree.insert('', 'end', values=list(row))
        except Exception as e:
            msg = "Check your internet connection\nUnable to fetch data from website or server down"
            messagebox.showerror(f"Error 404", msg, icon="error")

    df = pd.read_csv(filename)

    root = tk.Tk()
    root.title(title)
    
    canvas = Canvas(root, width=400, height=200)
    canvas.pack()

    label = Label(canvas, text=title, font=("Arial", 25))
    label.pack()

    style = ttk.Style()
    style.theme_use('clam')
    style.map('Treeview', foreground=fixed_map('foreground'), background=fixed_map('background'))

    tree = ttk.Treeview(canvas)
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"

    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    for i, row in df.iterrows():
        tree.insert('', 'end', values=list(row))

    tree.pack(padx=10, pady=10)

    button_get_data = Button(canvas, text="Refresh", width=25, command=fetch_rates)
    button_get_data.pack(padx=150, side=tk.LEFT)

    button_exit = Button(canvas, text="Exit", width=25, command=root.destroy)
    button_exit.pack(pady=10, side=tk.LEFT)

    label_footer = Label(root, text="https://www.forex.com.pk", font=("Arial", 10))
    label_footer.pack()

    root.mainloop()

# Open Market Rates
def currency_open_rates():
    display_rates("Open Market Rates",
        'https://www.forex.com.pk/open_market_rates.asp',
        {0: "Currency", 1: "Buying", 2: "Selling"},
        "open_market_rates.csv",
        11,[0,1,2])

# Inter Bank Rates
def currency_inter_bank_rates():
    display_rates("Inter Bank Rates",
        'https://www.forex.pk/inter_bank_rates.asp',
        {0: "Currency", 1: "Symbol", 2: "Bank Buying TT Clean", 3:"Bank Selling TT & OD"},
        "inter_bank_rates.csv",
        3,
        [0,1,2,3],
        1)

def foreign_exchange_rates():
    display_rates("Foreign Exchange Rates",
        'https://www.forex.pk/foreign-exchange-rate.htm',
        {0: "Currency", 1: "Symbol", 2: "Units per USD", 3:"USD per Unit"},
        "foreign_exchange_rates.csv",
        7,
        [0,1,2,3],
        2)

# currency_open_rates()  # To display Open Market Rates
# currency_inter_bank_rates()  # To display Inter Bank Rates