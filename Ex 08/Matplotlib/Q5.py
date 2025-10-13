# · Q5) Student Marks Comparison
# Plot a grouped bar chart showing marks scored by students in three different subjects (Math, Science, English).

import matplotlib.pyplot as plt
import numpy as np

# Student names and their marks in three subjects
students = ['Alice', 'Bob', 'Charlie', 'Diana']
math_marks = [85, 78, 92, 88]
science_marks = [90, 82, 88, 95]
english_marks = [78, 85, 80, 92]

# Set the width and positions for bars
bar_width = 0.25
x_pos = np.arange(len(students))

# Create grouped bar chart
plt.figure(figsize=(10, 6))
plt.bar(x_pos - bar_width, math_marks, width=bar_width, label='Math', color='red')
plt.bar(x_pos, science_marks, width=bar_width, label='Science', color='green')
plt.bar(x_pos + bar_width, english_marks, width=bar_width, label='English', color='blue')

# Add labels and title
plt.title('Student Marks Comparison', fontsize=14, fontweight='bold')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.xticks(x_pos, students)

# Add legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()