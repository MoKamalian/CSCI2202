# Amir Kamalian - CSCI 2202 - Lab 9
# Question 1 - This program takes a txt file of float data and returns a numpy array of that data.

# Question 1
import numpy as np


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


ldj = read_dat_file('/Users/mokamalian/Downloads/CSCI 2202 : W21:/Pycharm notes/LabA_Kamalian_Amir/coffeeTemp1.txt')
print(ldj)






