import pandas as pd

# Example DataFrame
data = {
    'Category': ['A', 'B', 'A', 'B', 'C', 'A'],
    'Value': [10, 20, 30, 40, 50, 60]
}

df = pd.DataFrame(data)

# Group by 'Category' and calculate the mean of 'Value'
grouped_mean = df.groupby('Category')['Value'].mean()

print(grouped_mean)
