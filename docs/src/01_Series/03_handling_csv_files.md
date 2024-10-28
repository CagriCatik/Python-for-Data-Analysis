# Handling csv files

Managing CSV (Comma-Separated Values) files is a fundamental aspect of data manipulation and analysis in Python. This tutorial provides an in-depth exploration of reading from and writing to CSV files using the Pandas library, a powerful tool for data analysis. The tutorial emphasizes precision and rigor, ensuring that each concept is thoroughly understood and correctly applied.

## External Datasets

Creating custom datasets can be beneficial for learning; however, for practical applications, leveraging external datasets is more efficient and realistic. One prominent source for a wide array of datasets is [Kaggle](https://www.kaggle.com/), a platform that hosts datasets contributed by the community, ranging from beginner to advanced levels.

### Accessing Kaggle Datasets

To utilize datasets from Kaggle:

1. **Sign Up**: Create a free account on [Kaggle.com](https://www.kaggle.com/).
2. **Dataset Exploration**: Navigate to the "Datasets" section to browse available datasets.
3. **Download**: Select and download the desired dataset, typically available in CSV format.

For this tutorial, the dataset under consideration contains information about the top 100 richest individuals globally. This dataset can be downloaded directly from the resources section provided or accessed via Kaggle.

## Reading CSV Files with Pandas

Pandas offers robust functionality for reading CSV files through the `read_csv` function. The following steps illustrate how to import and inspect a CSV file.

### Step 1: Importing Pandas

Begin by importing the Pandas library, conventionally aliased as `pd` to streamline subsequent code.

```python
import pandas as pd
```

### Step 2: Loading the CSV File

Assuming the CSV file (`richest.csv`) is located in the same directory as the Jupyter Notebook or Python script, it can be loaded as follows:

```python
richest = pd.read_csv('richest.csv')
```

Here, `richest` is a Pandas DataFrame containing the dataset's contents.

### Understanding Data Types

To confirm the type of the loaded data structure:

```python
type(richest)
```

This should output:

```
pandas.core.frame.DataFrame
```

This confirms that `richest` is a DataFrame, a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes.

## Selecting Specific Columns

Often, analysis requires focusing on specific columns within a dataset. Pandas facilitates column selection, enabling targeted data manipulation.

### Extracting a Single Column

To extract a single column, such as the names of the individuals, the `usecols` parameter can be utilized during the CSV reading process:

```python
richest_names = pd.read_csv('richest.csv', usecols=['Name'])
```

This operation results in a DataFrame containing only the 'Name' column.

### Converting to a Series

A Series is a one-dimensional labeled array capable of holding any data type. If the goal is to work with a Series rather than a DataFrame, the `squeeze` method can be applied:

```python
richest_series = richest_names.squeeze()
```

This converts the DataFrame with a single column into a Series. Verifying the type confirms the conversion:

```python
type(richest_series)
```

Output:

```
pandas.core.series.Series
```

## Exporting Data to CSV Files

Exporting data after manipulation is equally important. Pandas provides the `to_csv` method for this purpose, allowing data to be saved with various parameters to control the output format.

### Basic Export

To export the `richest_series` to a new CSV file:

```python
richest_series.to_csv('test.csv')
```

By default, this includes the DataFrame's index in the CSV file, resulting in an additional column representing the index.

### Controlling Index Inclusion

In scenarios where the index is not required or already present in the data, the `index` parameter can be set to `False` to exclude it:

```python
richest_series.to_csv('test.csv', index=False)
```

This ensures that only the data is written to the CSV without the index, maintaining the original structure.

### Reading the Exported CSV

To verify the export, the newly created `test.csv` can be read back into a DataFrame:

```python
people = pd.read_csv('test.csv')
```

Inspecting the type:

```python
type(people)
```

Output:

```
pandas.core.frame.DataFrame
```

Despite exporting a Series, reading the CSV without the index results in a DataFrame. To maintain consistency and retrieve a Series, the `squeeze` method can be applied:

```python
people_series = people.squeeze()
```

Confirming the type:

```python
type(people_series)
```

Output:

```
pandas.core.series.Series
```

## Practical Considerations

### File Paths

While the examples assume that CSV files reside in the same directory as the script or notebook, specifying absolute or relative paths is essential when files are located elsewhere. For example:

```python
richest = pd.read_csv('/path/to/directory/richest.csv')
```

Properly managing file paths ensures that scripts are portable and can locate necessary resources regardless of the execution environment.

### Error Handling

When dealing with file operations, it is prudent to implement error handling to manage scenarios such as missing files or incorrect file formats. Using try-except blocks can capture and handle exceptions gracefully.

```python
try:
    richest = pd.read_csv('richest.csv')
except FileNotFoundError:
    print("The specified file was not found.")
except pd.errors.EmptyDataError:
    print("No data found in the file.")
except pd.errors.ParserError:
    print("Error parsing the file.")
```

### Data Integrity

Ensuring the integrity of data during import and export processes is crucial. Verifying that the number of rows and columns remains consistent before and after operations helps maintain data consistency.

```python
# Original DataFrame shape
original_shape = richest.shape

# After export and import
people = pd.read_csv('test.csv')
new_shape = people.shape

assert original_shape[0] == new_shape[0], "Row count mismatch."
assert original_shape[1] == new_shape[1], "Column count mismatch."
```

## Advanced Parameters in `read_csv` and `to_csv`

Pandas’ `read_csv` and `to_csv` functions offer a multitude of parameters to handle various data formats and requirements.

### `read_csv` Parameters

- **`sep`**: Delimiter to use; default is comma.
- **`header`**: Row number to use as the column names.
- **`names`**: List of column names to use.
- **`dtype`**: Data type for data or columns.
- **`parse_dates`**: Boolean or list of columns to parse as dates.
- **`na_values`**: Additional strings to recognize as NA/NaN.
- **`usecols`**: Return a subset of the columns.

### `to_csv` Parameters

- **`path_or_buf`**: File path or object to write to.
- **`sep`**: String of length 1. Field delimiter.
- **`na_rep`**: String representation of NaN.
- **`columns`**: Columns to write.
- **`header`**: Write out column names.
- **`index_label`**: Column label for index column.
- **`mode`**: Python write mode.

Understanding and utilizing these parameters allows for greater control over data import and export processes, facilitating the handling of complex datasets.
