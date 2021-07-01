# Amir Kamalian - CSCI 2202 - Lab 7
# Ex 2 - This program illustrates the propagation of an error using two ways of calculating the
#        Verhulst equation.


r = 3
n = 0.01
v1 = []
v2 = []
difference = []
for m in range(0, 50):
    result = n + r * n * (1 - n)
    v1.append(result)
    n = result

    result2 = (1 + r) * n - r * n ** 2
    v2.append(result2)
    n = result2

    dif = result2 - result
    difference.append(dif)

for p, w, d in zip(v1, v2, difference):
    print('{0:1.12f}\t{1:1.12f}\t{2:1.12f}'.format(p, w, d))


