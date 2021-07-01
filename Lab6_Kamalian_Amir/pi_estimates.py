# Amir Kamalian - CSCI 2202 - Lab 6
# Question 1 - This program takes a number of estimates (n) and calculates the relative error for each
#              n estimate.


import math as m
import random
import numpy as np

test_listx = []
test_listy = []
estimates = []
relative_error = []

n = [10, 100, 1000, 10000]

for i in n:
    for f in range(1, i):
        x_throw = random.random()
        y_throw = random.random()
        if (x_throw ** 2) + (y_throw ** 2) <= 1:
            test_listx.append(x_throw)
            test_listy.append(y_throw)

    dart_throws = len(test_listx)
    pi_estimate = (4 * dart_throws) / i
    estimates.append(pi_estimate)
    rel_error = (pi_estimate - m.pi) / m.pi
    relative_error.append(rel_error)

    test_listx.clear()
    test_listy.clear()


for o in range(len(n)):
    print(f'{n[o]}\t{estimates[o]}\t{relative_error[o]}')




