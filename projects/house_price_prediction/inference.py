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