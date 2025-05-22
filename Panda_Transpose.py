import pandas as pd

def transpose_dataframe(df):
    """
    Takes a Pandas DataFrame and returns its transpose.

    Parameters:
    df (pd.DataFrame): The DataFrame to transpose.

    Returns:
    pd.DataFrame: The transposed DataFrame.
    """
    return df.transpose()

# Sample usage
if __name__ == "__main__":
    # Create a sample DataFrame
    data = {
        'Name': ['Alice', 'Bob'],
        'Age': [25, 30],
        'City': ['New York', 'Los Angeles']
    }

    df = pd.DataFrame(data)

    print("Original DataFrame:")
    print(df)

    # Transpose the DataFrame
    transposed_df = transpose_dataframe(df)

    print("\nTransposed DataFrame:")
    print(transposed_df)
