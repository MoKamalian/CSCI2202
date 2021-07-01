import numpy as np
from rootFinding import *

def f1(x):
    return x**2 - x - 1

def f2(x):
    return x**3 - 3*x - 1

def f3(x):
    return x**3 - 2*np.sin(x)

def f4(x):
    return np.tan(x) - 2*x

print("Bisection:")

# Bisection: 2(i) Positive Root 
print(bisection(f1, 1, 2, 1e-8))

# Bisection: 2(ii) Negative Root
print(bisection(f1, -1, 0, 1e-8))

# Bisection: 2(c) f1(x)
print(bisection(f2, 0, 1, 1e-8))

# Bisection: 2(d) f2(x)
print(bisection(f3, 0.5, 2, 1e-8))

# Bisection: 2(e) f3(x)
print(bisection(f4, 0, 2, 1e-8))
