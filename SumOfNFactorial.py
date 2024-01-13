num = int(input("Enter Number To Find Factorial: \n\t"))
# factorial = 1
# for i in range(1, num+1):
#     factorial = factorial* i 
# print(f"The Factorial Of", num, "Is : ", factorial)
    
sum = 1
for i in range(1, num):
    sum = sum + sum
print(f" The Sum Of First ", num, " Numbers Is : ", sum)