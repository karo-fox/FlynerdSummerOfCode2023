import random

num = random.randint(1, 30)
guess = 0
while guess != num:
    guess = int(input("Odgadnij liczbę: "))
    if guess < num:
        print("Za mało!")
    if guess > num:
        print("Za dużo!")
print("Gratulacje!")
