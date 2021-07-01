import random

# Set how long Mollie is willing to wait
mollieWait = 5

# Set how long Chloe is willing to wait
chloeWait = 7

# Create a counter for the number of times they meet
meet = 0

# Set a number of times to simulate the meeting chance
simulations = 10000000

# Run the simulations
for i in range(simulations):
    # Generate a random time for Mollie to show up
    mollie = random.random() * 30

    # Generate a random time for Chloe to show up
    chloe = random.random() * 30

    # If they show up at the same time, they meet
    if mollie == chloe:
        meet += 1

    # If Chloe arrives after Mollie, but before she leaves, they meet
    elif mollie < chloe <= (mollie + mollieWait):
        meet += 1

    # If Mollie arrives after Chloe, but before she leaves, they meet
    elif chloe < mollie <= (chloe + chloeWait):
        meet += 1

# Print the probability of meeting
print("Meeting Probability:", meet/simulations)
