import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def readDatFile(inFile):
    file = open(inFile, "r")
    x = []
    y = []
    line = file.readline()
    while line:
        fileSplit = line.split()
        x.append(float(fileSplit[0]))
        y.append(float(fileSplit[1]))
        line = file.readline()
    file.close()
    return np.array(x), np.array(y)

def plotRegression(x, y, r, xLabel, yLabel, time=3):
    plt.scatter(x, y)
    plt.plot(x, r)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.pause(time)
    plt.clf()

if __name__ == "__main__":
    # Read in the coffee data.
    x, y = readDatFile("coffeeTemp.txt")

    # Calculate the regression data on x,y
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

    # Calculate the y-values for the line of best fit.
    regression = slope * x + intercept

    # Generate the plot for x, y, and the regression.
    plotRegression(x, y, regression, "Time", "Temperature")
        
    # Calculate the delta T values from y.
    deltaT = np.diff(y)

    # Calculate the Tn - T_0 values from y and discard the last value.
    TnTo = y - 22.0
    TnTo = TnTo[:-1]

    # Calculate the regression data on TnTo,deltaT
    slope, intercept, r_value, p_value, std_err = stats.linregress(TnTo, deltaT)
    
    # Calculate the y-values for the line of best fit.
    regression = slope * TnTo + intercept

    # Generate the plot for TnTo, deltaT, and the regression
    plotRegression(TnTo, deltaT, regression, "Tn - T0", "delta T")
