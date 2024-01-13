# a = input("Enter Your Name: ")
# b = input("Enter Your Mobile Number: ")
# b = int(b) # Convert b to an Integer
# c = input("Enter Your Email Address: ")
# d = input("Enter Your Password: ")
# print(a)
# print(b)
# print(c)
# print(d)    

while True:
    try:
        a = int(input("Enter Mobile Number: "))
    except ValueError:
        print('Invalid Input')
        break
while True:
    try:
        b = str(input("Enter Email Id: "))
    except ValueError:
        print("Value Error") 
    break
while True:
    try:
        c = str(input("Enter Name: "))
    except ValueError:
        print("Value Error")
    break
while True:
    try:
        d = input("Enter Password: ")
    except ValueError:
        print("Value Error")
    break
while True:
    try:
        e = int(input("Enter Mobile Number: "))
    except ValueError:
        print("Value Error")
    break
print(a,b,c,d)
