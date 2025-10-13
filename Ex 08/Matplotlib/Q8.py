# · Q8) Stock Market Trend
# Plot a candlestick-style chart (or a simple line chart) showing the daily closing price of a company’s stock over 30 days.

import matplotlib.pyplot as plt

# Daily closing prices for 30 days
days = range(1, 31)
closing_prices = [150, 152, 155, 153, 158, 160, 162, 159, 157, 155,
                  158, 161, 165, 163, 160, 162, 164, 168, 170, 172,
                  169, 167, 165, 163, 160, 158, 162, 165, 168, 170]

# Create line chart
plt.figure(figsize=(12, 6))
plt.plot(days, closing_prices, color='green', linewidth=2, marker='o', markersize=3)

# Add labels and title
plt.title('Stock Market Trend - 30 Days Closing Prices', fontsize=14, fontweight='bold')
plt.xlabel('Trading Days')
plt.ylabel('Closing Price ($)')

# Add grid for better readability
plt.grid(True, alpha=0.3)

# Show the plot
plt.tight_layout()
plt.show()
