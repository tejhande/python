# n! = 1 * 2 * 3 * 4 * 5 * 6 *. . . . . . *n
# n! = [1 * 2 * 3 * 4 * 5 * 6 *. . . . . . *n-1] *n 
# n! = (n-1)! * n


# num = int(input("Enter Number To Find Factorial: \n\t"))
# product = 1
# print("\n\t")
# for i in range(num):
#     product = product * (i+1)
# print(product)

num = int(input("Enter Number To Find Factorial: \n\n\t"))
def factorial_iter(num):
    product = 1
    print("\n\t")
    for i in range(num):
        product = product * (i+1)
    return product

def factorial_recursive(num):
    if num==1 or num==0:
        return 1 
    return num * factorial_iter(num-1)


print(factorial_recursive(num), " Is The factorial Of ", num)
# print(factorial_iter(num))