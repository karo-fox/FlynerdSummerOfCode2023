people = input(
    "Wprowdź dowolną ilość imion rozdzielonych przecinkiem, np: Karolina, Dominik:\n"
)
for person in people.split(", "):
    print(f"Cześć, {person}")
