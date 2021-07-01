# Create a variable for storing initial velociy in m/s
v_0 = 5

# Create a variable for storing the acceleration due to gravity in m/s^2
g = 9.81

# Create a variable for storing the desired time in seconds
t = 0.6

# Calculate the ball position in meters
y = v_0 * t - 0.5 * g * t**2

# Inform the user of the current ball position
print("At t = " + str(t) + " the position of the ball is " + str(y))
