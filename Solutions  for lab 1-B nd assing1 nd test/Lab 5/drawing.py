import turtle
import math

# Just for convenience, I have created a function for setting
# up my turtle so that I don't have to keep repeating the same
# code over and over when testing.
def initializeTurtle(name="Turtle Drawing", inShape="turtle"):
    screen = turtle.Screen().title(name)
    turt = turtle.Turtle(shape=inShape)
    turt.speed(0)
    return turt

# This function should draw a line based on the number of
# segments, their length, and the angle between each segment.
def polyLine(t, n, length, angle):
    t.forward(length)
    for i in range(n-1):
        t.left(angle)
        t.forward(length)

# This will draw an entire polygon by treating it as a circle
# to get the perimeter, then we find the number of segments
# to draw an calculate their angle before feeding it into
# our polyLine function from before.
def polygon(t, numSides):
    angle = 360/numSides
    length = (2 * math.pi * 200) / numSides
    polyLine(t, numSides, length, angle)

# An arc is simply drawing a polyLine which follows a particular
# length and angle based on a subtended angle.
def drawArc(t, r, a):
    s = r * (a * math.pi/180)
    n = int(s // 5)
    length = s / n
    angle = a / n
    polyLine(t, n, length, angle)

# We should be able to draw a circle by drawing an
# arc subtended by the 360 degrees.
def drawCircle(t, r):
    drawArc(t, r, 360)

# We draw a petal by drawing an arc, then rotating the turtle
# such that he is facing the opposite direction he started in
# and then draw the same arc again, taking the turtle back
# to his starting position.
def drawPetal(t, r, a):
    heading = t.heading()
    drawArc(t, r, a)
    t.setheading(heading-180)
    drawArc(t, r, a)

# A stem is just a polyLine that runs up the middle of the screen,
# starting from a particular angle.
def drawStem(t, length, heading):
    fill, pen = t.color()
    size = t.width()
    t.color("brown", "brown")
    t.width(5)
    t.setheading(heading)

    polyLine(t, 1, length, 0)

    t.color(fill, pen)
    t.width(size)

# Drawing a flower brings all of the functions together so
# that we can draw a series of petals a particular angle apart
# from each other, attached to a single stem. We also add some
# pretty colors so everyone knows how creative we are.
def drawFlower(t, r, angle, numPetals, p):
    t.goto(0, -150)
    turtle.Screen().bgcolor("#add8e6")

    drawStem(t, 300, 90)

    fill, pen = t.color()
    size = t.width()
    t.color("yellow", "yellow")
    t.width(3)
    
    for i in range(numPetals):
        t.setheading(i * p)
        drawPetal(t, r, angle)

    t.color(fill, pen)
    t.width(size)

# This is our main function. It only runs if this is
# the program we execute first. You can uncomment things
# to test them individually, but I like my flower <3
if __name__ == "__main__":
    turtz = initializeTurtle("My Pretty Flower")
    turtz.hideturtle()
    #polyLine(turtz, 5, 50, 20)
    #polygon(turtz, 6)
    #drawArc(turtz, 100, 90)
    #drawCircle(turtz, 100)
    #drawPetal(turtz, 100, 90)
    #drawStem(turtz, 100, 90)
    drawFlower(turtz, 100, 60, 6, 60)


