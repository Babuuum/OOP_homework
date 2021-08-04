class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_rating_course(self, course):
        crutch = 0
        crutch_2 = []
        for search in self.grades[course]:
            crutch += search
            crutch_2.append(search)
        return float(crutch / len(crutch_2))

    def average_rating(self):
        crutch = 0
        crutch_2 = []
        for search in self.grades:
            for search_2 in self.grades[search]:
                crutch += search_2
                crutch_2.append(search_2)
        return float(crutch / len(crutch_2))

    def rating_comparison(self, student):
        if isinstance(student, Student):
            if self.average_rating() > student.average_rating():
                return f"{self.name}{self.surname}"
            elif self.average_rating() < student.average_rating():
                return f"{student.name}{student.surname}"
            else:
                return "средний бал равен"
        else:
            return "ошибка"

    def __str__(self):
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за лекции: {self.average_rating()} \n" \
               f"Курсы в процессе изучения: {str(self.courses_in_progress)[1:-1]} \n" \
               f"Завершенные курсы: {str(self.finished_courses)[1:-1]}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rating(self):
        crutch = 0
        crutch_2 = []
        for search in self.grades:
            for search_2 in self.grades[search]:
                crutch += search_2
                crutch_2.append(search_2)
        return float(crutch / len(crutch_2))

    def average_rating_course(self, course):
        crutch = 0
        crutch_2 = []
        for search in self.grades[course]:
            crutch += search
            crutch_2.append(search)
        return float(crutch / len(crutch_2))

    def rating_comparison(self, lecturer):
        if isinstance(lecturer, Lecturer):
            if self.average_rating() > lecturer.average_rating():
                return f"{self.name}{self.surname}"
            elif self.average_rating() < lecturer.average_rating():
                return f"{lecturer.name}{lecturer.surname}"
            else:
                return "средний бал равен"
        else:
            return "ошибка"

    def __str__(self):
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за лекции: {self.average_rating()}"

    def rate_class(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in self.grades:
                self.grades[course] += [grade]
            else:
                self.grades[course] = [grade]
        else:
            return 'Ошибка'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname}"


def all_students_average_rating(students, course):
    crutch = []
    for search in students:
        if isinstance(search, Student):
            crutch.append(search.average_rating_course(course))
        else:
            return "Ошибка"
    crutch.sort()
    return crutch[-1]


def all_lecturer_average_rating(lecturers, course):
    crutch = []
    for search in lecturers:
        if isinstance(search, Lecturer):
            crutch.append(search.average_rating_course(course))
        else:
            return "Ошибка"
    crutch.sort()
    return crutch[-1]


first_reviewer = Reviewer("Mr", "Check")

second_reviewer = Reviewer("Miss", "Check")

first_lecturer = Lecturer("Mr", "Teacher")
first_lecturer.grades = {"Python": [3, 4, 5, 6], "Git": [4]}

second_lecturer = Lecturer("Miss", "Teacher")
second_lecturer.grades = {"Python": [7, 8, 10, 10], "Git": [9]}

first_student = Student('Ruoy', 'Eman', 'your_gender')
first_student.finished_courses = ["Введение в программирование"]
first_student.courses_in_progress = ["Python", "Git"]
first_student.grades = {"Python": [3, 4, 5, 6], "Git": [4]}

second_student = Student("Hidetaka", "Miyazaki", "your_gender")
second_student.finished_courses = ["Введение в программирование"]
second_student.courses_in_progress = ["Python", "Git"]
second_student.grades = {"Python": [1, 1, 1, 0], "Git": [2]}

first_lecturer.rate_class(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 10)

students_list = [first_student, second_student]
lecturer_list = [first_lecturer, second_lecturer]


print(first_lecturer.grades)
print(first_student.grades)
print(first_student)
print(first_lecturer)
print(first_reviewer)
print(first_student.rating_comparison(second_student))
print(first_lecturer.rating_comparison(second_lecturer))
print(all_students_average_rating(students_list, "Python"))
print(all_lecturer_average_rating(lecturer_list, "Python"))