# Amir Kamalian - CSCI 2202 - Lab 5
# Question 1 - Combination of several functions used to draw a flower in Turtle

import math
import turtle

hendrix = turtle.Turtle(shape='arrow')

turtleWindow = turtle.Screen()

turtleWindow.title('Lab5')


def polyline(t: turtle, n: int, length, angle):
    '''Draws n number of line segments with certain length
    and angle to previous line'''
    for i in range(n):
        t.forward(length)
        t.left(angle)


# polyline(t=hendrix, n=5, length=55, angle=15)

def polygon(t: turtle, numside):
    '''Function draws a polygon with numside number
    of sides'''
    angle = 360 / numside
    direction = 500 / numside
    polyline(t=t, n=numside, angle=angle, length=direction)


def drawarc(t: turtle, alpha, r):
    '''Draws an arc depending on the angle (alpha)
    and radius (r) given'''
    s = r * math.radians(alpha)
    n = int(s // 5)
    angle = (alpha / n)
    polyline(t, n, 5, angle)


# drawarc(hendrix, 180, 50)

def draw_circle(t: turtle, r):
    '''Will draw circle using the drawarc function'''
    alpha = 360
    drawarc(t=t, alpha=alpha, r=r)


# draw_circle(hendrix, 50)

def draw_petal(t: turtle, alpha, r):
    '''Using the drawarc functions draws petals with certain
    angle (alpha) with radius (r)'''
    heading1 = turtle.heading()
    drawarc(t, alpha, r)
    angle2 = heading1 + 180
    turtle.setheading(angle2)
    drawarc(t, alpha, r)


# draw_petal(hendrix, 78, 200)

def draw_stem(t: turtle, length, heading):
    '''Draws stem of the flower from (0, 0) position'''
    turtle.pencolor('brown')
    turtle.setheading(heading)
    turtle.forward(length)


# draw_stem(hendrix, 200, 270)

def draw_flower(t: turtle, r, flower_angle, nump_petals, p):
    '''From the draw_petal function and the draw_stem function
    will draw a flower with certain number of petals p distance
    apart'''
    for petals in range(nump_petals):
        flower_angle += p
        draw_petal(t, flower_angle, r)
        flower_angle -= p
    rolling_stone = turtle.shape('arrow')
    draw_stem(rolling_stone, 200, 270)








