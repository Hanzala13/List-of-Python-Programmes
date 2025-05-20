import pandas as pd

# Sample data for demonstration
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 22, 30],
    'Score': [88, 95, 85]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Function to sort DataFrame rows in ascending order by all columns
def sort_dataframe(df):
    return df.sort_values(by=df.columns.tolist(), ascending=True)

# Call the function
sorted_df = sort_dataframe(df)

# Display the result
print("Original DataFrame:")
print(df)
print("\nSorted DataFrame:")
print(sorted_df)
