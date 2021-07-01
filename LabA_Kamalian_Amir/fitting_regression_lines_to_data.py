# Amir Kamalian - CSCI 2202 - Lab 9
# Question 2 - This program takes the coffee temperature data, produces a scatter plot and a line of best fit to the
#              the colling temperature data.

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats


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


coffee_data = read_dat_file('/Users/mokamalian/Downloads/CSCI 2202 : W21:/Pycharm notes/'
                            'LabA_Kamalian_Amir/coffeeTemp1.txt')


# Question 2 a)
time = []
for k in range(0, len(coffee_data), 2):
    time.append(coffee_data[k])
time = np.asarray(time)

temp = []
for w in range(1, len(coffee_data), 2):
    temp.append(coffee_data[w])
temp = np.asarray(temp)

plt.scatter(x=time, y=temp, marker='v', c='red')
plt.xlabel('time (min)')
plt.ylabel('temperature (C)')
plt.title('Cooling rate of Coffee')


# Question 2 b)
# T_change = -K(T_n - T_0)
# regress_line.slope*time + regress_line.intercept ---> equivalent to y = mx + b
regress_line = scipy.stats.linregress(x=time, y=temp)
plt.plot(time, regress_line.slope*time + regress_line.intercept, 'green')












