# Q5) Problem Statement:
# You are tasked with creating a dictionary that stores information about students and 
# their corresponding grades. Write a Python program that does the following:
# Create a dictionary where the keys are student names and the values are their grades.
# Add a new student and their grade to the dictionary.
# Update the grade of an existing student.
# Delete a student from the dictionary.
# Display all students and their grades in alphabetical order.
# Use dictionary inbuilt functions to:
# Get a list of all students (keys).
# Get a list of all grades (values).
# Check if a student is in the dictionary.
# Find the total number of students in the dictionary.
# Clear the dictionary of all entries.

s = "---------------------------------------"

def display_students(students):
    print(s)
    if not students:
        print("No students in the dictionary.")
    else:
        print("\nStudents and Grades (Alphabetical Order):")
        for name in sorted(students.keys()):
            print(name, ":", students[name])
    print(s)

def main():
    students = {}

    while True:
        print("\n--- Student Grade Management System ---")
        print("1. Add Student")
        print("2. Update Student Grade")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Show All Students (Keys)")
        print("6. Show All Grades (Values)")
        print("7. Check if a Student Exists")
        print("8. Total Number of Students")
        print("9. Clear All Students")
        print("10. Exit")
        print(s)

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            grade = int(input("Enter grade: "))
            students[name] = grade
            print(f"{name} added successfully!")

        elif choice == "2":
            name = input("Enter student name to update: ")
            if name in students:
                grade = int(input("Enter new grade: "))
                students[name] = grade
                print(f"{name}'s grade updated successfully!")
            else:
                print("Student not found!")

        elif choice == "3":
            name = input("Enter student name to delete: ")
            if name in students:
                del students[name]
                print(f"{name} deleted successfully!")
            else:
                print("Student not found!")

        elif choice == "4":
            display_students(students)

        elif choice == "5":
            print("All Students:", list(students.keys()))

        elif choice == "6":
            print("All Grades:", list(students.values()))

        elif choice == "7":
            name = input("Enter student name to check: ")
            if name in students:
                print(f"{name} exists in the dictionary.")
            else:
                print(f"{name} does not exist in the dictionary.")

        elif choice == "8":
            print("Total number of students:", len(students))

        elif choice == "9":
            students.clear()
            print("All students cleared!")

        elif choice == "10":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

main()
