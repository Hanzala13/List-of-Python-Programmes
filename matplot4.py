import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = np.random.normal(loc=50, scale=15, size=1000)

# Create histogram
plt.hist(data, bins=20, color='skyblue', edgecolor='black')

# Add labels and title
plt.title('Histogram of Sample Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show plot
plt.show()
