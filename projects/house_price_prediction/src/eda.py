# src/eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import os
from src.data_loading import TARGET_COLUMN

def explore_data(df: pd.DataFrame) -> None:
    """
    Perform exploratory data analysis with visualizations.

    Parameters:
    - df: DataFrame to analyze.
    """
    logging.info("Starting exploratory data analysis...")

    # Ensure 'eda/' directory exists
    os.makedirs('eda', exist_ok=True)

    # Correlation matrix
    plt.figure(figsize=(12,10))
    corr = df.corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.savefig('eda/correlation_matrix.png')  # Save the plot
    plt.close()

    # Distribution of target variable
    plt.figure(figsize=(8,6))
    sns.histplot(df[TARGET_COLUMN], kde=True, bins=30)
    plt.title("Distribution of House Prices")
    plt.xlabel("Price (in $1000's)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig('eda/price_distribution.png')
    plt.close()

    # Scatter plots of features vs target
    features = ['rm', 'lstat', 'ptratio']
    for feature in features:
        plt.figure(figsize=(8,6))
        sns.scatterplot(x=df[feature], y=df[TARGET_COLUMN])
        plt.title(f"{feature.upper()} vs Price")
        plt.xlabel(feature.upper())
        plt.ylabel("Price (in $1000's)")
        plt.tight_layout()
        plt.savefig(f'eda/{feature}_vs_price.png')
        plt.close()

    # Boxplot of 'chas' vs target
    if 'chas' in df.columns:
        plt.figure(figsize=(8,6))
        sns.boxplot(x=df['chas'], y=df[TARGET_COLUMN])
        plt.title("CHAS vs Price")
        plt.xlabel("CHAS (Charles River dummy variable)")
        plt.ylabel("Price (in $1000's)")
        plt.tight_layout()
        plt.savefig('eda/chas_vs_price.png')
        plt.close()

    logging.info("Exploratory data analysis completed. Plots saved in 'eda/' directory.")
