# Amir Kamalian - CSCI 2202 - Lab 4
# Ex 3 - Using Hanon's algorithm, this code takes a user input and calculates the square
#        root of the input

# 3. Hanon's algorithm

x = float(input('Enter a number: '))
g = x / 2

eps = 1.e-5
while abs(g * g - x) > eps:
    y = (g + x / g) / 2
    g = y

print(str(g))


x_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

for x in x_list:
    g = x / 2
    while abs(g * g - x) > eps:
        y = (g + x / g) / 2
        g = y
    print(str(g))




