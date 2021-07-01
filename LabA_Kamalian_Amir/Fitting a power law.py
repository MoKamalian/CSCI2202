# Amir Kamalian - CSCI 2202 - Lab 9
# Question 3 - This program takes the soot aggregation data and produces scatter plot of ln(r) and ln(t), where r is
#              radius in nanometers and t is time in minutes. A regression line to the data is fitted.


import numpy as np
from numpy import log
import matplotlib.pyplot as plt
import scipy.stats
from math import exp


def read_dat_file(infile: str):
    file = open(infile, 'r')
    data = []
    while True:
        line = file.readline()
        if not line:
            break
        line = line.split(' ')
        for o in line:
            data.append(float(o))
    return np.asarray(data)


# question 3
# radius of aggregate grows according to power law: r = r_0 * t^n
# using sootAggregation.text file; columns:     time    avg_radius    uncertainty
# time in minutes and radius in nm
# ln(t) vs ln(r)

sootAggData = read_dat_file('/Users/mokamalian/Downloads/CSCI 2202 : W21:/Pycharm notes/'
                            'LabA_Kamalian_Amir/sootAggregation.txt')

# separating all columns
time = []
for k in range(0, len(sootAggData), 3):
    time.append(sootAggData[k])
time = np.asarray(time)

radius = []
for w in range(1, len(sootAggData), 3):
    radius.append(sootAggData[w])
temp = np.asarray(radius)

uncert = []
for w in range(2, len(sootAggData), 3):
    uncert.append(sootAggData[w])
temp = np.asarray(uncert)


# creating new lists of time and radius but as ln(r) and ln(t)
time_ln = log(time)
radius_ln = log(radius)

plt.scatter(x=time_ln, y=radius_ln, marker='^', c='green')
plt.xlabel('ln(t) (time in minutes)')
plt.ylabel('ln(r) (radius in nm)')
plt.title('Soot aggregation over time')

regress_line2 = scipy.stats.linregress(x=time_ln, y=radius_ln)
plt.plot(time_ln, regress_line2.slope*time_ln + regress_line2.intercept, 'red')

intercept, slope = regress_line2.intercept, regress_line2.slope
ln_r = lambda x: slope*x + intercept

n = slope
print(exp(n))
print(exp(intercept))







