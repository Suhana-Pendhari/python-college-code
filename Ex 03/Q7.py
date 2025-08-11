# Q7) you are developing a small system for a library to manage book loans. The library 
# needs a function to determine if a book can be loaned out based on the number of available 
# copies. Additionally, you need another function to update the number of copies available 
# when a book is borrowed or returned.
# Requirements:
# 1.	Check Availability: Create a function can_loan(book_name, available_copies) that:
# o	Takes in the name of the book (book_name) and the number of available copies (available_copies).
# o	Returns True if the book is available to be loaned out (i.e., available_copies > 0), 
# otherwise returns False.
# 2.	Update Copies: Create a function update_copies(book_name, available_copies, action) that:
# o	Takes in the name of the book (book_name), the current number of available copies 
# (available_copies), and an action ('borrow' or 'return').
# o	If the action is 'borrow', decrease the number of available copies by 1.
# o	If the action is 'return', increase the number of available copies by 1.
# o	Return the updated number of copies.

def can_loan(book_name, available_copies):
    return available_copies > 0

def update_copies(book_name, available_copies, action):
    if action.lower() == "borrow":
        if available_copies > 0:
            available_copies -= 1
            print(f"You borrowed '{book_name}'.")
        else:
            print(f"'{book_name}' is not available for borrowing.")
    elif action.lower() == "return":
        available_copies += 1
        print(f"You returned '{book_name}'.")
    else:
        print("Invalid action. Please use 'borrow' or 'return'.")
    return available_copies

book = "Python Programming with Suhana"
copies = 2

while True:
    print(f"\nBook: {book} | Available copies: {copies}")
    print("1. Check availability")
    print("2. Borrow book")
    print("3. Return book")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        if can_loan(book, copies):
            print(f"'{book}' is available for loan.")
        else:
            print(f"'{book}' is not available right now.")
    
    elif choice == "2":
        copies = update_copies(book, copies, "borrow")
    
    elif choice == "3":
        copies = update_copies(book, copies, "return")
    
    elif choice == "4":
        print("Exiting Library System.")
        break
    else:
        print("Invalid choice! Please select 1-4.")

