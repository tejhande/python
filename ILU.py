for i in range(1,1):
    with open(f"Table/Love/Love{i}.txt", "w") as f:
        for j in range(1,2):
            a = ' I Love You '
            b = a
            b = str(b)
            f.write(b*i)
            if j!=0:
                f.write("\n")





