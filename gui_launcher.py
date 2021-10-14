# Import Necessary Libraries
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

# Creating object of tk class
root = tk.Tk()

# Setting up the Box 
root.geometry("480x480")
root.resizable(False, False)
root.iconbitmap('university_icon.ico')
root.title("University Finder")
root.config(background="green")

# Setting up Image for Button
photo = PhotoImage(file=r'Green_button.png')


def Widgets():
    head_label = Label(root,
                       text="FIND ME A UNIVERSITY!",
                       padx=15,
                       pady=15,
                       font="Rockwell 20",
                       bg="green",
                       fg="white")
    head_label.config(anchor=CENTER)
    head_label.pack()

    button = Button(root,
                    text="Click Me!",
                    image=photo,
                    command=navigate)
    button.config(anchor=CENTER)
    button.pack()


def navigate():
    # Import Functions from main.py
    import main


# Calling all Widgets into Action
Widgets()
# Infinite Loop for the Program
root.mainloop()
