def gameWin(Pratik, Tejas):
    if Pratik == Tejas:
        return None
    if Pratik == "s":
        if Tejas == "p":
            return True
        elif Tejas == "c":
            return False
    if Pratik == "p":
        if Tejas == "c":
            return True
        elif Tejas == "s":
            return False
    if Pratik == "c":
        if Tejas == "s":
            return True
        elif Tejas == "p":
            return False

Pratik = input("Pratik Select Your Choise(Stone(s),Paper(p),Scissors(c)):\t")
Tejas = input("Tejas Select Your Choise(Stone(s),Paper(p),Scissors(c)):\t")


a = gameWin(Pratik,Tejas)

if a == None:
    print("The Game Is Tie")
elif a == True:
    print("Tejas Win, Pratik Lose")
else:
    print("Pratik Win, Tejas Lose")