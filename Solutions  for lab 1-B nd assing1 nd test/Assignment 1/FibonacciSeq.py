# Fibonacci Rabbits

# Accept an integer N from the user.
N = int(input("Enter a positive integer: "))

# Initialize a list containing the first two Fibonacci numbers.
F = [0, 1]

# Use a for loop to calculate the first N Fibonacci numbers.
for i in range(N+1):
    F.append(F[-1] + F[-2])

# Print all of the Fibonacci numbers, with 5 per line.
print("Fibonacci Numbers:")
for i in range(len(F)):
    if i > 0 and i % 5 == 0:
        print()
    print(F[i], end="\t")
print()

# Print the answer to Leonardo's question.
print("\nAfter 12 months there will be", F[12], "rabbits.\n")

# Calculate the ratio between Fibonacci numbers.
print("Ratios of Fibonacci Numbers:")
for i in range(2, 21):
    print(str(i)+":", F[i]/F[i-1])
print()

