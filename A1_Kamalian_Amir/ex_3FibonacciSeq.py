# Amir Kamalian - CSCI 2202 - assignment 1
# Ex 3 a and b- This program takes input from the user and calculates the Fibonacci sequence. It also
#               take the values from the Fibonacci sequence and calculates the golden ratio.

# Ex 3 a)

n = int(input('Please enter a positive integer: '))

fib_number = []
start = 0
j = 1
fib_number.append(start)
fib_number.append(j)
for i in range(0, n + 1):
    t = fib_number[-2] + fib_number[-1]
    fib_number.append(t)


for i in fib_number:
    print('{:5d}'.format(i), end='')

# Ex 3 b)

print('\n')

d = 7
if 2 < d < 20:
    ratio = fib_number[d + 1] / fib_number[d]
    print(ratio)








