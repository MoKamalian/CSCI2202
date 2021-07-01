import random
import matplotlib.pyplot as plt
import numpy as np

# Set the number of darts
darts = 10000

# Set the number of simulations
simulations = 10000

# Create an array for holding frequencies
freq = np.zeros(7)

# Create an array of data ranges. We use 1000 as an effective "infinity" here.
freqL = np.array([3.10, 3.12, 3.14, 3.16, 3.18, 3.20, 1000])

# Create a list for storing all estimates.
estimates = []

# Run the simulations
for s in range(simulations):
    # Initialize the number of successful dart hits to 0
    hits = 0

    # Throw all the darts
    for i in range(darts):
        # Generate a random x value
        x = random.random()
    
        # Generate a random y value
        y = random.random()
    
        # If the (x,y) location is in the circle, we got a hit
        if x**2 + y**2 <= 1.0:
            hits += 1

    # Estimate the value of pi and store it.
    estimated = 4 * (hits/darts)
    estimates.append(estimated)
    
    # Count the estimation in our frequency list
    for i in range(len(freqL)):
        if estimated <= freqL[i]:
            freq[i] += 1
            break

# Create the range labels for the printout
freqL = ["<3.10", "3.12", "3.14", "3.16", "3.18", "3.20", ">3.20"]

# Print the estimates with reasonable formatting.
print("Ranges", end="\t\t")
for label in freqL:
    print(label, end="\t")

print("\nFrequency", end="\t")
for value in freq:
    print(value, end="\t")
print()

''' CREATE A HISTOGRAM '''

# Enter the histogram data.
plt.hist(estimates, 6)

# Set the title
plt.title("Simulation of Pi Estimation Frequency")

# Label the axes
plt.xlabel("Estimate Value")
plt.ylabel("Frequency")

# Display the histogram
plt.show()

''' CREATE A BAR GRAPH '''

# Get the x-axis categories. Note this is the format of a tuple, not a list.
x = ("<3.10", "3.12", "3.14", "3.16", "3.18", "3.20", ">3.20")

# Enter the x and y data. This uses the default bar width.
plt.bar(x, freq)

# Set the title.
plt.title("Simulation of Pi Estimation Frequency")

# Label the axes.
plt.xlabel("Estimate Value")
plt.ylabel("Frequency")

# Display the graph.
plt.show()
