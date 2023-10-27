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
    offers = bs.find_all('div', class_='css-1sw7q4x')

    # Loop through offers and scrape
    for offer in offers:
        title_element = offer.find('div', class_='css-u2ayx9')
        if title_element is not None:
            title = title_element.get_text().strip()
            title_truncated = (title[:60] + '..') if len(title) > 60 else title
            price = parse_price(offer.find('p', class_='css-10b0gli er34gjf0').get_text().strip())
            link = offer.find('a')
            offers_dict['title'].append(title_truncated)
            offers_dict['price'].append(price)
            offers_dict['link'].append(link['href'])
            print(title_truncated)

# Loop through pages 1 to 25
for page in range(1, 26):
    parse_page(page)

# Start connection to database
engine = create_engine(f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}')
# Check the database connection status
if engine.connect().closed:
    print("Not connected to the database.")
else:
    print("Connected to the database.")

# Taking data from DB
query = "SELECT * FROM olx"
df_check = pd.read_sql(query, engine)

# Create a dictionary to store data from the database
offers_dict_check = {
    'title': df_check['title'].tolist(),
    'price': df_check['price'].tolist(),
    'link': df_check['link'].tolist()
}

# Create a new dictionary to store unique entries
offers_dict_unique = {'title': [], 'price': [], 'link': []}

# Iterate through the entries in offers_dict
for title, price, link in zip(offers_dict['title'], offers_dict['price'], offers_dict['link']):
    # Check if the entry is not in offers_dict_check
    if (title, price, link) not in zip(offers_dict_check['title'], offers_dict_check['price'], offers_dict_check['link']):
        # Add the unique entry to offers_dict_unique
        offers_dict_unique['title'].append(title)
        offers_dict_unique['price'].append(price)
        offers_dict_unique['link'].append(link)

# Create dataframe from scraped data
df = pd.DataFrame.from_dict(offers_dict_unique)
# Add it to DB
df.to_sql(con=engine, name='olx', if_exists='append', index=False)

# Check if offers were added to dict correctly
print(offers_dict_unique)