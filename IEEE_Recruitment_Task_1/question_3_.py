import numpy as np

# Create random 5x5 matrix
matrix = np.random.randint(1, 101, size=(5, 5))
print("Original Matrix:\n", matrix)

# Max, Min, Mean
print("Max:", matrix.max())
print("Min:", matrix.min())
print("Mean:", matrix.mean())

# Normalize values between 0 and 1
normalized = (matrix - matrix.min()) / (matrix.max() - matrix.min())
print("\nNormalized Matrix:\n", normalized)

# Flatten, sort, and print
flattened = matrix.flatten()
sorted_array = np.sort(flattened)
print("\nFlattened & Sorted Array:\n", sorted_array)