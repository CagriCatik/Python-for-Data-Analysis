# Feature Descriptions

```python
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
```

1. **`crim`**: **Per Capita Crime Rate**
   - **Description**: Measures the amount of crime per capita by town.
   - **Unit**: Crimes per capita.

2. **`zn`**: **Proportion of Residential Land Zoned for Lots Over 25,000 sq.ft.**
   - **Description**: Indicates the proportion of residential land zoned for large lots.
   - **Unit**: Percentage (%) of the town.

3. **`indus`**: **Proportion of Non-Retail Business Acres per Town**
   - **Description**: Represents the proportion of the town's land dedicated to non-retail businesses.
   - **Unit**: Percentage (%) of the town.

4. **`chas`**: **Charles River Dummy Variable**
   - **Description**: A binary variable indicating whether the tract bounds the Charles River.
     - **1**: Bounds the river.
     - **0**: Does not bound the river.
   - **Unit**: Binary (0 or 1).

5. **`nox`**: **Nitric Oxides Concentration**
   - **Description**: Measures the concentration of nitric oxides (particulate matter) in the air.
   - **Unit**: Parts per 10 million (ppm).

6. **`rm`**: **Average Number of Rooms per Dwelling**
   - **Description**: Indicates the average number of rooms per dwelling.
   - **Unit**: Number of rooms.

7. **`age`**: **Proportion of Owner-Occupied Units Built Prior to 1940**
   - **Description**: Represents the proportion of owner-occupied units built before 1940.
   - **Unit**: Percentage (%) of the town.

8. **`dis`**: **Weighted Distances to Five Boston Employment Centers**
   - **Description**: Calculates the weighted distances to five major employment centers in Boston.
   - **Unit**: Miles.

9. **`rad`**: **Index of Accessibility to Radial Highways**
   - **Description**: Measures the accessibility to radial highways.
   - **Unit**: Integer index (e.g., 1 to 24).

10. **`tax`**: **Full-Value Property Tax Rate per $10,000**
    - **Description**: Indicates the full-value property tax rate per $10,000.
    - **Unit**: Dollars per $10,000.

11. **`ptratio`**: **Pupil-Teacher Ratio by Town**
    - **Description**: Represents the pupil-teacher ratio in the town.
    - **Unit**: Ratio (e.g., 15.3 means 15.3 students per teacher).

12. **`b`**: **1000(Bk - 0.63)^2 Where Bk is the Proportion of Blacks by Town**
    - **Description**: A measure calculated as `1000*(Bk - 0.63)^2`, where `Bk` is the proportion of blacks by town.
    - **Unit**: Derived value (unitless).

13. **`lstat`**: **Percentage of Lower Status of the Population**
    - **Description**: Indicates the percentage of the population considered to be of lower socio-economic status.
    - **Unit**: Percentage (%).

## **Purpose of `input_data`**

The `input_data` dictionary serves as an **example** to demonstrate how to structure input features when making a prediction using the trained model. Here's how it fits into the prediction workflow:

1. **Model Training**: During the training phase, the model learns the relationship between these features and the target variable (`medv`), which represents the **Median Value of Owner-Occupied Homes** in $1000's.

2. **Making Predictions**:
   - **Prepare Input**: You provide a new data point with values for each of these features.
   - **Data Preprocessing**: The input data undergoes the same preprocessing steps as the training data (e.g., scaling, encoding).
   - **Prediction**: The preprocessed input is fed into the model to generate a predicted `medv` value.

## **Example Prediction Workflow**

Here's how you can use the `input_data` to make a prediction:

1. **Load the Saved Model**:

   ```python
   from src.utils import load_model
   import pandas as pd

   # Load the trained model
   model = load_model('models/best_decision_tree_model.joblib')
   ```

2. **Prepare the Input Data**:

   ```python
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
   ```

3. **Make the Prediction**:

   ```python
   # Make prediction
   predicted_price = model.predict(input_df)[0]
   print(f"Predicted Price: {predicted_price:.2f} (in $1000's)")
   ```

   **Output Example**:
   ```
   Predicted Price: 24.00 (in $1000's)
   ```

## **Customizing Input Data**

You can modify the `input_data` dictionary with **actual values** relevant to the property you want to evaluate. Here's how:

1. **Gather Real-World Data**: Collect the necessary feature values for the property in question.
2. **Update the Dictionary**: Replace the example values with real values.

   ```python
   input_data = {
       'crim': 0.5,         # Example: 0.5 crimes per capita
       'zn': 25.0,          # Example: 25% of land zoned for large lots
       'indus': 10.0,       # Example: 10% non-retail business acres
       'chas': 1,           # Example: Bounds the Charles River
       'nox': 0.6,          # Example: 0.6 ppm of nitric oxides
       'rm': 7.0,           # Example: 7 rooms per dwelling
       'age': 30.0,         # Example: 30% built prior to 1940
       'dis': 3.5,          # Example: 3.5 miles to employment centers
       'rad': 5,            # Example: Accessibility index of 5
       'tax': 300,          # Example: $300 per $10,000 property tax
       'ptratio': 16.0,     # Example: 16 students per teacher
       'b': 380.0,          # Example: 380 (derived from population)
       'lstat': 5.0         # Example: 5% lower status population
   }
   ```

3. **Proceed with Prediction**: Use the updated `input_data` to make a new prediction.

## **Automating Predictions**

For practical applications, consider creating a **user interface** or **API** that collects input data, processes it, and returns predictions. Here's a simple example using a Python function:

```python
def predict_house_price(input_data: dict, model_path: str = 'models/best_decision_tree_model.joblib') -> float:
    """
    Predict the median value of a house based on input features.
    
    Parameters:
    - input_data: Dictionary containing feature values.
    - model_path: Path to the saved model file.
    
    Returns:
    - Predicted median house value in $1000's.
    """
    from src.utils import load_model
    import pandas as pd

    # Load the model
    model = load_model(model_path)
    
    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Make prediction
    predicted_price = model.predict(input_df)[0]
    
    return predicted_price

# Example usage
input_data = {
    'crim': 0.5,
    'zn': 25.0,
    'indus': 10.0,
    'chas': 1,
    'nox': 0.6,
    'rm': 7.0,
    'age': 30.0,
    'dis': 3.5,
    'rad': 5,
    'tax': 300,
    'ptratio': 16.0,
    'b': 380.0,
    'lstat': 5.0
}

predicted_price = predict_house_price(input_data)
print(f"Predicted Price: {predicted_price:.2f} (in $1000's)")
```

## **Understanding Each Feature's Impact**

Understanding how each feature affects the house price can provide valuable insights:

- **High `rm` (Average Rooms)**: Generally, more rooms lead to higher house prices.
- **High `lstat` (% Lower Status)**: Higher percentages typically correlate with lower house prices.
- **Low `ptratio` (Pupil-Teacher Ratio)**: Better educational environments (lower ratios) can increase house prices.
- **Proximity to Employment Centers (`dis`)**: Closer distances often result in higher prices due to convenience.
- **Accessibility (`rad`)**: Better access to highways can enhance property values.
- **Tax Rates (`tax`)**: Higher property taxes might negatively impact house prices.
- **Proximity to the Charles River (`chas`)**: Properties near the river often have premium values.
