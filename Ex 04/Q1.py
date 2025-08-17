# Q1) Grocery Store Inventory Management

# You are tasked with developing a small inventory management system for a 
# grocery store. The store keeps track of the items in its inventory using a 
# list. Each item has the following properties:
# Name of the item
# Quantity in stock
# Price per unit
# You need to write a Python program to:
# Add new items to the inventory.
# Update the quantity of existing items.
# Remove items from the inventory.
# Find the most expensive item in the inventory.
# Sort the inventory based on item names or prices.
# Check if an item exists in the inventory.

inventory = []
s = "--------------------------------------------"

def add_item(name, quantity, price):
    for item in inventory:
        if item['name'].lower() == name.lower():
            print(f"Item '{name}' already exists. Use update_quantity to change quantity.")
            return
    inventory.append({'name': name, 'quantity': quantity, 'price': price})
    print(f"Added '{name}' to inventory.")

def update_quantity(name, quantity):
    for item in inventory:
        if item['name'].lower() == name.lower():
            item['quantity'] = quantity
            print(f"Updated quantity of '{name}' to {quantity}.")
            return
    print(f"Item '{name}' not found in inventory.")

def remove_item(name):
    for i, item in enumerate(inventory):
        if item['name'].lower() == name.lower():
            del inventory[i]
            print(f"Removed '{name}' from inventory.")
            return
    print(f"Item '{name}' not found in inventory.")

def most_expensive_item():
    if not inventory:
        print("Inventory is empty.")
        return
    expensive = max(inventory, key=lambda x: x['price'])
    print(f"Most expensive item: {expensive['name']} at ${expensive['price']:.2f}")

def sort_inventory(by='name'):
    if by == 'name':
        sorted_inv = sorted(inventory, key=lambda x: x['name'].lower())
    elif by == 'price':
        sorted_inv = sorted(inventory, key=lambda x: x['price'])
    else:
        print("Sort by 'name' or 'price' only.")
        return
    print(f"Inventory sorted by {by}:")
    for item in sorted_inv:
        print(f"{item['name']}: Quantity={item['quantity']}, Price=${item['price']:.2f}")

def item_exists(name):
    for item in inventory:
        if item['name'].lower() == name.lower():
            print(f"Item '{name}' exists in inventory.")
            return True
    print(f"Item '{name}' does not exist in inventory.")
    return False

def display_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    print("Current Inventory:")
    for item in inventory:
        print(f"{item['name']}: Quantity = {item['quantity']}, Price = Rs{item['price']:.2f}")

while True:
    print(s)
    print("Choose an operation:")
    print(s)
    print("1. Add new item")
    print("2. Update quantity")
    print("3. Remove item")
    print("4. Find most expensive item")
    print("5. Sort inventory")
    print("6. Check if item exists")
    print("7. Display inventory")
    print("8. Exit")
    print(s)

    choice = input("Enter choice (1-8): ")

    if choice == '1':
        name = input("Item name: ")
        quantity = int(input("Quantity: "))
        price = float(input("Price per unit: "))
        add_item(name, quantity, price)

    elif choice == '2':
        name = input("Item name to update: ")
        quantity = int(input("New quantity: "))
        update_quantity(name, quantity)

    elif choice == '3':
        name = input("Item name to remove: ")
        remove_item(name)

    elif choice == '4':
        most_expensive_item()

    elif choice == '5':
        sort_by = input("Sort by 'name' or 'price': ").lower()
        sort_inventory(sort_by)

    elif choice == '6':
        name = input("Item name to check: ")
        item_exists(name)

    elif choice == '7':
        display_inventory()

    elif choice == '8':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again!")
