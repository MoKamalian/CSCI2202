import drawing

'''
NOTE: I have slightly modified the drawing.py module to provide better
      resolution to the arcs. Instead of using 5 to calculate arc
      segments, I use 0.1 so that there are many more, giving us
      more accurate arcs.
'''

def calculateFibonacci(N):
    # Initialize a list containing the first two Fibonacci numbers.
    F = [0, 1]

    # Use a for loop to calculate the first N Fibonacci numbers.
    for i in range(N-1):
        F.append(F[-1] + F[-2])

    # Return the list of Fibonacci numbers.
    return F

def goldenSpiral(n=10, scale=5):
    # Get a list Fibonacci numbers up to the nth,
    # then remove the leading 0 number.
    F = calculateFibonacci(n)[1:]

    # Create a canvas for a turtle to draw on, then
    # retrieve the associated turtle.
    turt = drawing.initializeTurtle("Golden Spiral")

    # Set the turtle's line size to 3.
    turt.pensize(3)

    # Create a list of color names as strings.
    colors = "red blue orange".split()

    # Force the turtle screen to update faster, so we
    # don't wait forever for the drawing to finish.
    drawing.turtle.tracer(1, 0.0001)

    # Loop through every Fibonacci number in our list.
    for i in range(len(F)):
        # Pick the next color, in order.
        turt.pencolor(colors[i % 3])

        # Draw an arc such that the scale is 5, the
        # angle is 90, and the resolution of the line
        # is very small, so it draws the arc perfectly.
        drawing.drawArc(turt, scale*F[i], 90, 0.1)

# If this module is the main module, then we run the
# golden spiral function with its default parameters.
if __name__ == "__main__":
    goldenSpiral()

    
