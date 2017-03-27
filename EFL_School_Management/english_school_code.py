
class School():
    def __init__(self, name):
        self.name = name

class Student():

    def __init__(self, student):
        self.student = student
        self.my_info = []
        
    def add_info(self,info):
        self.my_info.append(info)
        
class Lesson():

    def __init__(self,class_name):
        self.class_name = class_name
        self.students_in_class = []
        self.lessons_taken = []

    def add_student(self,name):
        self.students_in_class.append(name)


    def add_lessons_taken(self,lesson_title):
        self.lessons_taken.append(lesson_title)

