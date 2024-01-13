rules = ("Game Rules:\t 1] Gun(g) > Snake(s)\n\t\t 2] Snake(s) > Water(w)\n\t\t 3] Water(w) > Gun(g)")
Dev = ("Tejas Hande\n 8600828734 \n INSTAGRAM ID:- tejashande0 \n Email:- tejasamolhande@gmail.com \n WhatsApp:- wa.me/918600828734")
print("Enter 1 To Play")
print("Enter 2 For Rules")
print("Enter 3 To Know About Devloper")
print("Enter 4 To Exit ")
while True:
    ans = int(input("Enter Option Number: \n\t"))
    if ans == 1:
        while True:
            a1 = input("Enter First Player Name: \n\t")
            if a1.replace(" ", "").isalpha():
                break
            else:
                print("Invalid Input....")
        while True:
            b1 = str(input("Enter Second Player Name: \n\t"))
            if b1.replace(" ", "").isalpha():
                break
            else:
                print("Invalid Input....")  
        def gameWin(a1,b1):
            if a == b:
                return None
            elif a == 's':
                if b == 'w':
                    return False
                elif b == 'g':
                    return True
            elif a == 'w':
                if b == 'g':
                    return False
                elif b == 's':
                    return True
            elif a == 'g':
                if b == 's':
                    return False
                elif b == 'w':
                    return True
        while True:
            a = input(f"{a1}'s Turn : Snake(s) Water(w) or Gun(g)?\n\t")
            if a.replace(" ", "").isalpha():
                break
            else:
                print("Invalid Input....")
        while True:
            b = str(input(f"{b1}'s Turn : Snake(s) Water(w) or Gun(g)?\n\t"))
            if a.replace(" ", "").isalpha():
                break
            else:
                print("Invalid Input....")
        c = gameWin(a, b)
        print(f"{a1} Choose :\t {a}")
        print(f"{b1} Choose :\t {b}")
        if c == None :
            print("The Game Is Tie !")
        elif c == False :
            print(f"{b1} Lose {a1} Win")
        else:
            print(f"Congratulations!, {b1} Win {a1} Lose")
        break
    elif ans == 2:   
        print("You have selected option 2 - Game Rules")       
        print(rules)
    elif ans == 3:
        print("You have selected option 3 - Game Developer")       
        print(Dev)
    elif ans == 4:
        exit()
    else:
        print("Invalid Input....")
print("Done")
