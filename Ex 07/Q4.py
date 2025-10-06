# 4. Aggregate Functions Problems
# • "Find the average temperature of a city recorded over 30 days.",
# • "Analyze the marks of students in a class and display maximum, minimum, and mean marks.",
# • "Calculate the standard deviation of monthly rainfall data to understand variation in rainfall."

import numpy as np

#Problem 1:Average temperature over 30 days
temp = np.array([22.5, 24.1, 23.8, 25.2, 21.9, 22.7, 26.3, 24.8, 23.5, 25.1,
                        22.3, 24.6, 23.9, 25.8, 22.1, 23.2, 26.1, 24.3, 23.7, 25.5,
                        22.8, 24.9, 23.4, 25.7, 22.0, 23.1, 26.4, 24.5, 23.6, 25.3])
avgTemp = np.mean(temp)
print(f"Average Temperature: {avgTemp:.2f}°C")

#Problem 2:Student marks analysis
marks = np.array([85, 92, 78, 65, 88, 72, 95, 81, 69, 90, 76, 84, 79, 87, 93])
maxMarks = np.max(marks)
minMarks = np.min(marks)
meanMarks = np.mean(marks)
print(f"Max Marks: {maxMarks}")
print(f"Min Marks: {minMarks}")
print(f"Mean Marks: {meanMarks:.2f}")

#Problem 3:Standard deviation of monthly rainfall
rainfall = np.array([120, 85, 210, 45, 180, 95, 320, 65, 280, 110, 75, 150])
rainfallStd = np.std(rainfall)
print(f"Rainfall Standard Deviation: {rainfallStd:.2f} mm")
