class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade): # выставляем оценки лектору
        if (isinstance(lecturer, Lecturer) # Проверяем, что лектор - экземпляр класса Lecturer
            and course in self.courses_in_progress  # и что студент проходит этот курс
            and course in lecturer.courses_attached): # и что лектор ведёт этот курс
            
            if course in lecturer.grades:
                    lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
            return 'Оценка выставлена'    
        else:
            return 'Ошибка'    

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor): # лекторы
    def __init__(self, name, surname): 
        super().__init__(name, surname)
        self.grades = {} # Оценки за лекции от студентов

class Reviewer(Mentor): # эксперты, проверяющие домашние задания)
    def __init__(self, name, surname):
        super().__init__(name, surname)                        

    def rate_hw(self, student, course, grade): # Только Reviewer может оценивать домашние задания
        if (isinstance(student, Student) 
            and course in self.courses_attached 
            and course in student.courses_in_progress):
            
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
            return 'Оценка выставлена'    
        else:
            return 'Ошибка'

