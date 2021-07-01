import numpy as np

# For this function, we will use the quadratic formula
# to find the roots of a quadratic equation. This didn't
# have to be a function, but it's very easy to extract
# the code to remove the functional nature.
def findQuadraticRoots(a, b, c):
    # Calculate the denomniator
    denominator  = 2 * a

    # Calculate the discriminant (value under the root)
    discriminant = b**2 - 4 * a * c

    # If the denominator is 0, return the error values.
    if denominator == 0:
        return "Error1", "division by zero"

    # If the discriminant will give us two complex roots,
    # return the error values.
    if discriminant < 0:
        return "Error2", "has complex roots"

    # Otherwise calculate the two roots. If the discriminant
    # is zero, both will be the same.
    first  = (-b + np.sqrt(discriminant)) / denominator
    second = (-b - np.sqrt(discriminant)) / denominator

    # Return the two roots (or the same one twice!)
    return first, second

if __name__ == "__main__":
    # Print the roots for a positive discriminant.
    print("Roots for 5x^2 + 6x + 1: ", findQuadraticRoots(5, 6, 1))

    # Print the error for a negative discriminant.
    print("Roots for 5x^2 + 2x + 1: ", findQuadraticRoots(5, 2, 1))

    # Print a divsion by zero error.
    print("Roots for 0x^2 + 3x + 2: ", findQuadraticRoots(0, 3, 2))
