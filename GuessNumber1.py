# import random
# num = random.randint(1,100)
# i = 1
# while(i<=num):
#     (print("Attempt:- ",i))
#     i = i+1

# num = int(input("Enter a Number:- "))
# if num%2 == 0:
#     print("Number is Not prime")


# Input the number you want to check.
# Check if the number is less than 2. If so, return false.
# Check if the number is equal to 2. If so, return true.
# Check if the number is even (i.e., divisible by 2). If so, return false.
# Starting from 3, check all odd numbers up to the square root of the input number.
# If any of these odd numbers divides the input number without leaving a remainder, return false.
# If no odd number divides the input number without leaving a remainder, return true.

n=int(input)
def is_prime(n):
    if n < 2:
        print(n, "is not a prime number.")
        return False
    elif n == 2:
        print(n, "is a prime number.")
        return True
    elif n % 2 == 0:
        print(n, "is not a prime number.")
        return False
    else:
        for d in range(3, n, 2):
            if n % d == 0:
                print(n, "is not a prime number (divisible by", d, "with n % d =", n % d, ").")
                return False
        print(n, "is a prime number.")
        return True
is_prime(n)





