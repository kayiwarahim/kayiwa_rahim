# mro_example2.py

class Person:
    def role(self):
        print("Person")

class Student(Person):
    def role(self):
        print("Student")

class Teacher(Person):
    def role(self):
        print("Teacher")

class TeachingAssistant(Student, Teacher):
    pass

# Usage
ta = TeachingAssistant()
ta.role()  # Output: Student (due to MRO: Student before Teacher)

print(TeachingAssistant.__mro__)
# Output: (<class '__main__.TeachingAssistant'>, <class '__main__.Student'>, <class '__main__.Teacher'>, <class '__main__.Person'>, <class 'object'>)
