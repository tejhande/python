marks = []
n = int(input("E N O S :   "))
for i in range(0,n):
    print("E M F ", n, ": \n\t")
    element = int(input())
    marks.append(element)
print(marks)

def Shell_Sort(marks):
    n = len(marks)
    for i in range(0, n):
        for j in range(0, n -i -1):
            if marks[j + 1]> marks[j]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]
    print("Marks After Sorting:")
    for i in range(len(marks)):
        print(marks[i])

    
d = input("Y/N: ")
if d == "Y":
    Shell_Sort(marks)
else:
    print("Thanks")

