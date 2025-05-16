import numpy as np

# Define a 2x2 matrix
A = np.array([[4, 7],
              [2, 6]])

# Calculate the inverse
try:
    A_inv = np.linalg.inv(A)
    print("Inverse of the matrix:")
    print(A_inv)
except np.linalg.LinAlgError:
    print("The matrix is singular and cannot be inverted.")
