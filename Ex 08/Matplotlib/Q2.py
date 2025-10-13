# ·  Q2) COVID-19 Case Trends
# Plot a line graph showing the rise and fall of daily COVID-19 cases in a city over a span of 3 months.

import matplotlib.pyplot as plt

# Daily COVID-19 cases over 3 months
days = list(range(1, 91))
cases = [50, 55, 60, 65, 70, 80, 95, 110, 130, 150, 180, 210, 250, 300, 350, 
         400, 450, 500, 550, 600, 650, 700, 750, 780, 800, 810, 820, 815, 800, 
         780, 750, 720, 680, 650, 620, 590, 550, 520, 490, 460, 430, 400, 370, 
         340, 310, 280, 250, 220, 190, 160, 140, 120, 100, 90, 80, 70, 65, 60, 
         55, 50, 45, 40, 35, 30, 25, 20, 18, 16, 14, 12, 10, 8, 7, 6, 5, 4, 
         3, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Ensure both lists have same length
cases = cases[:len(days)]

# Create line graph
plt.plot(days, cases, color='red', linewidth=2)
plt.title('COVID-19 Daily Cases Over 3 Months')
plt.xlabel('Days')
plt.ylabel('Daily Cases')
plt.grid(True, alpha=0.3)
plt.show()
