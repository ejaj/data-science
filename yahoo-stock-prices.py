import requests
from bs4 import BeautifulSoup
import json


def get_date(header, symbol):
    url = f'https://uk.finance.yahoo.com/quote/{symbol}'
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.text, 'html.parser')
    stock = {
        'symbol': symbol,
        'price': soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text,
        'change': soup.find('fin-streamer', {'class': 'Fw(500) Pstart(8px) Fz(24px)'}).text
    }
    return stock


header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

symbols = [
    'ASPL.L',
    'ICON.L',
    'PREM.L',
    'BZT.L'
]
stock_data = []
for symbol in symbols:
    stock_data.append(get_date(header, symbol))
    print("Getting", symbol)
print(stock_data)
with open('data/yahoo_stock.json', 'w') as f:
    json.dump(stock_data, f)
