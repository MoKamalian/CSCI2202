# Amir Kamalian - CSCI 2202 - Assignment 1
# Ex 1 - This program draws a number of polygons in a circular pattern, rotated a certain
#        number of times.

import turtle

num_polygons = int(input('Enter a number of polygons: '))
numSides = int(input('Enter the number of sides: '))

turtleWindow = turtle.Screen()
turtleWindow.title('Lab2')
hendrix = turtle.Turtle(shape='turtle')

angle = 360 / numSides
direction = 500 / numSides
angle_add = 360 / num_polygons
pol_angle = 0
colour = ['blue', 'green']

for n in range(num_polygons):
    pol_angle += angle_add
    hendrix.setheading(pol_angle)
    if (n % 2) == 0:
        hendrix.pencolor('red')
    elif (n % 2) != 0:
        hendrix.pencolor('green')
    for i in range(numSides):
        hendrix.forward(direction)
        hendrix.left(angle)











