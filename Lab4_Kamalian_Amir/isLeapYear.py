# Amir Kamalian - CSCI 2202 - Lab 4
# Ex 2 - Given the year, the code will output whether that year is a leap year or not


user_in = int(input('Enter a year: '))

if (user_in % 100) == 0:
    if user_in < 1582:
        print(f'{user_in} is not a leap year')
    elif user_in > 1582 and (user_in % 400) == 0:
        print(f'{user_in} is a leap year')
    else:
        print(f'{user_in} is not a leap year')
elif user_in > 1582:
    if (user_in % 4) == 0:
        print(f'{user_in} is a leap year')
    else:
        print(f'{user_in} is not a leap year')
else:
    print(f'{user_in} is not a leap year')




