import requests

ETH_PRICE_URL = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD'


def getPriceFromNetwork():
    resp = requests.get(ETH_PRICE_URL)
    pokemon = resp.json()
    print(pokemon['USD'])
