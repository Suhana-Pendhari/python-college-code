# Q8) You are tasked with creating a simple ATM machine simulation in Python. The ATM should allow a user to:
# 1.Check their account balance.
# 2.Deposit money.
# 3.Withdraw money.
# 4.Exit the application.
# Requirements:
# 1.The ATM should start with an initial balance of $1000.
# 2.The user should be prompted with a menu of options:
# o Check Balance
# o Deposit Money
# o Withdraw Money
# o Exit
# 3.The user should be able to perform multiple operations until they choose to exit.
# 4.Implement necessary checks and validations:
# oThe user cannot withdraw more than the available balance.
# oThe user should only be able to deposit and withdraw positive amounts.
# 5.Use appropriate control statements to manage the flow of the application.

balance = 1000

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == '1':
        print(f"Your current balance is: ${balance:.2f}")

    elif choice == '2':
        amount = input("Enter amount to deposit: ").strip()
        if amount.replace('.', '', 1).isdigit():
            amount = float(amount)
            if amount > 0:
                balance += amount
                print(f"${amount:.2f} deposited successfully.")
                print(f"New balance: ${balance:.2f}")
            else:
                print("Deposit amount must be positive.")
        else:
            print("Invalid amount. Please enter a positive number.")

    elif choice == '3':
        amount = input("Enter amount to withdraw: ").strip()
        if amount.replace('.', '', 1).isdigit():
            amount = float(amount)
            if amount <= 0:
                print("Withdrawal amount must be positive.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print(f"${amount:.2f} withdrawn successfully.")
                print(f"Remaining balance: ${balance:.2f}")
        else:
            print("Invalid amount. Please enter a positive number.")

    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option (1-4).")
