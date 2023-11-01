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
    __name = "name"

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def show_info(self):
        print(f"Name: {self.name}")


class Subject(Academy):
    def __init__(self, name, hours, materials):
        super().__init__(name)
        self.hours = hours
        self.materials = materials

    def lesson(self):
        print(f"This week we have {self.hours} hours of {self.name} and use {self.materials}.")


English = Subject("English", 6, "workbooks")
English.show_info()
English.lesson()


class Examination(Subject):
    def __init__(self, name, hours, materials, date):
        super().__init__(name, hours, materials)
        self.date = date

    def happen(self):
        print(f"{self.name} exam will be happen {self.date} and will be continue for {self.hours} hours. "
              f"You can use {self.materials} materials.")


Maths = Examination("Maths", 2, "no", "25/11/2023")
Maths.show_info()
Maths.happen()
