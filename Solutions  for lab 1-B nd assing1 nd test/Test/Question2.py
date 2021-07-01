# Question 2: Generate and analyze a Collatz sequence.

# Accept an integer N from the user.
N = int(input("Enter a positive integer N: "))

# Create a list for holding the sequence with N as the first value.
sequence = [N]

# As long as N does not equal 1, continue iterating.
while N != 1:
    # If N is even, then N = N/2
    if N % 2 == 0:
        N = N // 2
    # If N is odd, then N = 3N + 1
    else:
        N = 3 * N + 1

    # After N has been recalculated, add it to the sequence list.
    sequence.append(N)

# Print the length of the sequence, and the sequence list, as
# per the instructions on the test.
print("The sequence for N =", sequence[0], "has length", len(sequence))
print("It is: ", sequence)
