marks = []
n = int(input("Enter No Of Students You Want To Store: \n\t"))
for i in range(0,n):
    print("Enter Marks Of Student No. ",  i+1, ":\n\t")
    element = int(input())
    marks.append(element)
print("Marks Entered For", n , "Students Are:", marks)

def Shell_Sort(marks):
    n = len(marks)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if marks[j] > marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]
    print("Marks of students after performing Shell Sort on the list :")
    for i in range(len(marks)):
        print(marks[i])

d = input("You Want To Sort Marks With Shell Sort(Type Y/N): \n\t")
if d == "Y":
    Shell_Sort(marks)
else:
    print("Thanks For Using Our Program !")