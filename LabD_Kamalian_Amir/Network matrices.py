# Amir Kamalian - CSCI 2202 - Lab D
# Part 1 - This program displays a 5x5 network matrix graph. Connections are counted as 1 no connections are counted
#          as 0. The number of walks of length k are also calculated based on users input, k.

import numpy as np
import matplotlib.pyplot as plt

# problem 1
# below is the adjacency matrix
A = np.array([[0, 1, 0, 0, 0],
              [1, 0, 0, 0, 1],
              [0, 1, 0, 0, 1],
              [0, 0, 1, 0, 1],
              [0, 1, 0, 1, 0]])

walks = int(input('Enter the number walks K: '))

print(np.linalg.matrix_power(A, walks))




