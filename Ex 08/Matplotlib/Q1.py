# Q1) Matplotlib:
# ·  Monthly Sales Visualization
# Plot a bar chart showing the total sales of a retail shop for each month in 2024.

import matplotlib.pyplot as plt

# Monthly sales data for 2024
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [15000, 18000, 22000, 19000, 25000, 30000, 
         32000, 28000, 26000, 29000, 35000, 40000]

# Create bar chart
plt.figure(figsize=(12, 6))
plt.bar(months, sales, color='skyblue')

# Add labels and title
plt.title('Monthly Sales - 2024', fontsize=14, fontweight='bold')
plt.xlabel('Months')
plt.ylabel('Sales ($)')

# Show the plot
plt.tight_layout()
plt.show()
