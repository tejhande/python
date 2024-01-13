from hashlib import md5


myDict = {
    "Fast":"In a Quick Manner",
    "Tejas":"Password"
    }
word = input("Enter Word To Find In Dictionary: ")

print(myDict[(word)])