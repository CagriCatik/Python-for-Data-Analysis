# src/hyperparameter_tuning.py

import logging
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

def hyperparameter_tuning(model: Pipeline, X_train, y_train, param_grid: dict) -> Pipeline:
    """
    Perform hyperparameter tuning using GridSearchCV.

    Parameters:
    - model: Pipeline with a regressor.
    - X_train: Training features.
    - y_train: Training target.
    - param_grid: Dictionary with parameters names as keys and lists of parameter settings to try as values.

    Returns:
    - Best estimator after GridSearchCV.
    """
    logging.info("Starting hyperparameter tuning...")

    grid_search = GridSearchCV(
        model, param_grid, cv=5, scoring='r2', n_jobs=-1, verbose=1
    )
    grid_search.fit(X_train, y_train)

    logging.info(f"Best parameters: {grid_search.best_params_}")
    logging.info(f"Best R2 Score: {grid_search.best_score_:.4f}")

    best_model = grid_search.best_estimator_
    return best_model
