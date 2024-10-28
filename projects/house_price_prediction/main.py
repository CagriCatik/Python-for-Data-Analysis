# scripts/main.py

import logging
import os
from src.data_loading import load_data
from src.data_preprocessing import preprocess_data
from src.eda import explore_data
from src.model_training import train_models
from src.model_evaluation import evaluate_model
from src.hyperparameter_tuning import hyperparameter_tuning
from src.utils import save_model

def setup_logging():
    """
    Set up logging configuration.
    """
    os.makedirs('logs', exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s:%(message)s',
        handlers=[
            logging.FileHandler("logs/project.log"),
            logging.StreamHandler()
        ]
    )

def main():
    """
    Main function to orchestrate the workflow.
    """
    setup_logging()

    # Define file paths
    data_filepath = os.path.join('data', 'boston_housing.csv')
    model_save_path = os.path.join('models', 'best_decision_tree_model.joblib')

    # Create necessary directories if they don't exist
    os.makedirs('eda', exist_ok=True)
    os.makedirs('models', exist_ok=True)

    # Load data
    df = load_data(data_filepath)

    # EDA
    explore_data(df)

    # Preprocess data
    X, y, preprocessor = preprocess_data(df)

    # Split data
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    logging.info(f"Data split into train and test sets with sizes {X_train.shape} and {X_test.shape}")

    # Train models
    models = train_models(X_train, y_train, preprocessor)

    # Evaluate models
    for name, model in models.items():
        logging.info(f"Evaluating {name}...")
        metrics = evaluate_model(model, X_test, y_test)
        logging.info(f"{name} Evaluation Metrics:")
        for metric, value in metrics.items():
            logging.info(f"{metric}: {value:.4f}")

    # Hyperparameter tuning for Decision Tree
    dt_pipeline = models['Decision Tree']
    param_grid = {
        'regressor__max_depth': [None, 5, 10, 20, 30],
        'regressor__min_samples_split': [2, 5, 10],
        'regressor__min_samples_leaf': [1, 2, 4]
    }

    best_dt = hyperparameter_tuning(dt_pipeline, X_train, y_train, param_grid)

    # Evaluate the best Decision Tree
    logging.info("Evaluating the best Decision Tree after hyperparameter tuning...")
    best_dt_metrics = evaluate_model(best_dt, X_test, y_test)
    logging.info("Best Decision Tree Evaluation Metrics:")
    for metric, value in best_dt_metrics.items():
        logging.info(f"{metric}: {value:.4f}")

    # Save the best model
    save_model(best_dt, model_save_path)

    logging.info("Project execution completed successfully.")

if __name__ == "__main__":
    main()
