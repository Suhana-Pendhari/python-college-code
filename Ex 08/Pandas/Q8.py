# Q8) Library Records (drop column)
# A library stores details of books (Book ID, Title, Author, Publisher, Edition). 
# Read the dataset from Excel and drop the column "Publisher" since it is not needed
# for analysis.

import pandas as pd

df = pd.read_excel('./Data/library.xlsx')

df = df.drop('Publisher', axis=1)

print(df)
