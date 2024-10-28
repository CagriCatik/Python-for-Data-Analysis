# src/data_loading.py

import pandas as pd
import logging
import sys

TARGET_COLUMN = 'medv'  # Define the target column

def load_data(filepath: str) -> pd.DataFrame:
    """
    Load the Boston housing dataset from a CSV file.

    Parameters:
    - filepath: Path to the CSV file.

    Returns:
    - DataFrame containing the dataset.
    """
    try:
        data = pd.read_csv(filepath)
        logging.info(f"Data loaded successfully with shape {data.shape}")
        logging.debug(f"Column Names: {data.columns.tolist()}")

        # Validate target column presence
        if TARGET_COLUMN not in data.columns:
            logging.error(f"Target column '{TARGET_COLUMN}' not found in the dataset.")
            print(f"Available columns: {data.columns.tolist()}")
            sys.exit(1)
        
        return data
    except FileNotFoundError as e:
        logging.error(f"File not found: {filepath}")
        raise e
    except Exception as e:
        logging.error(f"An error occurred while loading data: {e}")
        raise e
