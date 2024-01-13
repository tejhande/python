def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    result = 1
    for i in range(int(b)):
        result = result * a
    return result

def logarithm(a, b):
    result = 0
    while a <= b:
        a = a * 10
        result = result + 1
    return result

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Logarithm")
print("7. Exit")

choice = int(input("Enter choice (1/2/3/4/5/6/7): "))

if choice == 7:
    print("Exiting calculator...")
    exit()

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == 4:
    print(num1, "/", num2, "=", divide(num1, num2))

elif choice == 5:
    print(num1, "**", num2, "=", power(num1, num2))

elif choice == 6:
    print("log", num1, "of", num2, "=", logarithm(num1, num2))

else:
    print("Invalid input")
