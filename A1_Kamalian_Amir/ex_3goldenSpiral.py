# Amir Kamalian - CSCI 2202 - assignment 1
# Ex 3 - This program draws the Fibonacci spiral using the drawarc function from lab 5.


import turtle
import math

# Ex 3 c)


def polyline(t: turtle, n: int, length, angle):
    '''Draws n number of line segments with certain length
    and angle to previous line'''
    for i in range(n):
        turtle.forward(length)
        turtle.left(angle)


def polygon(t: turtle, numside):
    '''Function draws a polygon with numside number
    of sides'''
    angle = 360 / numside
    direction = 500 / numside
    polyline(t=turtle, n=numside, angle=angle, length=direction)


def drawarc(t: turtle, alpha, r):
    '''Draws an arc depending on the angle (alpha)
    and radius (r) given'''
    s = r * math.radians(alpha)
    n = int(s // 5)
    angle = (alpha / n)
    polyline(t, n, 5, angle)


def feb_spiral(turt):
    fib_numberc = []
    startc = 0
    second = 1
    fib_numberc.append(startc)
    fib_numberc.append(second)
    for i in range(0, 10 + 1):
        result = fib_numberc[-2] + fib_numberc[-1]
        fib_numberc.append(result)

    reverse_fib = list(reversed(fib_numberc))
    cycle = 0
    for s in reverse_fib:
        if s == 0:
            break
        else:
            if cycle % 2 == 0:
                tt = turt.pencolor('yellow')
                drawarc(t=tt, alpha=90, r=s)
                cycle += 1
            else:
                tt = turt.pencolor('red')
                drawarc(t=tt, alpha=90, r=s)
                cycle += 1


jimi = turtle.Turtle(shape='arrow')
feb_spiral(jimi)








