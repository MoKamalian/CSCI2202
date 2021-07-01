import numpy as np
from rootFinding import *

def f1(x):
    return x**2 - x - 1

def f1Prime(x):
    return 2*x - 1

def f2(x):
    return np.log(2+x) - np.sqrt(x)

def f2Prime(x):
    if x > 0:
        return 1/(2+x) - 1/(2*np.sqrt(x))
    else:
        return -1/2

def f3(x):
    return x**3 - 3*x - 1

def f3Prime(x):
    return 3*x**2 - 3

def f4(x):
    return x**3 - 2*np.sin(x)

def f4Prime(x):
    return 3*x**2 - 2*np.cos(x)

def f5(x):
    return np.tan(x) - 2*x

def f5Prime(x):
    return (1/(np.cos(x)**2)) - 2

print("Newton-Raphson:")

# Newton-Raphson: 1(d) Positive Root 
print(newtonRaphson(f1, f1Prime, 2, 1e-8))

# Newton-Raphson: 1(d) Negative Root
print(newtonRaphson(f1, f1Prime, 0, 1e-8))

# Newton-Raphson: 1(e)
print(newtonRaphson(f2, f2Prime, 2, 1e-8))

# Newton-Raphson: 1(f) f_1(x)
print(newtonRaphson(f3, f3Prime, 1, 1e-8))

# Newton-Raphson: 1(f) f_2(x)
print(newtonRaphson(f4, f4Prime, 2, 1e-8))

# Newton-Raphson: 1(f) f_3(x)
print(newtonRaphson(f5, f5Prime, 1, 1e-8))
