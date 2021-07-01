from numpy import *
import matplotlib.pyplot as plt

def plot_line(f, xn, fxn, slope):
    xf = linspace(-2,2,100)
    yf = f(xf)
    xt = linspace(xn-2,xn+2,10)
    yt = slope*xt + (fxn - slope*xn)
    plt.plot(xt, yt, 'r-', xf, yf, 'b-')
    plt.grid('on')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.pause(1)
    #count += 1
    plt.clf()

def bisection(f, x0, x1, tol, m=50):
    if x0 >= x1:
        return "Error1", "x1 >= x0"
    elif f(x0) * f(x1) > 0:
        return "Error2", "f(a) * f(b) > 0"
    elif x1 - x0 <= tol:
        return "Error3", "Interval is smaller than tolerance"
    for i in range(m):
        x2 = (x1 + x0) / 2
        fx = f(x2)
        if abs(fx) <= tol:
            return x2, i+1
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
    return "Fail", "Found no root in " + int(m) + " iterations"

def newtonRaphson(f, fPrime, x0, tol, plot=False):
    f0 = f(x0)
    fPrime0 = fPrime(x0)
    for i in range(50):
        if fPrime0 == 0:
            return "Error1", "f'(x0) is 0"
        if abs(f0) <= tol:
            break
        x0 = x0 - (f0/fPrime0)
        f0 = f(x0)
        fPrime0 = fPrime(x0)
        if plot:
            plot_line(f, x0, f0, fPrime0)
    return x0, i+1

