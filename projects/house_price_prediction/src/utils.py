# src/utils.py

import joblib
import logging

def save_model(model, filename: str) -> None:
    """
    Save the trained model to a file.

    Parameters:
    - model: Trained model.
    - filename: Name of the file to save the model.
    """
    joblib.dump(model, filename)
    logging.info(f"Model saved to {filename}")

def load_model(filename: str):
    """
    Load a trained model from a file.

    Parameters:
    - filename: Name of the file from which to load the model.

    Returns:
    - Loaded model.
    """
    model = joblib.load(filename)
    logging.info(f"Model loaded from {filename}")
    return model
