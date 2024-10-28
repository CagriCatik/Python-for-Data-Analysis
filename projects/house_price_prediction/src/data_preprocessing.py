# src/data_preprocessing.py

import pandas as pd
import logging
from typing import Tuple
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

from src.data_loading import TARGET_COLUMN

def preprocess_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series, ColumnTransformer]:
    """
    Preprocess the dataset:
    - Handle missing values
    - Encode categorical variables
    - Feature scaling

    Parameters:
    - df: DataFrame to preprocess.

    Returns:
    - X: Features.
    - y: Target variable.
    - preprocessor: Preprocessing pipeline.
    """
    X = df.drop(TARGET_COLUMN, axis=1)
    y = df[TARGET_COLUMN]

    # Convert 'chas' to categorical if it's not already
    if 'chas' in X.columns:
        X['chas'] = X['chas'].astype('category')

    # Identify numerical and categorical columns
    numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()

    logging.info(f"Numerical columns: {numerical_cols}")
    logging.info(f"Categorical columns: {categorical_cols}")

    # Define preprocessing steps
    numerical_transformer = Pipeline(steps=[
        ('imputer',  SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

    return X, y, preprocessor
