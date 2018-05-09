from student import *

while True:
    choice = input("1. Add Student Data \n2. Display Student data\n3. Press q to Quit\n")
    if choice == '1':
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        add_student(student_name, student_id)
        continue
    elif choice == '2':
        print_student_details()
    elif choice == 'q':
        print("Bye Bye!!")
        break
    else:
        print("Wrong Choice")
        continue