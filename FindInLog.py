with open("log.txt") as f:
    content = f.read().lower()
if "python" in content:
    print("Yes, python Is Present")
else:    
    print("No, python Is Not Present")