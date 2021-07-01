# Amir Kamalian - CSCI 2202 - Lab 4
# Ex 4 a) - This code will take number from user and have that be the number of series used to get an
#           estimate for pi

# Ex 4. piSeries

n = int(input('Enter a number: '))

f = 0
for i in range(1, n, 4):
    f += 4 / i
    f -= 4 / (i + 2)

print(f)








