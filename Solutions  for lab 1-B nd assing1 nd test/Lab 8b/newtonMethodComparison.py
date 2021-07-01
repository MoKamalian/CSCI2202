import numpy as np

def newton1(f, fPrime, x0, tol):
    f0 = f(x0)
    fPrime0 = fPrime(x0)
    values = [x0]
    for i in range(50):
        if fPrime0 == 0:
            return "Error1", "f'(x0) is 0", []
        if abs(f0) <= tol:
            break
        x0 = x0 - f0
        values.append(x0)
        f0 = f(x0)
        fPrime0 = fPrime(x0)
    return x0, i+1, values

def newtonFx0(f, fPrime, x0, tol):
    f0 = f(x0)
    fPx0 = fPrime(x0)
    fPrime0 = fPrime(x0)
    values = [x0]
    for i in range(50):
        if fPrime0 == 0:
            return "Error1", "f'(x0) is 0", []
        if abs(f0) <= tol:
            break
        x0 = x0 - (f0/fPx0)
        values.append(x0)
        f0 = f(x0)
        fPrime0 = fPrime(x0)        
    return x0, i+1, values

def newtonFxn(f, fPrime, x0, tol):
    f0 = f(x0)
    fPrime0 = fPrime(x0)
    values = [x0]
    for i in range(50):
        if fPrime0 == 0:
            return "Error1", "f'(x0) is 0", []
        if abs(f0) <= tol:
            break
        x0 = x0 - (f0/fPrime0)
        values.append(x0)
        f0 = f(x0)
        fPrime0 = fPrime(x0)        
    return x0, i+1, values

def f1(x):
    return 2*x - np.cos(x)

def f1Prime(x):
    return np.sin(x) + 2

if __name__ == "__main__":
    out1   = newton1(f1, f1Prime, 0.5, 1e-7)[2]
    outFx0 = newtonFx0(f1, f1Prime, 0.5, 1e-7)[2]
    outFxn = newtonFxn(f1, f1Prime, 0.5, 1e-7)[2]

    length = max(len(out1), len(outFx0), len(outFxn))

    print("Iter   c = 1       f'(x0)      f'(xn)")

    for i in range(length):
        print("  {:2d}".format(i), end=" ")

        if i < len(out1):
            print(" {: 1.7f}".format(out1[i]), end=" ")

        if i < len(outFx0):        
            print(" {: 1.7f}".format(outFx0[i]), end=" ")

        if i < len(outFxn):
            print(" {: 1.7f}".format(outFxn[i]), end=" ")

        print()











        
        
    
