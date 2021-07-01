# Amir Kamalian - CSCI 2202 - Lab 3
# Question 2 - Projectile motion of a turtle

import math
from math import cos, sin as cos, sin
import turtle

launch_angle = float(input('Enter angle of launch: '))
v_i = float(input('Enter initial velocity: '))

turtleWindow = turtle.Screen()
turtleWindow.title('Lab2')
hendrix = turtle.Turtle(shape='turtle')

hendrix.color('black')
hendrix.up()
hendrix.setposition(-200, 0)
hendrix.down()

g = 9.81
x_i = -200
y_i = 0
theta = math.radians(launch_angle)
t = 16

x_list = []
y_list = []
t_list = []

for t in range(1, t):

    x = x_i + v_i * cos(theta) * t
    y = y_i + v_i * sin(theta) * t - g / 2 * t ** 2
    # forgot to account for the changing velocity in
    # y direction.
    # also didn't update the x and y values

    x_list.append(x)
    y_list.append(y)
    t_list.append(t)

    hendrix.setheading(theta)
    hendrix.setposition(x, y)
    hendrix.stamp()


for i in range(len(x_list)):
    print(x_list[i], '\t', y_list[i], '\t', t_list[i])

print('\n')

max_height = (v_i ** 2 * sin(theta) ** 2) / (2 * g)
print(max_height)
max_distance = (sin(2 * theta) * v_i ** 2) / g
print(max_distance)

angles = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]




