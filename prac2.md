# 2.student.mark.oop.py

class Person:
    def __init__(self, id, name, dob):
        self._id = id          # Encapsulation
        self._name = name
        self._dob = dob

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name


class Student(Person):
    def __init__(self, id, name, dob):
        super().__init__(id, name, dob)
        self._marks = {}      # course_id -> mark

    def add_mark(self, course_id, mark):
        self._marks[course_id] = mark

    def list_marks(self):
        return self._marks


class Course:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name


class MarkSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    # ----------------------------
    # Student functions
    # ----------------------------
    def input_student(self):
        id = input("Student ID: ")
        name = input("Name: ")
        dob = input("DOB: ")
        self.students.append(Student(id, name, dob))

    def list_students(self):
        print("\n--- Student List ---")
        for s in self.students:
            print(f"ID: {s.get_id()} - Name: {s.get_name()}")

    # ----------------------------
    # Course functions
    # ----------------------------
    def input_course(self):
        id = input("Course ID: ")
        name = input("Course name: ")
        self.courses.append(Course(id, name))

    def list_courses(self):
        print("\n--- Course List ---")
        for c in self.courses:
            print(f"ID: {c.get_id()} - Course: {c.get_name()}")

    # ----------------------------
    # Mark functions
    # ----------------------------
    def input_mark(self):
        self.list_courses()
        course_id = input("Choose course ID: ")

        self.list_students()
        for s in self.students:
            mark = float(input(f"Enter mark for {s.get_name()}: "))
            s.add_mark(course_id, mark)

    def list_marks(self):
        course_id = input("Enter course ID to view marks: ")

        print(f"\n--- Marks for course {course_id} ---")
        for s in self.students:
            marks = s.list_marks()
            if course_id in marks:
                print(f"{s.get_name()}: {marks[course_id]}")
            else:
                print(f"{s.get_name()}: No mark")

    # ----------------------------
    # Menu
    # ----------------------------
    def run(self):
        while True:
            print("\n===== Student Mark System (OOP) =====")
            print("1. Add student")
            print("2. Add course")
            print("3. Add marks")
            print("4. List students")
            print("5. List courses")
            print("6. List marks")
            print("0. Exit")

            choice = input("Choose: ")

            if choice == "1":
                self.input_student()
            elif choice == "2":
                self.input_course()
            elif choice == "3":
                self.input_mark()
            elif choice == "4":
                self.list_students()
            elif choice == "5":
                self.list_courses()
            elif choice == "6":
                self.list_marks()
            elif choice == "0":
                break
            else:
                print("Invalid option")


if __name__ == "__main__":
    system = MarkSystem()
    system.run()
