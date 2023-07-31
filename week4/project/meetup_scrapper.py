from bs4 import BeautifulSoup
import requests

url = 'https://www.meetup.com/pl-PL/find/?source=EVENTS&location=pl--Gliwice&categoryId=546'

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

events = []
for elem in doc.find_all('div', 'p-0 bg-clip-padding bg-cover bg-transparent relative h-full flex bg-white z-0 break-words transition-shadow duration-300 w-full flex-row justify-start py-4 border-t border-gray3 md:pt-4 md:pb-5'):
    nested = elem.find_all('div', 'overflow-hidden w-full')[0]
    date = ' '.join(map(lambda x: x.contents[0], nested.find('time').find_all('span')[:1]))
    subject = nested.find('h2').contents[0]
    organizer = nested.find_all('p', 'line-clamp-1 md:hidden')[0].contents[1]
    location = nested.find_all('p', 'line-clamp-1 md:hidden')[1].contents[0]
    event = {
        'date': date,
        'location': location,
        'subject': subject,
        'organizer': organizer,
    }
    events.append(event)

for event in events:
    print(f'{event["subject"]} by {event["organizer"]}')
    print(f'{event["date"]} in {event["location"]}')
    print()

with open('week4/project/backup.csv', 'w') as file:
    for event in events:
        file.write(f'{event["date"]};{event["location"]};{event["subject"]};{event["organizer"]}\n')
