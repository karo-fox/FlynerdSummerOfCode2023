import random

with open("week3\day5\words.txt") as file:
    words = file.readlines()

while True:
    number = random.randint(1, len(words))
    guess = 0

    while guess != number:
        guess = int(input(f"Podaj liczbę od 1 do {len(words)}: "))
    print(f"Ukryte słowo to {words[number-1]}")

    ui = input("Czy chcesz zagrać jeszcze raz? [TAK/nie]: ")
    if ui == "nie":
        break
