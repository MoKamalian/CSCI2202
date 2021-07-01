# Amir Kamalian - CSCI 2202 - Lab 2
# Ex 3 - Turtle chase: programming two turtles so that one chases other as it goes across the screen.

import turtle

turtleWindow = turtle.Screen()

turtleWindow.title('Lab2')

# Hendrix is the 'car' and rolling_stone is the 'dog'.
hendrix = turtle.Turtle(shape='turtle')
rolling_stone = turtle.Turtle(shape='turtle')
hendrix.fillcolor('green')
rolling_stone.fillcolor('blue')
x = 1000

# setting the positions of the turtles
hendrix.penup()
rolling_stone.penup()
hendrix.setposition(-x / 2, 0)
rolling_stone.setposition(0, 300)

# setting the heading of the turtles
hendrix.pendown()
hendrix.pencolor('red')
rolling_stone.pendown()
rolling_stone.pencolor('blue')


n = 0
while n != 375:
    hendrix.setheading(0)
    rolling_stone.setheading(rolling_stone.towards(hendrix))
    hendrix.forward(2.7)
    rolling_stone.forward(2.2)
    n += 1










