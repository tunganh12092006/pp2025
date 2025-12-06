class Student:
    def __init__(self, sid, name, dob):
        self.id = sid
        self.name = name
        self.dob = dob
        def input(self):
        self.id = input("Student ID: ")
        self.name = input("Name: ")
        self.dob = input("DoB: ")
class Course:
    def __init__(self, cid, name):
        self.id = cid
        self.name = name
        def input(self):
        self.id = input("Course ID: ")
        self.name = input("Course name: ")
class StudentMarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {} 
    def input_students(self):
        n = int(input("Number of students: "))
        for _ in range(n):
            s = Student("", "", "")
            s.input()
            self.students.append(s)
            def list_students(self):
        print("\n--- Students ---")
        for s in self.students:
            print(f"{s.id} - {s.name} - {s.dob}")
    def input_courses(self):
        n = int(input("Number of courses: "))
        for _ in range(n):
            c = Course("", "")
            c.input()
            self.courses.append(c)
            self.marks[c.id] = {}
    def list_courses(self):
        print("\n--- Courses ---")
        for c in self.courses:
            print(f"{c.id} - {c.name}")
    def input_marks(self):
        cid = input("\nCourse ID to input marks: ")
        if cid not in self.marks:
            print("Course not found!")
            return
            print(f"Entering marks for {cid}:")
        for s in self.students:
            m = float(input(f"Mark for {s.name}: "))
            self.marks[cid][s.id] = m
            def show_marks(self):
        cid = input("Course ID to show marks: ")
        if cid not in self.marks:
            print("Course not found!")
            returnprint(f"\n--- Marks for course {cid} ---")
        for s in self.students:
            mark = self.marks[cid].get(s.id, "No mark")
            print(f"{s.name}: {mark}")
    def menu(self):
        self.input_students()
        self.input_courses()
        self.input_marks()
        print("\n1. List students")
        print("2. List courses")
        print("3. Show marks")
        choice = int(input("Your choice: "))
        if choice == 1:
            self.list_students()
        elif choice == 2:
            self.list_courses()
        elif choice == 3:
            self.show_marks()
def main():
    manager = StudentMarkManager()
    manager.menu()
