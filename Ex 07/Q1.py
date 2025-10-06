# 1. Array Creation Problems
# • "Create a program that stores the daily sales of a shop for 7 days in a NumPy array and print the sales array.",
# • "Represent the marks of 5 students in 3 subjects using a 2D NumPy array and calculate the total marks per student."

import numpy as np

s = "----------------------------------------"
sales = []
n = 7
for i in range (0, n, 1):
    sales.append(int(input(f"Enter day {i+1} sales: ")))

numpyArray = np.array(sales)
print("Numpy Array: ", numpyArray)

print(s)

student = []
nStudent = 5
nSubject = 3

for i in range (0, nStudent, 1):
    marks = []
    print(f"Enter marks of 3 Subjects for Student {i+1}: ")
    for j in range (0, nSubject, 1):
        marks.append(int(input(f"Subject {j+1}: ")))
    student.append(marks)

numpyStudent = np.array(student)
print(numpyStudent)
print(np.shape(numpyStudent))
print(np.ndim(numpyStudent))

print(s)
j = 1
for i in numpyStudent:
    print(f"Total marks of Student {j} of 3 subjects: {np.sum(i)}")
    j=j+1

print(s)