class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Student(Person):
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
            print(f'Курс "{course_name}" добавлен в изучаемые.')
        else:
            print('Такой курс уже есть!')

    def add_finish_course(self, course_name: str):
        if course_name in self.courses_in_progress:
            self.courses_in_progress.remove(course_name)
            self.finished_courses.append(course_name)
        else:
            self.finished_courses.append(course_name)
        print(f'Курс "{course_name}" добавлен в завершенные.')

    def add_grade(self, course_name: str, grade: int):
        if course_name in self.courses_in_progress and \
                isinstance(grade, int) and 1 <= grade <= 10:
            if course_name in self.grades:
                self.grades[course_name].append(grade)
            else:
                self.grades[course_name] = [grade]
            print(f'Для курса "{course_name}" добавлена оценка {grade}.')
        else:
            print('Указали некорректную оценку или такого курса нет!\n')

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
               f'Завершенные курсы: {finished_courses}\n'


class Mentor(Person):
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student: Student, course: str, grade: int):
        if isinstance(student, Student) and \
                course in self.courses_attached and \
                course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'{super().__str__()}'


class Lecturer(Mentor):
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

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
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return f'{super().__str__()}\n'


if __name__ == "__main__":
    best_student = Student('Ruoy', 'Eman', 'your_gender')
    best_student.add_course('Python')
    best_student.add_course('Python2')
    best_student.add_grade('Python', 5)
    best_student.add_grade('Python', 7)
    best_student.add_grade('Python2', 3)
    best_student.add_finish_course('Python3')
    print(best_student)


    best_student2 = Student('Ruoy2', 'Eman2', 'your_gender')
    best_student2.courses_in_progress += ['Python']
    print(best_student2)

    cool_mentor = Lecturer('Some', 'Buddy')
    cool_mentor.courses_attached += ['Python']
    print(cool_mentor)

    # print(best_student == cool_mentor)

    cool_mentor.rate_hw(best_student, 'Python', 10)
    cool_mentor.rate_hw(best_student, 'Python', 10)
    cool_mentor.rate_hw(best_student, 'Python', 10)

    print(best_student.grades)
    print(cool_mentor.courses_attached)
