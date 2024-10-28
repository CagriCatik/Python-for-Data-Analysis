import pandas as pd
import numpy as np
import joblib
import os

# Define the directory where models and encoders are saved
model_dir = 'models'

# Paths to the saved model and encoders
model_path = os.path.join(model_dir, 'vehicle_price_model.joblib')
encoder_fuel_type_path = os.path.join(model_dir, 'label_encoder_fuel-type.joblib')
encoder_aspiration_path = os.path.join(model_dir, 'label_encoder_aspiration.joblib')
encoder_engine_location_path = os.path.join(model_dir, 'label_encoder_engine-location.joblib')
encoder_num_of_doors_path = os.path.join(model_dir, 'label_encoder_num-of-doors.joblib')

# Load the trained model
try:
    model = joblib.load(model_path)
    print(f"Loaded model from '{model_path}'.")
except FileNotFoundError:
    print(f"Error: The model file '{model_path}' was not found.")
    exit()

# Load the LabelEncoders
try:
    encoder_fuel_type = joblib.load(encoder_fuel_type_path)
    encoder_aspiration = joblib.load(encoder_aspiration_path)
    encoder_engine_location = joblib.load(encoder_engine_location_path)
    encoder_num_of_doors = joblib.load(encoder_num_of_doors_path)
    print("Loaded all LabelEncoders.")
except FileNotFoundError as e:
    print(f"Error: {e}")
    exit()

# Function to preprocess new data
def preprocess_new_data(input_data):
    """
    Preprocesses the input data to match the training data's format.
    
    Parameters:
    - input_data (dict): A dictionary containing feature names and their corresponding values.
    
    Returns:
    - pd.DataFrame: A preprocessed DataFrame ready for prediction.
    """
    # Convert input data to DataFrame
    df_new = pd.DataFrame([input_data])
    
    # Define numerical and categorical columns as per training
    numeric_columns = [
        'symboling', 'normalized-losses', 'wheel-base', 'length', 'width',
        'height', 'curb-weight', 'engine-size', 'bore', 'stroke',
        'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg',
        'highway-mpg'
    ]
    
    categorical_columns = [
        'make', 'fuel-type', 'aspiration', 'body-style',
        'drive-wheels', 'engine-type',
        'num-of-cylinders', 'fuel-system'
    ]
    
    # Handle missing values if any (you can define specific strategies)
    # For simplicity, we'll fill numerical NaNs with mean and categorical NaNs with mode
    for column in numeric_columns:
        if column in df_new.columns:
            df_new[column] = pd.to_numeric(df_new[column], errors='coerce')
            if df_new[column].isnull().sum() > 0:
                # Set to mean value used during training
                if column == 'normalized-losses':
                    df_new[column].fillna(122.00, inplace=True)
                elif column == 'bore':
                    df_new[column].fillna(3.33, inplace=True)
                elif column == 'stroke':
                    df_new[column].fillna(3.26, inplace=True)
                elif column == 'horsepower':
                    df_new[column].fillna(104.26, inplace=True)
                elif column == 'peak-rpm':
                    df_new[column].fillna(5125.37, inplace=True)
                else:
                    # For other numerical columns, set to mean or a default value
                    df_new[column].fillna(df_new[column].mean(), inplace=True)
    
    for column in categorical_columns:
        if column in df_new.columns:
            df_new[column] = df_new[column].astype('category')
            if df_new[column].isnull().sum() > 0:
                # Set to mode or a default category
                if column == 'num-of-doors':
                    df_new[column].fillna('four', inplace=True)
                else:
                    df_new[column].fillna(df_new[column].mode()[0], inplace=True)
    
    # Encode binary categorical variables using the loaded LabelEncoders
    try:
        df_new['fuel-type'] = encoder_fuel_type.transform(df_new['fuel-type'])
        df_new['aspiration'] = encoder_aspiration.transform(df_new['aspiration'])
        df_new['engine-location'] = encoder_engine_location.transform(df_new['engine-location'])
        df_new['num-of-doors'] = encoder_num_of_doors.transform(df_new['num-of-doors'])
        print("Encoded binary categorical variables.")
    except ValueError as ve:
        print(f"Encoding error: {ve}")
        exit()
    
    # One-Hot Encoding for multi-class categorical variables
    df_new = pd.get_dummies(
        df_new,
        columns=['make', 'body-style', 'drive-wheels', 
                 'engine-type', 'num-of-cylinders', 'fuel-system'],
        drop_first=True
    )
    print("Applied One-Hot Encoding to multi-class categorical variables.")
    
    # Ensure that the new data has the same dummy variables as the training data
    # Load training feature columns from the model
    training_features = model.feature_names_in_
    
    # Add missing columns with zeros
    for col in training_features:
        if col not in df_new.columns:
            df_new[col] = 0
    
    # Ensure the order of columns matches the training data
    df_new = df_new[training_features]
    
    return df_new

# Example: Define new input data
new_vehicle = {
    'symboling': 3,
    'normalized-losses': 100,
    'make': 'toyota',
    'fuel-type': 'gas',
    'aspiration': 'std',
    'body-style': 'sedan',
    'drive-wheels': 'fwd',
    'engine-location': 'front',  # Added 'engine-location'
    'engine-type': 'ohc',
    'num-of-cylinders': 'four',
    'fuel-system': 'mpfi',
    'wheel-base': 97.5,
    'length': 176.6,
    'width': 64.1,
    'height': 54.3,
    'curb-weight': 2823,
    'engine-size': 136,
    'bore': 3.19,
    'stroke': 3.40,
    'compression-ratio': 9.0,
    'horsepower': 111.0,
    'peak-rpm': 5000.0,
    'city-mpg': 21,
    'highway-mpg': 27
}


# Preprocess the new data
preprocessed_data = preprocess_new_data(new_vehicle)
print("\nPreprocessed New Data:")
print(preprocessed_data)

# Make prediction
predicted_price = model.predict(preprocessed_data)
print(f"\nPredicted Vehicle Price: ${predicted_price[0]:.2f}")
