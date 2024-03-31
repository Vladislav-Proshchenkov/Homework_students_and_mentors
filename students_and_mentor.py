class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия {self.surname}\n'
                f'Средняя оценка за домашние задания: {self._gate_average_grade()}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {', '.join(self.finished_courses)}')

    def _gate_average_grade(self):
        for value in self.grades.values():
            self.grades = round(sum(value) / len(value),1)
        return self.grades

    def __lt__(self, other):
        if self.grades < other.grades:
            print(f'Средний балл {self.grades} < среднего балла {other.grades}')
        else:
            print(f'Средний балл {self.grades} > среднего балла {other.grades}')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self._gate_average_grade()}')

    def _gate_average_grade(self):
        for value in self.grades.values():
            self.grades = round(sum(value) / len(value), 1)
        return self.grades

    def __lt__(self, other):
        if self.grades < other.grades:
            print(f'Средний балл {self.grades} < среднего балла {other.grades}')
        else:
            print(f'Средний балл {self.grades} > среднего балла {other.grades}')



class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


lecturer_1 = Lecturer('Пётр', 'Петров')
lecturer_1.courses_attached += ['Git']

some_lecturer = Lecturer('Some', 'Lecturer')
some_lecturer.courses_attached += ['Git']

student_1 = Student('Вася', 'Иванов', 'м')
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']
student_1.finished_courses += ['Python']
student_1.rate_lecturer(lecturer_1, 'Git', 8)
student_1.rate_lecturer(lecturer_1, 'Git', 7)

some_student = Student('Ruoy', 'Eman', 'м')
some_student.courses_in_progress += ['Git']
some_student.courses_in_progress += ['Python']
some_student.finished_courses += ['Введение в программирование']
some_student.rate_lecturer(some_lecturer, 'Git', 8)
some_student.rate_lecturer(some_lecturer, 'Git', 7)
some_student.rate_lecturer(some_lecturer, 'Git', 10)

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 8)
some_reviewer.rate_hw(some_student, 'Python', 7)
some_reviewer.rate_hw(some_student, 'Python', 7)

reviewer_1 = Reviewer('Иван', 'Сидоров')
reviewer_1.courses_attached += ['Git']
reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_1, 'Git', 8)
reviewer_1.rate_hw(student_1, 'Git', 7)

print('Проверяющие:', end='\n\n')
print(some_reviewer, end='\n\n')
print(reviewer_1, end='\n\n')
print('Лекторы:', end='\n\n')
print(some_lecturer, end='\n\n')
print(lecturer_1, end='\n\n')
print('Студенты:', end='\n\n')
print(some_student, end='\n\n')
print(student_1, end='\n\n')
print('Сравнение лекторов:')
some_lecturer.__lt__(lecturer_1)
print('Сравнение студентов:')
some_student.__lt__(student_1)