# Amir Kamalian - CSCI 2202 - A2
# Problem 1a) - This program solves the equation x*cosh(50/x) = x+10 and also returns the number of iterations it
#               took to solve equation.

from math import cosh, sinh
# ex 1


def newton_method(f, F, x0: float,
                  maxi: float, tolerance: float):
    x_n = 0
    n = 0
    while n < maxi or f(x=x_n) > tolerance:
        x_n = x0 - (f(x=x0) / F(x=x0))
        x0 = x_n
        n += 1
    return x_n, n


f1 = lambda x: x * (cosh(50 / x)) - x - 10
F1 = lambda x: cosh(50 / x) - ((50*sinh(50 / x)) / x) - 1

root, iterations = newton_method(f1, F1, 120, 1000, 0.0000001)
print('Root of f1: {0:6.2f}\nNumber of iterations: {1}'.format(root, iterations))





