# Amir Kamalian - CSCI 2202 - Lab 2
# Ex 2 - Python program takes in input from the user as the number of sides for a polygon and draws
#        a spiral with the shape of that polygon.

import turtle

numSides = int(input('Enter the number of sides: '))

turtleWindow = turtle.Screen()

turtleWindow.title('Lab2')

hendrix = turtle.Turtle(shape='turtle')

angle = 360 / numSides

side_length = 0
while side_length != 200:
    side_length += 2
    hendrix.pencolor('black')
    hendrix.forward(side_length)
    hendrix.left(angle)













