# Question 3: Dice Rolling Probabilities

import random

# Set the number of simulations (default 100000).
N = 100000

# Set up counters for keeping track of the number
# of times each condition is met.
countSix    = 0
countTwelve = 0

# Simulate the dice rolling N times.
for _ in range(N):
    # Generate 12 dice rolls, where each die is a d6 (1-6).
    dice = [random.randint(1, 6) for _ in range(12)]

    # Look at the first six dice and see if there's at least
    # one six. If yes, our count goes up by 1.
    if dice[:6].count(6) >= 1:
        countSix += 1

    # Look at all twelve dice and see if there's at least two
    # sixes. If yes, our count goes up by 1.
    if dice.count(6) >= 2:
        countTwelve += 1

# Print the final probability calculations.
print("Probability of getting at least one 6 in six dice rolls:", countSix/N)
print("Probability of getting at least two 6's in twelve dice rolls:", countTwelve/N)
