# Question 1: Count the bases in a DNA sequence.

# Accept a DNA sequence from the user.
DNA = input("Enter a DNA sequence: ")

# Create a list containing all the possible DNA bases.
bases = ["A", "C", "G", "T"]

# Print the initial output text.
print("The frequency of bases is:  ", end="")

# For every base in the base list, use the str.count(..) method
# to return the number of times that base appears in the DNA
# sequence, then print it to the screen. This is performed using
# a special style of for-loop which takes the regular format:
#
#   for base in bases:
#       print(base + ":", DNA.count(base), end="  ")
# 
# and compresses it down to one line by putting the loop body
# before the for-loop header. This is very commonly used for
# quickly making lists of values.
[print(base + ":", DNA.count(base), end="  ") for base in bases]
