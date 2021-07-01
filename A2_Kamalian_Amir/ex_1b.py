# Amir Kamalian - CSCI 2202 - A2
# Problem 1b) - This program finds the intersect points bw two polynomials f1 and f3 using the Newton method.

# ex 1


def newton_method(f, F, x0: float,
                  maxi: float, tolerance: float):
    x_n = 0
    n = 0
    while n < maxi or f(x=x_n) > tolerance:
        x_n = x0 - (f(x=x0) / F(x=x0))
        x0 = x_n
        n += 1
    return [x_n, n]


f1 = lambda x: (x**3) - (2*x) + 1
f2 = lambda x: x**2

f3 = lambda x: (x**3) - (2*x) + 1 - (x**2)
F3 = lambda x: (3 * (x**2)) - (2*x) - 2
intersect1, iterations1 = newton_method(f3, F3, 1.5, 2000, 0.000001)
intersect2, iterations2 = newton_method(f3, F3, 0.3, 2000, 0.000001)
intersect3, iterations3 = newton_method(f3, F3, -1, 2000, 0.000001)

print('intersect 1: ({0:9.3f}, {1:9.3f})\n'
      'intersect 2: ({2:9.3f}, {3:9.3f})\n'
      'intersect 3: ({4:9.3f}, {5:9.3f})'.format(intersect1, f2(x=intersect1),
                                                 intersect2, f2(x=intersect2),
                                                 intersect3, f2(x=intersect3)))








