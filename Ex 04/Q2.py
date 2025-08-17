# Q2) Problem Statement:
# You are tasked with building a simple Bank Management System. The system will manage 
# customer accounts and perform basic operations like creating new accounts, viewing 
# account details, depositing money, and withdrawing money. The customer data is stored 
# in a list of dictionaries, where each dictionary represents a customer’s account.
# Each customer account should have the following details:
# Account Number (Unique identifier)
# Customer Name
# Account Balance
# Functionalities:
# Add New Account:
# Use the append() function to add a new customer's account to the list.
# View Account Details:
# Search for a customer using their account number. Use the index() function to find the 
# account in the list and display details.
# Deposit Money:
# Update the balance of the account by adding the deposit amount using basic list 
# indexing or list comprehension.
# Withdraw Money:
# Check if the balance is sufficient, then subtract the withdrawal amount using list 
# indexing or list comprehension.
# Remove an Account:
# Use the remove() function to delete a customer’s account from the list based on 
# their account number.
# List All Accounts:
# Use a loop to iterate over the list and print all the accounts.

accounts = []
s = "--------------------------------------------"

def add_account(account_number, customer_name, balance):
    if any(acc['account_number'] == account_number for acc in accounts):
        print(f"Account number {account_number} already exists.")
        return
    accounts.append({
        'account_number': account_number,
        'customer_name': customer_name,
        'balance': balance
    })
    print(f"Account {account_number} created for {customer_name} with balance ${balance:.2f}.")

def find_account_index(account_number):
    account_numbers = [acc['account_number'] for acc in accounts]
    try:
        return account_numbers.index(account_number)
    except ValueError:
        return -1

def view_account(account_number):
    idx = find_account_index(account_number)
    if idx == -1:
        print(f"Account {account_number} not found.")
        return
    acc = accounts[idx]
    print(f"Account Number: {acc['account_number']}\nCustomer Name: {acc['customer_name']}\nBalance: ${acc['balance']:.2f}")

def deposit(account_number, amount):
    idx = find_account_index(account_number)
    if idx == -1:
        print(f"Account {account_number} not found.")
        return
    if amount <= 0:
        print("Deposit amount must be positive.")
        return
    accounts[idx]['balance'] += amount
    print(f"Deposited ${amount:.2f} to account {account_number}. New balance: ${accounts[idx]['balance']:.2f}")

def withdraw(account_number, amount):
    idx = find_account_index(account_number)
    if idx == -1:
        print(f"Account {account_number} not found.")
        return
    if amount <= 0:
        print("Withdrawal amount must be positive.")
        return
    if accounts[idx]['balance'] >= amount:
        accounts[idx]['balance'] -= amount
        print(f"Withdrew ${amount:.2f} from account {account_number}. New balance: ${accounts[idx]['balance']:.2f}")
    else:
        print("Insufficient balance.")

def remove_account(account_number):
    idx = find_account_index(account_number)
    if idx == -1:
        print(f"Account {account_number} not found.")
        return
    accounts.remove(accounts[idx])
    print(f"Account {account_number} removed.")

def list_all_accounts():
    if not accounts:
        print("No accounts found.")
        return
    print("List of all accounts:")
    for acc in accounts:
        print(f"Account Number: {acc['account_number']}, Name: {acc['customer_name']}, Balance: Rs. {acc['balance']:.2f}")

while True:
    print(s)
    print("--- Bank Management System ---")
    print(s)
    print("1. Add New Account")
    print("2. View Account Details")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Remove Account")
    print("6. List All Accounts")
    print("7. Exit")
    print(s)

    choice = input("Enter choice (1-7): ")

    if choice == '1':
        acc_num = input("Enter account number: ")
        name = input("Enter customer name: ")
        try:
            balance = float(input("Enter initial balance: "))
            if balance < 0:
                print("Balance cannot be negative.")
                continue
        except ValueError:
            print("Invalid balance amount.")
            continue
        add_account(acc_num, name, balance)

    elif choice == '2':
        acc_num = input("Enter account number to view: ")
        view_account(acc_num)

    elif choice == '3':
        acc_num = input("Enter account number to deposit into: ")
        try:
            amount = float(input("Enter deposit amount: "))
        except ValueError:
            print("Invalid amount.")
            continue
        deposit(acc_num, amount)

    elif choice == '4':
        acc_num = input("Enter account number to withdraw from: ")
        try:
            amount = float(input("Enter withdrawal amount: "))
        except ValueError:
            print("Invalid amount.")
            continue
        withdraw(acc_num, amount)

    elif choice == '5':
        acc_num = input("Enter account number to remove: ")
        remove_account(acc_num)

    elif choice == '6':
        list_all_accounts()

    elif choice == '7':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 7.")
