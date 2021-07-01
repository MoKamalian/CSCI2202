from random import random as uniform
from random import normalvariate as normal
from complexRoots import *

# Return the probability that random quadratic values
# in uniform [0, 1) will produce complex roots.
def uniformMonteCarlo(N):
    # Create a counting variable.
    count = 0

    # Produce N simulations.
    for i in range(N):
        # Generate uniform random values for a, b, c.
        a = uniform()
        b = uniform()
        c = uniform()

        # If the quadratic has complex roots, add 1 to
        # the count. Otherwise add 0.
        count += 1 if hasComplexRoots(a, b, c) else 0

    # Return the ratio of complex-to-real roots.
    return count / N

# Return the probability that random quadratic values
# in normal distribution [0, 1) will produce complex roots.
def normalMonteCarlo(N):
    # Create a counting variable.
    count = 0

    # Produce N simulations.
    for i in range(N):
        # Generate normal random values for a, b, c.
        a = normal(0, 1)
        b = normal(0, 1)
        c = normal(0, 1)

        # If the quadratic has complex roots, add 1 to
        # the count. Otherwise add 0.
        count += 1 if hasComplexRoots(a, b, c) else 0

    # Return the ratio of complex-to-real roots.
    return count / N

if __name__ == "__main__":
    print("Uniform Probability at n = 10000   :", uniformMonteCarlo(10000000))
    print("NormalDist Probability at n = 10000:", normalMonteCarlo(10000000))
