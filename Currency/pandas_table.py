import tkinter as tk
from pandastable import Table, TableModel
import pandas as pd
import matplotlib.tri as tri

# Create a sample pandas DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

# Create a tkinter window
root = tk.Tk()
root.title("Pandas DataFrame in Tkinter")

# Create a TableModel object from the pandas DataFrame
model = TableModel(dataframe=df)

# Create a Table object and display it in the tkinter window
table = Table(root, model=model)
table.show()

# Run the tkinter main loop
root.mainloop()
