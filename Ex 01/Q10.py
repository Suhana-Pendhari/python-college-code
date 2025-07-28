# 10.Student Marks Normalization
# •	Take raw marks of students out of 70 and normalize them to a scale of 100 
# using arithmetic and assignment operators. Display the normalized scores as percentages.

n = int(input("Enter number of students: "))

normalized_scores = []

for i in range(n):
    raw_marks = float(input(f"Enter raw marks out of 70 for Student {i+1}: "))
    
    normalized = raw_marks
    normalized *= (100 / 70)
    
    normalized_scores.append(round(normalized, 2))

print("\n--- Normalized Scores (Out of 100) ---")
for i in range(n):
    print(f"Student {i+1}: {normalized_scores[i]}%")
