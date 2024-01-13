content = True
i = 0
with open("log.txt") as f:
    while content:
        i += 1
        content = f.readline()
        if "python" in content.lower():
            print(content)
            print("Yes, python Is Present in ", end = "")
            print("Line Number ",i,)
            print("\n")