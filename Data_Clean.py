import pandas as pd

# Sample DataFrame with missing values
data = {
    'Name': ['Alice', 'Bob', None],
    'Age': [25, None, 30],
    'City': ['New York', 'Paris', 'London']
}
df = pd.DataFrame(data)

# Remove rows with any missing values
df_cleaned = df.dropna()

print(df_cleaned)
