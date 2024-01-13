def game():
    return 11

score = game()
score = str(score)
f = open("HighScore.txt","r")
t = f.read()
HighScore = t
if HighScore == " ":
    f = open("HighScore.txt","w")
    t = f.write(str(score))
elif HighScore < score :
    f = open("HighScore.txt","w")
    t = f.write(str(score))
print(t)
f.close()