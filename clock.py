import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Digital Clock")
root.configure(bg="black")  # set window background

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = tk.Label(root, font=("ds-digital", 80), bg="black", fg="cyan")  # use tk.Label, not ttk.Label
label.pack(anchor='center')

time()
root.mainloop()