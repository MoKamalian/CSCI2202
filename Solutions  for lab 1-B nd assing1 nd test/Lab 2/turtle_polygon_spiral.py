import turtle

# Create a variable for the number of sides to make
sides = int(input("Enter the number of sides: "))

# Retrieve the Turtle window from the software and store it.
# This may be useful later.
window = turtle.Screen()

# Create a turtle named Turtz
turtz = turtle.Turtle(shape='turtle')

# Turtz is a green turtle who leaves a blue trail
turtz.color("blue", "green")

# Set the turtle speed equal to the number of sides.
turtz.speed(sides)

# If we want a polygon with N sides, then each time we
# turn, we need to go 360/N degrees.
angle = 360 / sides

# Set a starting side length
distance = 1

# While the side is still less than 200 units long, continue looping
while distance <= 200:
    # Move the turtle forward the current distance
    turtz.forward(distance)

    # Turn the turtle to the left based on our calculated angle
    turtz.left(angle)

    # Increase the length of the next side by 2
    distance += 2
