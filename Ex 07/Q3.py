# 3. Mathematical Operations Problems
# • "Calculate the profit/loss of a company for 12 months by subtracting expense array from income array.",
# • "Compare the calorie intake vs calorie burn of a person for 7 days and find out daily calorie balance.",
# • "Compute the price after discount for a list of products using multiplication of price array with discount array."

import numpy as np

#Problem 1:Company profit/loss for 12 months
income = np.array([5000, 6000, 4500, 7000, 8000, 5500, 6500, 7200, 6800, 5900, 6300, 7100])
expense = np.array([4500, 5200, 4800, 6200, 7500, 5100, 5800, 6900, 6400, 5600, 6000, 6800])
profitLoss = income - expense
print("Monthly Profit/Loss:", profitLoss)

#Problem 2:Daily calorie balance for 7 days
cIntake = np.array([2200, 1800, 2500, 2000, 2300, 1900, 2100])
cBurn = np.array([1800, 2000, 2200, 1900, 2100, 1700, 1950])
cBalance = cIntake - cBurn
print("Daily Calorie Balance:", cBalance)

#Problem 3:Price after discount for products
oPrices = np.array([100, 250, 80, 150, 300])
discount = np.array([0.8, 0.7, 0.9, 0.85, 0.6])
fPrice = oPrices * discount
print("Final Prices after Discount:", fPrice)
