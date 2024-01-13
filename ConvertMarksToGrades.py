marks = int(input("Enter Your Marks:\n\t"))
if marks>=90:
    grade = "EX"
elif marks>=80:
    grade = "A"
elif marks>=70:
    grade = "B" 
elif marks>=60:
    grade = "C"
elif marks>=50:
    grade = "D"
else:
    grade = "Your Failed Padhai Lihkai Karo IAS YAS bano aur Desh ko Sambhalo"
print("Your Grade Is: \n\t" , grade)