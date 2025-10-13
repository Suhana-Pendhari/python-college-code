# · Q9) Company Expenditure Breakdown
# Use a pie chart to represent different categories of a company’s annual expenditure (Salaries, Marketing, R&D, Operations, Others).

import matplotlib.pyplot as plt

# Company expenditure by category
categories = ['Salaries', 'Marketing', 'R&D', 'Operations', 'Others']
expenditure = [45, 15, 20, 12, 8]  # in percentage

# Create pie chart
plt.figure(figsize=(8, 6))
plt.pie(expenditure, labels=categories, autopct='%1.1f%%', startangle=90)

# Add title
plt.title('Company Annual Expenditure Breakdown', fontsize=14, fontweight='bold')

# Show the plot
plt.show()
