# Q7) You are tasked with developing a simple inventory management system for a small 
# retail store. The system needs to keep track of products in the inventory, including 
# their quantities and prices. The store manager wants to be able to:
# 1.Add new products to the inventory.
# 2.Update the quantity of existing products.
# 3.Check the stock level of a product and warn if it's running low.
# 4.Calculate the total value of the inventory.

inventory = {}

while True:
    print("\nInventory Management System")
    print("1. Add new product")
    print("2. Update product quantity")
    print("3. Check stock level")
    print("4. Calculate total inventory value")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == '1':
        product = input("Enter product name: ").strip()
        if product in inventory:
            print(product + " already exists in inventory.")
        else:
            quantity = input("Enter quantity: ").strip()
            price = input("Enter price per unit: ").strip()
            
            if not quantity.isdigit() or float(price) < 0:
                print("Invalid input. Quantity must be a non-negative integer and price must be non-negative number.")
            else:
                quantity = int(quantity)
                price = float(price)
                if quantity < 0 or price < 0:
                    print("Quantity and price must be non-negative.")
                else:
                    inventory[product] = {"quantity": quantity, "price": price}
                    print("Added " + product + " to inventory.")

    elif choice == '2':
        product = input("Enter product name to update quantity: ").strip()
        if product not in inventory:
            print(product + " not found in inventory.")
        else:
            change = input("Enter quantity to add (use negative to reduce): ").strip()
            if (change.startswith('-') and change[1:].isdigit()) or change.isdigit():
                change = int(change)
                new_quantity = inventory[product]["quantity"] + change
                if new_quantity < 0:
                    print("Quantity cannot be negative.")
                else:
                    inventory[product]["quantity"] = new_quantity
                    print("Updated quantity of " + product + " to " + str(new_quantity) + ".")
            else:
                print("Invalid input. Quantity must be an integer.")

    elif choice == '3':
        product = input("Enter product name to check stock: ").strip()
        if product not in inventory:
            print(product + " not found in inventory.")
        else:
            quantity = inventory[product]["quantity"]
            print("Stock level for " + product + ": " + str(quantity))
            if quantity < 5:
                print("Warning: Stock running low!")

    elif choice == '4':
        total = 0
        for product in inventory:
            total += inventory[product]["quantity"] * inventory[product]["price"]
        print("Total inventory value: $" + "{:.2f}".format(total))

    elif choice == '5':
        print("Exiting system. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
