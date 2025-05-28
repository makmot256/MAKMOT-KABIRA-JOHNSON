# Python solution to your assignment for a University System that displays 
# information using a parent class Person and subclasses Student, Lecturer, and Staff:

# Base class
class Person:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Role: {self.role}")

# Subclass: Student
class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age, "Student")
        self.student_id = student_id
        self.course = course

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")
        print()

# Subclass: Lecturer
class Lecturer(Person):
    def __init__(self, name, age, department, subject):
        super().__init__(name, age, "Lecturer")
        self.department = department
        self.subject = subject

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
        print(f"Subject: {self.subject}")
        print()

# Subclass: Staff
class Staff(Person):
    def __init__(self, name, age, position, department):
        super().__init__(name, age, "Staff")
        self.position = position
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Position: {self.position}")
        print(f"Department: {self.department}")
        print()

# Example usage
student = Student("Alice", 20, "S12345", "Computer Science")
lecturer = Lecturer("Dr. John", 45, "Engineering", "Electrical Systems")
staff = Staff("Grace", 35, "Secretary", "Admissions")

# Display info for each
student.display_info()
lecturer.display_info()
staff.display_info()
