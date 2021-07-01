# Amir Kamalian - CSCI 2202 - Lab 4
# Ex 4 b) - Code takes input n and uses that to estimate pi (n being the number of series) and also estimates
#           pi with n + 1 terms.

n = int(input('Enter a number: '))

f = 0
for i in range(1, n, 4):
    f += 4 / i
    f -= 4 / (i + 2)

for i in range(1, n + 1, 4):
    f += 4 / i
    f -= 4 / (i + 2)


print(f)
print(n)




