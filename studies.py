class Reviewer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'Имя: {self.first_name}\nФамилия: {self.last_name}'

    
class Lecturer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = []  # Список оценок за лекции

    def add_grade(self, grade):
        self.grades.append(grade)

    @property
    def average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    def __str__(self):
        return f'Имя: {self.first_name}\nФамилия: {self.last_name}\nСредняя оценка за лекции: {self.average_grade:.1f}'

    def __lt__(self, other):
        return self.average_grade < other.average_grade

    def __le__(self, other):
        return self.average_grade <= other.average_grade

    def __eq__(self, other):
        return self.average_grade == other.average_grade

    def __gt__(self, other):
        return self.average_grade > other.average_grade

    def __ge__(self, other):
        return self.average_grade >= other.average_grade


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = []  # Список оценок за домашние задания
        self.courses_in_progress = []
        self.finished_courses = []

    def add_grade(self, grade):
        self.grades.append(grade)

    @property
    def average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    def __str__(self):
        return (f'Имя: {self.first_name}\n'
                f'Фамилия: {self.last_name}\n'
                f'Средняя оценка за домашние задания: {self.average_grade:.1f}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, other):
        return self.average_grade < other.average_grade

    def __le__(self, other):
        return self.average_grade <= other.average_grade

    def __eq__(self, other):
        return self.average_grade == other.average_grade

    def __gt__(self, other):
        return self.average_grade > other.average_grade

    def __ge__(self, other):
        return self.avera_ge_grade >= other.average_grade

# Пример использования
reviewer = Reviewer("Some", "Buddy")
lecturer = Lecturer("Some", "Buddy")
student = Student("Ruoy", "Eman")

# Добавим оценки
lecturer.add_grade(9)
lecturer.add_grade(10)
student.add_grade(8)
student.add_grade(9)

# Устанавливаем курсы для студента
student.courses_in_progress = ["Python", "Git"]
student.finished_courses = ["Введение в программирование"]

# Вывод информации о проверяющем, лекторе и студенте
print(reviewer)
print(lecturer)
print(student)

# Сравнение лекторов
lecturer2 = Lecturer("Another", "Lecturer")
lecturer2.add_grade(8)
lecturer2.add_grade(7)

print(lecturer > lecturer2)  # True или False в зависимости от средней оценки
print(lecturer2 < lecturer)   # True или False в зависимости от средней оценки

# Сравнение студентов
student2 = Student("Another", "Student")
student2.add_grade(9)
student2.add_grade(10)

print(student > student2)  # True или False в зависимости от средней оценки
print(student2 < student)   # True или False в зависимости от средней оценки
