class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id,course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course
        
    def display_info(self):
        super().display_info()
        print(f"Role: Student, Student ID: {self.student_id}", 
              f"Course: {self.course}")
        
class Lecturer(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department
        
    def display_info(self):
        super().display_info()
        print(f"Role: Lecturer, Employee ID: {self.employee_id}", 
              f"Department: {self.department}")
        
class Staff(Person):
    def __init__(self, name, age, staff_id, role):
        super().__init__(name, age)
        self.staff_id = staff_id
        self.role = role
        
    def display_info(self):
        super().display_info()
        print(f"Role: Staff, Employee ID: {self.staff_id}", 
              f"Role: {self.role}")
        
if __name__ == "__main__":
    # Create instances of each class
    student = Student("Alice", 20, "S123", "Computer Science")
    lecturer = Lecturer("Dr. Bob", 40, "E678", "Mathematics")
    staff = Staff("Charlie", 35, "ST112", "Administrative Assistant")
    
    student.display_info()
    print() 
    lecturer.display_info()
    print() 
    staff.display_info()