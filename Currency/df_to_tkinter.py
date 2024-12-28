import tkinter as tk
from tkinter import ttk
import pandas as pd

# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

# Create Tkinter window
root = tk.Tk()
root.title("Pandas DataFrame in Tkinter")

# Create a Treeview widget
tree = ttk.Treeview(root)
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

root.mainloop()
