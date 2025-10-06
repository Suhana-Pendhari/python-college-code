# 5. Reshaping and Slicing Problems
# • "Store the rainfall data of 9 cities in a 1D array and reshape it into a 
# 3x3 matrix representing 3 regions with 3 cities each.",
# • "Extract the second row (representing February data) from a reshaped 12x30 
# array of temperature values for a year.",
# • "Pick out only the weekend sales data from a reshaped weekly sales matrix (7 days)."

import numpy as np

# Problem 1: Reshape rainfall data from 1D to 3x3 matrix
rain1D = np.array([120, 85, 210, 45, 180, 95, 320, 65, 280])
rain2D = rain1D.reshape(3, 3)
print("Rainfall 3x3 Matrix:")
print(rain2D)

# Problem 2: Extract February data from 12x30 temperature array
temperatures = np.random.randint(15, 35, size=(12, 30))
febData = temperatures[1]
print(f"\nFebruary temperatures (first 5 days): {febData[:5]}")

# Problem 3: Extract weekend sales from weekly data
weeklySales = np.array([1500, 1200, 1300, 1400, 1600, 2500, 2200])  # Mon-Sun
weekendSales = weeklySales[5:]  # Saturday (index 5) and Sunday (index 6)
print(f"\nWeekend sales: {weekendSales}")
