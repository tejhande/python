# a = int(input("Enter Number: \n\t\t"))
# print(a)
# if(a>30):
#     print("The Value Of", a, "Is Greater Than 30")
# elif(a>7):
#     print("The Value Of", a, "Is Greater Than 7")
# else:
#     print("The Value Of", a, "Is not Greater Than 30 or 7")
# print("Done")


a = int(input("Enter First Number: \n\t"))
b = int(input("Enter Second Number: \n\t"))
c = int(input("Enter Third Number: \n\t"))

def Max(a,b,c):
    if (a > b):
        if (a>c):
            return a
        else:
            return c
    elif (b>c):
        return b
    else:
            return c

m = Max(a,b,c)
print(m, "Is The Greatest Number Among", a, b, c)