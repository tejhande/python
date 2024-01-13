'''num1 = int(input("Enter Number: \n\t"))
num2 = int(input("Enter Number: \n\t"))
num3 = int(input("Enter Number: \n\t"))
def maximum(num1, num2, num3):
    if (num1 > num2):
        if (num1 > num3):
            return num1
        else:
            return num3
    else:
        if (num2 > num3):
            return  num2 
        else:
            return num3
a = maximum(num1, num2, num3)
print("The Maximum Number Is: " + str(a))
'''

# // Find greatest number in given 3 numbers? 

a = int(input("To make perfect sqaure:- "))
def square(a):
    print("The square of number is: ", a*a)
square(a)
