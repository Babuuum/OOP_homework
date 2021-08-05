class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_rating(self):
        crutch = 0
        crutch_2 = []
        for search in self.grades:
            for search_2 in self.grades[search]:
                crutch += search_2
                crutch_2.append(search_2)
        return float(crutch / len(crutch_2))

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_rating() < other.average_rating()
        else:
            return "Ошибка"

    def rating_comparison(self, student):
        if isinstance(student, Student):
            if student < self:
                return f"{self.name} {self.surname}"
            elif self < student:
                return f"{student.name} {student.surname}"
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

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_rating() < other.average_rating()
        else:
            return "Ошибка"

    def rating_comparison(self, lecturer):
        if isinstance(lecturer, Lecturer):
            if lecturer < self:
                return f"{self.name} {self.surname}"
            elif self < lecturer:
                return f"{lecturer.name} {lecturer.surname}"
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


some_reviewer = Reviewer("Mr", "Check")

some_lecturer = Lecturer("Mr", "Teacher")
some_lecturer.grades = {"Python": [3, 4, 5, 6], "Git": [4]}

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.finished_courses = ["Введение в программирование"]
some_student.courses_in_progress = ["Python", "Git"]
some_student.grades = {"Python": [3, 4, 5, 6], "Git": [4]}

print(some_reviewer)
print(some_lecturer)
print(some_student)
