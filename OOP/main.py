class Student:

    def __init__(self, name: str, surname: str, gender: str) -> None:
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []

    def __str__(self) -> str:
        return self.surname + ' ' + self.name


if __name__ == "__main__":
    st1 = Student(name='Denis', surname='Tsybin', gender='Male')
    st1.finished_courses.append('test1')
    st2 = Student(name='Ivan', surname='Petrov', gender='Male')
    print(st1, st1.finished_courses)
    print(st2, st2.finished_courses)
