import random
def gameWin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


print("Computer's Turn : Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your Turn : Snake(s) Water(w) or Gun(g)?")
a = gameWin(comp, you)

print(f"Computer Chose :\t {comp}")
print(f"You Chose  :\t {you}")


if a == None :
    print("The Game Is Tie !")
elif a == False :
    print("You Lose Computer Win")
else:
    print("Congratulations!, You Win Computer Lose")