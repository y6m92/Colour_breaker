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
    
    if len(guess_list) != 3:
        print("Please enter exactly three colours.")
        continue
    
    if guess_list == secret:
        print("You cracked the code!")
        won = True
        break
    else:
        print("Not quite, hints coming soon...")
        attempts -= 1



