import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]

# Create scatter plot
plt.scatter(x, y)
plt.title('Scatter Plot of Two Variables')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.grid(True)
plt.show()
