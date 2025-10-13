# · Q6) Sports Performance Analysis
# Create a scatter plot showing the relationship between number of hours practiced and score obtained by athletes.

import matplotlib.pyplot as plt

# Hours practiced vs scores obtained by athletes
hours_practiced = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
scores_obtained = [65, 68, 72, 75, 78, 82, 85, 88, 90, 92, 94, 95, 96]

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(hours_practiced, scores_obtained, color='purple', s=80, alpha=0.7)

# Add labels and title
plt.title('Sports Performance: Practice Hours vs Scores', fontsize=14, fontweight='bold')
plt.xlabel('Hours Practiced')
plt.ylabel('Scores Obtained')

# Add grid for better readability
plt.grid(True, alpha=0.3)

# Show the plot
plt.tight_layout()
plt.show()
