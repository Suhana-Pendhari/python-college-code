# Q6) Dictionary Operations:
# • Create functions to add a key-value pair, remove a key, and retrieve a 
# value from a dictionary. Test these functions with user-provided inputs.

def add_key_value(dictionary, key, value):
    dictionary[key] = value
    print(f"Added: {key} -> {value}")

def remove_key(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        print(f"Removed key: {key}")
    else:
        print(f"Key '{key}' not found.")

def retrieve_value(dictionary, key):
    if key in dictionary:
        print(f"Value for '{key}': {dictionary[key]}")
    else:
        print(f"Key '{key}' not found.")

my_dict = {}

while True:
    print("\nDictionary Operations Menu")
    print("1. Add key-value pair")
    print("2. Remove key")
    print("3. Retrieve value")
    print("4. Display dictionary")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        k = input("Enter key: ")
        v = input("Enter value: ")
        add_key_value(my_dict, k, v)
        
    elif choice == "2":
        k = input("Enter key to remove: ")
        remove_key(my_dict, k)
        
    elif choice == "3":
        k = input("Enter key to retrieve value: ")
        retrieve_value(my_dict, k)
        
    elif choice == "4":
        print("Current Dictionary:", my_dict)
        
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please select between 1 and 5.")

