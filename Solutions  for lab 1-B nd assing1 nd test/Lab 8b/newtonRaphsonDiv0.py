import numpy as np
from rootFinding import *

def f(x):
    return np.tanh(x)

def fP(x):
    return 1 - np.tanh(x)**2

print("Netwon-Raphson(tanh(x), 1 - tanh^2(x), 1.08, 1e-5)")
x, numIter = newtonRaphson(f, fP, 1.08, 1e-5, True)
print("Output:", x, numIter)

print("Netwon-Raphson(tanh(x), 1 - tanh^2(x), 1.09, 1e-5)")
x, numIter = newtonRaphson(f, fP, 1.09, 1e-5, True)
print("Output:", x, numIter)
