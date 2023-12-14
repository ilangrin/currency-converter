import requests

API_KEY = 'fca_live_6LIM6kXb5yI7XZ4PzxA5URQXaFgN2clXlr1cnECP'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
CURRENCIES = ["USD", "EUR", "ILS", "CAD", "AUD"]

def currency_converter(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Error in getting data.")
        return None

while True:
    base = input("Enter the base currency (q for quit, c for calculator): ").upper()

    if base == "Q":
        break
    elif base == "C":
        base = input("Enter the base currency for conversion: ").upper()
        if base not in CURRENCIES:
            print("Invalid currency.")
            continue
        amount_str = input("Amount to convert: ")
        if not amount_str.isdigit():
            print("Invalid amount.")
            continue
        amount = int(amount_str)
        data = currency_converter(base)
        if not data:
            continue
        for ticker, rate in data.items():
            converted_amount = amount * rate
            print(f"{amount} {base} is {converted_amount} {ticker}")
    else:
        data = currency_converter(base)
        if not data:
            continue
        del data[base]
        for ticker, value in data.items():
            print(f"{ticker}: {value}")
