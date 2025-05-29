import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 45, 12, 36]
}
df = pd.DataFrame(data)

# Create a bar plot
sns.barplot(x='Category', y='Values', data=df)

# Display the plot
plt.title('Bar Plot of Categories')
plt.show()
