# Get Marks Of The Student From User And Store It As An Array
marks = []
n = int(input("Enter No Of Students You Want To Store Marks: \n\t"))
for i in range(0,n):
    print("Enter Marks Of Student No.", i+1, ":\n\t\t")
    element = int(input())
    marks.append(element)
print("Marks Entered:", marks)

# Define Insertation Short

def Insertation_Sort(marks):
    for i in range(1,n):
        j = i
        while marks[j - 1] > marks[j] and j > 0:
            marks[j], marks[j - 1] = marks[j - 1], marks[j]
            j -= 1
    print("Marks After Insertation Sorting:", marks)

# Define Shell Sort

def Shell_Sort(marks):
    n = len(marks)
    for i in range(0, n):
        for j in range(0, n -i -1):
            if marks[j + 1]> marks[j]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]
    print("Marks After Shell Sorting:")
    for i in range(len(marks)):
        print(marks[i])

# Ask User What He Wants To Do
flag = 1
while flag == 1:
    print("***************MENU***************")
    print("1: Insertation Sort")
    print("2: Shell Sort")
    print("3: Exit")
    d = (input("Enter Choice(1/2/3):\n\t"))
    if d == "1":
        Insertation_Sort(marks)
        # a = ("\n\tDo You Want To Perform Shell Sort?(Y/N): \n\t")
        # if a == "Y":
        #     Shell_Sort(marks)
        # else:
        #     print("Thanks For Using Our Program")
        
    elif d == "2":
        Shell_Sort(marks)
        # a = ("\n\tDo You Want To Perform Insertation Sort?(Y/N): \n\t")
        # if a == "Y":
        #     Insertation_Sort(marks)
        # else:
        #     print("Thanks For Using Our Program")
        
    elif d == "3":
        print("Thanks For Using Our Program")
        flag = 0
    else:
        print("Invalid Choice")