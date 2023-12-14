import requests


API_KEY = 'fca_live_6LIM6kXb5yI7XZ4PzxA5URQXaFgN2clXlr1cnECP'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
CURRENCIES = ["USD", "EUR", "NES", "CAD", "AUD"]
def currency_converter(base):
    currencies ="," .join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"

