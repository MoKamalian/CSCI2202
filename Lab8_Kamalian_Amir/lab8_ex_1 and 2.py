# Amir Kamalian - CSCI 2202 - Lab 8
# Question 1 and 2 - 1) this program determines the probability of presence of complex roots. 2) this
#                    program takes in a function and calculates its roots according to the Bisection
#                    method.

# Ex 1 a) nd b)

from typing import Callable
from math import sin, tan, log
import random as r


def has_complex_root(a: int, b: int, c: int):
    return (b**2) - (4 * a * c) < 0


count1 = 0
for i in range(1000):
    a1 = r.random()
    b1 = r.random()
    c1 = r.random()
    count1 += 1 if has_complex_root(a=a1, b=b1, c=c1) else 0

probability = count1 / 1000
print(probability)

count2 = 0
for i in range(1000):
    a2 = r.normalvariate(mu=0, sigma=1)
    b2 = r.normalvariate(mu=0, sigma=1)
    c2 = r.normalvariate(mu=0, sigma=1)
    count2 += 1 if has_complex_root(a=a2, b=b2, c=c2) else 0

probability2 = count2 / 1000
print(probability2)


# Ex 2


def bisection(a: float, b: float, tol: float,
              fun: Callable, m=1000):
    func = fun
    n = (log(abs(a - b)) - log(2 * tol)) / log(2)
    m = int(n)
    j = 0
    c = (a + b) / 2
    while j < m and abs(func(x=c)) < tol:
        c = (a + b) / 2
        if abs(func(x=c)) > tol:
            if func(x=c) * func(x=b) < 0:
                a = c
            else:
                b = c
        j += 1
    return c, j


def f1(x):
    result1 = x**2 - x - 1
    return result1


def f2(x):
    result2 = x**3 - 3*x - 1
    return result2


def f3(x):
    result3 = x**3 - 2*sin(x)
    return result3


def f4(x):
    result4 = tan(x) - 2*x
    return result4


f1a, f1b = bisection(-1, 0, 0.000000001, f1)
print('root: {:3.5f}\tNumber of iterations: {:3}'.format(f1a, f1b))

f2a, f2b = bisection(0, 2, 0.000000001, f2)
print('root: {:3.5f}\tNumber of iterations: {:3}'.format(f2a, f2b))

f3a, f3b = bisection(0.5, 2, 0.000000001, f3)
print('root: {:3.5f}\tNumber of iterations: {:3}'.format(f3a, f3b))

f4a, f4b = bisection(0, 2, 0.000000001, f4)
print('root: {:3.5f}\tNumber of iterations: {:3}'.format(f4a, f4b))





