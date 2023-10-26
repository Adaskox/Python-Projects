from bs4 import BeautifulSoup
import requests

URL = 'https://www.olx.pl/elektronika/komputery/kostomloty/q-komputer/?search%5Bdist%5D=50&last_seen_id=840898905&reason=observed_search'

def parse_price(price):
    return price.replace('zł', '').strip()

def parse_page(number):
    page = requests.get(f'{URL}&page={number}')
    bs = BeautifulSoup(page.content, 'html.parser')
    offers = bs.find_all('div', class_='css-1sw7q4x')
    #print(offers)
    for offer in offers:
        #footer = offer.find('td', class_='css-veheph er34gjf0')
        title_element = offer.find('div', class_='css-u2ayx9')
        if title_element is not None:
            title = title_element.get_text().strip()
            price = parse_price(offer.find('p', class_='css-10b0gli er34gjf0').get_text().strip())
            link = offer.find('a')
            print(title + ' CENA: ' + price)
            print(link['href'])
        else:
            print("Title not found for an offer.")

for page in range(1, 5):
    parse_page(page)
