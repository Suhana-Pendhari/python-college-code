# Q2) Banking System:
# Create a banking system with classes for customers, accounts (savings, checking), 
# transactions (deposits, withdrawals), and account management functionalities.

class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

    def __str__(self):
        return f"Customer {self.customer_id}: {self.name}"


class Account:
    def __init__(self, account_number, customer, balance=0):
        self.account_number = account_number
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New Balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. New Balance: {self.balance}")
        else:
            print("Withdrawal failed. Check balance or amount.")

    def __str__(self):
        return f"Account {self.account_number} | Customer: {self.customer.name} | Balance: {self.balance}"


class SavingsAccount(Account):
    def __init__(self, account_number, customer, balance=0, interest_rate=0.03):
        super().__init__(account_number, customer, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}. New Balance: {self.balance}")


class CheckingAccount(Account):
    def __init__(self, account_number, customer, balance=0, overdraft_limit=500):
        super().__init__(account_number, customer, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and (self.balance + self.overdraft_limit) >= amount:
            self.balance -= amount
            print(f"Withdrawn {amount}. New Balance: {self.balance}")
        else:
            print("Withdrawal failed. Overdraft limit reached.")


class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def open_account(self, account):
        self.accounts.append(account)

    def show_accounts(self):
        print("\nBank Accounts:")
        for acc in self.accounts:
            print(acc)


bank = Bank()

#Add customers
c1 = Customer("Suhana", 101)
c2 = Customer("Aman", 102)
bank.add_customer(c1)
bank.add_customer(c2)

#Open accounts
a1 = SavingsAccount(1001, c1, 1000)
a2 = CheckingAccount(2001, c2, 500)
bank.open_account(a1)
bank.open_account(a2)

#Show all accounts
bank.show_accounts()

#Perform some transactions
a1.deposit(500)
a1.add_interest()
a2.withdraw(800)
a2.deposit(300)

#Show accounts again
bank.show_accounts()
