import numpy as np

# Generate a random NumPy array with 10 elements between 0 and 100
array = np.random.randint(0, 100, size=10)

# Display the array
print("Generated array:", array)

# Find the maximum and minimum values
max_value = np.max(array)
min_value = np.min(array)

# Display the results
print("Maximum value:", max_value)
print("Minimum value:", min_value)
