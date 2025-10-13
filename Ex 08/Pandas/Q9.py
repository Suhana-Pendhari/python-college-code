# Q9) Flight Delay Records (CSV + head, tail, describe)
# An airline maintains records of flights in a CSV file with Flight ID, Departure, Arrival, 
# and Delay (minutes). Load the dataset and:
# Display the first 3 and last 3 flights.
# Use describe() to get statistics about flight delays.

import pandas as pd

# Read data from CSV file
df = pd.read_csv('./Data/flight.csv')

# Display first 3 flights
print("First 3 flights:")
print(df.head(3))
print("\n" + "="*40 + "\n")

# Display last 3 flights
print("Last 3 flights:")
print(df.tail(3))
print("\n" + "="*40 + "\n")

# Display statistics about flight delays
print("Flight Delay Statistics:")
print(df['Delay'].describe())
