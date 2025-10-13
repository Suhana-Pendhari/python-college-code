import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Layout Managers Demo")
        self.root.geometry("800x600")
        
        # Create notebook for different layout examples
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create frames for each layout manager
        self.pack_frame = ttk.Frame(self.notebook)
        self.grid_frame = ttk.Frame(self.notebook)
        self.place_frame = ttk.Frame(self.notebook)
        self.combined_frame = ttk.Frame(self.notebook)
        
        self.notebook.add(self.pack_frame, text="Pack Layout")
        self.notebook.add(self.grid_frame, text="Grid Layout")
        self.notebook.add(self.place_frame, text="Place Layout")
        self.notebook.add(self.combined_frame, text="Combined Layout")
        
        # Create examples for each layout manager
        self.create_pack_layout()
        self.create_grid_layout()
        self.create_place_layout()
        self.create_combined_layout()
    
    def validate_login(self, username, password, layout_type):
        """Validate login credentials"""
        if username == "admin" and password == "password":
            messagebox.showinfo("Login Successful", 
                              f"Welcome {username}!\n(Layout: {layout_type})")
        else:
            messagebox.showerror("Login Failed", 
                               "Invalid credentials!\nTry: admin/password")
    
    def create_pack_layout(self):
        """Create login form using Pack layout manager"""
        # Title
        title_label = tk.Label(self.pack_frame, text="Pack Layout Login", 
                              font=('Arial', 16, 'bold'))
        title_label.pack(pady=20)
        
        # Description
        desc_label = tk.Label(self.pack_frame, 
                             text="Uses pack() with side, fill, and pad options",
                             font=('Arial', 10))
        desc_label.pack(pady=5)
        
        # Main container frame
        container = tk.Frame(self.pack_frame, bg='lightgray', padx=20, pady=20)
        container.pack(padx=50, pady=30, fill='both', expand=True)
        
        # Username section
        username_frame = tk.Frame(container)
        username_frame.pack(fill='x', pady=10)
        
        username_label = tk.Label(username_frame, text="Username:", 
                                 font=('Arial', 12), width=15, anchor='w')
        username_label.pack(side='left', padx=(0, 10))
        
        self.username_pack = tk.Entry(username_frame, font=('Arial', 12))
        self.username_pack.pack(side='left', fill='x', expand=True)
        
        # Password section
        password_frame = tk.Frame(container)
        password_frame.pack(fill='x', pady=10)
        
        password_label = tk.Label(password_frame, text="Password:", 
                                 font=('Arial', 12), width=15, anchor='w')
        password_label.pack(side='left', padx=(0, 10))
        
        self.password_pack = tk.Entry(password_frame, font=('Arial', 12), show='*')
        self.password_pack.pack(side='left', fill='x', expand=True)
        
        # Buttons frame
        button_frame = tk.Frame(container)
        button_frame.pack(fill='x', pady=20)
        
        login_btn = tk.Button(button_frame, text="Login", 
                             font=('Arial', 12, 'bold'),
                             bg='lightblue',
                             command=lambda: self.validate_login(
                                 self.username_pack.get(), 
                                 self.password_pack.get(), 
                                 "Pack Layout"))
        login_btn.pack(side='left', padx=(0, 10))
        
        clear_btn = tk.Button(button_frame, text="Clear", 
                             font=('Arial', 12),
                             command=self.clear_pack_fields)
        clear_btn.pack(side='left')
    
    def create_grid_layout(self):
        """Create login form using Grid layout manager"""
        # Title
        title_label = tk.Label(self.grid_frame, text="Grid Layout Login", 
                              font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        # Description
        desc_label = tk.Label(self.grid_frame, 
                             text="Uses grid() with row, column, rowspan, columnspan",
                             font=('Arial', 10))
        desc_label.grid(row=1, column=0, columnspan=2, pady=5)
        
        # Main container frame
        container = tk.Frame(self.grid_frame, bg='lightyellow', padx=20, pady=20)
        container.grid(row=2, column=0, columnspan=2, padx=50, pady=30, sticky='nsew')
        
        # Configure grid weights for responsiveness
        self.grid_frame.grid_rowconfigure(2, weight=1)
        self.grid_frame.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(4, weight=1)
        container.grid_columnconfigure(1, weight=1)
        
        # Username
        username_label = tk.Label(container, text="Username:", 
                                 font=('Arial', 12))
        username_label.grid(row=0, column=0, sticky='w', pady=10, padx=(0, 10))
        
        self.username_grid = tk.Entry(container, font=('Arial', 12))
        self.username_grid.grid(row=0, column=1, sticky='ew', pady=10)
        
        # Password
        password_label = tk.Label(container, text="Password:", 
                                 font=('Arial', 12))
        password_label.grid(row=1, column=0, sticky='w', pady=10, padx=(0, 10))
        
        self.password_grid = tk.Entry(container, font=('Arial', 12), show='*')
        self.password_grid.grid(row=1, column=1, sticky='ew', pady=10)
        
        # Remember me checkbox
        self.remember_var = tk.BooleanVar()
        remember_cb = tk.Checkbutton(container, text="Remember me", 
                                    variable=self.remember_var,
                                    font=('Arial', 10))
        remember_cb.grid(row=2, column=0, columnspan=2, sticky='w', pady=10)
        
        # Buttons
        login_btn = tk.Button(container, text="Login", 
                             font=('Arial', 12, 'bold'),
                             bg='lightgreen',
                             command=lambda: self.validate_login(
                                 self.username_grid.get(), 
                                 self.password_grid.get(), 
                                 "Grid Layout"))
        login_btn.grid(row=3, column=0, pady=20, padx=(0, 10), sticky='ew')
        
        clear_btn = tk.Button(container, text="Clear", 
                             font=('Arial', 12),
                             command=self.clear_grid_fields)
        clear_btn.grid(row=3, column=1, pady=20, sticky='ew')
    
    def create_place_layout(self):
        """Create login form using Place layout manager"""
        # Title
        title_label = tk.Label(self.place_frame, text="Place Layout Login", 
                              font=('Arial', 16, 'bold'))
        title_label.place(relx=0.5, rely=0.1, anchor='center')
        
        # Description
        desc_label = tk.Label(self.place_frame, 
                             text="Uses place() with absolute and relative positioning",
                             font=('Arial', 10))
        desc_label.place(relx=0.5, rely=0.15, anchor='center')
        
        # Main container
        container = tk.Frame(self.place_frame, bg='lightcoral', 
                           width=400, height=250)
        container.place(relx=0.5, rely=0.5, anchor='center')
        
        # Username
        username_label = tk.Label(container, text="Username:", 
                                 font=('Arial', 12), bg='lightcoral')
        username_label.place(relx=0.1, rely=0.2, anchor='w')
        
        self.username_place = tk.Entry(container, font=('Arial', 12), width=15)
        self.username_place.place(relx=0.5, rely=0.2, anchor='center')
        
        # Password
        password_label = tk.Label(container, text="Password:", 
                                 font=('Arial', 12), bg='lightcoral')
        password_label.place(relx=0.1, rely=0.4, anchor='w')
        
        self.password_place = tk.Entry(container, font=('Arial', 12), 
                                     show='*', width=15)
        self.password_place.place(relx=0.5, rely=0.4, anchor='center')
        
        # Buttons
        login_btn = tk.Button(container, text="Login", 
                             font=('Arial', 12, 'bold'),
                             bg='lightpink',
                             command=lambda: self.validate_login(
                                 self.username_place.get(), 
                                 self.password_place.get(), 
                                 "Place Layout"))
        login_btn.place(relx=0.3, rely=0.7, anchor='center', width=100)
        
        clear_btn = tk.Button(container, text="Clear", 
                             font=('Arial', 12),
                             command=self.clear_place_fields)
        clear_btn.place(relx=0.7, rely=0.7, anchor='center', width=100)
    
    def create_combined_layout(self):
        """Create login form using combination of all layout managers"""
        # Title with pack
        title_label = tk.Label(self.combined_frame, 
                              text="Combined Layout Managers", 
                              font=('Arial', 16, 'bold'))
        title_label.pack(pady=20)
        
        desc_label = tk.Label(self.combined_frame, 
                             text="Uses Pack, Grid, and Place together",
                             font=('Arial', 10))
        desc_label.pack(pady=5)
        
        # Main container using pack
        main_container = tk.Frame(self.combined_frame, bg='lightgreen', 
                                padx=20, pady=20)
        main_container.pack(padx=50, pady=30, fill='both', expand=True)
        
        # Left section using grid
        left_frame = tk.Frame(main_container, bg='white', padx=10, pady=10)
        left_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        # Login form in left frame using grid
        login_label = tk.Label(left_frame, text="Login Form", 
                              font=('Arial', 14, 'bold'), bg='white')
        login_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Username
        tk.Label(left_frame, text="Username:", font=('Arial', 12), 
                bg='white').grid(row=1, column=0, sticky='w', pady=5)
        self.username_combined = tk.Entry(left_frame, font=('Arial', 12))
        self.username_combined.grid(row=1, column=1, sticky='ew', pady=5)
        
        # Password
        tk.Label(left_frame, text="Password:", font=('Arial', 12), 
                bg='white').grid(row=2, column=0, sticky='w', pady=5)
        self.password_combined = tk.Entry(left_frame, font=('Arial', 12), show='*')
        self.password_combined.grid(row=2, column=1, sticky='ew', pady=5)
        
        left_frame.grid_columnconfigure(1, weight=1)
        
        # Buttons using pack in a frame
        button_frame = tk.Frame(left_frame, bg='white')
        button_frame.grid(row=3, column=0, columnspan=2, pady=20)
        
        login_btn = tk.Button(button_frame, text="Login", 
                             font=('Arial', 12, 'bold'),
                             bg='lightblue',
                             command=lambda: self.validate_login(
                                 self.username_combined.get(), 
                                 self.password_combined.get(), 
                                 "Combined Layout"))
        login_btn.pack(side='left', padx=(0, 10))
        
        clear_btn = tk.Button(button_frame, text="Clear", 
                             font=('Arial', 12),
                             command=self.clear_combined_fields)
        clear_btn.pack(side='left')
        
        # Right section using place
        right_frame = tk.Frame(main_container, bg='lightblue', 
                              width=200, height=200)
        right_frame.pack(side='right', fill='both', expand=True)
        
        info_label = tk.Label(right_frame, text="Layout Info", 
                             font=('Arial', 12, 'bold'), bg='lightblue')
        info_label.place(relx=0.5, rely=0.1, anchor='center')
        
        info_text = """Pack: Simple stacking
Grid: Table-like structure
Place: Absolute positioning
        
Best Practice:
• Use Pack for simple layouts
• Use Grid for forms
• Use Place for precise control
• Combine for complex UIs"""
        
        info_content = tk.Label(right_frame, text=info_text, 
                               font=('Arial', 9), bg='lightblue', justify='left')
        info_content.place(relx=0.5, rely=0.5, anchor='center')
    
    def clear_pack_fields(self):
        """Clear pack layout fields"""
        self.username_pack.delete(0, tk.END)
        self.password_pack.delete(0, tk.END)
        self.username_pack.focus()
    
    def clear_grid_fields(self):
        """Clear grid layout fields"""
        self.username_grid.delete(0, tk.END)
        self.password_grid.delete(0, tk.END)
        self.remember_var.set(False)
        self.username_grid.focus()
    
    def clear_place_fields(self):
        """Clear place layout fields"""
        self.username_place.delete(0, tk.END)
        self.password_place.delete(0, tk.END)
        self.username_place.focus()
    
    def clear_combined_fields(self):
        """Clear combined layout fields"""
        self.username_combined.delete(0, tk.END)
        self.password_combined.delete(0, tk.END)
        self.username_combined.focus()

def main():
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()