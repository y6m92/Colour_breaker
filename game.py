import random

print(" Welcome to Colour Code Breaker! ")
print("Try to guess the colours.\n")

colours = ["red", "blue", "green", "yellow", "purple"]
print("Available colours:", ", ".join(colours))

secret = [random.choice(colours) for _ in range(3)]

attempts = 5
won = False

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
            
    print("Hints:")
    for i in range(3):
        print(f"{guess_list[i]} -> {hints[i]}")
        
    attempts -= 1



