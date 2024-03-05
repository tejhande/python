while True:
    try:

        a = input("Enter First Number: \n\t")
        b = input("Enter Second Number: \n\t")
        a = int(a)
        b = int(b)
        print("Addition Of", a , "And" , b , "Is:" ,a + b)
    except Exception as e:
        print(e) #1
        break