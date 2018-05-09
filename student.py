students = []


def get_student_details():
    students_details = []
    for student in students:
        students_details = [student["name"].title(), student["student_id"]]
    return students_details


def print_student_details():
    students_details = get_student_details()
    print(students_details)


def add_student(name, student_id):
    student = {"name": name, "student_id": student_id}
    students.append(student)


print(students)


