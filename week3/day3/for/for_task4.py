times = int(input("Ile razy uruchomić program?: "))
for _ in range(times):
    num = int(input("Podaj dowolną liczbę: "))
    if num % 3 == 0 and num % 4 == 0:
        print("hurra")
    elif num % 3 == 0:
        print(f"{num} jest wielokrotnością 3")
    elif num % 4 == 0:
        print(f"{num} jest wielokrotnością 4")
    else:
        print("*")
    print()
