# Series

## Introduction

A series is a one-dimensional labeled array that can hold any data type, such as integers, strings, floating-point numbers, or Python objects. The axis labels are collectively referred to as the index. You can create a series from a list or from a dictionary just by using the series class constructor. The index does not have to be an integer; it can be anything you want it to be, or at least anything that is supported by Python. You can hold shift plus tab while inside a constructor or any place that takes parameters to open up the documentation. If you hold shift plus tab again while you’re in there, it’s going to expand it so you can always read the documentation and find out what kind of parameters it takes.

## Attributes

Every time you create a Pandas object, you have the opportunity to use an attribute or method for that object. Attributes often provide information about the object, while methods actually perform actions on the object that can modify it.

First, let's look at some of the most common attributes you can use with Pandas objects. As always, we first import Pandas as PD. Then we create two variables: one with a list of numbers and one with a list of letters. Next, we create a Series for each of these variables.

For example, let's first create a numeric series, which is `pd.Series` of those numbers. This gives us a series of type Integer. We do the same with the letters, creating a series of letters, assigning it to a variable, and displaying it.

The first attribute we will cover is the dtype. When you enter num_series.dtype, you get information about the data type of that series. A shortcut in Jupyter Notebook is that when typing something like num and pressing the Tab key, you get auto-completion. Here you can insert a variable like num_series, then . and press Tab again to get all the methods and attributes of that object. For example, num_series.dtype will be shown as a valid attribute name. Clicking on it and pressing Shift + Enter will execute the code again.

If you use this attribute on a letter series containing strings, you will get a `dtype` of 'O', which stands for Object.

You can also retrieve the values from a series. If you append .values to our letter series, this time you get an array, not a series. So, we have an array of type Object containing these strings.

Similar to values, you can also get information about the index. When using num_series.index, it shows that this is a range index, as it starts from one number and ends at another. Essentially, it is a range from zero to five with a step size of one.

Sometimes, you will work with series that do not contain all information and have some NaNs (not a number). You can use the hasNans attribute to check if a series has missing values or NaNs. For example, I created an incomplete series here containing the data A, B, and None. None is considered a missing value, and the index will be one, two, three. Three will have a missing value. You can check this by applying hasNans to this incomplete series to see if it contains NaNs.

Furthermore, we have shape, which returns the shape of a series as a tuple. This may seem useless for series as each series only contains one column, always being a one-dimensional array. However, if you want to use it with DataFrames, you can do so.

Finally, we have size, which returns the size of the series. Since it contains five elements, it will return five. If the number of elements changes, you can determine this with this attribute.

These were some of the most common attributes you can use with series. In the resources section, I have included the documentation so you can scroll through and see what else is available. This will definitely be a useful resource when working with Pandas, as there may be other attributes you will need at some point.

Now, let's implement Python examples for the content:

```py
import pandas as pd

# Creating a numeric series
num_list = [1, 2, 3, 4, 5]
num_series = pd.Series(num_list)

# Creating a letter series
letter_list = ['A', 'B', 'C', 'D', 'E']
letter_series = pd.Series(letter_list)

# Accessing dtype attribute
num_dtype = num_series.dtype
letter_dtype = letter_series.dtype

# Retrieving values from a series
num_values = num_series.values
letter_values = letter_series.values

# Accessing index information
num_index = num_series.index
letter_index = letter_series.index

# Checking for NaNs in a series
incomplete_series = pd.Series(['A', 'B', None])
has_nans = incomplete_series.hasnans

# Accessing shape and size attributes
num_shape = num_series.shape
num_size = num_series.size

# Displaying the results
print("Numeric Series:")
print("dtype:", num_dtype)
print("values:", num_values)
print("index:", num_index)
print("shape:", num_shape)
print("size:", num_size)

print("\nLetter Series:")
print("dtype:", letter_dtype)
print("values:", letter_values)
print("index:", letter_index)
print("has NaNs:", has_nans)
```

## Methods

In the previous part, the attributes that can be used with series, or at least the most common ones, were covered. Now, the same will be done with methods. As mentioned earlier, information about the object is provided by attributes, while actions are performed by methods, and the original object can even be changed. Let's jump right into it by importing Pandas as PD. Once that is done, a variable called values will be created, which will be a series of this data. Many floating-point numbers are present in it, and there's even one missing value, or as it is called in Python, None.

