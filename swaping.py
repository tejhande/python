while True:
    try:
        a = int(input("Enter 1st Number:-"))
        break
    except ValueError:
        print("Invalid Input......")
while True:
    try:
        b = int(input("Enter 2nd Number:-"))
        break
    except ValueError:
        print("Invalid Input......")
def swap(x,y):
#1
    # temp = x
    # x = y           
    # y = temp

#2
    # x = x+y
    # y = x-y
    # x = x-y

#3
    # x = x ^ y
    # y = x ^ y
    # x = x ^ y

#4
    a = x^y
    x = a
    y = a
    x = a
    print("a =",x,"b =",y)
    exit
    print("Done")
            
            
print("a =",a,"b =",b)
swap(a,b)





x = int(input("Enter the value of 'x': "))
y = int(input("Enter the value of 'y': "))

print("Before swapping: x =", x, ", y =", y)
# a = x^y
x = x^y
y = x^y
x = x^y

print("After swapping: x =", x, ", y =", y)
