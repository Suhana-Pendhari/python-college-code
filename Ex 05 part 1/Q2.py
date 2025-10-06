# Q2) Develop a script that prompts the user to enter multiple lines of text 
# and writes them to a file (output.txt).

def write_lines_to_file():
    print("Enter lines of text (press Enter on a blank line to finish):")
    lines = []

    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    with open('output.txt', 'w') as file:
        for line in lines:
            file.write(line + '\n')

    print("Your input has been saved to output.txt")

write_lines_to_file()
