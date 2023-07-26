from bs4 import BeautifulSoup
import requests

url = "https://karo-fox.github.io/FlynerdSummerOfCode2023/"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

days = doc.find_all("div", class_="card")
for card in days:
    day_name = card.find("h3", "heading vertical").contents[0]
    day_descriptions = (
        card.find("section", class_="card-content")
        .find("section", class_="day-description")
        .find_all("li")
    )
    items = list(map(lambda x: x.contents[0], day_descriptions))
    print(f'{day_name}\n{", ".join(items)}\n')

