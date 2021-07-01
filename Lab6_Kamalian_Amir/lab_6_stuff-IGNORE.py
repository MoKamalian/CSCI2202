# Amir Kamalian - CSCI 2202 - Lab 6
# Question 1 -

'''
-Simple simulation we are doing in this lab
-With simulations we are trying to see the effect of a physical process as close to the real world as
possible on our computer
-Simulations play a large part in the sciences in may fields
-We are using simulations to come up with an estimate of pi
-One thing you absolutly need is a random number generator. Its never truly random but the pattern is so
long range that really its essentially a patter.
-We use the random module to generate random numbers
-Arrays in python.

-We throw a large number of darts (100'000) will assume that they all fall within the square but a certian
fraction will fall within a circle,
-The darts fall uniformly on the circle so it dosnt matter if we only take one quadrant of the square
-We can focus on one quadrant of the square / circle
-The number of darts in the circle divided by the total number of darts thrown will give you the estimate
of pi

-What does it mean to throw a dart?
-It means we have a position of (x, y)
-We can use random to generate values for x and y
-Now we need to count how many throws are in the circle
-The circle line is x^2 + y^2 = r^2
-Soooo if your points are less than r^2 (1 in this case) it means its inside our circle
-If it is larger than one than it is outside our circle
-Hits will be the number of darts in our circle and we divide that by N-total
-The principle thing operating here is chance
-Once you are done the first part you'll store the values in a numpy array (we'll import numpy of course)
-Make the numpy array of zeros about 6 elements long and store your measurements there
-We make little bins with number brackets that we will store our estimates
-10'000 dart throws will give one estimate but we will run the whole simulation 10'000 times and so we end up
with 10'000 estimate values for pi

-The third exercise is another simulation
-arrival time is a random number
-have to set an interval of 5 minutes for one person and 7 for the other person and a limit for both
-What is the chance they will meet?
-You'll do the same thing as before and run a simulation of the chance they will meet
'''


import math as m
import random
import numpy as np

test_listx = []
test_listy = []

n =
for i in range(1, n):
    x_throw = random.random()
    y_throw = random.random()
    if (x_throw ** 2) + (y_throw ** 2) <= 1:
        test_listx.append(x_throw)
        test_listy.append(y_throw)


dart_throws = len(test_listx)
pi_estimate = (4 * dart_throws) / n
print(pi_estimate)


#________________________________________________________________________________________________________

# This is all the stuff done before numpy

import math as m
import random
# import numpy as np

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

#________________________________________________________________________________________________________


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

# for o in range(len(n)):
# print(f'{n[o]}\t{estimates[o]}\t{relative_error[o]}')


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

# print(a)

fig, bars = plt.subplots()

x = np.arange(1, 7)
bars.bar(x, a)
bars.set_xticks(x)
bars.set_xticklabels(("3.10", '3.12', '3.14', '3.16', '3.18', "3.20"))

plt.show()



