from bs4 import BeautifulSoup
import requests

url = "https://karo-fox.github.io/FlynerdSummerOfCode2023/"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

days = doc.find_all("div", class_="card")
for card in days:
    day = (
        card.find("section", class_="card-content")
        .find("section", class_="day-description")
    )
    if day.find("h3", class_="sub-heading"):
        print(day.find("h3", class_="sub-heading").contents[0])
