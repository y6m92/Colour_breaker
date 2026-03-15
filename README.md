# Colour Code Breaker

A simple Python game where the player tries to guess a secret sequence of colours.  
The program randomly generates a code of three colours, and the player has **five attempts** to guess it.

## Features
- Randomly generated colour code
- Hint system to guide the player
- Input validation
- Limited number of attempts
- Two versions:
  - Text-based version
  - Graphical interface using Tkinter

## Project Structure
Colour_breaker/
│
├── game.py        # Text-based version
├── gui_game.py    # Tkinter GUI version
└── README.md      # Project documentation

## How to Run

Run the text version:

python game.py

Run the GUI version:

python gui_game.py

## Gameplay

Available colours: red, blue, green, yellow, purple

Enter three colours separated by spaces:  
red blue green  

Hints:
red -> Right colour, wrong spot  
blue -> Not used  
green -> Perfect match  

## Requirements
- Python 3
- Tkinter (included with Python)

## Author
Developed as part of a programming assignment.  
All code written by me. Microsoft Copilot was used only for reviewing and understanding the code.
