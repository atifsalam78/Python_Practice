import customtkinter as ctk
from tkcalendar import Calendar
import tkinter as tk
from tkinter import ttk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

appWidth, appHeight = 1100, 600

class MyFrame(ctk.CTkFrame):
        def __init__(self, master, **kwargs):
             super().__init__(master, **kwargs)             
           
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        def new_file_clicked(event=None):
            print("The New File menu was clicked!")

        def about_app(event=None):
             print('''This app is created by Atif Salam
                      Version 1.0
                      Year 2024''')

        menubar = tk.Menu()
        menubar.configure(bg="blue")
        self.config(menu=menubar)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TMenubar", background="blue")

        file_menu = tk.Menu(menubar, tearoff=False)
        about_menu = tk.Menu(menubar, tearoff=False)

        file_menu.add_command(label="New",
                          accelerator="ctrl+N",
                          command=new_file_clicked)
        
        about_menu.add_command(label="About",
                          accelerator="ctrl+A",
                          command=about_app)
        
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(menu=file_menu, label="File")
        menubar.add_cascade(menu=about_menu, label="About")
           

        self.title("Invoice Management")
        self.geometry(f"{appWidth}x{appHeight}")
        # self.grid_rowconfigure(0, weight=1)  # configure grid system
        # self.grid_columnconfigure(0, weight=1)
        
        # Header
        self.header_frame = MyFrame(master=self)
        self.header_frame.grid(row=0, column=0, padx=20, pady=20, sticky="n")
        self.mainLabel = ctk.CTkLabel(master = self.header_frame, text="Invoice Management System", font=("Arial", 40))
        self.mainLabel.grid(row=0, column=0, padx=300)


        # Entry
        self.entry_frame = MyFrame(master=self)
        self.entry_frame.grid(row=1, column=0, padx=20, pady=20, sticky="n")

        self.serialLabel = ctk.CTkLabel(master = self.entry_frame, text="Serial No.", font=("Arial", 14)).grid(row=1, column=0, 
                              padx=20, pady=20, 
                              sticky="ew")       
        self.serialEntry = ctk.CTkEntry(master = self.entry_frame, placeholder_text="Serial No.").grid(row=1, column=1, 
                              padx=20, pady=20, 
                              sticky="ew")
        
        self.POLabel = ctk.CTkLabel(master = self.entry_frame, text="PO Number", font=("Arial", 14)).grid(row=1, column=2, 
                              padx=20, pady=20, 
                              sticky="ew")       
        self.POEntry = ctk.CTkEntry(master = self.entry_frame, placeholder_text="PO Number").grid(row=1, column=3, 
                              padx=20, pady=20, 
                              sticky="ew")
        
        self.vendorLabel = ctk.CTkLabel(master = self.entry_frame, text="Vendor Name", font=("Arial", 14)).grid(row=1, column=4, 
                              padx=20, pady=20, 
                              sticky="ew")        
        self.vendorEntry = ctk.CTkEntry(master = self.entry_frame, placeholder_text="Vendor Name").grid(row=1, column=5, 
                              padx=20, pady=20, 
                              sticky="ew")
        
        self.MRRLabel = ctk.CTkLabel(master = self.entry_frame, text="MRR", font=("Arial", 14)).grid(row=2, column=0, 
                              padx=20, pady=20, 
                              sticky="ew")       
        
        self.MRROption = ctk.CTkOptionMenu(master = self.entry_frame, values=["1745", "1746"]).grid(row=2, column=1, 
                              padx=20, pady=20, 
                              sticky="ew")

        
        self.amountLabel = ctk.CTkLabel(master = self.entry_frame, text="Amount", font=("Arial", 14)).grid(row=2, column=2, 
                              padx=20, pady=20, 
                              sticky="ew")       
        
        self.amountEntry = ctk.CTkEntry(master = self.entry_frame, placeholder_text="amount").grid(row=2, column=3, 
                              padx=20, pady=20, 
                              sticky="ew")
        
        self.invoiceLabel = ctk.CTkLabel(master = self.entry_frame, text="Invoice Number", font=("Arial", 14)).grid(row=2, column=4, 
                              padx=20, pady=20, 
                              sticky="ew")       
        
        self.invoiceEntry = ctk.CTkEntry(master = self.entry_frame, placeholder_text="Invoice Number").grid(row=2, column=5, 
                              padx=20, pady=20, 
                              sticky="ew")      
       
        # Invoice Date
        self.invoiceDate = ctk.CTkLabel(master = self.entry_frame, text="Invoice Date", font=("Arial", 14))
        self.invoiceDate.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

        self.invoiceCal = Calendar(master = self.entry_frame, selectmode='day', font=("Arial", 8),
        showweeknumbers=False, cursor="hand2", date_pattern= 'y-mm-dd',
        borderwidth=0, bordercolor='white')
        self.invoiceCal.grid(row=3, column=1, padx=20, pady=20, sticky='ew')


        # Invoice Submit Date
        self.invoiceSubmitDate = ctk.CTkLabel(master = self.entry_frame, text="Invoice Submit Date", font=("Arial", 14))
        self.invoiceSubmitDate.grid(row=3, column=2, padx=20, pady=20, sticky="ew")

        self.invoiceSubmitCal = Calendar(master = self.entry_frame, selectmode='day', font=("Arial", 8),
        showweeknumbers=False, cursor="hand2", date_pattern= 'y-mm-dd',
        borderwidth=0, bordercolor='white')
        self.invoiceSubmitCal.grid(row=3, column=3, padx=20, pady=20, sticky='ew')
        
if __name__=="__main__":
    app = App()
    app.mainloop()
    
