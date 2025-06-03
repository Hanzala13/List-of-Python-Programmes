import pandas as pd
import matplotlib.pyplot as plt

def generate_box_plot(df):
    """
    Generates a box plot for each numerical column in the given DataFrame.

    Parameters:
    df (pd.DataFrame): A pandas DataFrame containing the data.

    Returns:
    None
    """
    if df.empty:
        print("The DataFrame is empty.")
        return

    # Only select numeric columns
    numeric_df = df.select_dtypes(include=['number'])

    if numeric_df.empty:
        print("No numeric data to plot.")
        return

    plt.figure(figsize=(10, 6))
    numeric_df.boxplot()
    plt.title("Box Plot of DataFrame Columns")
    plt.ylabel("Values")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
