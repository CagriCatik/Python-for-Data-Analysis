import pandas as pd

# Sample vehicle speed data in km/h recorded every minute over 5 minutes
speeds = [65, 70, 68, None, 72]  # A `None` value represents a data gap or sensor fault.
speed_series = pd.Series(speeds, name="Speed (km/h)")

# Display the created Series
print("Speed Series Data:\n", speed_series, "\n")

# 1. Checking the data type of the Series
speed_dtype = speed_series.dtype
print("Data Type of Speed Series:", speed_dtype)

# 2. Retrieving the values as a NumPy array
speed_values = speed_series.values
print("Speed Values as Array:", speed_values)

# 3. Checking the index of the Series
speed_index = speed_series.index
print("Index Information:", speed_index)

# 4. Checking for any missing (NaN) values
has_missing_values = speed_series.hasnans
print("Presence of NaNs:", has_missing_values)

# 5. Getting the shape of the Series
speed_shape = speed_series.shape
print("Shape of Speed Series:", speed_shape)

# 6. Getting the size (total number of elements) of the Series
speed_size = speed_series.size
print("Number of Data Points:", speed_size)

# Handling NaN values

# 1. Identifying NaNs
nan_check = speed_series.isna()
print("NaN Check:\n", nan_check)
contains_nan = speed_series.hasnans
print("Contains NaN:", contains_nan)

# 2. Removing NaNs
cleaned_speed_series = speed_series.dropna()
print("Series with NaNs Removed:\n", cleaned_speed_series)

# 3. Filling NaNs with Zero
filled_with_zero = speed_series.fillna(0)
print("Series with NaNs Filled (0):\n", filled_with_zero)

# 4. Filling NaNs with Mean
mean_value = speed_series.mean()
filled_with_mean = speed_series.fillna(mean_value)
print("Series with NaNs Filled (Mean):\n", filled_with_mean)

# 5. Forward and Backward Filling
ffilled_speed_series = speed_series.ffill()
bfilled_speed_series = speed_series.bfill()
print("Series with Forward Fill:\n", ffilled_speed_series)
print("Series with Backward Fill:\n", bfilled_speed_series)
