import math
import random

# Set the number of darts
darts = [10, 100, 1000, 10000]

# Print the data table headers to the screen.
print("Number of Trials\tEstimate\tRelative Error")

# Run the simulations
for N in darts:
    # Initialize the number of successful dart hits to 0
    hits = 0

    # Throw all the darts
    for i in range(N):
        # Generate a random x value
        x = random.random()
        
        # Generate a random y value
        y = random.random()
        
        # If the (x,y) location is in the circle, we got a hit
        if x**2 + y**2 <= 1.0:
            hits += 1

    # Estimate the value of pi
    estimated = 4 * (hits/N)

    # Calculate the relative error.
    error = (estimated - math.pi) / math.pi

    # Print the results to the screen.
    print(N, "\t", estimated, "", error, sep="\t")
