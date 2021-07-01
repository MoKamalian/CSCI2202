import turtle
import math
from random import random, randint

# Create a variable for the number of sides to make
sides = int(input("Enter the number of sides: "))

# Create a variable for the number of polygons
polygons = int(input("Enter the number of polygons: "))

# Retrieve the Turtle window from the software and store it.
# This may be useful later.
window = turtle.Screen()

# Store a distance for your turtle to walk.
# This formula finds the perimeter of a circle (2*pi*r) with 
# radius 100 and divides that distance by the number of sides,
# telling us what each side's length should be.
walkingDistance = (2 * math.pi * 100) / sides

# Calculate the angles at which to start drawing each polygon.
angle = 360 / sides
angles = [360/polygons*x for x in range(polygons)]

# Create a turtle named Turtz
turtz = turtle.Turtle(shape='turtle')

# Turtz is a green turtle who leaves a blue trail
turtz.color("blue", "green")

# Set the turtle speed equal to the number of sides.
turtz.speed(sides)

# Create a list of two colors
colorList = ["red", "blue"]

# Set the offset for angle drawing
offset = angle / sides

# Set a starting count
count = 0

# We need to move and turn our turtle once for every side
for a in angles:
        # Update count for the color list
        count = (count + 1) % len(colorList)

        # Alternate between two colors using count
        turtz.pencolor(colorList[count])

        # Set Turtz to the next angle to start drawing a polygon from.
        turtz.setheading(a + offset)

        # Loop through the polygon sides.
        for i in range(sides):
                # Make the turtle walk forward
                turtz.forward(walkingDistance)

                # Turn the turtle to the left
                turtz.left(angle)
