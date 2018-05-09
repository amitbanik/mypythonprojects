students = []


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        #return "Name: " + self.name + " ID: " + self.student_id
        return "Name: " + self.name

    def get_name_capitalize(self):
        return self.name.title()


mark = Student("mark", "123")
print(mark)


