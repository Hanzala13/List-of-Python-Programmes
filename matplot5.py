import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame with multiple variables
data = sns.load_dataset("iris")  # Using the built-in iris dataset

# Create a scatter plot matrix (pair plot)
sns.pairplot(data)

# Show the plot
plt.show()
