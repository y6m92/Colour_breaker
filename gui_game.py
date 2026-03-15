import tkinter as tk
import random

# Create main window
win = tk.Tk()
win.title(" Colour Code Breaker ")

# List of colours
colours = ["red", "blue", "green", "yellow", "purple"]
secret = [random.choice(colours) for _ in range(3)]
attempts = 5

label = tk.Label(win, text="Welcome to Colour Code Breaker!")
label.pack(pady=20)

instruction = tk.Label(win, text="Enter three colours separated by spaces: ")
instruction.pack()

entry = tk.Entry(win, width=40)
entry.pack(pady=5)

hint = tk.Label(win, text="", fg="blue")
hint.pack(pady=10)

attempts = tk.Label(win, text="Attempts left: 5")
attempts.pack()

def check_guess():
    global attempts
    
    guess = entry.get().lower().split()
    
    if len(guess) != 3:
        hint.config(text="Please enter exactly three colours.")
        return
    
    if guess == secret:
        hint.config(text="You cracked the code!")
        return
    

win.mainloop()