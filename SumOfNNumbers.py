num = int(input("Enter Number To Find Sum : \n\n\t"))

def factorial_iter(num):
    sum = 0
    print("\n\t")
    for i in range(num):
        sum = sum + (i+1)
    return sum

def factorial_recursive(num):
    if num==1 or num==0:
        return 1 
    return num + factorial_iter(num-1)


print(factorial_recursive(num), " Is The Sum Of First", num, "Natural Numbers")