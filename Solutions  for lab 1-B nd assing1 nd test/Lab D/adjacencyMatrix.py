import numpy as np

# Set the dimensions of the matrix. Adjacency matrices are squares,
# so we only need one dimension value.
n = 5

# Set a value for the path length.
k = 3

# Create your matrix A with default values of 0 throughout.
A = np.zeros((n, n))

# Create your edge list.
edges = [[0,1], [1,0], [1,4], [2,1], [2,4], [3,2], [3,4], [4,1], [4,3]]

# Insert all your edges into both adjacency matrices.
for edge in edges:
    A[edge[0]][edge[1]] = 1

# Print the initial matrix state
print("Initial Matrix:")
print(A)

# Make a copy of A for powering
A2 = np.copy(A)

# Run the multiplication k-1 times.
for t in range(k-1):
    A = A2@A

# Print the final result matrix
print("\nResult for Paths of Length", k)
print(A)

print("\nNumber of paths:", sum(sum(A)))
