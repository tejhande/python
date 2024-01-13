import random

randNumber = random.randint(1,99999)
# print(randNumber)
userGuess = None
guesses = 0
while(userGuess != randNumber):
    userGuess = int(input("Enter Your Guess: \n\t"))
    guesses += 1
    if userGuess == randNumber:
        print("You Guessed It Right")
    else:
        if(userGuess<randNumber):
            print("You Guessed It Wrong! Enter A Larger Number")
        else:
            print("You Guessed It Wrong! Enter A Smaller Number")
print(f"You Guessed It In {guesses} guesses ")

with open("HighScore1.txt",'r') as f:
    highScore = int(f.read())
    print("Previous High Score: \t", highScore)
if (guesses<highScore):
    print("You Have Just Broken Previous HighScore")
    with open("HighScore1.txt",'w') as f:
        f.write(str(guesses))
    
