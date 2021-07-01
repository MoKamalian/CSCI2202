# Amir Kamalian - CSCI 2202 - A2
# Problem 3 - This program plots the trajectory of a baseball with consideration to effect of drag on the trajectory.

import numpy as np
import matplotlib.pyplot as plt
from math import radians, sin, cos, sqrt

# Problem 3

v0 = float(input('Enter projectile speed: '))
angle = radians(float(input('Enter launch angle: ')))

# variables
m = 0.145     # in kg
radius = 0.0366     # in meters
CSA = 0.0042085   # in m^2
C = 0.5
density_air = 1.2   # kg/m^3
D = (density_air * C * CSA) / 2

# time values
Delta_t = 0.05
N = 3000
t_max = N * Delta_t
t = 0

# initial values
x_prev = -200
y_prev = 0
g = 9.8
vx_prev = v0 * cos(angle)
vy_prev = v0 * sin(angle) - g*t


x = []
y = []
while t < t_max:
    # drag acceleration
    a_x = -(D / m) * (sqrt(vx_prev**2 + vy_prev**2)) * vx_prev
    a_y = -g - (D / m) * (sqrt(vx_prev**2 + vy_prev**2)) * vy_prev

    # new component velocities
    vx_new = vx_prev + a_x * Delta_t
    vy_new = vy_prev + a_y * Delta_t

    # new component positions
    x_new = x_prev + vx_prev * Delta_t + 0.5 * a_x * (Delta_t**2)
    y_new = y_prev + vy_prev * Delta_t + 0.5 * a_y * (Delta_t**2)
    x.append(x_new)
    y.append(y_new)

    # resetting variables
    vx_prev = vx_new
    vy_prev = vy_new
    x_prev = x_new
    y_prev = y_new

    t += 1


plt.plot(np.asarray(x), np.asarray(y))
plt.show()




