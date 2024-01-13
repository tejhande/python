marks = []
n = int(input("Enter No Of Students You Want To Store: \n\t"))
for i in range(0,n):
    print("Enter Marks Of Student No. ",  i+1, ":\n\t")
    element = int(input())
    marks.append(element)
print("Marks Entered For", n , "Students Are:", marks)

def Insertation_Sort(marks):
    for i in range(1,n):
        j = i
        while marks[j - 1] > marks[j] and j > 0:
            marks[j], marks[j - 1] = marks[j - 1], marks[j]
            j -= 1
    print("Marks After Sorting With Insertation Sort", marks)

d = input("You Want To Sort Marks With Insertation Sort(Type Y/N): \n\t")
if d == "Y":
    Insertation_Sort(marks)
else:
    print("Thanks For Using Our Program !")