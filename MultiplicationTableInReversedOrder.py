num = int(input("Enter Number To Print Reversed Multiplication Table: \n\t"))

for i in range(1,11):
    # print(num,"X", i,": ", num*i)
    # b = (num, 'X', i, ': ', num*i)
    b = (num *i)
    b = str(b)
    a = b
    a = list(a)
    a.reverse()
    print(a)
