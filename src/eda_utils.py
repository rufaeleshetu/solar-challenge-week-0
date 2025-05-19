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
        """
        plt.plot(self.df[column], title=title)
        plt.tight_layout()
        plt.show()

    def summary_stats(self):
        """
        Return summary statistics of the dataset.
        """
        return self.df.describe()
    
    