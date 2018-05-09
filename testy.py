students = []


class Student:

    school_name='ABC'

    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        #return "Name: " + self.name + " ID: " + self.student_id
        return "Name: " + self.name.capitalize()

    def get_school_name(self):
        return self.school_name


stu = Student('mark')
print(stu)
print(stu.school_name)


