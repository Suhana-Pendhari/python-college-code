# Q5) List Manipulation:
# • Develop functions to perform operations on lists, such as finding the maximum 
# element, reversing the list, and calculating the sum of elements.

def find_max(lst):
    return max(lst)

def reverse_list(lst):
    return lst[::-1]

def sum_list(lst):
    return sum(lst)

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print(f"Maximum element: {find_max(numbers)}")
print(f"Reversed list: {reverse_list(numbers)}")
print(f"Sum of elements: {sum_list(numbers)}")
