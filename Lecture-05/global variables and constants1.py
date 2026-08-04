#This program simulates 10 tosses of a coin.
import random

# Constant
Heads = 1
Tails = 2
Tosses = 10

def tosses_coin():
    for toss in range(Tosses):
        # Simulate the coin toss.
        if random.randint(Heads, Tails) == Heads:
            print("Heads")
        else:
            print("Tails")

# Call the main function.
tosses_coin()