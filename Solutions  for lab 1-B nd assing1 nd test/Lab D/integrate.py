import math

def inverseX(x):
    if x == 0:
        return 0.0
    return 1/x

def trapezoidal(f, a, b, n):
    deltaX = (b - a)/n
    An = 0
    for i in range(n):
        xA = a + deltaX * i
        xB = a + deltaX * (i+1)
        An += (f(xA)*deltaX) + (f(xB)*deltaX)
    return An * 0.5

def midpoint(f, a, b, n):
    deltaX = (b-a)/n
    An = 0
    for i in range(n):
        xA = a + deltaX * i
        xB = a + deltaX * (i+1)
        mid = (xA + xB) / 2
        An += f(mid) * deltaX
    return An

def testFunction(typeF, f, a, b, nList, actual):
    error = [1]
    for i in range(len(nList)):
        result = typeF( f, a, b, nList[i] )
        print("\tTest("+str(nList[i])+") =", result)
        error.append( actual - result )
    for i in range(1, len(error)):
        print("\tError("+str(nList[i-1])+") =",error[i],end=" ")
        if i > 1:
            print("(" + "{:4.2f}".format(error[i-1]/error[i]) + ")")
        else:
            print()

def main():
    n = [2, 10, 50, 250]
    print("\nEstimating ln(2) =", math.log(2))
    print("\nTrapezoidal:")
    testFunction(trapezoidal, inverseX, 1, 2, n, math.log(2))
    print("\nMidpoint:")
    testFunction(midpoint, inverseX, 1, 2, n, math.log(2))
    
if __name__ == "__main__":
    print("INTEGRATE.PY: This is the main Python program. Running the main function.")
    main()
else:
    print("INTEGRATE.PY: This is not the main Python program. Loading as a module.")
