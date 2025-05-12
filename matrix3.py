import numpy as np

# Generate an array with numbers from 0 to 9
arr = np.arange(10)

# Reshape the array into a 3x3 matrix (we need only first 9 elements)
matrix = arr[:9].reshape(3, 3)

print(matrix)
