import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def generate_pair_plot(df):
    """
    Generates a pair plot to visualize the relationships between variables in a DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame containing numerical data.

    Returns:
    None
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")

    sns.pairplot(df)
    plt.show()
