# Q3) Student Marks Sheet (read from dictionary)
# The marks of students in subjects (Math, Science, English) are stored in a Python dictionary. 
# Convert it into a DataFrame and display the details using head() and tail().

import pandas as pd

dic = {
    "name": ["Suhana", "Aman", "Rihana", "Mirasab", "Zakriya", "Kaliya"],
    "marks": [[10, 20, 30], [20, 30, 40], [20, 40, 50], [80, 40, 30], [10, 50, 70], [50, 60, 70]]
}
df = pd.DataFrame(dic)
print("\nAll data: ")
print(df)

print("\nUsing Head function: ")
print(df.head())

print("\nUsing tail function: ")
print(df.tail())
