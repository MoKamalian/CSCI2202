# Amir Kamalian - CSCI 2202 - Lab 2
# Ex 1 - This program allows turtle to draw polygons with the number of sides according to input
#        from the user.

import turtle

numSides = int(input('Enter the number of sides: '))

turtleWindow = turtle.Screen()

turtleWindow.title('Lab2')

hendrix = turtle.Turtle(shape='turtle')

angle = 360 / numSides
direction = 500 / numSides

for i in range(numSides):
    hendrix.pencolor('black')
    hendrix.forward(direction)
    hendrix.left(angle)





