# Question 4b: Write a function for determining a leap year.

# Create a method named isLeap. It takes in a single
# parameter, year, which should be an integer.
def isLeap(year):
    # The three things the instructions ask you to check are:
    # A. Is the year a century year? (Divisible by 100)
    # B. Is the year divisible by 4?
    # C. Is the year divisible by 400?
    # The following three lines calculate the True/False
    # outcome of each condition and store it in a variable.
    A = (year % 100 == 0)
    B = (year % 4 == 0)
    C = (year % 400 == 0)

    # Return the True/False outcome of the following two cases:
    # not A and B: If the year is not divisble by 100, but it is
    #              divisible by 4, then it's a leap year.
    # C:           If the year is divisible by 400, then it is
    #              a leap year. We don't have to check if it's
    #              a century year, because if the year is divisible
    #              by 400, then it must also be divisible by all the
    #              factors of 400. 100 is a factor of 400, so we don't
    #              need to check (A and C). We can just check C.
    return (not A and B) or C
