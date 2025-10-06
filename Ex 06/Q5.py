# Q5) Student Management System:
# Build a system to manage students, courses, grades, and academic records. 
# Implement classes for students, courses, grades, teachers, and administrative functions.

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}

    def add_grade(self, course, grade):
        self.grades[course.course_id] = grade
        print(f"Grade {grade} added for {self.name} in {course.name}")

    def printAcademicRecord(self):
        print(f"\nAcademic Record for {self.name} (ID: {self.student_id}):")
        if not self.grades:
            print("No grades recorded.")
            return
        for course_id, grade in self.grades.items():
            print(f"Course {course_id}: Grade {grade}")

class Teacher:
    def __init__(self, name, teacher_id, specialty):
        self.name = name
        self.teacher_id = teacher_id
        self.specialty = specialty

    def printData(self):
        print(f"Teacher {self.teacher_id}: {self.name}, Specialty: {self.specialty}")


class Course:
    def __init__(self, name, course_id, teacher):
        self.name = name
        self.course_id = course_id
        self.teacher = teacher

    def printData(self):
        print(f"Course {self.course_id}: {self.name}, Teacher: {self.teacher.name}")


class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_course(self, course):
        self.courses.append(course)

    def print_all_students(self):
        print("\nAll Students:")
        for s in self.students:
            print(f"{s.student_id} - {s.name}")

    def print_all_courses(self):
        print("\nAll Courses:")
        for c in self.courses:
            c.printData()


school = School()

#Add teachers
t1 = Teacher("Dr. Rihana", 301, "Mathematics")
t2 = Teacher("Dr. Mirasab", 302, "Physics")
school.add_teacher(t1)
school.add_teacher(t2)

#Add courses
c1 = Course("Calculus", 101, t1)
c2 = Course("Mechanics", 102, t2)
school.add_course(c1)
school.add_course(c2)

#Add students
s1 = Student("Suhana", 201)
s2 = Student("Aman", 202)
school.add_student(s1)
school.add_student(s2)

#Assign grades
s1.add_grade(c1, "A")
s1.add_grade(c2, "B+")
s2.add_grade(c1, "B")
s2.add_grade(c2, "A-")

#Print academic records
s1.printAcademicRecord()
s2.printAcademicRecord()

#Show all students and courses
school.print_all_students()
school.print_all_courses()
