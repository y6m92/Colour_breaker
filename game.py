

import random

# Welcome message 
print(" Welcome to Colour Code Breaker! ")
print("Try to guess the colours.\n")

# List of colours
colours = ["red", "blue", "green", "yellow", "purple"]
print("Available colours:", ", ".join(colours))

# Randomly generate the secret code (3 colours)
secret = [random.choice(colours) for _ in range(3)]

# user can input 5 attempts
attempts = 5
won = False

# Main game loop
while attempts > 0 and not won:
    print("\nAttempts left:", attempts)
    guess_input = input("Enter three colours separated by spaces: ").lower()
    guess_list = guess_input.split()
    
    # First: validate input length
    if len(guess_list) != 3:
        print("Please enter exactly three colours. ")
        continue
    
    # Then: check if correct
    if guess_list == secret:
        print("You cracked the code!")
        won = True
        break
    
    # Then: give hints
    hints = []
    for i in range(3):
        if guess_list[i] == secret[i]:
            hints.append("Perfect match")
        elif guess_list[i] in secret:
            hints.append("Right colour, wrong spot")
        else:
            hints.append("Not used")
            
    # Display hints            
    print("Hints:")
    
    for i in range(3):
        print(f"{guess_list[i]} -> {hints[i]}")
        
    attempts -= 1

# If user loses
if not won:
    print("\nYou ran out of attempts.")
    print("The secret code was:"," ".join(secret))
    
# Ask if user wants to play again    
play_again = input("\nPlay again? (y/n): ").lower()
if play_again == "y":
    print("Restart the game to play again.")
else:
    print("Thanks for playing!")

