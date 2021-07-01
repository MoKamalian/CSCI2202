# Amir Kamalian - CSCI 2202 - Lab 6
# Question 3 - This program takes in the number of simulations (n) of Chloe meeting Mollie where Mollie
#              will leave if Chloe is 5 minutes late (when Mollie arrives first) and Chloe will leave
#              if Mollie is late 7 minutes (is Chloe arrives first).

import random

met = []
not_met = []
n = 1000000

for i in range(n):
    '''Meeting bw 930 and 1000; simulated
       that with 0.3 and 0.6'''
    chloe = random.uniform(0.3, 0.6)
    mollie = random.uniform(0.3, 0.6)

    if mollie < chloe:
        if (chloe - mollie) < 0.05:
            met.append(1)
        elif (chloe - mollie) > 0.05:
            not_met.append(1)
    if chloe < mollie:
        if (mollie - chloe) < 0.07:
            met.append(1)
        elif (mollie - chloe) > 0.07:
            not_met.append(1)

met_prob = len(met) / n

print(met_prob)





