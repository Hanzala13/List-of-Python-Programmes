import matplotlib.pyplot as plt

# Example data points
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

# Create the line plot
plt.plot(x, y, marker='o')  # 'o' marks the data points

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')

# Show the plot
plt.grid(True)
plt.show()
