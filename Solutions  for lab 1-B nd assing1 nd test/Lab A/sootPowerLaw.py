from coffeePlot import *
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Read in the data file in the format of t, r
t, r = readDatFile("growingAggregate.txt")

# Take ln(t_n) and ln(r_n) to ensure straight regressions.
t = np.log(t)
r = np.log(r)

# Calculate the regression data on t, r.
regress = stats.linregress(t, r)

# Calculate the y values for the line of best fit.
# n = slope and r0 = intercept.
regression = regress[0] * t + regress[1]

# Generate the plot for t, r, and the regression.
plotRegression(t, r, regression, "Time", "Radius")
