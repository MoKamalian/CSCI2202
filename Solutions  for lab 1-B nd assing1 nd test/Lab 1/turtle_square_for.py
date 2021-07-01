import turtle

# Retrieve the Turtle window from the software and store it.
# This may be useful later.
window = turtle.Screen()

# Create a turtle named Turtz
turtz = turtle.Turtle(shape='turtle')

# Turtz is a green turtle who leaves a blue trail
turtz.color("blue", "green")

# We need to move and turn our turtle once for every side
for i in range(4):
        # Make the turtle walk forward
        turtz.forward(100)

        # Turn the turtle to the left
        turtz.left(90)
