def gameWin(p1,p2):
    if p1 == p2:
        return None
    elif p1 == "s":
        if p2 == "w":
            return False
        elif p2 == "g":
            return True
    elif p1 == "w":
        if p2 == "g":
            return False
        elif p2 == "s":
            return True
    elif p1 == "g":
        if p2 == "s":
            return False
        elif p2 == "w":
            return True
p1 = input("p1 Turn s/w/g: ")
p2 = input("p2 Turn s/w/g: ")
b = gameWin(p1, p2)
if b == None :
    print("Tie")
elif b == False :
    print("p1 Win")
else:
    print("p2 Win")
    