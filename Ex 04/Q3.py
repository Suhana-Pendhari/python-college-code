# Q3) Problem Statement:
# You are tasked with building a contact management system for a small business. 
# Each contact in the system should store the following immutable information about the person:
# Name (string)
# Phone number (string)
# Email address (string)
# Since the business wants to ensure that this information cannot be changed once 
# entered (for data integrity), you decide to use tuples to store each contact.
# Write a Python function add_contact() that takes a name, phone number, and email 
# address as arguments and returns a tuple containing the contact information.
# Create a function display_contacts() that takes a list of contact tuples and prints 
# them in a user-friendly format.
# Demonstrate how to add multiple contacts to a list and display them.

s = "----------------------------------"

def add_contact(name, phone, email):
    return (name, phone, email)

def display_contacts(contacts):
    print(s)
    if not contacts:
        print("No contacts available.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"Contact {i}:")
            print("  Name :", contact[0])
            print("  Phone:", contact[1])
            print("  Email:", contact[2])
            print(s)


contacts = []
while True:
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Exit")
    print(s)
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        contacts.append(add_contact(name, phone, email))
        print(s)
        print("Contact added successfully!")
        print(s)
    
    elif choice == "2":
        display_contacts(contacts)
    
    elif choice == "3":
        print("Exiting program. Goodbye!")
        print(s)
        break
    
    else:
        print("Invalid choice! Please try again.")
        print(s)
