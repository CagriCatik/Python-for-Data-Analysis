# src/model_training.py

import logging
from typing import Dict
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

def train_models(X_train, y_train, preprocessor) -> Dict[str, Pipeline]:
    """
    Train different regression models using pipelines.

    Parameters:
    - X_train: Training features.
    - y_train: Training target.
    - preprocessor: Preprocessing pipeline.

    Returns:
    - Dictionary of trained models.
    """
    models = {
        'Linear Regression': Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('regressor', LinearRegression())
        ]),
        'Decision Tree': Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('regressor', DecisionTreeRegressor(random_state=42))
        ])
    }

    for name, pipeline in models.items():
        logging.info(f"Training {name}...")
        pipeline.fit(X_train, y_train)
        logging.info(f"{name} trained successfully.")

    return models
