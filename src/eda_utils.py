import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(filepath):
    """
    Load a CSV file into a DataFrame with error handling.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data or empty DataFrame if error occurs.
    """
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"[ERROR] File not found: {filepath}")
        return pd.DataFrame()
    except pd.errors.ParserError:
        print(f"[ERROR] Could not parse the file: {filepath}")
        return pd.DataFrame()


def get_numeric_columns(df):
    """
    Get numeric column names from the DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        list: List of numeric column names.
    """
    return df.select_dtypes(include=np.number).columns.tolist()


def validate_columns(df, required_columns):
    """
    Validate that all required columns exist in the DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame.
        required_columns (list): List of expected column names.

    Raises:
        ValueError: If any column is missing.
    """
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")


def compute_zscores(df, columns):
    """
    Compute absolute Z-scores for the specified columns.

    Args:
        df (pd.DataFrame): Input DataFrame.
        columns (list): List of numeric columns.

    Returns:
        pd.DataFrame: Z-score DataFrame.
    """
    try:
        zscores = np.abs(stats.zscore(df[columns]))
        return pd.DataFrame(zscores, columns=columns)
    except Exception as e:
        print(f"[ERROR] Failed to compute Z-scores: {e}")
        return pd.DataFrame()


def filter_outliers(df, zscore_df, threshold=3):
    """
    Remove rows with Z-score above the threshold.

    Args:
        df (pd.DataFrame): Original data.
        zscore_df (pd.DataFrame): Z-score DataFrame.
        threshold (float): Z-score threshold.

    Returns:
        pd.DataFrame: Filtered DataFrame without outliers.
    """
    try:
        mask = (zscore_df < threshold).all(axis=1)
        return df[mask]
    except Exception as e:
        print(f"[ERROR] Filtering outliers failed: {e}")
        return df


def impute_missing_values(df, columns):
    """
    Impute missing values in specified columns using median.

    Args:
        df (pd.DataFrame): Input DataFrame.
        columns (list): Columns to impute.

    Returns:
        pd.DataFrame: DataFrame with imputed values.
    """
    for col in columns:
        if df[col].isna().sum() > 0:
            median_val = df[col].median()
            df[col].fillna(median_val, inplace=True)
    return df


def plot_correlation_heatmap(df, title="Correlation Heatmap"):
    """
    Plot a heatmap of correlations between numeric columns.

    Args:
        df (pd.DataFrame): DataFrame to analyze.
        title (str): Title for the plot.
    """
    try:
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
        plt.title(title)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"[ERROR] Failed to generate heatmap: {e}")


def plot_time_series(df, column, title="Time Series Plot"):
    """
    Plot a time series line plot of a selected column.

    Args:
        df (pd.DataFrame): DataFrame with time and target column.
        column (str): Column to plot.
        title (str): Plot title.
    """
    try:
        plt.figure(figsize=(12, 4))
        plt.plot(df[column])
        plt.title(title)
        plt.xlabel("Index / Time")
        plt.ylabel(column)
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"[ERROR] Failed to generate time series plot: {e}")
