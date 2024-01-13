for i in range(1,11):
    with open(f"Table/Multiplication_Table_Of_{i}.txt", "w") as f:
        for j in range(1,11):
            f.write(f"{i} X {j} = {i*j}")
            if j!=10:
                f.write("\n")