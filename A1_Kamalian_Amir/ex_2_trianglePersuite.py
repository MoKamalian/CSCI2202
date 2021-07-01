# Amir Kamalian - CSCI 2202 - Assignment 1
# Ex 2 - This program has three turtles chase each other in a spiral pattern and terminating when they
#        meet.

import turtle

turtleWindow = turtle.Screen()

turtleWindow.title('Lab2')

# Hendrix is the 'car' and rolling_stone is the 'dog'.
hendrix = turtle.Turtle(shape='turtle')
rolling_stone = turtle.Turtle(shape='turtle')
pink_floyd = turtle.Turtle(shape='turtle')
hendrix.fillcolor('green')
rolling_stone.fillcolor('blue')
pink_floyd.fillcolor('pink')


# setting the positions of the turtles
hendrix.penup()
rolling_stone.penup()
pink_floyd.penup()
hendrix.setposition(0, 173.20508)
rolling_stone.setposition(-200, -173.20508)
pink_floyd.setposition(200, -173.20508)

# setting the heading of the turtles
hendrix.pendown()
hendrix.pencolor('red')
rolling_stone.pendown()
rolling_stone.pencolor('blue')
pink_floyd.pendown()
pink_floyd.pencolor('pink')


n = 0
while n != 265:
    rolling_stone.setheading(rolling_stone.towards(hendrix))
    rolling_stone.forward(1)
    hendrix.setheading(hendrix.towards(pink_floyd))
    hendrix.forward(1)
    pink_floyd.setheading(pink_floyd.towards(rolling_stone))
    pink_floyd.forward(1)
    n += 1






