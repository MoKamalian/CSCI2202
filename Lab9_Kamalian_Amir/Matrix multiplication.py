# Amir Kamalian - CSCI 2202 - Lab 9
# Part 1 and 2 - Part one simply creates a transition matrix meant to calculate the population change from 2007 to
#                2009 and also contains a transp(A) function (for transposing an array). Part 2 has two functions;
#                the first function (matmult()) takes two matrices and returns their product, and the second function
#                (mMult_noRet()) also calculates the product of two matrices but also takes a zeros array as a
#                parameter with the same dimensions as the product.


import numpy as np
from numpy.typing import ArrayLike
from random import randrange
import matplotlib.pyplot as plt
import scipy.linalg as sla


# Part 1: Making a transition matrix
initial_pop = np.array([[82], [163]])
pop_change = np.array([[0.96, 0.01], [0.04, 0.99]])


for i in range(2007, 2013):
    n = pop_change@initial_pop
    print(f'{i}:\n{n}\n')
    initial_pop = n


def transp(A):
    return np.transpose(A)


# Part 2: creating a matrix multiplyer

# Question 1: matmult function

# To be a compatible multiplication, the number of columns
# of X has to equal the number of rows of Y.
# The columns of Y are multiplies by the rows of X
# The completed product will contain the same number of rows as the first matrix,
# many rows as the first and as many columns as the second matrix


def matmult(m1: ArrayLike, m2: ArrayLike):
    rows = m1.shape[0]
    columns = m2.shape[1]
    result = np.zeros(shape=(rows, columns))
    for i in range(rows):
        # This will give use the number of times we need to
        # loop based for rows (3 rows here)
        for j in range(columns):
            # this gives the number of columns (3 columns here)
            for k in range(len(m2)):
                # since we have the length of column we can use
                # that to loop that many times
                result[i, j] += m1[i, k] * m2[k, j]
                # m1[i, k] -->i.e. for each row we will go through it
                # 'k' times which is the number of columns for m2.
                # m2[k, j] -->i.e. this will go through each row 'k' then
                # select the first column number 'j' for multiplication (but will not go
                # through the row entirely); instead it will select the next 'k' column
                # and again select the column number 'j'
                # m1[i, k] and m2[k, j] means m1 has the same number of rows as m2 has columns
    return result


# Test matrices
x1 = np.array([[3, -2],
               [2, 4],
               [1, -3]])

y2 = np.array([[-2, 1, 3],
               [4, 1, 6]])
print(matmult(x1, y2))

print('\n')
# Test matrices 2
x2 = np.array([[1, 2, 4],
               [6, 7, 9],
               [1, 9, 4]])

y2 = np.array([[4, 8],
               [1, 2],
               [5, 9]])
print(matmult(x2, y2))

print('\n')


# Question 2: mMult-noRet(X, Y, Z)

x3 = np.ndarray(shape=(5, 5))
for v in range(len(x3)):
    for o in range(len(x3[0])):
        t = randrange(0, 9, 1)
        x3[v, o] = t

y3 = np.ndarray(shape=(5, 5))
for m in range(len(y3)):
    for h in range(len(y3[0])):
        t = randrange(0, 9, 1)
        y3[m, h] = t

print(f'{x3}\n')
print(f'{y3}\n')

the_rows = x3.shape[0]
the_columns = y3.shape[1]
Z = np.zeros(shape=(the_rows, the_columns))


def mMult_noRet(X: ArrayLike, Y: ArrayLike, Z):
    rows = X.shape[0]
    columns = Y.shape[1]
    for q in range(rows):
        for j in range(columns):
            for k in range(len(Y)):
                Z[q, j] += X[q, k] * Y[k, j]
    return None








