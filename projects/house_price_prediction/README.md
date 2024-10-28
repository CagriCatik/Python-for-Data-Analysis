# Boston House Price Prediction

## Overview

The **Boston House Price Prediction** project aims to predict the median value of owner-occupied homes (`medv`) in Boston using various features such as crime rate, average number of rooms, property tax rate, and more. Leveraging data analysis, preprocessing, machine learning model training, evaluation, and hyperparameter tuning, this project provides insights and a predictive framework for real estate valuations in Boston.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Project Components](#project-components)
- [Results](#results)
- [Logging](#logging)
- [Model Saving and Loading](#model-saving-and-loading)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)


### Create and Activate a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

- **On Windows:**

  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- **On Unix or MacOS:**

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### Install Dependencies

Ensure you have `pip` installed and run:

```bash
pip install -r requirements.txt
```

## Usage

Ensure that the `boston_housing.csv` dataset is placed inside the `data/` directory. To execute the project workflow:

```bash
python main.py
```

**Note:** Always run the script from the project root directory to ensure correct module imports.

## Project Components

### 1. Data Loading

- **Module:** `src/data_loading.py`
- **Function:** `load_data(filepath: str) -> pd.DataFrame`
- **Description:** Loads the Boston housing dataset from a CSV file and validates the presence of the target column (`medv`).

### 2. Data Preprocessing

- **Module:** `src/data_preprocessing.py`
- **Function:** `preprocess_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series, ColumnTransformer]`
- **Description:** Handles missing values, encodes categorical variables, and scales numerical features.

### 3. Exploratory Data Analysis (EDA)

- **Module:** `src/eda.py`
- **Function:** `explore_data(df: pd.DataFrame) -> None`
- **Description:** Generates and saves visualizations such as correlation matrices, distribution plots, scatter plots, and box plots.

### 4. Model Training

- **Module:** `src/model_training.py`
- **Function:** `train_models(X_train, y_train, preprocessor) -> Dict[str, Pipeline]`
- **Description:** Trains different regression models (Linear Regression and Decision Tree) using preprocessing pipelines.

### 5. Model Evaluation

- **Module:** `src/model_evaluation.py`
- **Function:** `evaluate_model(model, X_test, y_test) -> Dict[str, float]`
- **Description:** Evaluates trained models using metrics like MAE, MSE, RMSE, and R² Score.

### 6. Hyperparameter Tuning

- **Module:** `src/hyperparameter_tuning.py`
- **Function:** `hyperparameter_tuning(model: Pipeline, X_train, y_train, param_grid: dict) -> Pipeline`
- **Description:** Optimizes model parameters using GridSearchCV to enhance performance.

### 7. Utilities

- **Module:** `src/utils.py`
- **Functions:**
  - `save_model(model, filename: str) -> None`: Saves the trained model to a file.
  - `load_model(filename: str)`: Loads a trained model from a file.
- **Description:** Provides utility functions for model persistence.

### 8. Main Script

- **Script:** `scripts/main.py`
- **Description:** Orchestrates the entire workflow by calling functions from various modules in sequence—loading data, performing EDA, preprocessing, training models, evaluating, tuning, and saving the best model.

## Results

Upon successful execution, the following outcomes are expected:

- **EDA Plots:** Saved in the `eda/` directory as PNG images (e.g., `correlation_matrix.png`, `price_distribution.png`, etc.).
- **Model Logs:** Detailed logs recorded in `logs/project.log`.
- **Trained Models:** The best Decision Tree model saved in `models/best_decision_tree_model.joblib`.

## Logging

The project utilizes Python's `logging` module to capture detailed execution logs.

- **Log File:** `logs/project.log`
- **Log Levels:** INFO and ERROR messages are recorded to help trace the workflow and diagnose issues.

**Example Log Entries:**

```
INFO:Data loaded successfully with shape (506, 14)
INFO:Numerical columns: ['crim', 'zn', 'indus', 'nox', 'rm', 'age', 'dis', 'rad', 'tax', 'ptratio', 'b', 'lstat']
INFO:Categorical columns: ['chas']
INFO:Training Linear Regression...
INFO:Linear Regression trained successfully.
...
INFO:Best parameters: {'regressor__max_depth': 10, 'regressor__min_samples_split': 2, 'regressor__min_samples_leaf': 1}
INFO:Best R2 Score: 0.85
...
INFO:Model saved to models/best_decision_tree_model.joblib
INFO:Project execution completed successfully.
```

## Model Saving and Loading

The best-performing model is saved using `joblib` for future use.

- **Saving the Model:**

  ```python
  from src.utils import save_model

  save_model(best_model, 'models/best_decision_tree_model.joblib')
  ```

- **Loading the Model:**

  ```python
  from src.utils import load_model

  model = load_model('models/best_decision_tree_model.joblib')
  ```

**Example Prediction:**

```python
import pandas as pd
from src.utils import load_model

# Load the saved model
model = load_model('models/best_decision_tree_model.joblib')

# Example input data
input_data = {
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

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# Make prediction
predicted_price = model.predict(input_df)[0]
print(f"Predicted Price: {predicted_price:.2f} (in $1000's)")
```

**Output:**

```
Predicted Price: 24.00 (in $1000's)
```

## Troubleshooting

### 1. `ModuleNotFoundError: No module named 'src'`

**Cause:** Python cannot locate the `src` package when running the script.

**Solution:**

- Ensure that the `__init__.py` file exists in the `src/` directory.
- Run the script from the project root directory.
- Modify `sys.path` within `scripts/main.py` to include the project root.

**Example Modification in `scripts/main.py`:**

```python
import sys
import os

# Add project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)
```

### 2. `ImportError: cannot import name 'Pipeline' from 'typing'`

**Cause:** Incorrect import statement; `Pipeline` should be imported from `sklearn.pipeline`, not from `typing`.

**Solution:**

- **Incorrect Import:**

  ```python
  from typing import Pipeline
  ```

- **Correct Import:**

  ```python
  from sklearn.pipeline import Pipeline
  ```

**Action Steps:**

1. Open `src/hyperparameter_tuning.py`.
2. Locate and correct the import statement.

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**
2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add Your Feature"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

## License

This project is licensed under the [MIT License](LICENSE).

---

*Feel free to reach out if you encounter any issues or have suggestions for improvements. Happy coding!*
```