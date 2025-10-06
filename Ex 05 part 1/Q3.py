# Q3) Create a program that appends new content (e.g., additional lines of text) to an
# existing file (existing_data.txt) without overwriting the original content.

def append_to_file():
    print("Enter lines to append (press Enter on a blank line to finish):")
    
    with open('existing_data.txt', 'a') as file:  # 'a' mode opens file for appending
        while True:
            line = input()
            if line == "":
                break
            file.write(line + '\n')

    print("Content appended to existing_data.txt")

append_to_file()
