import tkinter as tk

class CustomMenu(tk.Menu):
    def __init__(self, master=None, **kwargs):
        tk.Menu.__init__(self, master, **kwargs)

        # Add your custom menu items
        self.add_command(label="New", command=self.new_file)
        self.add_command(label="Open", command=self.open_file)
        self.add_separator()
        self.add_command(label="Exit", command=master.quit)

    def new_file(self):
        print("Option 1 selected")

    def open_file(self):
        print("Option 2 selected")

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Menu Example")

        # Create a menu bar
        menubar = tk.Menu(self.root)

        # Attach the custom menu to the menu bar
        custom_menu = CustomMenu(self.root)
        menubar.add_cascade(label="Custom Menu", menu=custom_menu)

        # Configure the root window to use the menu bar
        self.root.config(menu=menubar)

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
