for i in range(1, 11):
    for j in range(1, 11):
        num = str(i * j)
        space = " " * (5 - len(num))
        print(f"{num}{space}", end="")
    print()
