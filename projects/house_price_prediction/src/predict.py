# src/predict.py

import sys
import logging
from src.utils import load_model
import pandas as pd

def make_prediction(model_path: str, input_data: dict) -> float:
    """
    Make a prediction using the saved model.

    Parameters:
    - model_path: Path to the saved model file.
    - input_data: Dictionary containing input features.

    Returns:
    - Predicted price.
    """
    try:
        model = load_model(model_path)
        input_df = pd.DataFrame([input_data])
        predicted_price = model.predict(input_df)[0]
        logging.info(f"Predicted Price: {predicted_price:.2f} (in $1000's)")
        return predicted_price
    except Exception as e:
        logging.error(f"An error occurred during prediction: {e}")
        raise e

if __name__ == "__main__":
    # Example usage:
    # python src/predict.py
    # You can modify this section to accept command-line arguments or integrate with other systems.
    example_input = {
        'crim': 0.1,
        'zn': 12.5,
        'indus': 7.87,
        'chas': 0,
        'nox': 0.524,
        'rm': 6.5,
        'age': 65.2,
        'dis': 4.09,
        'rad': 1,
        'tax': 296,
        'ptratio': 15.3,
        'b': 396.9,
        'lstat': 4.98
    }
    model_path = 'models/best_decision_tree_model.joblib'
    make_prediction(model_path, example_input)
