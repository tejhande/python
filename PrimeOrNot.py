num = int(input("Enter Number To Find It Is Prime Or Not: \n\t"))
prime = True
for i in range(2, num):
    if(num%i == 0):
        prime = False
        break
if(num%i == 0):
    print(i, " Is The First Number Which Completely Divides", num)
if prime:
    print(num, "Is A Prime Number")
else:
    print(num, "Is Not A Prime Number")