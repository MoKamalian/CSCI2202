# Amir Kamalian - CSCI 2202 - Lab 4
# Ex 1 - From a list of numbers this code will find the highest and lowest number from that list.

user_input = input('Enter three numbers (separate by space, no commas): ')

numbers = []
for f in user_input.split(' '):
    float(f)
    numbers.append(f)


print(numbers)
print(max(numbers))
print(min(numbers))

