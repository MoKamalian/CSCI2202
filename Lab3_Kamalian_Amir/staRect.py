# Amir Kamalian - CSCI 2202 - Lab 3
# Question 1 a) - Using asterisks to make a rectangle

r = int(input('Enter an integer (r): '))
c = int(input('Enter an integer (c): '))


for i in range(r):
    for n in range(c):
        print('*', end='')
    print()


# one line rectangle

rows = int(input('Enter rows: '))
columns = int(input('Enter columns: '))

print((('*' * columns) + '\n') * rows)





