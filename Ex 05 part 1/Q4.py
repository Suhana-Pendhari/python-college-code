# Q4) Write a Python program that write data from a text file and processes it.

# You are developing a text processing application where user inputs are stored in
# a text file named ABC.txt. Your task is to write a Java program that:

# Opens the file ABC.txt. If the file does not exist, the program should create it.
# Appends the text "This is an appended line of text." to the end of the file.
# Ensures that the data is properly appended without overwriting the existing contents of the file.
# After appending, print a confirmation message: "Data has been appended successfully.

def append_to_file():
    filename = "ABC.txt"
    text_to_append = "This is an appended line of text."

    with open(filename, "a") as file:  # 'a' mode opens the file for appending (creates if not exists)
        file.write(text_to_append + "\n")

    print("Data has been appended successfully.")

append_to_file()

