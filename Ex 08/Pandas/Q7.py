# Q7) Bank Customer Data (add column)
# A bank maintains customer data (Customer ID, Name, Balance) in a CSV file.
# Load the dataset and add a new column "Account Type" where customers with 
# Balance > 50,000 are labeled "Premium" and others "Standard".

import pandas as pd

df = pd.read_csv('./Data/bank.csv')

df['Account Type'] = ['Premium' if balance > 50000 else 'Standard' for balance in df['Balance']]

print(df)
