# Importing necessary libraries
import pandas as pd

# Load the dataset (replace 'your_dataset.csv' with the path to your actual dataset)
data = pd.read_csv('your_dataset.csv')

# Display the first 5 rows of the dataset
print("Initial data:")
print(data.head())

# Check for missing values
missing_values = data.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)

# Fill missing values with the mean (for numerical columns)
data_filled = data.fillna(data.mean())

# Display basic statistics of the dataset
print("\nSummary Statistics:")
print(data_filled.describe())

# Example analysis: group by a specific column and calculate mean
grouped_data = data_filled.groupby('column_name').mean()
print("\nGrouped data by 'column_name':")
print(grouped_data)

# Save the cleaned dataset to a new CSV file
data_filled.to_csv('cleaned_data.csv', index=False)
print("\nCleaned data saved to 'cleaned_data.csv'.")
