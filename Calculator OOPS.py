'''
class Calculator:
    def __init__(self,num):
        self.number = num
    def square(self):
        print(f"Square of {self.number} is {self.number **2}")
    def squareRoot(self):
        print(f"Square Root Of {self.number} is {self.number **0.5}")
    def cube(self):
        print(f"Cube of {self.number} is {self.number **3}")
# number = int(input("Enter A Number To Calculate: "))
a = Calculator(2)
a.square()
a.squareRoot()
a.cube()
'''

'''
class Calculator:
    def __init__(self,num):
        self.number = num 
    def square(self):
        print(self.number **2)
    def squareRoot(self):
        print(self.number **0.5)
    def cube(self):
        print(self.number **3)
number = int(input())
a = Calculator(number)
a.square()
a.squareRoot()
a.cube()
'''