The first method that will be used is the max method, which returns the maximum value from this series. If that is run, there will be an error because the line of code that defines values was forgotten to be run. This issue was encountered because running cells in the correct order is crucial for things to work. values was never defined, so that will be run, and then values.max will be rerun. This time, the max value of four will be returned, as that is the maximum value in this array of data.

Similarly, min will be used to get the minimum value from this series, which will return 0.5 as the lowest value. None is not considered a number. If the sum of all values is desired, sum will be used. It adds all values together and returns the sum. The average of a series can also be obtained using mean, where the average of these values is 1.9.

The choice to get the index of the max and min value instead of their values can be made using idxmax and idxmin. For example, values.idxmax will return the index of the max value, which is four. Similarly, values.idxmin will return the index of the min value, which is two.

Another useful method is isnull, which returns a series checking whether each value is null or not. If values.isnull is run, it will return a series with False for the first three values and True for the fourth value, as it is a null value. The data type of this series is boolean.

If rounding off the decimals is desired, round can be used. The round method takes one argument, which is the number of decimal places to round to. For instance, values.round(2) will round to two decimal places.

Exploring the Pandas series documentation for more methods is highly encouraged. There are many methods available, and while the most important ones will be covered in this course, new ones may be discovered as more work is done with Pandas.

Now, let's implement additional Python examples based on the content:

```py
import pandas as pd

# Creating a series with floating-point numbers and a missing value (None)
values = pd.Series([1.2, 3.5, 2.8, None, 4.0, 0.5])

# Using max method to get the maximum value
max_value = values.max()

# Using min method to get the minimum value
min_value = values.min()

# Using sum method to get the sum of all values
sum_values = values.sum()

# Using mean method to get the average of the series
average_value = values.mean()

# Using idxmax and idxmin to get the index of max and min values
index_max = values.idxmax()
index_min = values.idxmin()

# Using isnull method to check for null values in the series
null_check = values.isnull()

# Using round method to round off decimals to two decimal places
rounded_values = values.round(2)

# Displaying the results
print("Max Value:", max_value)
print("Min Value:", min_value)
print("Sum of Values:", sum_values)
print("Average Value:", average_value)
print("Index of Max Value:", index_max)
print("Index of Min Value:", index_min)
print("Null Check:", null_check)
print("Rounded Values:", rounded_values)
```


## Handling CSV files

Until now, our own data has been created, which can be quite fun, but at the same time, 1,000,000 hours are not going to be spent creating our own datasets.

Instead, external datasets are going to be used, and one great place for external datasets to be found is on Kaggle.com. You can sign up for free and datasets can be searched for there. In this lesson, how to read CSV files and how to export them will be looked at in case they need to be saved with some special parameters or information.

A dataset containing the top 100 richest people in the world will be used, and it has been included in the resources section of this lecture. The CSV file can be downloaded directly, or it can be accessed from the source on Kaggle.com. The recommendation is to download it and place it in the folder containing your notebooks, just for this example. Later, it can be placed in other locations.

To simplify for this course, every time a CSV file is used, it will be placed inside the folder containing the notebook for easy reference inside Jupyter notebook.

Firstly, Pandas will be imported as PD to use its functionality, and then an attempt to read a CSV file will be made. In this case, a variable called richest will be created, and PD.read_csv will be called. The first argument to pass in is the location or path to that CSV file. Since it's in the same folder, its literal name can be used. Otherwise, if it's somewhere else, the entire path needs to be inserted. In this case, to check if it works, these two will be removed for now. If it's run and richest is returned, the dataset or data frame should be obtained as a return. If the type of richest is checked using type(richest), a data frame will be obtained, but it will be covered later.

What is wanted right now is to get back a series, and a series is a one-dimensional array, which means it cannot have many values. Only one column is allowed. To achieve this, use_columns will be defined, and it will be passed that only the name should be obtained. Now, if it's rerun, one column should be obtained. However, this is still considered a data frame with one column, and this can be verified by rerunning the type check. It's still a data frame. It needs to be converted to a series, and to do that, squeeze needs to be called. If there's only one column with an index, dot.squeeze will turn that into a series. If shift + enter is done, a series of objects with a length of 101 should be obtained. The next step is to check the type of richest, and it should return pandas.core.series.series, indicating that it is of type series. What was done there is reading the CSV file and squeezing that column into a series. This is how it can be read when dot.squeeze is used.

