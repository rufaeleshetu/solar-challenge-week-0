import pandas as pd
import matplotlib.pyplot as plt

def load_data(path):
    """
    Load a CSV file into a pandas DataFrame.
    """
    return pd.read_csv(path)

def plot_timeseries(df, column, title):
    """
    Plot a time-series column from the DataFrame.
    """
    plt.figure(figsize=(10, 4))
    df[column].plot()
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel(column)
    plt.tight_layout()
    plt.show()