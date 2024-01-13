def centimeter(inch):
    return inch * 2.54

c = int(input("Enter Measurment In INCH: \n\t"))
i = centimeter(c)
print(c, "INCH In CENTIMETER Is : "+ str(i))