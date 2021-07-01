# Amir Kamalian - CSCI 2202 - Lab 6
# Question 2 - This program takes the number of pi estimates (n), sorts them into different bin sizes and
#              produces a histogram of the sorted pi estimates based on the bin sizes.

import math as m
import random
import numpy as np
import matplotlib.pyplot as plt

test_listx = []
test_listy = []
estimates = []
relative_error = []

n = [10000, 10000, 10000, 10000, 10000, 10000] * 10000

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


a = np.zeros(6)

bin0 = []
bin1 = []
bin2 = []
bin3 = []
bin4 = []
bin5 = []
trash_bin = []

for e in estimates:
    if e < 3.10:
        bin0.append(e)
    elif 3.10 < e < 3.12:
        bin1.append(e)
    elif 3.12 < e < 3.14:
        bin2.append(e)
    elif 3.14 < e < 3.16:
        bin3.append(e)
    elif 3.16 < e < 3.18:
        bin4.append(e)
    elif 3.18 < e < 3.20:
        bin5.append(e)
    else:
        trash_bin.append(e)

a[0] = len(bin0)
a[1] = len(bin1)
a[2] = len(bin2)
a[3] = len(bin3)
a[4] = len(bin4)
a[5] = len(bin5)

print(a)

fig, bars = plt.subplots()

x = np.arange(1, 7)
bars.bar(x, a)
bars.set_xticks(x)
bars.set_xticklabels(("3.10", '3.12', '3.14', '3.16', '3.18', "3.20"))

plt.show()
