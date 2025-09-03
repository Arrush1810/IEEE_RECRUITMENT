mport numpy as np

# Create random 5x5 matrix
matrix = np.random.randint(1, 101, size=(5, 5))
print("Original Matrix:\n", matrix)

# Extract middle 3x3 matrix
middle = matrix[1:4, 1:4]
print("\nMiddle 3x3 Matrix:\n", middle)

# First row of 3x3 and last column
first_row = middle[0, :]
last_col = middle[:, -1]
dot_product = np.dot(first_row, last_col)

print("\nFirst Row:", first_row)
print("Last Column:", last_col)
print("Dot Product:", dot_product)