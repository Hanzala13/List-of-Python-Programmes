import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {
    'Department': ['Sales', 'HR', 'IT', 'Sales', 'HR', 'IT', 'IT', 'Sales', 'HR', 'Sales']
}
df = pd.DataFrame(data)

# Count the frequency of each category in the 'Department' column
counts = df['Department'].value_counts()

# Plotting the pie chart
plt.figure(figsize=(6,6))
plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Department Distribution')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.show()
