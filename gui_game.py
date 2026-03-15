# I acknowledge the use of Microsoft Copilot for reviewing and understanding the code.
# All code in this file was written by me.

import tkinter as tk
import random

# Create main window
win = tk.Tk()
win.title(" Colour Code Breaker ")

# List of colours
colours = ["red", "blue", "green", "yellow", "purple"]
secret = [random.choice(colours) for _ in range(3)]

attempts_left = 5

label = tk.Label(win, text="Welcome to Colour Code Breaker!")
label.pack(pady=20)

instruction = tk.Label(win, text="Enter three colours separated by spaces: ")
instruction.pack()

entry = tk.Entry(win, width=40)
entry.pack(pady=5)

hint = tk.Label(win, text="", fg="blue")
hint.pack(pady=10)

attempts_label = tk.Label(win, text="Attempts left: 5")
attempts_label.pack()

def check_guess():
    global attempts_left
    
    guess = entry.get().lower().split()
    
    if len(guess) != 3:
        hint.config(text="Please enter exactly three colours.")
        return
    
    if guess == secret:
        hint.config(text="You cracked the code!")
        return
    
    # Build hints 
    hints = []
    for i in range(3):
        if guess[i] == secret[i]:
            hints.append("Perfect match")
        elif guess[i] in secret:
            hints.append("Right colour, wrong spot")
        else:
            hints.append("Not used")
            
    # Show hints
    hint_text = ""
    for i in range(3):
        hint_text += f"{guess[i]} -> {hints[i]}\n"
        
    hint.config(text=hint_text)
    
    # Reduce attempts 
    attempts_left -= 1
    attempts_label.config(text=f"Attempts left: {attempts_left}")
    
    # Lose condition
    if attempts_left == 0:
        hint.config(text=f"You ran out of attempts. \nSecret was: {' '.join(secret)}")

# Submit button
submit = tk.Button(win, text="Submit Guess", command=check_guess)
submit.pack(pady=5)

win.mainloop()