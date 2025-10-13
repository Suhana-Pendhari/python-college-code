# Q6) Weather Data (slicing)
# A weather department collects daily data (Date, Temperature, Rainfall, Humidity).
# Load the dataset and display only the Temperature and Rainfall columns for the first 
# 10 days using slicing.

import pandas as pd

# Read data from CSV file
df = pd.read_csv('./Data/weather.csv')

# Display the original DataFrame
print("Original Weather DataFrame:")
print(df)

print("Temperature and Rainfall for first 10 days:")
result = df.loc[:9, ['Temperature', 'Rainfall']]
print(result)
