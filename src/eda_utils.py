import pandas as pd
import matplotlib.pyplot as plt



class SolarDataAnalyzer:
    """
    A utility class for loading and analyzing solar data.
    """

    def __init__(self, filepath):
        """
        Initialize the analyzer by loading the CSV data.

        Args:
            filepath (str): Relative path to the CSV file.
        """
        self.df = pd.read_csv(filepath)

    def plot_column(self, column, title="Column Over Time"):
        """
        Plot a time series line graph for a given column.

        Args:
            column (str): Column name to plot.
            title (str): Title of the plot.
        """
        plt.plot(self.df[column])
        plt.title(title)
        plt.xlabel("Time")
        plt.ylabel(column)
        plt.tight_layout()
        plt.show()

    def summary_stats(self):
        """
        Return summary statistics of the dataset.
        """
        return self.df.describe()
    