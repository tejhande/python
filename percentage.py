# percentage = int(input("Enter Percentage: "))
# if percentage > 60:
#     print("First Class")
# elif 50 <= percentage < 60:
#     print("Second Class")
# elif 40 <= percentage < 50:
#     print("Pass Class")
# else:
#     print("You're Fail")
# print(f"You Got {percentage} Percentage")

while True:
    try:
        percentage = float(input("Enter Percentage: "))
        if percentage > 60:
            print("First Class")
        elif 50 <= percentage < 60:
            print("Second Class")
        elif 40 <= percentage < 50:
            print("Pass Class")
        else:
            print("You're Fail")
        print(f"You Got {percentage} Percentage")
    except ValueError:
        print("Invalid input............")