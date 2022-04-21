class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades={}


    def add_finished_courses(self, course_name):
        print (course_name,self.courses_in_progress)

        if course_name not in self.courses_in_progress:

            print("Студент не изучает данный курс")
            return
        self.courses_in_progress.remove(course_name)
        return self.finished_courses.append(course_name)

    def add_courses_in_progress(self, course_name):
        self.courses_in_progress.append(course_name)

    def add_grades(self, lecturer, course, grades):

        if course not in lecturer.attached_courses:
            print("Преподаватель не ведет данный курс")
            return

        if course not in self.courses_in_progress:
            print("Студент не обучается на данном курсе")
            return

        if grades < 1 or grades > 10:
            print("Оценки вводятся по 10 бальной шкале")
            return
        if course not in lecturer.grades.keys():
            lecturer.grades[course] = []
        lecturer.grades[course].append(grades)

        print(f"Баллы за лекцию по: {course} - {lecturer.grades[course]}")

    # def average(self):
    #     # Средняя по каждому предмету
    #     for k in self.grades.keys():
    #         s = sum(self.grades[k]) / len(self.grades[k])
    #         self.average_grades[k] = s
    #     return self.average_grades

    def average(self):
            #Средняя по каждому предмету
        for k, v in self.grades.items():
            s = (sum(v)) / len(v)
            self.average_grades[k] = s
        return self.average_grades
        print(f'средний балл: {self.average_grades}')



    def __str__(self):
        return f"Student:\n Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашнее задание: {self.average_grades}\n Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n Завершенные курсы: {', '.join(self.finished_courses)}\n"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.attached_courses = []
        self.average_for_lecture = {}

    def add_courses(self, courses):
        self.attached_courses.append(courses)



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_for_lecture = {}

    def average(self):

        for k, v in self.grades.items():
            s = (sum(v)) / len(v)
            self.average_for_lecture[k] = s
        return self.average_for_lecture
        # print(f' средний балл: {self.average_for_lecture}')
    def __str__(self):
        return f"Lecturer:\n Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self.average_for_lecture }\n"

class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def add_grades(self, student, course, grades):


        if course not in self.attached_courses:
            print("Преподаватель не ведет данный курс")
            return

        if course not in [i for i in student.courses_in_progress]:
            print("Студент не обучается на данном курсе")
            return

        if grades < 1 or grades > 10:
            print("Оценки вводятся по 10 бальной шкале")
            return
        if course not in student.grades.keys():
            student.grades[course] = []
        student.grades[course].append(grades)

        print(f"Баллы за курс по: {course} - {student.grades[course]}")

    def __str__(self):
        return f"Reviewer:\n Имя: {self.name}\n Фамилия: {self.surname}\n "



def average_students(list_name,list_courses):

    for g in list_courses:
        summa=0
        kol_vo=0
        for i in list_name:
            if g not in i.grades.keys():
                continue
            for z in i.grades[g]:
                summa= summa+z
                kol_vo+=1
        if summa==0:
            print(f'По курсу {g} средняя оценка 0')
            continue
        print(f'За домашнии задания по курсу {g} средний балл {summa/kol_vo}')

def average_lecturer(list_name,list_courses):

    for g in list_courses:
        summa=0
        kol_vo=0
        for i in list_name:
            if g not in i.grades.keys():
                continue
            for z in i.grades[g]:
                summa= summa+z
                kol_vo+=1
        if summa==0:
            print(f'По курсу {g} средняя оценка 0')
            continue
        print(f'За лекции по курсу {g} средний балл {summa/kol_vo} ')

s1 = Student("Иван ", "Иванов", "М")
s1.add_courses_in_progress("Python")
s1.add_courses_in_progress("Git")
s1.add_courses_in_progress("Введение в програмирование")
s1.add_finished_courses('Введение в програмирование')

s2= Student("Анна", "Петрова", "Ж")
s2.add_courses_in_progress("Git")
s2.add_courses_in_progress("Python")
s2.add_courses_in_progress("Введение в програмирование")
s2.add_finished_courses('Введение в програмирование')

r1=Reviewer("Федор", "Достоевский")
r2=Reviewer("Александр", "Белов")
l1 = Lecturer("Дмитрий", "Ленский")
l2= Lecturer("Михаил", "Шорохов")

l1.add_courses("Python")
l1.add_courses("Git")
l2.add_courses("Python")

s1.add_grades(l1, "Python", 3)
s1.add_grades(l1, "Python", 5)
s1.add_grades(l1, "Git", 8)
s1.add_grades(l1, "Git", 9)
s2.add_grades(l2, "Python", 7)
s2.add_grades(l2, "Python", 1)
s2.add_grades(l2, "Python", 3)

r1.add_courses("Python")
r1.add_courses("Git")
r2.add_courses("Python")
r2.add_courses("Git")

r1.add_grades(s1, "Python", 3)
r1.add_grades(s1, "Python", 4)
r1.add_grades(s1, "Python", 5)
r1.add_grades(s1, "Python", 2)
r1.add_grades(s1, "Git", 5)
r1.add_grades(s1, "Git", 5)
r1.add_grades(s1, "Python", 8)
r2.add_grades(s2, "Python", 7)
r2.add_grades(s2, "Git", 9)
r2.add_grades(s2, "Git", 6)
r2.add_grades(s2, "Python", 3)
r2.add_grades(s2, "Python", 9)
s1.average()
s2.average()
l1.average()
l2.average()
print("----------------------------------------------------------------")
print(s1)
print(s2)
average_students([s1,s2],['Git','Python'])
print(l1)
print(l2)
average_lecturer([l1,l2],['Git','Python'])
print(r1)
print(r2)

cvnvh