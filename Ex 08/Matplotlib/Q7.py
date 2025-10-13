# · Q7) Website Traffic Analysis
# Plot a line chart showing number of visitors to a website each day for one month and highlight the peak day.
    
import matplotlib.pyplot as plt

# Daily website visitors for one month (30 days)
days = range(1, 31)
visitors = [120, 135, 110, 145, 160, 180, 220, 190, 210, 175, 
            165, 155, 140, 130, 125, 150, 170, 200, 240, 195, 
            185, 165, 155, 145, 135, 120, 110, 105, 115, 125]

# Find the peak day
peak_day = days[visitors.index(max(visitors))]
peak_visitors = max(visitors)

# Create line chart
plt.figure(figsize=(12, 6))
plt.plot(days, visitors, color='blue', linewidth=2, marker='o', markersize=4)

# Highlight the peak day
plt.plot(peak_day, peak_visitors, 'ro', markersize=10, label=f'Peak: {peak_visitors} visitors')

# Add labels and title
plt.title('Website Traffic Analysis - One Month', fontsize=14, fontweight='bold')
plt.xlabel('Days')
plt.ylabel('Number of Visitors')

# Add legend and grid
plt.legend()
plt.grid(True, alpha=0.3)

# Show the plot
plt.tight_layout()
plt.show()

