#This file will contains the class definition and the implementation of each member function.

class ManagementSystem:
    def __init__(self):
        self.students = {}  # Dictionary to store student information
        self.courses = []   # List of dictionaries to store course information

    def add_student(self, name, student_id):
        if student_id not in self.students:
            self.students[student_id] = {'name': name, 'courses': []}
            print(f"Student {name} with ID {student_id} added successfully.")
        else:
            print(f"Student with ID {student_id} already exists in the system.")

    def enroll_student_in_course(self, student_id, course_code):
        if student_id in self.students:
            course = next((c for c in self.courses if c['code'] == course_code), None)
            if course:
                if course_code not in self.students[student_id]['courses']:
                    self.students[student_id]['courses'].append(course_code)
                    print(f"Student with ID {student_id} enrolled in course {course_code}.")
                else:
                    print(f"Student is already enrolled in course {course_code}.")
            else:
                print(f"Course with code {course_code} does not exist.")
        else:
            print(f"Student with ID {student_id} not found.")

    def view_student_details(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            print(f"Student ID: {student_id}")
            print(f"Name: {student['name']}")
            print("Courses Enrolled In:")
            for course_code in student['courses']:
                course = next((c for c in self.courses if c['code'] == course_code), None)
                if course:
                    print(f"- {course_code} ({course['name']})")
        else:
            print(f"Student with ID {student_id} not found.")

    def view_course_details(self, course_code):
        course = next((c for c in self.courses if c['code'] == course_code), None)
        if course:
            print(f"Course Code: {course_code}")
            print(f"Course Name: {course['name']}")
            print("Students Enrolled:")
            for student_id, student in self.students.items():
                if course_code in student['courses']:
                    print(f"- {student['name']} (ID: {student_id})")
        else:
            print(f"Course with code {course_code} not found.")

    def list_all_students(self):
        print("List of All Students:")
        for student_id, student in self.students.items():
            print(f"Name: {student['name']}, ID: {student_id}")

    def list_all_courses(self):
        print("List of All Courses:")
        for course in self.courses:
            print(f"Code: {course['code']}, Name: {course['name']}")

    def add_course(self, course_code, course_name):
        if not any(c['code'] == course_code for c in self.courses):
            self.courses.append({'code': course_code, 'name': course_name})
            print(f"Course {course_name} with code {course_code} added successfully.")
        else:
            print(f"Course with code {course_code} already exists in the system.")
