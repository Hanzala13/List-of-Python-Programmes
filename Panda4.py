import pandas as pd

def add_calculated_column(df):
    """
    Adds a new column 'C' to the DataFrame, which is the sum of columns 'A' and 'B'.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame with at least columns 'A' and 'B'.
    
    Returns:
    pd.DataFrame: The DataFrame with the new column added.
    """
    df['C'] = df['A'] + df['B']
    return df

# Example usage
if __name__ == "__main__":
    # Create a sample DataFrame
    data = {
        'A': [10, 20, 30, 40],
        'B': [1, 2, 3, 4]
    }
    df = pd.DataFrame(data)
    
    # Print original DataFrame
    print("Original DataFrame:")
    print(df)

    # Add calculated column
    df = add_calculated_column(df)

    # Print updated DataFrame
    print("\nDataFrame after adding calculated column 'C':")
    print(df)
