# 6. Matrix Operations Problems
# • "Calculate the total marks of students by multiplying the marks matrix with a weight matrix of subjects.",
# • "Perform matrix multiplication to transform 2D coordinates (points on a map) using a transformation matrix.",
# • "Transpose a timetable matrix to switch rows (days) into columns (time slots)."

import numpy as np

# Problem 1: Calculate total marks using matrix multiplication
# Students (rows) × Subjects (columns)
marks = np.array([
    [85, 92, 78],  # Student 1
    [65, 88, 72],  # Student 2  
    [95, 81, 69],  # Student 3
    [76, 84, 79]   # Student 4
])
weights = np.array([0.3, 0.4, 0.3])  # Weight for each subject
totalMarks = np.dot(marks,weights)  # Matrix multiplication
print("Total marks for each student:")
print(totalMarks)

# Problem 2: Transform 2D coordinates using matrix multiplication
# Original points (x, y coordinates)
points = np.array([
    [2, 3],   # Point 1
    [5, 1],   # Point 2
    [4, 6],   # Point 3
    [1, 2]    # Point 4
])
# Transformation matrix
transform = np.array([
    [0.8, -0.6],
    [0.6, 0.8]
])
transformPoints = np.dot(points,np.transpose(transform))  # Matrix multiplication
print("\nTransformed coordinates:")
print(transformPoints)

# Problem 3: Transpose timetable matrix
# Original: rows = days, columns = time slots
timetable = np.array([
    ['Math', 'Sci', 'Eng', 'Hist'],  # Monday
    ['Eng', 'Math', 'Hist', 'Sci'],  # Tuesday
    ['Sci', 'Eng', 'Math', 'Hist'],  # Wednesday
    ['Hist', 'Math', 'Sci', 'Eng'],  # Thursday
    ['Eng', 'Hist', 'Sci', 'Math']   # Friday
])
transposeTT = np.transpose(timetable)  # Transpose
print("\nTransposed timetable (rows = time slots, columns = days):")
print(transposeTT)
