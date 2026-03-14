import random

print(" Welcome to Colour Code Breaker! ")
print("Try to guess the colours.\n")

colours = ["red", "blue", "green", "yellow", "purple"]
print("Available colours:", ", ".join(colours))

secret = [random.choice(colours) for _ in range(3)]




