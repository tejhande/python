class Person:
    def __init__(self, FirstName, LastName):
        self.FirstName = FirstName
        self.LastName = LastName

    def printname(self):
        print(self.FirstName, self.LastName)

p1 = Person("Tony", "Stark")
p1.printname()

class Student (Person):
    pass

stud = Student("Varun", "Dhavan")
stud.printname()
