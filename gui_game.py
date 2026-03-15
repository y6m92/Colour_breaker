import tkinter as tk
import random

# Create main window
win = tk.Tk()
win.title(" Colour Code Breaker ")

# List of colours
colours = ["red", "blue", "green", "yellow", "purple"]

label = tk.Label(win, text="Welcome to Colour Code Breaker!")
label.pack(pady=20)

instruction = tk.Label(win, text="Enter three colours separated by spaces: ")
instruction.pack()

entry = tk.Entry(win, width=40)
entry.pack(pady=5)

win.mainloop()