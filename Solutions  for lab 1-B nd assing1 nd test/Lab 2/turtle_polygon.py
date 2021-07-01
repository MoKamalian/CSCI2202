import turtle
import math

# Create a variable for the number of sides to make
sides = int(input("Enter the number of sides: "))

# Retrieve the Turtle window from the software and store it.
# This may be useful later.
window = turtle.Screen()

# Store a distance for your turtle to walk.
# This formula finds the perimeter of a circle (2*pi*r) with 
# radius 200 and divides that distance by the number of sides,
# telling us what each side's length should approximately be.
walkingDistance = (2 * math.pi * 200) / sides

# Create a turtle named Turtz
turtz = turtle.Turtle(shape='turtle')

# Turtz is a green turtle who leaves a blue trail
turtz.color("blue", "green")

# Set the turtle speed equal to the number of sides.
turtz.speed(sides)

# If we want a polygon with N sides, then each time we
# turn, we need to go 360/N degrees.
angle = 360 / sides

# We need to move and turn our turtle once for every side
for i in range(sides):
        # Make the turtle walk forward
        turtz.forward(walkingDistance)

        # Turn the turtle to the left
        turtz.left(angle)
