#  Процедурний стиль
def student_info(name, age):
    print(f"Student Name: {name}")
    print(f"Age: {age}")

def procedural_version():
    name = "Olena"
    age = 18
    student_info(name, age)

# Об'єктно-орієнтований стиль
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")

def oop_version():
    student = Student("Olena", 18) 
    student.display_info()

print("== Procedural ==")
procedural_version()

print("\n== OOP ==")
oop_version()
