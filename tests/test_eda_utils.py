import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pandas as pd
from src.eda_utils import SolarDataAnalyzer


def test_summary_stats_returns_dataframe():
    df = pd.DataFrame({
        'GHI': [100, 200, 150, 180],
        'DNI': [90, 210, 140, 160]
    })
    df.to_csv('test_sample.csv', index=False)

    analyzer = SolarDataAnalyzer('test_sample.csv')
    summary = analyzer.summary_stats()

    assert isinstance(summary, pd.DataFrame)
    assert 'GHI' in summary.columns or 'GHI' in summary.index
