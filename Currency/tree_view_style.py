# ###############
# From: https://core.tcl.tk/tk/info/509cafafae

from tkinter import *
from tkinter.ttk import Treeview, Style
import tkinter as tk
from tkinter import ttk
def fixed_map(option):
    # Fix for setting text colour for Tkinter 8.6.9
    #
    # Returns the style map for 'option' with any styles starting with
    # ('!disabled', '!selected', ...) filtered out.
    #
    # style.map() returns an empty list for missing options, so this
    # should be future-safe.
    return [elm for elm in style.map('Treeview', query_opt=option) if elm[:2] != ('!disabled', '!selected')]
# ############

# Create a Frame ( root = tkinter.Tk() )
root = tk.Tk()
dataTables_Frame = Frame(root, width=1400, height=1000, bg="light sea green")
dataTables_Frame.grid(column=0, row=0, columnspan = 9, rowspan = 10, sticky="EN")
dataTables_Frame.grid_propagate(False)
# Get style
style = ttk.Style()
# Required to get heading colour to work
style.theme_use('clam')
# Required to get .tag_configure('colour', background='PaleGreen2') to work
style.map('Treeview', foreground=fixed_map('foreground'),  background=fixed_map('background'))
# Name Columns
cols = ['One','Two','Three','Four','Five']
dataTree = ttk.Treeview(columns=cols, show="headings") 
# Add Colour for headings
style.configure("Treeview.Heading", background='light yellow')
# Add Colour to a Tag so alterative data rows are coloured
dataTree.tag_configure('colour', background='PaleGreen2')
# Add scroll bars
vsb_dataTree = ttk.Scrollbar(orient="vertical", command=dataTree.yview)
hsb_dataTree = ttk.Scrollbar(orient="horizontal", command=dataTree.xview)
dataTree.grid(column=0, row=0, sticky='nsew', in_=dataTables_Frame)
vsb_dataTree.grid(column=1, row=0, sticky='ns', in_=dataTables_Frame)
hsb_dataTree.grid(column=0, row=1, sticky='ew', in_=dataTables_Frame)
# Stop Resizw
dataTree.grid_propagate(False)

# ANSWER TO QUESTION
# Generate Table
for i in cols: # ['One','Two','Three','Four','Five']
    dataTree.heading(column=f'{i}',text=f'{i}',anchor='center')
    # if right justified text is required add - anchor=E or anchor=W for left justification
    # NOTE - How to 'right justify text' as been asked by others on 'stackoverflow'
    dataTree.column(column=f'{i}', width=150,minwidth=50,stretch=False, anchor=E)
# Add 'Separator line' to each column    
for i in range(0,len(cols)):
    # need - weight=1 for it to work
    dataTree.grid_columnconfigure(i, weight=1)
    # Note - sticky=W seems to align better than 'E'
    ttk.Separator(master=dataTree, orient=VERTICAL, style='black.TSeparator', takefocus= 0).grid(row=1, column=i, ipady=200, pady=1, sticky=W) 
# Add some Data colouring alterative rows
for i in range(0,20):
    if i % 2 == 0: # Even
        dataTree.insert("", "end", values=("24", "09", "2:00 AM"), tags=('colour'))
    else: # Odd
        dataTree.insert("", "end", values=("30 MM", "09", "13:00 AM"))
