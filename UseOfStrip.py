# this = ("    Hello How Are You        ")
# print(this)
# print(this.strip())

def remove_and_strip(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = ("    Hello How Are You        ")
n = remove_and_strip(this, " How")
print(n)
