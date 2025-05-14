import numpy as np

def transpose_array(arr):
    """
    This function takes a NumPy array and returns its transpose.
    
    Parameters:
    arr (numpy.ndarray): Input NumPy array
    
    Returns:
    numpy.ndarray: Transposed array
    """
    return arr.T

# Sample input array
original_array = np.array([[1, 2, 3],
                           [4, 5, 6]])

# Get the transpose
transposed_array = transpose_array(original_array)

# Print the results
print("Original Array:")
print(original_array)

print("\nTransposed Array:")
print(transposed_array)
