# Question 4a/b: Calculate the number of days of the year up to a given date.

# Import our isLeap(..) method from Part A.
from isLeapYear import isLeap

# Accept the date from the user in the proper format.
dateIn = input("Enter a date in the format DD-MM-YYYY: ")

# Split that input by -'s.
dateList = dateIn.split("-")

# Store the values from the user in descriptive variables.
day = int(dateList[0])
month = int(dateList[1])
year = int(dateList[2])

# Create a list containing the number of days in each month.
# Note that the list starts at 0, which is the number of days
# which have passed before January 1st. This means the list
# is actually storing the number of days which have passed
# in the month prior to the current month, where the last
# value is the number of days which have passed in December.
# We leverage this knowledge when we calculate the total days.
daysPerMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Since we have our days per month formatted as above, we can
# calculate the number of days with the following logic:
#   1. Our month value is in the range [1, 12].
#   2. This means daysPerMonth[month-1] is the number of days
#      in the month before the current one.
#   3. Therefore, the number of days that have passed before
#      this month must be the sum of all the values in our
#      daysPerMonth list up to, but not including, the index
#      of the current month. For example, if we're looking at
#      the date March 4, then the days before March must be total
#      of the days in the month before January (0), the days in
#      the month before February (31), and the days in the month
#      before March (28), which is 0 + 31 + 28 = 59 days.
#   4. Once we have that total, we simply add the number of days
#      we are into the current month, which is just the days value.
#      As with our March 4 example, we have 59 days already and if
#      we add 4 more, there must be 63.
total = sum(daysPerMonth[0:month]) + day

# If the year is a leap year, then February has 29 days instead
# of 28. This only matters if we're in the month of March or later.
# If it's March or later, all we do is add a day to our total.
if isLeap(year) and month > 2:
    total += 1

# We then print the date and day count as specified.
print(dateIn, "is day", total)
