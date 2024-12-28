from tkinter import *

class Table:
    def __init__(self, root):
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width = 20, fg="blue", 
                               font=("Arial", 16, "bold"))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

# Take data
lst = [(1,'Atif Salam','Shah Faisal',45),
       (2,'Faisal Shah','Gulshan-e-Iqbal',41),
       (3,'Arshad Shah','Soldier Bazar',45),
       (4,'Navaid-ul-Islam','Gulsitan-e-Johar',45),
       (5,'Faisal Imtiaz','North Karachi',50)]

# find total numnbers of rows
# columns in lst
total_rows= len(lst)
total_columns = len(lst[0])

# create root window
root = Tk()
t = Table(root)
root.mainloop()