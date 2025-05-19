import pandas as pd

# Step 1: Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance'],
    'Salary': [50000, 60000, 70000, 52000, 58000, 62000]
}

df = pd.DataFrame(data)

# Step 2: Filtering - Employees with Salary > 55000
filtered_df = df[df['Salary'] > 55000]
print("Filtered DataFrame (Salary > 55000):")
print(filtered_df)

# Step 3: Grouping - Average salary by department
grouped_df = df.groupby('Department')['Salary'].mean()
print("\nAverage Salary by Department:")
print(grouped_df)
