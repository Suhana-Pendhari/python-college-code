# Q5) Program to demonstrate working of with keyword

with open('example.txt', 'w') as file:
    file.write("Hello, this is a demo of the with keyword.\n")
    file.write("It ensures the file is properly closed automatically.\n")
    file.write("-----By Suhana the Coder")

with open('example.txt', 'r') as file:
    content = file.read()
    print("Content of the file:")
    print(content)
