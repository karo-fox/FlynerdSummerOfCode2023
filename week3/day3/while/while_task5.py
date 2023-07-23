import random

options = ["Yasha", "Beau", "Nott", "Caleb", "Fjord", "Jester", "Molly", "Cad"]
word = random.choice(options)
word1 = list(word)
random.shuffle(word1)
shuffled = "".join(word1)

ui = ""
while ui != word:
    print(shuffled)
    ui = input("Odgadnij imię bohatera: ")
    if ui == "q" or ui == "Q":
        break
    if ui == word:
        print("Gratulacje")
