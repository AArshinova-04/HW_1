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
        else:
            return 'Ошибка'    
        
    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        average_grade_count = self.average_grade()
        return (f'Имя {self.name}\n'
                f'Фамилия {self.surname}\n' 
                f'Средняя оценка за домашние задания: {average_grade_count:.1f}\n' 
                f'Курсы в процессе изучения: {courses_in_progress}\n'
                f'Завершенные курсы: {finished_courses}')

    def average_grade(self): # вычислим среднюю оценку студента за домашнее задание
        all_grades = []
        for grades in self.grades.values():
            for grade in grades:
                all_grades.append(grade)
        return sum(all_grades) / len(all_grades)    
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() == other.average_grade()

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() > other.average_grade()    

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor): # лекторы
    def __init__(self, name, surname): 
        super().__init__(name, surname)
        self.grades = {} # Оценки за лекции от студентов

    def __str__(self):
        average_grade_count = self.average_grade()
        return (f'Имя {self.name}\n'
                f'Фамилия{self.surname}\n'
                f'Средняя оценка за лекции:{average_grade_count:.1f}\n')

    def average_grade(self): # Вычислим среднюю оценку за лекции от студентов
        if not self.grades:
            return 0
        all_grades = []
        for grades in self.grades.values():
            for grade in grades:
                all_grades.append(grade)
        return sum(all_grades) / len(all_grades)        
    
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() == other.average_grade()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() > other.average_grade()    

class Reviewer(Mentor): # эксперты, проверяющие домашние задания
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
        else:
            return 'Ошибка'

#lecturer = Lecturer('Иван', 'Иванов')
#reviewer = Reviewer('Пётр', 'Петров')
#student = Student('Алёхина', 'Ольга', 'Ж')
 
#student.courses_in_progress += ['Python', 'Java']
#lecturer.courses_attached += ['Python', 'C++']
#reviewer.courses_attached += ['Python', 'C++']
 
#print(student.rate_lecture(lecturer, 'Python', 7))   # None
#print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка
#print(student.rate_lecture(lecturer, 'С++', 8))      # Ошибка
#print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка
 
#print(lecturer.grades)  # {'Python': [7]}  

def average_hw_grade_for_course(students, course_name):
    total_grades = []
    for student in students:
        if course_name in student.grades:
            total_grades.extend(student.grades[course_name])
    if not total_grades:
        return 0
    return sum(total_grades) / len(total_grades)

def average_lecture_grade_for_course(lecturers, course_name):
    total_grades = []
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            total_grades.extend(lecturer.grades[course_name])
    if not total_grades:
        return 0
    return sum(total_grades) / len(total_grades)

