
# Set em to 1 to start.
em = 1

# Set the number of divisions to 0.
n = 0

# As long as em + 1 is greater than 1, divide em by 2
# and count another division.
while em + 1 > 1:
    em /= 2
    n += 1

# Print the final results. We end a step late,
# but some simple math will put everything back in line.
print("Divisions:", n-1)
print("Em       :", em*2)
print("Em + 1   :", em*2+1)
print("Em/2 + 1 :", em+1)
