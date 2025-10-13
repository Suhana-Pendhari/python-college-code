# Q4) E-commerce Order Data (sorting)
# An e-commerce company stores orders in a CSV file with Order ID, Customer, and Order Amount. 
# Load the file and sort the orders in descending order of the Order Amount.

import pandas as pd

df = pd.read_csv('./Data/orders.csv')

print("=== E-commerce Order Data Analysis ===")
print(df)

print("\nOrders sorted by Order Amount (Descending):")
sorted = df.sort_values('Order_Amount', ascending=False)
print(sorted)
