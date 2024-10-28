import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib  # Import joblib for model serialization
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import os

# Suppress SettingWithCopyWarning for cleaner output
pd.options.mode.chained_assignment = None

# Define the local path to the dataset
file_path = 'imports-85.data'  # Ensure this file is in the current working directory

# Define column names as per the dataset documentation
column_names = [
    'symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration',
    'num-of-doors', 'body-style', 'drive-wheels', 'engine-location',
    'wheel-base', 'length', 'width', 'height', 'curb-weight',
    'engine-type', 'num-of-cylinders', 'engine-size', 'fuel-system',
    'bore', 'stroke', 'compression-ratio', 'horsepower', 'peak-rpm',
    'city-mpg', 'highway-mpg', 'price'
]

# Read the dataset into a Pandas DataFrame
try:
    df = pd.read_csv(
        file_path,
        names=column_names,
        na_values='?',      # Interpret '?' as NaN
        sep=',',            # Comma as delimiter
        skipinitialspace=True
    )
    print("Dataset successfully loaded.")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please ensure the file exists in the specified path.")
    exit()
except Exception as e:
    print(f"An error occurred while loading the dataset: {e}")
    exit()

# Initial Data Inspection
print("\nInitial DataFrame Head:")
print(df.head())
print("\nDataFrame Info:")
print(df.info())

# Data Preprocessing

# Define numerical and categorical columns
numeric_columns = [
    'symboling', 'normalized-losses', 'wheel-base', 'length', 'width',
    'height', 'curb-weight', 'engine-size', 'bore', 'stroke',
    'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg',
    'highway-mpg', 'price'
]

categorical_columns = [
    'make', 'fuel-type', 'aspiration', 'num-of-doors', 'body-style',
    'drive-wheels', 'engine-location', 'engine-type',
    'num-of-cylinders', 'fuel-system'
]

# Convert numeric columns to appropriate data types
for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors='coerce')

# Convert categorical columns to 'category' dtype
for column in categorical_columns:
    df[column] = df[column].astype('category')

# Display data types after conversion
print("\nData Types After Conversion:")
print(df.dtypes)

# Handling Missing Values

# Identify missing values
missing_data = df.isnull().sum()
print("\nMissing Values per Column:")
print(missing_data)

# Impute missing values for numerical columns with mean
for column in numeric_columns:
    if df[column].isnull().sum() > 0:
        mean_value = df[column].mean()
        df[column] = df[column].fillna(mean_value)  # Explicit assignment
        print(f"Imputed missing values in '{column}' with mean value {mean_value:.2f}")

# Impute missing values for categorical columns with mode
for column in categorical_columns:
    if df[column].isnull().sum() > 0:
        mode_value = df[column].mode()[0]
        df[column] = df[column].fillna(mode_value)  # Explicit assignment
        print(f"Imputed missing values in '{column}' with mode value '{mode_value}'")

# Drop rows where 'price' is missing
initial_row_count = df.shape[0]
df = df.dropna(subset=['price'])  # Explicit assignment
final_row_count = df.shape[0]
dropped_rows = initial_row_count - final_row_count
print(f"Dropped {dropped_rows} rows due to missing 'price' values.")

# Verify that there are no remaining missing values
print("\nMissing Values After Handling:")
print(df.isnull().sum())

# View the first five records after preprocessing
print("\nFirst Five Records After Preprocessing:")
print(df.head())

# Summary statistics for numerical columns
print("\nSummary Statistics for Numerical Columns:")
print(df[numeric_columns].describe())

# DataFrame information
print("\nDataFrame Information:")
print(df.info())

# Check for duplicate rows
duplicate_count = df.duplicated().sum()
print(f"\nNumber of Duplicate Rows: {duplicate_count}")

# Remove duplicate rows if any
if duplicate_count > 0:
    df = df.drop_duplicates()  # Explicit assignment
    print(f"Duplicate Rows After Removal: {df.duplicated().sum()}")
else:
    print("No duplicate rows found.")

# Encoding Categorical Variables

# Initialize separate LabelEncoders for each binary categorical variable
label_encoders = {}
binary_columns = ['fuel-type', 'aspiration', 'engine-location', 'num-of-doors']

for col in binary_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le
    print(f"Encoded binary column '{col}' with LabelEncoder.")

# Save each LabelEncoder separately
model_dir = 'models'
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

for col, le in label_encoders.items():
    encoder_path = os.path.join(model_dir, f'label_encoder_{col}.joblib')
    joblib.dump(le, encoder_path)
    print(f"LabelEncoder for '{col}' saved at '{encoder_path}'.")

# One-Hot Encoding for Multi-Class Categorical Variables
df = pd.get_dummies(
    df,
    columns=['make', 'body-style', 'drive-wheels', 
             'engine-type', 'num-of-cylinders', 'fuel-system'],
    drop_first=True
)
print("Applied One-Hot Encoding to multi-class categorical variables.")

# Feature Selection
features = df.drop(['price'], axis=1)
target = df['price']

# Exploratory Data Analysis

# Correlation Matrix
plt.figure(figsize=(20, 20))
sns.heatmap(features.corr(), annot=False, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Distribution of Price
sns.histplot(target, kde=True, bins=30)
plt.title('Distribution of Vehicle Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Top Correlated Features with Price
correlation = df.corr()
top_features = correlation['price'].abs().sort_values(ascending=False).head(10)
print("\nTop Correlated Features with Price:")
print(top_features)

# Model Development

# Data Splitting
X_train, X_test, y_train, y_test = train_test_split(
    features, target, test_size=0.2, random_state=42
)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)
print("\nModel training completed.")

# Model Prediction
y_pred = model.predict(X_test)
print("Model prediction completed.")

# Model Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")

# Visualization of Actual vs Predicted Prices
plt.figure(figsize=(10,6))
plt.scatter(y_test, y_pred, color='blue', alpha=0.6, label='Predicted vs Actual')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linewidth=2, label='Perfect Prediction')
plt.title('Actual vs Predicted Vehicle Prices')
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.legend()
plt.show()

# Saving the Trained Model

# Save the trained Linear Regression model
model_path = os.path.join(model_dir, 'vehicle_price_model.joblib')
joblib.dump(model, model_path)
print(f"Trained model saved at '{model_path}'.")
