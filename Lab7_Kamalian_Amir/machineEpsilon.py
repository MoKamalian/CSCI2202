# Amir Kamalian - CSCI 2202 - Lab 7
# Ex 1 - This program calculates the machine epsilon.

a = 7.2 + 0.2 + 8.9 - 2.1
print(a)

epsilon = 1
f = 0
while f != 1:
    epsilon = epsilon / 2
    f += epsilon

print(float(epsilon * 2))







