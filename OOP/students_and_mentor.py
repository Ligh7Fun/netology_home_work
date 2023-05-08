#  узнать как указать тип объеекта "класс" который описан ниже
class Person:
    """Базовый класс для всех людей"""
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'\nИмя: {self.name}\nФамилия: {self.surname}'


class Student(Person):
    """Класс студентов"""
    def __init__(self, name: str, surname: str, gender: str):
        super().__init__(name, surname)
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.get_avg_grade() == other.get_avg_grade()
        else:
            return 'Нельзя сравнить объекты разных классов!'

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.get_avg_grade() != other.get_avg_grade()
        else:
            return 'Нельзя сравнить объекты разных классов!'

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.get_avg_grade() < other.get_avg_grade()
        else:
            return 'Нельзя сравнить объекты разных классов!'

    def __le__(self, other):
        if isinstance(other, Student):
            return self.get_avg_grade() <= other.get_avg_grade()
        else:
            return 'Нельзя сравнить объекты разных классов!'

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.get_avg_grade() > other.get_avg_grade()
        else:
            return 'Нельзя сравнить объекты разных классов!'

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.get_avg_grade() >= other.get_avg_grade()
        else:
            return 'Нельзя сравнить объекты разных классов!'

    def get_avg_grade(self):
        if len(self.grades.values()):
            grades = []
            for grade in self.grades.values():
                grades += grade
            return round(sum(grades) / len(grades), 1)
        else:
            return 0

    def add_course(self, course_name: str):
        if course_name not in self.courses_in_progress:
            self.courses_in_progress.append(course_name)
            print(f'\nКурс "{course_name}" добавлен в изучаемые.')
        else:
            print('Такой курс уже есть!')

    def add_finish_course(self, course_name: str):
        if course_name in self.courses_in_progress:
            self.courses_in_progress.remove(course_name)
            self.finished_courses.append(course_name)
        else:
            self.finished_courses.append(course_name)
        print(f'\nКурс "{course_name}" добавлен в завершенные.')

    def add_grade(self, lector, course_name: str, grade: int):
        if course_name in self.courses_in_progress and \
                isinstance(grade, int) and \
                1 <= grade <= 10 and \
                course_name in lector.courses_attached and \
                isinstance(lector, Lecturer):
            lector.grades.setdefault(course_name, []).append(grade)
            print(f'\nЛектору {lector.surname} {lector.name} '
                  f'для курса "{course_name}" добавлена оценка {grade}.')
        else:
            print('\nУказали некорректные данные!')

    def __str__(self):
        if len(self.courses_in_progress):
            courses_in_progress = ', '.join(self.courses_in_progress)
        else:
            courses_in_progress = 'Нет таких курсов'

        if len(self.finished_courses):
            finished_courses = ', '.join(self.finished_courses)
        else:
            finished_courses = 'Нет таких курсов'

        return f'{super().__str__()}\n' \
               f'Средняя оценка за домашние задания: {self.get_avg_grade()}\n' \
               f'Курсы в процессе изучения: {courses_in_progress}\n' \
               f'Завершенные курсы: {finished_courses}'


class Mentor(Person):
    """Класс наставников"""
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course: str, grade: int):
        if isinstance(student, Student) and \
                course in self.courses_attached and \
                course in student.courses_in_progress:
            student.grades.setdefault(course, []).append(grade)
        else:
            raise NotImplementedError('Данному объекту нет возможности выставлять оценки!')

    def add_attached_course(self, course_name: str):
        if course_name not in self.courses_attached:
            self.courses_attached.append(course_name)
            print(f'\nКурс "{course_name}" добавлен преподавателю.')
        else:
            print('Такой курс уже есть у преподавателя!')

    def __str__(self):
        return f'\n{super().__str__()}'


class Lecturer(Mentor):
    """Класс лекторов"""
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def rate_hw(self, student, course: str, grade: int):
        raise NotImplementedError('Данному объекту нет возможности выставлять оценки!')

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.get_avg_grade() == other.get_avg_grade()
        else:
            return 'Нельзя сравнить объекты разных классов!'

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.get_avg_grade() != other.get_avg_grade()
        else:
            return 'Нельзя сравнить объекты разных классов!'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_avg_grade() < other.get_avg_grade()
        else:
            return 'Нельзя сравнить объекты разных классов!'

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.get_avg_grade() <= other.get_avg_grade()
        else:
            return 'Нельзя сравнить объекты разных классов!'

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_avg_grade() > other.get_avg_grade()
        else:
            return 'Нельзя сравнить объекты разных классов!'

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.get_avg_grade() >= other.get_avg_grade()
        else:
            return 'Нельзя сравнить объекты разных классов!'

    def __str__(self):
        return f'{super().__str__()}\n' \
               f'Средняя оценка за лекции: {self.get_avg_grade()}'

    def get_avg_grade(self):
        if len(self.grades.values()):
            grades = []
            for grade in self.grades.values():
                grades += grade
            return round(sum(grades) / len(grades), 1)
        else:
            return 0


class Reviewer(Mentor):
    """Класс проверяющих(ревьюверов)"""
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return f'{super().__str__()}'


def get_course_grades(students: Student, course_name: str) -> float:
    grades = []
    for student in students:
        if course_name in student.courses_in_progress:
            grades += student.grades[course_name]

        if len(grades) > 0:
            return sum(grades) / len(grades)
        else:
            return .0

def get_course_lectures_rating_avg(lecturers: Lecturer, course_name: str):
    pass


if __name__ == "__main__":
    student1 = Student('Ivan', 'Petrov', 'Male')
    student2 = Student('Maria', 'Ivanova', 'Female')

    lector1 = Lecturer('Petr', 'Ivanov')
    lector2 = Lecturer('Vlad', 'Smirnov')

    reviewer1 = Reviewer('Artem', 'Sidorov')
    reviewer2 = Reviewer('Damir', 'Petrov')

    student1.add_course('Python')
    student1.add_finish_course('C')
    student2.add_course('C++')
    student2.add_finish_course('Perl')
    student1.add_grade(lector1, 'Python', 5)
    student1.add_grade(lector1, 'Python', 9)
    student1.add_grade(lector2, 'Python', 3)

    lector1.add_attached_course('Python')
    lector2.add_attached_course('C++')

    reviewer1.courses_attached += ['Python']
    reviewer2.courses_attached += ['C++']

    reviewer1.rate_hw(student1, 'Python', 5)
    reviewer1.rate_hw(student1, 'Python', 7)
    reviewer1.rate_hw(student1, 'Python', 10)

    reviewer2.rate_hw(student2, 'C++', 4)
    reviewer2.rate_hw(student2, 'C++', 6)
    reviewer2.rate_hw(student2, 'C++', 9)

    student2.add_grade(lector1, 'C++', 4)
    student2.add_grade(lector2, 'C++', 5)
    student2.add_grade(lector2, 'C++', 7)

    print(student1)
    print(student2)
    print(lector1)
    print(lector2)
    print(reviewer1)
    print(reviewer2)
