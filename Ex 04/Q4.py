# Q4) Problem Statement:
# You are given two lists of integers, list1 and list2. Write a Python program 
# that performs the following operations using set:
# Union: Find all unique elements that appear in either list1 or list2.
# Intersection: Find all elements that appear in both list1 and list2.
# Difference: Find the elements that appear in list1 but not in list2.
# Symmetric Difference: Find all elements that appear in list1 or list2 but not in both.
# Subset Check: Check if list1 is a subset of list2.
# Superset Check: Check if list1 is a superset of list2.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Convert lists to sets
set1 = set(list1)
set2 = set(list2)

# Union
print("Union:", set1 | set2)

# Intersection
print("Intersection:", set1 & set2)

# Difference
print("Difference (list1 - list2):", set1 - set2)

# Symmetric Difference
print("Symmetric Difference:", set1 ^ set2)

# Subset Check
print("Is list1 a subset of list2?", set1.issubset(set2))

# Superset Check
print("Is list1 a superset of list2?", set1.issuperset(set2))
