import requests


API_KEY = 'fca_live_6LIM6kXb5yI7XZ4PzxA5URQXaFgN2clXlr1cnECP'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
CURRENCIES = ["USD", "EUR", "ILS", "CAD", "AUD"]
def currency_converter(base):
    currencies ="," .join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as  e:
        print(e)
        return None

base =input("enter the base currencies (q for quit): ").upper()

if base not in CURRENCIES:
    print("invalid currency")

data = currency_converter(base)
del data[base]
for ticker, value in data.items():
    print((f"{ticker}: {value}"))



