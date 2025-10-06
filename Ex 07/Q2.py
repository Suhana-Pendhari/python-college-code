# 2. Array Initialization Problems
# • "Simulate a blank black image of size 5x5 using a NumPy array filled with zeros."
# • "Generate a 4x4 identity matrix to represent a transformation in computer graphics.",
# • "Create a timetable slot system for 10 time slots where all slots are initially set as available (ones matrix)."

import numpy as np

zero = np.zeros((5,5))
print(zero)

identity = np.eye(4)
print(identity)

one = np.ones(10)
print(one)
