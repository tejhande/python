def farh(cel):
    return ((cel * 9/5)) + 32 

c = int(input("Enter temperature in Celcius: \n\t"))
f = farh(c)
print("Fahrenheit Temrature is: "+ str(f))