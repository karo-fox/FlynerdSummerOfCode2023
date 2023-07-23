num = int(input("Podaj dowolną liczbę całkowitą do 15: "))

print("for")
fans = 1
for i in range(1, num + 1):
    fans *= i
print(fans)

print("while")
wans = 1
count = 1
while count <= num:
    wans *= count
    count += 1
print(wans)
