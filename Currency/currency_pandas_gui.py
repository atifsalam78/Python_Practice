import pandas as pd
from datetime import datetime
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk
import json
from pandasgui import show

df = pd.read_csv("currency_data.csv")
gui = show(df)
gui.close()




