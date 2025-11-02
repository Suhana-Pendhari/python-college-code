# Q1) Hospital Patient Records (head, tail)
# A hospital stores patient records in a CSV file with details such as Patient ID, Name, Age, 
# and Disease. Load the dataset and display the first 5 and last 5 patients admitted.

import pandas as pd

df = pd.read_csv('./Data/Patients.csv')

print("=== Hospital Patient Records Analysis ===")
print("\n1. First 5 patients (head):")
print(df.head())

print("\n2. Last 5 patients (tail):")
print(df.tail())
