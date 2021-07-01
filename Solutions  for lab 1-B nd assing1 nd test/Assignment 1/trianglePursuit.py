import turtle
import math

# Retrieve the Turtle window from the software and store it.
# This may be useful later.
window = turtle.Screen()
window.title("Turtz Chases Burtz!")

# Store a speed for turtles to walk
walkingSpeed = 8

# Create three turtles, Burtz, Turtz, and Murtz
burtz = turtle.Turtle(shape='turtle')
turtz = turtle.Turtle(shape='turtle')
murtz = turtle.Turtle(shape='turtle')

# The turtles are green and their paths are unique colours
burtz.color("red", "green")
turtz.color("blue", "green")
murtz.color("purple", "green")

# We don't want the turtles to draw lines yet
burtz.penup()
turtz.penup()
murtz.penup()

# Calculate the distance from the center based on side length of 400.
# The distance from the center of an equilateral triangle to any
# corner is (SideLength) / root(3).
distance = 400 / math.sqrt(3)

# Move Burtz, Turtz, and Murtz to their starting positions
startAngle = -30
burtz.setheading(startAngle)
turtz.setheading(startAngle + 120)
murtz.setheading(startAngle + 240)
burtz.forward(distance)
turtz.forward(distance)
murtz.forward(distance)

# Make sure the turtles are looking at each other
turtz.setheading(turtz.towards(burtz.pos()))
burtz.setheading(burtz.towards(murtz.pos()))
murtz.setheading(murtz.towards(turtz.pos())) 

# Let the turtles draw lines
burtz.pendown()
turtz.pendown()
murtz.pendown()

# Set the drawing update speed so that turtles can actually finish.
turtle.tracer(1, 0.001)

# Let all turtles chase until they're within 2*WalkingSpeed units of each other
while burtz.distance(turtz) > 2 * walkingSpeed:
    # Move the turtles forward one unit
    turtz.forward(walkingSpeed)
    burtz.forward(walkingSpeed)
    murtz.forward(walkingSpeed)

    # Adjust Turtz so he's still looking at Burtz
    turtz.setheading(turtz.towards(burtz.pos()))
    burtz.setheading(burtz.towards(murtz.pos()))
    murtz.setheading(murtz.towards(turtz.pos()))
