# Base class for all people in the university
class Person:
    def __init__(self, name, age, university_id):
        self.name = name
        self.age = age
        self.university_id = university_id

    def get_details(self):
        # Basic info for all people
        return f"Name: {self.name}, Age: {self.age}, ID: {self.university_id}"

# Subclass for students
class Student(Person):
    def __init__(self, name, age, university_id, course, year):
        super().__init__(name, age, university_id)
        self.course = course
        self.year = year

    def get_details(self):
        # Overrides parent method to add student-specific info
        return f"{super().get_details()}, Course: {self.course}, Year: {self.year}"

# Subclass for lecturers
class Lecturer(Person):
    def __init__(self, name, age, university_id, department, subject):
        super().__init__(name, age, university_id)
        self.department = department
        self.subject = subject

    def get_details(self):
        # Lecturer-specific information
        return f"{super().get_details()}, Department: {self.department}, Subject: {self.subject}"

# Subclass for administrative staff
class Staff(Person):
    def __init__(self, name, age, university_id, position, office):
        super().__init__(name, age, university_id)
        self.position = position
        self.office = office

    def get_details(self):
        # Staff-specific information
        return f"{super().get_details()}, Position: {self.position}, Office: {self.office}"

# University system to manage people
class UniversitySystem:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        # Adds a person (Student, Lecturer, or Staff) to the university list
        if isinstance(person, Person):
            self.people.append(person)
        else:
            print("Invalid person object.")

    def display_all_people(self):
        # Display all registered people
        if not self.people:
            print("No people registered yet.")
            return

        print("\n--- University Members ---")
        for person in self.people:
            print(person.get_details())

# Sample usage
def main():
    university = UniversitySystem()

    # Adding sample students, lecturers, and staff
    student1 = Student("Alice Johnson", 20, "S123", "Computer Science", 2)
    lecturer1 = Lecturer("Dr. Smith", 45, "L456", "Engineering", "Mechanics")
    staff1 = Staff("Mr. Robert", 38, "ST789", "Registrar", "Admin Office")

    # Register them in the system
    university.add_person(student1)
    university.add_person(lecturer1)
    university.add_person(staff1)

    # Display all registered people
    university.display_all_people()

if __name__ == "__main__":
    main()
