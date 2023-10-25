# This file will contain the main program, where the student must test their program.
from Student import ManagementSystem

if __name__ == "__main__":
    system = ManagementSystem()

    while True:
        print("\nStudent Management System Menu:")
        print("1. Add Student")
        print("2. Enroll Student in Course")
        print("3. View Student Details")
        print("4. View Course Details")
        print("5. List All Students")
        print("6. List All Courses")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            system.add_student(name, student_id)
        elif choice == "2":
            student_id = input("Enter student ID: ")
            course_code = input("Enter course code: ")
            system.enroll_student_in_course(student_id, course_code)
        elif choice == "3":
            student_id = input("Enter student ID: ")
            system.view_student_details(student_id)
        elif choice == "4":
            course_code = input("Enter course code: ")
            system.view_course_details(course_code)
        elif choice == "5":
            system.list_all_students()
        elif choice == "6":
            system.list_all_courses()
        elif choice == "7":
            print("Exiting the Student Management System.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
