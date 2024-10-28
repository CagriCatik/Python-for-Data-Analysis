# src/model_evaluation.py

import numpy as np
import logging
from typing import Dict
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def evaluate_model(model, X_test, y_test) -> Dict[str, float]:
    """
    Evaluate the model using various regression metrics.

    Parameters:
    - model: Trained model.
    - X_test: Testing features.
    - y_test: Testing target.

    Returns:
    - Dictionary of evaluation metrics.
    """
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, predictions)

    metrics = {
        'MAE': mae,
        'MSE': mse,
        'RMSE': rmse,
        'R2_Score': r2
    }

    return metrics
