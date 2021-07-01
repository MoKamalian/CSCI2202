from math import *
import turtle

# Get the value for Theta from the user and convert it to radians.
theta = float(input("Enter a value for theta: ")) * (pi/180)

# Get the value for initial velocity from the user.
v0 = float(input("Enter a value for the initial velocity: "))

# Get the Turtle canvas and create a new turtle named Turtz
screen = turtle.Screen()
turtz = turtle.Turtle(shape="turtle")
turtz.hideturtle()
turtz.speed(0)
screen.tracer(1, 0.001)

# Draw a cartesian plane for easy viewing.
turtz.penup()
turtz.setpos(-10000, 0)
turtz.pendown()
turtz.setpos(20000, 0)
turtz.penup()
turtz.setpos(0, 20000)
turtz.pendown()
turtz.setpos(0, -20000)
turtz.penup()

# Initialize the values for the turtle's starting position.
x0 = -200
y0 = 0

# Initialize the gravity constant.
g = 9.81

# Create variables for holding the maximum range and height values
maximumRange  = 0
maximumHeight = 0

# Create the time counting values.
t     = 0
dT    = 0.05
N     = 300
t_max = N * dT

# Move the turtle to the starting position
turtz.setpos(x0, y0)
turtz.pendown()
turtz.showturtle()
turtz.speed(1)
turtz.setheading(theta / (pi/180))
turtz.stamp()

# Create the initial values for acceleration, velocity, and position.
currentAX = 0
currentAY = -g
previousVX = v0 * cos(theta)
previousVY = v0 * sin(theta) - g*t
previousX = x0
previousY = y0

# Create lists for storing x, y, and t values
xPos = []
yPos = []
tPos = []

# Create a count for stamping
count = 0

# Iterate through time until we reach the maximum.
while t < t_max:
    # Calculate the current x and y position, as well as the current y velocity.
    currentVX = previousVX + currentAX * dT
    currentVY = previousVY + currentAY * dT

    currentX = previousX + currentVX * dT + (0.5) * currentAX * dT**2
    currentY = previousY + currentVY * dT + (0.5) * currentAY * dT**2

    # If we have crossed the x-axis, we know where our maximum range is
    if previousY > 0 and currentY <= 0:
        maximumRange = currentX - x0
        turtz.fillcolor("red")

    # If our velocity has peaked, choose the y-value closer to velocity = 0.
    if previousVY > 0 and currentVY <= 0:
        if abs(previousVY) < abs(currentVY):
            maximumHeight = previousY
        else:
            maximumHeight = currentY            

    # Add the appropriate x, y, and t values to the lists.
    xPos.append(currentX)
    yPos.append(currentY)
    tPos.append(t)

    # Set the heading for Turtz to look at the next point.
    turtz.setheading(turtz.towards(currentX, currentY))

    # Move Turtz to that point.
    turtz.setposition(currentX, currentY)

    # Apply the turtle stamp.
    if count % 10 == 0:
        turtz.stamp()

    # Update the previous x and y values and start again.
    previousX = currentX
    previousY = currentY
    previousVX = currentVX
    previousVY = currentVY

    # Update the time and counter
    t += dT
    count += 1

# Output the lists in a somewhat nicely formatted manner (though not perfect every time).
print("Time\tX Position\tY Position")

for i in range(len(xPos)):
    print('{:3.2f}'.format(tPos[i]), "\t",\
          '{:6.3f}'.format(xPos[i]), "\t",\
          '{:6.3f}'.format(yPos[i]))

# Output the maximum values.
print("The highest point the turtle reached was", '{:4.3f}'.format(maximumHeight))
print("The distance travelled before hitting the ground was", '{:4.3f}'.format(maximumRange))

