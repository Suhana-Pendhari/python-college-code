import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Student Registration")
root.geometry("350x250")

# Create form elements
tk.Label(root, text="Student Registration", font=('Arial', 14, 'bold')).pack(pady=10)

# Name
tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# Email
tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)

# Course
tk.Label(root, text="Course:").pack()
course_var = tk.StringVar(value="Computer Science")
course_menu = tk.OptionMenu(root, course_var, "Computer Science", "Electrical", "Mechanical")
course_menu.pack(pady=5)

def submit():
    if name_entry.get() and email_entry.get():
        messagebox.showinfo("Success", f"Registered!\nName: {name_entry.get()}\nEmail: {email_entry.get()}\nCourse: {course_var.get()}")
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        course_var.set("Computer Science")
    else:
        messagebox.showerror("Error", "Please fill all fields")

# Submit button
tk.Button(root, text="Register", command=submit, bg='lightblue', font=('Arial', 12)).pack(pady=20)

root.mainloop()