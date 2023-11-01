class Person:
    __name = "name"
    __age = 18

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 2:
            self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age >= 16:
            self.__age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Teacher(Person):
    def __init__(self, name, age, institution, experience):
        super().__init__(name, age)
        self.institution = institution
        self.experience = experience

    def work(self):
        print(f"{self.name} works in {self.institution} for {self.experience} years.")


Anna = Teacher("Anna", 40, "university", 12)
Anna.show_info()
Anna.work()


class Student(Person):
    def __init__(self, name, age, course, score):
        super().__init__(name, age)
        self.course = course
        self.score = score

    def study(self):
        print(f"{self.name} studying on the {self.course} course with middle score {self.score}.")


Peter = Student("Peter", 19, 3, 4)
Peter.show_info()
Peter.study()


class Academy:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
        self.subjects = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def show_info(self):
        print(f"Name: {self.name}, teachers: {self.teachers}, students: {self.students}.")


academy = Academy("NTU")
academy.add_teacher("Tom")
academy.add_student(["Ann", "Jack", "Peter"])
academy.add_subject("Maths")
academy.show_info()


class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_info(self):
        print(f"Name: {self.name}, teachers: {self.teacher}, students: {self.students}.")


chemistry = Subject("chemistry", "Ivan")
chemistry.add_student(["Ann", "Jack", "Peter"])
chemistry.show_info()


class Examination(Subject):
    def __init__(self, name, teacher, date):
        super().__init__(name, teacher)
        self.date = date

    def happen(self):
        print(f"Name: {self.name}, teacher: {self.teacher}, date: {self.date}.")


Maths = Examination("Maths", "John", "25/11/2023")
Maths.happen()
