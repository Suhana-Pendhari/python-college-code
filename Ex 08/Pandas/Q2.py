# Q2) Sales Report Analysis (describe)
# A supermarket maintains daily sales data (Product, Quantity, Price) in an Excel file. 
# Load the dataset and generate a statistical summary (mean, min, max, std) of the
# Quantity and Price columns.

import pandas as pd

df = pd.read_excel('./Data/supermarket.xlsx')

print("=== Supermarket Sales Report Analysis ===")
print(df)

print("\nStatistical summary of Quantity and Price columns:")

print(df[['Quantity', 'Price']].describe())
