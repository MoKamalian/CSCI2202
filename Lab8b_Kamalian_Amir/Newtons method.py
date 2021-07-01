# Amir Kamalian - CSCI 2202 - Lab 8b
# Question 1 -


from math import cos, sin, tan, log, sqrt, tanh
from typing import Iterable
import matplotlib.pyplot as plt
import numpy as np

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


f1 = lambda x: 2*x - cos(x)
fd1 = lambda x: 2 + sin(x)
b = newton_method(f1, fd1, 0.5, 500, 0.000001)
print(str(b))


f2 = lambda x: x**2 - x - 1
fd2 = lambda x: 2*x - 1
h = newton_method(f2, fd2, 2, 500, 0.000001)
print(str(h))


f3 = lambda x: x**3 - 3*x - 1
fd3 = lambda x: 3 * (x**2) - 3
j = newton_method(f3, fd3, 2, 500, 0.000001)
print(str(j))


f4 = lambda x: x**3 - 2*sin(x)
fd4 = lambda x: 3 * (x**2) - 2*cos(x)
y = newton_method(f4, fd4, 1, 500, 0.000001)
print(str(y))


f5 = lambda x: tan(x) - 2*x
fd5 = lambda x: (1 / (cos(x)**2)) - 2
w = newton_method(f5, fd5, 0.5, 500, 0.000001)
print(str(w))


f6 = lambda x: log(x + 2) - sqrt(x)
fd6 = lambda x: 1 / (x + 2) + 1 / (2*sqrt(x))
q = newton_method(f5, fd5, 2, 500, 0.000001)
print(str(q))


f7 = lambda x: tanh(x)
fd7 = lambda x: 1 - tanh(x)**2
q = newton_method(f5, fd5, 1.09, 500, 0.000001)
print(str(q))


def plot_line(f, fxn, xn, slope):
    # plots function and its tangent
    xf = np.linspace(-2, 2, 100)
    yf = f(xf)
    xt = np.linspace(xn - 2, xn + 2, 10)
    yt = slope*xt + (fxn - slope*xn)
    plt.figure()
    plt.plot(xt, yt, 'r-', xf, yf, 'b-')
    plt.grid('on')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()






