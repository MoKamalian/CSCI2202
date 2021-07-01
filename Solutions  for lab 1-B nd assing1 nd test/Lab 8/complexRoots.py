# We can use this import style to import all of the
# methods stored in the quadraticRoots module.
from quadraticRoots import *

# We return true if the roots of the given
# quadratic values are complex.
def hasComplexRoots(a, b, c):
    # Since findQuadraticRoots returns a specific
    # error when the roots are complex, we can return
    # the result of the boolean condition below.
    return findQuadraticRoots(a, b, c)[0] == "Error2"

if __name__ == "__main__":
    # Print the roots for a positive discriminant.
    print("5x^2 + 6x + 1 (Real)     :", hasComplexRoots(5, 6, 1))

    # Print the error for a negative discriminant.
    print("5x^2 + 2x + 1 (Complex)  :", hasComplexRoots(5, 2, 1))

    # Print a divsion by zero error.
    print("0x^2 + 3x + 2 (Div0Error):", hasComplexRoots(0, 3, 2))
