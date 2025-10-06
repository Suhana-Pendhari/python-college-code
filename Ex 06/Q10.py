# Q10) Online Quiz or Exam System:
# Design an online quiz or exam system with classes for quizzes, questions, 
# answers, students, grading, and results. Implement functionalities for quiz 
# creation, student assessments, and scoring.

class Question:
    def __init__(self, question_text, options, correct_answer):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

    def print_question(self):
        print(f"\nQuestion: {self.question_text}")
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")

class Quiz:
    def __init__(self, quiz_name):
        self.quiz_name = quiz_name
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def print_quiz(self):
        print(f"\nQuiz: {self.quiz_name}")
        for q in self.questions:
            q.print_question()

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def printData(self):
        print(f"Student {self.student_id}: {self.name}")

class Result:
    def __init__(self, student, quiz):
        self.student = student
        self.quiz = quiz
        self.score = 0

    def calculate_score(self, answers):
        for question, answer in zip(self.quiz.questions, answers):
            if answer == question.correct_answer:
                self.score += 1

    def printResult(self):
        print(f"\nResult for {self.student.name} in Quiz '{self.quiz.quiz_name}': {self.score}/{len(self.quiz.questions)}")


class ExamSystem:
    def __init__(self):
        self.students = []
        self.quizzes = []

    def add_student(self, student):
        self.students.append(student)

    def add_quiz(self, quiz):
        self.quizzes.append(quiz)

    def conduct_quiz(self, student_id, quiz_name, student_answers):
        student = next((s for s in self.students if s.student_id == student_id), None)
        quiz = next((q for q in self.quizzes if q.quiz_name == quiz_name), None)

        if student and quiz:
            result = Result(student, quiz)
            result.calculate_score(student_answers)
            result.printResult()
        else:
            print("Student or Quiz not found.")

system = ExamSystem()

#Add students
s1 = Student("Suhana", 201)
s2 = Student("Aman", 202)
system.add_student(s1)
system.add_student(s2)

#Create quiz
quiz1 = Quiz("Math Quiz")

q1 = Question("2 + 2 = ?", ["3", "4", "5"], "4")
q2 = Question("5 * 3 = ?", ["15", "10", "8"], "15")
q3 = Question("10 - 7 = ?", ["3", "2", "4"], "3")

quiz1.add_question(q1)
quiz1.add_question(q2)
quiz1.add_question(q3)

system.add_quiz(quiz1)

#Conduct quiz for students (student_answers are simulated here)
system.conduct_quiz(201, "Math Quiz", ["4", "15", "3"]) #all correct
system.conduct_quiz(202, "Math Quiz", ["3", "15", "2"]) #one wrong
