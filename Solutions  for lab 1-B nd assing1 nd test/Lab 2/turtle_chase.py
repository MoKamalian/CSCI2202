import turtle

# Retrieve the Turtle window from the software and store it.
# This may be useful later.
window = turtle.Screen()
window.title("Turtz Chases Burtz!")

# Store a speed for Burtz and Turtz to walk
walkingSpeed = 6

# Create a variable to hold the distance for Burtz to run
distanceToRun = 600

# Create two turtles, Burtz and Turtz
burtz = turtle.Turtle(shape='turtle')
turtz = turtle.Turtle(shape='turtle')

# The turtles are green and their paths are unique colours
burtz.color("red", "green")
turtz.color("blue", "green")

# We don't want the turtles to draw lines yet
burtz.penup()
turtz.penup()

# Move Burtz and Turtz to their starting positions
burtz.setposition(-1 * distanceToRun/2, 0)
turtz.setposition(0, distanceToRun/2)

# Make sure Turtz is looking at Burtz
turtz.setheading(turtz.towards(burtz.pos()))

# Let both turtles run the distance we have stored
for i in range(int(distanceToRun/walkingSpeed)):
    # By default, the turtles should draw
    burtz.pendown()
    turtz.pendown()

    # If the current time step is even, don't let the turtles draw
    if i % 2 == 0:
        burtz.penup()
        turtz.penup()

    # Move Burtz and Turtz forward one step
    turtz.forward(walkingSpeed)
    burtz.forward(walkingSpeed)

    # Adjust Turtz so he's still looking at Burtz
    turtz.setheading(turtz.towards(burtz))




    
