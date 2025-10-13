# · Q3) Population Distribution
# Draw a pie chart showing the percentage distribution of population in different age groups (0–18, 19–35, 36–60, 60+).

import matplotlib.pyplot as plt

# Population distribution by age groups
age_groups = ['0-18', '19-35', '36-60', '60+']
population = [25, 30, 35, 10]  # in percentage

# Create pie chart
plt.figure(figsize=(8, 6))
plt.pie(population, labels=age_groups, autopct='%1.1f%%', startangle=90)

# Add title
plt.title('Population Distribution by Age Groups', fontsize=14, fontweight='bold')

# Show the plot
plt.show()
