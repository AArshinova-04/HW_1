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
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n' 
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
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {average_grade_count:.1f}\n')

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
        
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')    

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

# Создадим по 2 экземпляра каждого классов:
student1 = Student('Анна', 'Иванова', 'Ж')
student2 = Student('Петр', 'Сидоров', 'М')

lecturer1 = Lecturer('Мария', 'Петрова')
lecturer2 = Lecturer('Алексей', 'Смирнов')

reviewer1 = Reviewer('Ольга', 'Кузнецова')
reviewer2 = Reviewer('Дмитрий', 'Васильев')

# Назначим курсы студентам и лекторам:
student1.courses_in_progress = ['Python', 'Java']
student1.finished_courses = ['Введение в программирование']

student2.courses_in_progress = ['Python', 'C++']
student2.finished_courses = ['Алгоритмы']

lecturer1.courses_attached = ['Python', 'Java']
lecturer2.courses_attached = ['Python', 'C++']

reviewer1.courses_attached = ['Python', 'Java']
reviewer2.courses_attached = ['Python', 'C++']

# Выставим оценки студентам (ревьюверами):
reviewer1.rate_hw(student1, 'Python', 5)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Java', 7)
reviewer2.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student2, 'C++', 9)

# Выставим оценки лекторам (студентами):
student1.rate_lecture(lecturer1, 'Python', 7)
student1.rate_lecture(lecturer1, 'Java', 9)
student2.rate_lecture(lecturer2, 'Python', 10)
student2.rate_lecture(lecturer2, 'C++', 9)

# Выведем информацию об экземплярах:
print("\n=== Информация о студентах ===")
print(student1)
print("\n" + "-"*50 + "\n")
print(student2)
print("\n" + "-"*50 + "\n")

print("\n=== Информация о лекторах ===")
print(lecturer1)
print("\n" + "-"*50 + "\n")
print(lecturer2)
print("\n" + "-"*50 + "\n")

print("\n=== Информация о ревьюверах ===")
print(reviewer1)
print("\n" + "-"*50 + "\n")
print(reviewer2)
print("\n" + "-"*50 + "\n")

# Сравним студентов по средним оценкам:
print("\n=== Сравнение студентов ===")
print(f"Студент1 > Студент2: {student1 > student2}")
print(f"Студент1 < Студент2: {student1 < student2}")
print(f"Студент1 == Студент2: {student1 == student2}")

# Сравним лекторов по средним оценкам:
print("\n=== Сравнение лекторов ===")
print(f"Лектор1 > Лектор2: {lecturer1 > lecturer2}")
print(f"Лектор1 < Лектор2: {lecturer1 < lecturer2}")
print(f"Лектор1 == Лектор2: {lecturer1 == lecturer2}")

# Применим функции для подсчета средних оценок по курсам:
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

print("\n=== Средние оценки по курсам ===")
course = 'Python'
hw_average = average_hw_grade_for_course(students_list, course)
lecture_average = average_lecture_grade_for_course(lecturers_list, course)

print(f"Средняя оценка за домашние задания по курсу '{course}': {hw_average:.1f}")
print(f"Средняя оценка за лекции по курсу '{course}': {lecture_average:.1f}")