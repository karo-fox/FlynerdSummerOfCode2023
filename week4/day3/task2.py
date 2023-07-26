import requests #skorzystaj z pakietu request

req = requests.get("http://numbersapi.com/random/year") # odpytujemy API
print(req.text)

"""
Sprawdź czy pobrany tekst ze strony zawiera liczbę "13"
Zapytaj użytkownika o dowolny ciąg znaków.
Sprawdź czy tekst ze strony zawiera też ciąg zadany przez użytkownika
"""

print("1. Tak" if "13" in req.text else "1. Nie")
string = input("Podaj dowolny ciąg znaków: ")
print("2. Tak" if string in req.text else "2. Nie")