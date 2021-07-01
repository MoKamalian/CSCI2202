
# Create an initial value for both equations, Verhulst and Alternate.
V = 0.01
A = 0.01

# Set the value of r
r = 3

# Print the output header line to the screen
print("Verhulst1\t\tVerhulst2\t\tDifference")

# Recalculate where each algorithm deviates. Perform 50 such recalculations.
for i in range(50):
    # Find the difference between the algorithms.
    difference = abs(V - A)

    # Print the values to the screen.
    print("{:6.20f}\t{:6.20f}\t{:6.20f}".format(V, A, difference))

    # Calculate p(n+1) = p(n) + r * p(n) * (1 - p(n))
    V = V + r * V * (1 - V)

    # Calculate p(n+1) = (1 + r) * p(n) - r * p(n)^2
    A = (1 + r) * A - r * A**2



