import pandas as pd

# Step 1: Create a Python list
data_list = [10, 25, 7, 42, 30]

# Step 2: Convert the list into a Pandas Series
series = pd.Series(data_list)

print("Original Series:")
print(series)

# Step 3: Filter values greater than 20
filtered = series[series > 20]
print("\nFiltered (values > 20):")
print(filtered)

# Step 4: Sort the Series
sorted_series = series.sort_values()
print("\nSorted Series:")
print(sorted_series)