Moving down, if the CSV file needs to be exported, reference to the CSV file or to that series can be made, and the dot notation with to_csv followed by the CSV name that needs to be included can be used. To demonstrate this, the index will be removed for now, and it will be shown what that does as soon as these two cells are run. Now, if it's run, a CSV file should be placed inside the current folder. As seen, there's a test.csv, and that CSV file can also be read. Just by typing PD.read_csv, that series should be obtained back. However, it won't be a series when it's read because there are now two columns with a column that is also the index. That's quite ridiculous and not wanted. To fix this, the index parameter inside to_csv is set to false. If that line of code is run, and then test.csv that has been created is read, it won't generate that extra index. It will keep what was there earlier because there was already an index. It can be assigned to people, and those people can be returned, and the same thing will be obtained back down here. Now, the type of people can be checked. In this case, it will return a data frame because by default, when a CSV file is read, it is returned as a data frame. Dot.squeeze needs to be called if there's one column because that will turn it back into a series. When the type of people is checked, a series should be obtained back.

```py
import pandas as pd

# Creating a series with a dataset of the top 100 richest people in the world
richest = pd.read_csv('top_100_richest.csv')

# Extracting only the 'Name' column to get a series
richest_series = richest['Name'].squeeze()

# Displaying the series
print("Top 100 Richest People Names:")
print(richest_series)

# Exporting the series to a CSV file without including the index
richest_series.to_csv('richest_names.csv', index=False)

# Reading the CSV file back into a series
people = pd.read_csv('richest_names.csv', squeeze=True)

# Displaying the series obtained from the CSV file
print("\nPeople from CSV File:")
print(people)
```


## head() & tail()

The process of reading CSV files using Pandas was recently acquired. Initially, PD is imported. Subsequently, reading from a CSV file is accomplished using PD, dot read underscore CSV. In this case, reading is carried out from the "top richest in the world dot csv" file, and the outcome is assigned to the variable "richest," which is then returned. As observed, the entire data frame is obtained, displaying the first five elements, the last five elements as a preview, and ellipses for everything in between. However, if there is no interest in the last five elements or only a preview of five elements is desired, a method called dot head or just head is provided by Pandas. By default, removing the number (e.g., ten) will yield the first five elements. The execution of richest dot head will return the first five elements from the CSV file. Inserting a number (e.g., ten) will provide that number of elements, enabling a more convenient way to preview a data frame. In cases where the last five elements are not relevant, and a better understanding of the data frame's contents is desired, this method proves useful for visualization. A negative number can be entered into head to exclude the last elements. For instance, executing richest dot head with minus ten will return everything besides the last ten rows. This is evident from the index range going from 0 to 90, missing ten rows out of the 101-row dataset. Similar to head, a method called dot tail exists. The invocation of dot tail will provide the last ten items from the dataset or data frame. Executing dot tail with a negative number will return all rows starting from the end but exclude the first ten elements. For example, running dot tail with minus ten will display every element until 100, starting at the index of ten. Now, additional Python examples based on the transformed text will be implemented:

```py
import pandas as pd

# Reading from the "top richest in the world.csv" file
richest = pd.read_csv("datasets/TopRichestInWorld.csv")

# Using head to get the first five elements by default
head_default = richest.head()

# Using head to get the first ten elements
head_ten = richest.head(10)

# Using head with a negative number to exclude the last ten elements
head_minus_ten = richest.head(-10)

# Using tail to get the last ten elements
tail_ten = richest.tail(10)

# Using tail with a negative number to exclude the first ten elements
tail_minus_ten = richest.tail(-10)

# Displaying the results
print("Default Head (First Five Elements):\n", head_default)
print("\nHead (First Ten Elements):\n", head_ten)
print("\nHead (Exclude Last Ten Elements):\n", head_minus_ten)
print("\nTail (Last Ten Elements):\n", tail_ten)
print("\nTail (Exclude First Ten Elements):\n", tail_minus_ten)

```

## Sorting values in a Series


## Counting values in a Series


## Accessing elements via position


## Accessing elements via index
