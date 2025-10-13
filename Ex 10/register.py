import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json

class StudentRegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Registration System - Tkinter Widgets Demo")
        self.root.geometry("900x700")
        self.root.configure(bg='#f0f8ff')
        
        # Initialize variables
        self.students_data = []
        self.setup_variables()
        self.create_widgets()
        
    def setup_variables(self):
        """Initialize tkinter variables"""
        # String variables
        self.full_name = tk.StringVar()
        self.email = tk.StringVar()
        self.phone = tk.StringVar()
        self.address = tk.StringVar()
        self.father_name = tk.StringVar()
        self.mother_name = tk.StringVar()
        self.emergency_contact = tk.StringVar()
        
        # Other variables
        self.gender = tk.StringVar(value="Male")
        self.course = tk.StringVar(value="Computer Science")
        self.year = tk.StringVar(value="First Year")
        self.dob_day = tk.StringVar(value="1")
        self.dob_month = tk.StringVar(value="January")
        self.dob_year = tk.StringVar(value="2000")
        self.blood_group = tk.StringVar(value="A+")
        
        # Boolean variables for checkboxes
        self.hostel_facility = tk.BooleanVar()
        self.transport_facility = tk.BooleanVar()
        self.scholarship = tk.BooleanVar()
        self.terms_accepted = tk.BooleanVar()
        
        # List variables
        self.hobbies = []
        self.extracurricular = tk.StringVar()

    def create_widgets(self):
        """Create and arrange all widgets"""
        # Main title
        title_label = tk.Label(
            self.root, 
            text="🎓 Student Registration Form", 
            font=('Arial', 20, 'bold'), 
            bg='#2c3e50', 
            fg='white',
            pady=10
        )
        title_label.pack(fill='x', padx=10, pady=5)

        # Create notebook for tabs
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # Personal Information Tab
        personal_frame = ttk.Frame(notebook)
        notebook.add(personal_frame, text="Personal Information")

        # Academic Information Tab
        academic_frame = ttk.Frame(notebook)
        notebook.add(academic_frame, text="Academic Information")

        # Additional Information Tab
        additional_frame = ttk.Frame(notebook)
        notebook.add(additional_frame, text="Additional Information")

        # Records Tab
        records_frame = ttk.Frame(notebook)
        notebook.add(records_frame, text="Student Records")

        # Create widgets for each tab
        self.create_personal_tab(personal_frame)
        self.create_academic_tab(academic_frame)
        self.create_additional_tab(additional_frame)
        self.create_records_tab(records_frame)

        # Footer buttons
        self.create_footer_buttons()

    def create_personal_tab(self, parent):
        """Create personal information tab widgets"""
        # Main frame with scrollbar
        main_frame = tk.Frame(parent, bg='#f0f8ff')
        main_frame.pack(fill='both', expand=True)

        canvas = tk.Canvas(main_frame, bg='#f0f8ff')
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Personal Details Section
        personal_section = tk.LabelFrame(
            scrollable_frame, 
            text="Personal Details", 
            font=('Arial', 12, 'bold'),
            bg='#f0f8ff',
            padx=10,
            pady=10
        )
        personal_section.pack(fill='x', padx=10, pady=5)

        # Full Name
        tk.Label(personal_section, text="Full Name:*", bg='#f0f8ff', 
                font=('Arial', 10)).grid(row=0, column=0, sticky='w', pady=5)
        tk.Entry(personal_section, textvariable=self.full_name, 
                font=('Arial', 10), width=30).grid(row=0, column=1, pady=5, padx=5)

        # Email
        tk.Label(personal_section, text="Email:*", bg='#f0f8ff', 
                font=('Arial', 10)).grid(row=1, column=0, sticky='w', pady=5)
        tk.Entry(personal_section, textvariable=self.email, 
                font=('Arial', 10), width=30).grid(row=1, column=1, pady=5, padx=5)

        # Phone
        tk.Label(personal_section, text="Phone:*", bg='#f0f8ff', 
                font=('Arial', 10)).grid(row=2, column=0, sticky='w', pady=5)
        tk.Entry(personal_section, textvariable=self.phone, 
                font=('Arial', 10), width=30).grid(row=2, column=1, pady=5, padx=5)

        # Date of Birth
        tk.Label(personal_section, text="Date of Birth:", bg='#f0f8ff', 
                font=('Arial', 10)).grid(row=3, column=0, sticky='w', pady=5)
        
        dob_frame = tk.Frame(personal_section, bg='#f0f8ff')
        dob_frame.grid(row=3, column=1, sticky='w', pady=5)
        
        # Day dropdown
        days = [str(i) for i in range(1, 32)]
        tk.Label(dob_frame, text="Day:", bg='#f0f8ff', font=('Arial', 9)).pack(side='left')
        day_combo = ttk.Combobox(dob_frame, textvariable=self.dob_day, 
                               values=days, width=5, state='readonly')
        day_combo.pack(side='left', padx=2)
        
        # Month dropdown
        months = ['January', 'February', 'March', 'April', 'May', 'June', 
                 'July', 'August', 'September', 'October', 'November', 'December']
        tk.Label(dob_frame, text="Month:", bg='#f0f8ff', font=('Arial', 9)).pack(side='left', padx=(10,2))
        month_combo = ttk.Combobox(dob_frame, textvariable=self.dob_month, 
                                 values=months, width=10, state='readonly')
        month_combo.pack(side='left', padx=2)
        
        # Year dropdown
        years = [str(i) for i in range(1980, 2010)]
        tk.Label(dob_frame, text="Year:", bg='#f0f8ff', font=('Arial', 9)).pack(side='left', padx=(10,2))
        year_combo = ttk.Combobox(dob_frame, textvariable=self.dob_year, 
                                values=years, width=5, state='readonly')
        year_combo.pack(side='left', padx=2)

        # Gender
        tk.Label(personal_section, text="Gender:", bg='#f0f8ff', 
                font=('Arial', 10)).grid(row=4, column=0, sticky='w', pady=5)
        gender_frame = tk.Frame(personal_section, bg='#f0f8ff')
        gender_frame.grid(row=4, column=1, sticky='w', pady=5)
        
        tk.Radiobutton(gender_frame, text="Male", variable=self.gender, 
                      value="Male", bg='#f0f8ff').pack(side='left')
        tk.Radiobutton(gender_frame, text="Female", variable=self.gender, 
                      value="Female", bg='#f0f8ff').pack(side='left', padx=10)
        tk.Radiobutton(gender_frame, text="Other", variable=self.gender, 
                      value="Other", bg='#f0f8ff').pack(side='left')

        # Blood Group
        tk.Label(personal_section, text="Blood Group:", bg='#f0f8ff', 
                font=('Arial', 10)).grid(row=5, column=0, sticky='w', pady=5)
        blood_groups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
        blood_combo = ttk.Combobox(personal_section, textvariable=self.blood_group, 
                                 values=blood_groups, width=10, state='readonly')
        blood_combo.grid(row=5, column=1, sticky='w', pady=5, padx=5)

        # Address
        tk.Label(personal_section, text="Address:", bg='#f0f8ff', 
                font=('Arial', 10)).grid(row=6, column=0, sticky='nw', pady=5)
        address_text = tk.Text(personal_section, width=30, height=3, font=('Arial', 10))
        address_text.grid(row=6, column=1, pady=5, padx=5)
        self.address_text = address_text

        # Parent Information Section
        parent_section = tk.LabelFrame(
            scrollable_frame, 
            text="Parent/Guardian Information", 
            font=('Arial', 12, 'bold'),
            bg='#f0f8ff',
            padx=10,
            pady=10
        )
        parent_section.pack(fill='x', padx=10, pady=10)

        # Father's Name
        tk.Label(parent_section, text="Father's Name:", bg='#f0f8ff', 
                font=('Arial', 10)).grid(row=0, column=0, sticky='w', pady=5)
        tk.Entry(parent_section, textvariable=self.father_name, 
                font=('Arial', 10), width=30).grid(row=0, column=1, pady=5, padx=5)

        # Mother's Name
        tk.Label(parent_section, text="Mother's Name:", bg='#f0f8ff', 
                font=('Arial', 10)).grid(row=1, column=0, sticky='w', pady=5)
        tk.Entry(parent_section, textvariable=self.mother_name, 
                font=('Arial', 10), width=30).grid(row=1, column=1, pady=5, padx=5)

        # Emergency Contact
        tk.Label(parent_section, text="Emergency Contact:", bg='#f0f8ff', 
                font=('Arial', 10)).grid(row=2, column=0, sticky='w', pady=5)
        tk.Entry(parent_section, textvariable=self.emergency_contact, 
                font=('Arial', 10), width=30).grid(row=2, column=1, pady=5, padx=5)

        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def create_academic_tab(self, parent):
        """Create academic information tab widgets"""
        main_frame = tk.Frame(parent, bg='#f0f8ff')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)

        # Course Selection
        course_section = tk.LabelFrame(
            main_frame, 
            text="Course Information", 
            font=('Arial', 12, 'bold'),
            bg='#f0f8ff',
            padx=10,
            pady=10
        )
        course_section.pack(fill='x', pady=5)

        # Course dropdown
        tk.Label(course_section, text="Select Course:*", bg='#f0f8ff', 
                font=('Arial', 10)).grid(row=0, column=0, sticky='w', pady=5)
        courses = ['Computer Science', 'Electrical Engineering', 'Mechanical Engineering', 
                  'Civil Engineering', 'Electronics & Communication', 'Information Technology',
                  'Business Administration', 'Commerce', 'Arts', 'Science']
        course_combo = ttk.Combobox(course_section, textvariable=self.course, 
                                  values=courses, width=25, state='readonly')
        course_combo.grid(row=0, column=1, sticky='w', pady=5, padx=5)

        # Year of Study
        tk.Label(course_section, text="Year of Study:*", bg='#f0f8ff', 
                font=('Arial', 10)).grid(row=1, column=0, sticky='w', pady=5)
        years = ['First Year', 'Second Year', 'Third Year', 'Fourth Year', 'Fifth Year']
        year_combo = ttk.Combobox(course_section, textvariable=self.year, 
                                values=years, width=15, state='readonly')
        year_combo.grid(row=1, column=1, sticky='w', pady=5, padx=5)

        # Subjects Listbox
        subjects_section = tk.LabelFrame(
            main_frame, 
            text="Select Subjects", 
            font=('Arial', 12, 'bold'),
            bg='#f0f8ff',
            padx=10,
            pady=10
        )
        subjects_section.pack(fill='x', pady=10)

        # Listbox with scrollbar
        listbox_frame = tk.Frame(subjects_section, bg='#f0f8ff')
        listbox_frame.pack(fill='x', pady=5)

        subjects_listbox = tk.Listbox(listbox_frame, selectmode='multiple', 
                                    height=6, font=('Arial', 10))
        subjects_scrollbar = tk.Scrollbar(listbox_frame, orient='vertical')
        
        subjects_listbox.config(yscrollcommand=subjects_scrollbar.set)
        subjects_scrollbar.config(command=subjects_listbox.yview)

        # Add subjects to listbox
        all_subjects = [
            'Mathematics', 'Physics', 'Chemistry', 'Programming', 'Database Management',
            'Data Structures', 'Algorithms', 'Computer Networks', 'Operating Systems',
            'Software Engineering', 'Web Development', 'Machine Learning', 'AI'
        ]
        for subject in all_subjects:
            subjects_listbox.insert(tk.END, subject)

        subjects_listbox.pack(side='left', fill='x', expand=True)
        subjects_scrollbar.pack(side='right', fill='y')
        self.subjects_listbox = subjects_listbox

        # Previous Education
        education_section = tk.LabelFrame(
            main_frame, 
            text="Previous Education", 
            font=('Arial', 12, 'bold'),
            bg='#f0f8ff',
            padx=10,
            pady=10
        )
        education_section.pack(fill='x', pady=5)

        # Create a treeview for education details
        columns = ('Exam', 'Board', 'Year', 'Percentage')
        education_tree = ttk.Treeview(education_section, columns=columns, show='headings', height=4)
        
        # Define headings
        for col in columns:
            education_tree.heading(col, text=col)
            education_tree.column(col, width=100)

        # Add sample data
        sample_data = [
            ('10th', 'CBSE', '2018', '85%'),
            ('12th', 'CBSE', '2020', '78%'),
            ('Diploma', 'State Board', '2022', '82%')
        ]
        for data in sample_data:
            education_tree.insert('', tk.END, values=data)

        education_tree.pack(fill='x', pady=5)

    def create_additional_tab(self, parent):
        """Create additional information tab widgets"""
        main_frame = tk.Frame(parent, bg='#f0f8ff')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)

        # Facilities Section
        facilities_section = tk.LabelFrame(
            main_frame, 
            text="Facilities Required", 
            font=('Arial', 12, 'bold'),
            bg='#f0f8ff',
            padx=10,
            pady=10
        )
        facilities_section.pack(fill='x', pady=5)

        # Checkboxes for facilities
        tk.Checkbutton(facilities_section, text="Hostel Facility", 
                      variable=self.hostel_facility, bg='#f0f8ff',
                      font=('Arial', 10)).pack(anchor='w', pady=2)
        tk.Checkbutton(facilities_section, text="Transport Facility", 
                      variable=self.transport_facility, bg='#f0f8ff',
                      font=('Arial', 10)).pack(anchor='w', pady=2)
        tk.Checkbutton(facilities_section, text="Apply for Scholarship", 
                      variable=self.scholarship, bg='#f0f8ff',
                      font=('Arial', 10)).pack(anchor='w', pady=2)

        # Hobbies Section
        hobbies_section = tk.LabelFrame(
            main_frame, 
            text="Hobbies & Interests", 
            font=('Arial', 12, 'bold'),
            bg='#f0f8ff',
            padx=10,
            pady=10
        )
        hobbies_section.pack(fill='x', pady=10)

        # Checkbuttons for hobbies
        hobbies = [
            ('Reading', 'reading'),
            ('Sports', 'sports'),
            ('Music', 'music'),
            ('Dancing', 'dancing'),
            ('Painting', 'painting'),
            ('Programming', 'programming'),
            ('Gaming', 'gaming'),
            ('Photography', 'photography')
        ]

        hobbies_frame = tk.Frame(hobbies_section, bg='#f0f8ff')
        hobbies_frame.pack(fill='x', pady=5)

        self.hobby_vars = {}
        for i, (text, value) in enumerate(hobbies):
            var = tk.BooleanVar()
            self.hobby_vars[value] = var
            cb = tk.Checkbutton(hobbies_frame, text=text, variable=var, 
                              bg='#f0f8ff', font=('Arial', 9))
            cb.grid(row=i//4, column=i%4, sticky='w', padx=5, pady=2)

        # Extracurricular Activities
        tk.Label(hobbies_section, text="Extracurricular Activities:", 
                bg='#f0f8ff', font=('Arial', 10)).pack(anchor='w', pady=(10,5))
        
        activities = ['Sports Team', 'Cultural Club', 'Technical Club', 'NSS', 'NCC']
        activity_combo = ttk.Combobox(hobbies_section, textvariable=self.extracurricular, 
                                    values=activities, width=20)
        activity_combo.pack(anchor='w', pady=5)

        # Terms and Conditions
        terms_section = tk.LabelFrame(
            main_frame, 
            text="Terms & Conditions", 
            font=('Arial', 12, 'bold'),
            bg='#f0f8ff',
            padx=10,
            pady=10
        )
        terms_section.pack(fill='x', pady=10)

        terms_text = """I hereby declare that all information provided in this form is true and correct to the best of my knowledge. I understand that any false information may lead to cancellation of my admission."""

        terms_label = tk.Label(terms_section, text=terms_text, bg='#f0f8ff', 
                             font=('Arial', 9), justify='left', wraplength=600)
        terms_label.pack(anchor='w', pady=5)

        tk.Checkbutton(terms_section, text="I accept the terms and conditions", 
                      variable=self.terms_accepted, bg='#f0f8ff',
                      font=('Arial', 10, 'bold')).pack(anchor='w', pady=10)

    def create_records_tab(self, parent):
        """Create student records tab with table"""
        main_frame = tk.Frame(parent, bg='#f0f8ff')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)

        # Title
        tk.Label(main_frame, text="Registered Students", 
                font=('Arial', 14, 'bold'), bg='#f0f8ff').pack(pady=10)

        # Create treeview for records
        columns = ('ID', 'Name', 'Email', 'Course', 'Year', 'Gender', 'Phone')
        self.records_tree = ttk.Treeview(main_frame, columns=columns, show='headings', height=15)

        # Define headings
        for col in columns:
            self.records_tree.heading(col, text=col)
            self.records_tree.column(col, width=120)

        # Scrollbar for treeview
        scrollbar = ttk.Scrollbar(main_frame, orient='vertical', command=self.records_tree.yview)
        self.records_tree.configure(yscrollcommand=scrollbar.set)

        # Pack treeview and scrollbar
        self.records_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # Control buttons for records
        control_frame = tk.Frame(main_frame, bg='#f0f8ff')
        control_frame.pack(fill='x', pady=10)

        tk.Button(control_frame, text="Refresh Records", 
                 command=self.load_records, bg='#4CAF50', fg='white',
                 font=('Arial', 10)).pack(side='left', padx=5)
        tk.Button(control_frame, text="Clear All Records", 
                 command=self.clear_records, bg='#f44336', fg='white',
                 font=('Arial', 10)).pack(side='left', padx=5)
        tk.Button(control_frame, text="Export to JSON", 
                 command=self.export_records, bg='#2196F3', fg='white',
                 font=('Arial', 10)).pack(side='left', padx=5)

    def create_footer_buttons(self):
        """Create footer buttons"""
        footer_frame = tk.Frame(self.root, bg='#2c3e50')
        footer_frame.pack(fill='x', padx=10, pady=10)

        # Submit Button
        submit_btn = tk.Button(
            footer_frame, 
            text="🚀 Submit Registration", 
            command=self.submit_form,
            font=('Arial', 12, 'bold'),
            bg='#27ae60',
            fg='white',
            padx=20,
            pady=10
        )
        submit_btn.pack(side='left', padx=10)

        # Clear Button
        clear_btn = tk.Button(
            footer_frame, 
            text="🗑️ Clear Form", 
            command=self.clear_form,
            font=('Arial', 12),
            bg='#e74c3c',
            fg='white',
            padx=20,
            pady=10
        )
        clear_btn.pack(side='left', padx=10)

        # Preview Button
        preview_btn = tk.Button(
            footer_frame, 
            text="👁️ Preview Data", 
            command=self.preview_data,
            font=('Arial', 12),
            bg='#3498db',
            fg='white',
            padx=20,
            pady=10
        )
        preview_btn.pack(side='left', padx=10)

        # Exit Button
        exit_btn = tk.Button(
            footer_frame, 
            text="❌ Exit", 
            command=self.root.quit,
            font=('Arial', 12),
            bg='#7f8c8d',
            fg='white',
            padx=20,
            pady=10
        )
        exit_btn.pack(side='right', padx=10)

    def submit_form(self):
        """Handle form submission"""
        if not self.validate_form():
            return

        # Get selected subjects
        selected_subjects = []
        for i in self.subjects_listbox.curselection():
            selected_subjects.append(self.subjects_listbox.get(i))

        # Get selected hobbies
        selected_hobbies = []
        for hobby, var in self.hobby_vars.items():
            if var.get():
                selected_hobbies.append(hobby)

        # Create student record
        student_data = {
            'id': len(self.students_data) + 1,
            'full_name': self.full_name.get(),
            'email': self.email.get(),
            'phone': self.phone.get(),
            'gender': self.gender.get(),
            'dob': f"{self.dob_day.get()} {self.dob_month.get()} {self.dob_year.get()}",
            'blood_group': self.blood_group.get(),
            'address': self.address_text.get("1.0", tk.END).strip(),
            'father_name': self.father_name.get(),
            'mother_name': self.mother_name.get(),
            'emergency_contact': self.emergency_contact.get(),
            'course': self.course.get(),
            'year': self.year.get(),
            'subjects': selected_subjects,
            'hostel_facility': self.hostel_facility.get(),
            'transport_facility': self.transport_facility.get(),
            'scholarship': self.scholarship.get(),
            'hobbies': selected_hobbies,
            'extracurricular': self.extracurricular.get(),
            'registration_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.students_data.append(student_data)
        self.load_records()
        
        messagebox.showinfo("Success", "Student registration completed successfully!")
        self.clear_form()

    def validate_form(self):
        """Validate form data"""
        if not self.full_name.get():
            messagebox.showerror("Error", "Please enter full name")
            return False
        
        if not self.email.get():
            messagebox.showerror("Error", "Please enter email address")
            return False
        
        if not self.phone.get():
            messagebox.showerror("Error", "Please enter phone number")
            return False
        
        if not self.terms_accepted.get():
            messagebox.showerror("Error", "Please accept terms and conditions")
            return False
        
        return True

    def clear_form(self):
        """Clear all form fields"""
        # Clear string variables
        self.full_name.set("")
        self.email.set("")
        self.phone.set("")
        self.address.set("")
        self.father_name.set("")
        self.mother_name.set("")
        self.emergency_contact.set("")
        
        # Reset other variables
        self.gender.set("Male")
        self.course.set("Computer Science")
        self.year.set("First Year")
        self.dob_day.set("1")
        self.dob_month.set("January")
        self.dob_year.set("2000")
        self.blood_group.set("A+")
        self.extracurricular.set("")
        
        # Clear checkboxes
        self.hostel_facility.set(False)
        self.transport_facility.set(False)
        self.scholarship.set(False)
        self.terms_accepted.set(False)
        
        # Clear text widgets
        self.address_text.delete("1.0", tk.END)
        
        # Clear listbox selections
        self.subjects_listbox.selection_clear(0, tk.END)
        
        # Clear hobby checkboxes
        for var in self.hobby_vars.values():
            var.set(False)

    def preview_data(self):
        """Preview entered data"""
        preview_text = f"""
        🎓 STUDENT REGISTRATION PREVIEW
        {'='*40}
        👤 Personal Information:
        Name: {self.full_name.get()}
        Email: {self.email.get()}
        Phone: {self.phone.get()}
        Gender: {self.gender.get()}
        DOB: {self.dob_day.get()} {self.dob_month.get()} {self.dob_year.get()}
        Blood Group: {self.blood_group.get()}
        
        🏠 Address:
        {self.address_text.get("1.0", tk.END).strip()}
        
        👨‍👩‍👧 Parent Information:
        Father: {self.father_name.get()}
        Mother: {self.mother_name.get()}
        Emergency: {self.emergency_contact.get()}
        
        📚 Academic Information:
        Course: {self.course.get()}
        Year: {self.year.get()}
        """
        
        messagebox.showinfo("Form Preview", preview_text)

    def load_records(self):
        """Load records into treeview"""
        # Clear existing records
        for item in self.records_tree.get_children():
            self.records_tree.delete(item)
        
        # Add new records
        for student in self.students_data:
            self.records_tree.insert('', tk.END, values=(
                student['id'],
                student['full_name'],
                student['email'],
                student['course'],
                student['year'],
                student['gender'],
                student['phone']
            ))

    def clear_records(self):
        """Clear all records"""
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all records?"):
            self.students_data.clear()
            self.load_records()

    def export_records(self):
        """Export records to JSON file"""
        try:
            with open('student_records.json', 'w') as f:
                json.dump(self.students_data, f, indent=2)
            messagebox.showinfo("Success", "Records exported to student_records.json")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export records: {str(e)}")

def main():
    root = tk.Tk()
    app = StudentRegistrationForm(root)
    root.mainloop()

if __name__ == "__main__":
    main()