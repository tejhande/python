f = open('song.txt',)
data = f.read()
if 'emiway' in data.lower():
    print("Emiway Is Present In Song.txt")
else:
    print("Emiway Is Not Present In Song.txt")
print(data)
f.close()