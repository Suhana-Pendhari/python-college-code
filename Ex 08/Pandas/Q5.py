# Q5) Employee Records (indexing)
# An IT company keeps employee details (Employee ID, Name, Department, Salary). 
# Read the data from Excel and set Employee ID as the index of the DataFrame.

import pandas as pd

# Read data from CSV file
df = pd.read_excel('./Data/employees.xlsx')

# Display the original DataFrame
print("Original DataFrame:")
print(df)

df.set_index('Employee ID', inplace=True)

# Display the DataFrame after setting index
print("DataFrame with Employee ID as index:")
print(df)
