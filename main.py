class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average_hw()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def _average_hw(self):
        av = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 1)
        return av

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент')
            return
        return self._average_hw() < other._average_hw()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


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
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_lecture()}'
        return res

    def _average_lecture(self):
        av_lect = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 1)
        return av_lect

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор')
            return
        return self._average_lecture() < other._average_lecture()


some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

any_student = Student('John', 'doe', 'male')
any_student.courses_in_progress += ['Python']
any_student.finished_courses += ['Введение в программирование']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

any_reviewer = Reviewer('John', 'Smith')
any_reviewer.courses_attached += ['Python']

some_reviewer.rate_hw(some_student, 'Python', 9.6)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)

any_reviewer.rate_hw(any_student, 'Python', 5)
any_reviewer.rate_hw(any_student, 'Python', 6)
any_reviewer.rate_hw(any_student, 'Python', 7)

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

any_lecturer = Lecturer('Kot', 'Matroskin')
any_lecturer.courses_attached += ['Python']

some_student.rate_lecture(some_lecturer, 'Python', 10)
some_student.rate_lecture(some_lecturer, 'Python', 9)
some_student.rate_lecture(some_lecturer, 'Python', 10)
some_student.rate_lecture(some_lecturer, 'Python', 10)

any_student.rate_lecture(any_lecturer, 'Python', 10)
any_student.rate_lecture(any_lecturer, 'Python', 9)
any_student.rate_lecture(any_lecturer, 'Python', 10)

students_list = [some_student, any_student]


def average_hw_for_students(students_list, course):
    count = 0
    sum_rate = 0
    for i in students_list:
        for j in i.grades[course]:
            sum_rate += j
            count += 1
    return round(sum_rate / count, 1)


lecturers_list = [some_lecturer, any_lecturer]


def average_lecture_for_lecturer(lecturers_list, course):
    count = 0
    sum_rate = 0
    for i in lecturers_list:
        for j in i.grades[course]:
            sum_rate += j
            count += 1
    return round(sum_rate / count, 1)


print(some_student.grades)
print(any_student.grades)
print(some_lecturer.grades)
print(any_lecturer.grades)
print(some_reviewer)
print(some_lecturer)
print(some_student)
print(any_student < some_student)
print(any_lecturer > some_lecturer)
print(average_hw_for_students(students_list, 'Python'))
print(average_hw_for_students(lecturers_list, 'Python'))
