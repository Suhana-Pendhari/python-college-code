# · Q4) Temperature Variations
# Plot a line graph showing minimum and maximum daily temperatures of a city over one
# week on the same graph with different colors.

import matplotlib.pyplot as plt

# Daily temperatures for one week
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
max_temp = [32, 34, 36, 35, 33, 31, 30]  # Maximum temperatures
min_temp = [22, 24, 25, 23, 21, 20, 19]  # Minimum temperatures

# Create line graph
plt.figure(figsize=(10, 6))
plt.plot(days, max_temp, color='red', marker='o', linewidth=2, label='Max Temp')
plt.plot(days, min_temp, color='blue', marker='s', linewidth=2, label='Min Temp')

# Add labels and title
plt.title('Daily Temperature Variations Over One Week', fontsize=14, fontweight='bold')
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')

# Add legend and grid
plt.legend()
plt.grid(True, alpha=0.3)

# Show the plot
plt.tight_layout()
plt.show()
