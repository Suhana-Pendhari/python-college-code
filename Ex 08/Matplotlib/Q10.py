# · Q10) Weather Report
# Plot a bar graph showing average rainfall in each month of a year.

import matplotlib.pyplot as plt

# Average monthly rainfall (in mm)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
rainfall = [25, 30, 45, 60, 85, 120, 150, 140, 110, 75, 50, 35]

# Create bar chart
plt.figure(figsize=(12, 6))
plt.bar(months, rainfall, color='skyblue')

# Add labels and title
plt.title('Average Monthly Rainfall', fontsize=14, fontweight='bold')
plt.xlabel('Months')
plt.ylabel('Rainfall (mm)')

# Show the plot
plt.tight_layout()
plt.show()
