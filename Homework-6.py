class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self.__dict__)
        self.average_raiting = 0

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lesson(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in \
                self.courses_in_progress:
            lecturer.grades.append(grade)
            lecturer.average_raiting = round(sum(lecturer.grades) / len(lecturer.grades), 2)

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname} \n'
                f'Средняя оценка за домашние задания: {self.average_raiting} \n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
                f'Завершенный курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Это не студент")
            return
        return self.average_raiting < other.average_raiting


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = []
        lecturers_list.append(self.__dict__)
        self.average_raiting = 0

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname} \n'
                f'Средняя оценка за лекции: {self.average_raiting}')

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Это не лектор")
            return
        return self.average_raiting < other.average_raiting


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname}')

    def rate_hw(self, student, course, grade):
        super().rate_hw(student, course, grade)
        sum_hw = 0
        counter = 0
        for key, value in student.grades.items():
            sum_hw += sum(value) / len(value)
            counter += 1
        student.average_raiting = round(sum_hw / counter, 2)


students_list = []

def average_grade_stud(students, courses):
    sum_gs = 0
    counter = 0
    for student in students:
        for key, value in student["grades"].items():
            if courses in key:
                sum_gs += sum(value) / len(value)
                counter += 1
    return round(sum_gs / counter, 2)

lecturers_list = []

def average_grade_lect(lecturers, courses):
    sum_gl = 0
    counter = 0
    for lecturer in lecturers:
        if courses in lecturer["courses_attached"]:
                sum_gl += sum(lecturer["grades"]) / len(lecturer["grades"])
                counter += 1
    return round(sum_gl / counter, 2)


student_Dmitry = Student("Дмитрий", "Никитин", "М")
student_Dmitry.courses_in_progress += ["Python", "Java"]
student_Dmitry.finished_courses += ["Git"]

student_Ekaterina = Student("Екатерина", "Никитина", "ж")
student_Ekaterina.courses_in_progress += ["Java", "Python"]
student_Ekaterina.finished_courses += ["Git"]

lecturer_Peter = Lecturer("Петр", "Первый")
lecturer_Peter.courses_attached += ["Python"]

lecturer_Ivan = Lecturer("Иван", "Грозный")
lecturer_Ivan.courses_attached += ["Java"]

reviewer_Alexandr = Reviewer("Александр", "Невский")
reviewer_Alexandr.courses_attached += ["Java"]

reviewer_Vasiliy = Reviewer("Василий", "Учаев")
reviewer_Vasiliy.courses_attached += ["Python"]


reviewer_Alexandr.rate_hw(student_Ekaterina, "Java", 8)
reviewer_Alexandr.rate_hw(student_Ekaterina, "Java", 3)
reviewer_Alexandr.rate_hw(student_Ekaterina, "Java", 5)
reviewer_Vasiliy.rate_hw(student_Ekaterina, "Python", 10)

reviewer_Vasiliy.rate_hw(student_Dmitry, "Python", 4)
reviewer_Vasiliy.rate_hw(student_Dmitry, "Python", 6)
reviewer_Vasiliy.rate_hw(student_Dmitry, "Python", 7)
reviewer_Alexandr.rate_hw(student_Dmitry, "Java", 5)

student_Dmitry.rate_lesson(lecturer_Peter, "Python", 10)
student_Dmitry.rate_lesson(lecturer_Peter, "Python", 10)
student_Dmitry.rate_lesson(lecturer_Peter, "Python", 9)
student_Dmitry.rate_lesson(lecturer_Ivan, "Java", 9)

student_Ekaterina.rate_lesson(lecturer_Ivan, "Java", 8)
student_Ekaterina.rate_lesson(lecturer_Ivan, "Java", 8)
student_Ekaterina.rate_lesson(lecturer_Ivan, "Java", 7)
student_Ekaterina.rate_lesson(lecturer_Peter, "Python", 10)


print(student_Ekaterina.grades)
print(student_Dmitry.grades)
print()
print(lecturer_Peter.grades)
print(lecturer_Ivan.grades)
print()
print(lecturer_Ivan)
print()
print(lecturer_Peter)
print()
print(reviewer_Vasiliy)
print()
print(reviewer_Alexandr)
print()
print(student_Dmitry)
print()
print(student_Ekaterina)
print()
print(lecturer_Peter < lecturer_Ivan)
print(lecturer_Peter > lecturer_Ivan)
print()
print(student_Dmitry < student_Ekaterina)
print(student_Dmitry > student_Ekaterina)
print()
print(f'Средняя оценка за домашние задания по курсу Python для всех студентов: '
      f'{average_grade_stud(students_list, "Python")}')
print()
print(f'Средняя оценка за лекции по курсу Python для всех лекторов: {average_grade_lect(lecturers_list, "Python")}')
print()
print(f'Средняя оценка за домашние задания по курсу Java для всех студентов: '
      f'{average_grade_stud(students_list, "Java")}')
print()
print(f'Средняя оценка за лекции по курсу Java для всех лекторов: {average_grade_lect(lecturers_list, "Java")}')
