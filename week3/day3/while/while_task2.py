import random

num = random.randint(1, 30)
guess = 0
while guess != num:
    guess = int(input("Odgadnij liczbę: "))
print("Gratulacje!")
