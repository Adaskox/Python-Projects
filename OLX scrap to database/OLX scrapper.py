import requests
import pandas as pd
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from mysql import USERNAME, PASSWORD, HOST, DATABASE

# Dictionary to store scraped data
offers_dict = {'title':[], 'price':[], 'link':[]}
# URL to scrape
URL = 'https://www.olx.pl/elektronika/komputery/kostomloty/q-komputer/?min_id=872348166&reason=observed_search&search%5Bdist%5D=50'

# Remove 'zl' and whitespaces
def parse_price(price):
    return price.replace('zł', '').strip()

#Define function to parse lisings
def parse_page(number):
    page = requests.get(f'{URL}&page={number}')
    bs = BeautifulSoup(page.content, 'html.parser')
    offers = bs.find_all('div', class_='css-oukcj3')

    # Loop through offers and scrape
    for offer in offers:
        title_element = offer.find('div', class_='css-u2ayx9')
        if title_element is not None:
            title = title_element.get_text().strip()
            price = parse_price(offer.find('p', class_='css-10b0gli er34gjf0').get_text().strip())
            link = offer.find('a')
            offers_dict['title'].append(title)
            offers_dict['price'].append(price)
            offers_dict['link'].append(link['href'])

# Loop through pages 1 to 25
for page in range(1, 26):
    parse_page(page)

# Create dataframe from scraped data and display 5 rows
df = pd.DataFrame.from_dict(offers_dict)
df.head(5)

# Store dataframe to database
engine = create_engine(f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}')
df.to_sql(con=engine, name='OLX', if_exists='append', index=False)