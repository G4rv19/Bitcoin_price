import requests

def get_bitcoin_price():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        rate_str = data['bpi']['USD']['rate']
        rate_str = rate_str.replace(',', '')  # Remove the comma from the string
        return float(rate_str)
    except requests.exceptions.RequestException as e:
        print(f"Error making the request: {e}")
        return None

def main():
    bitcoin_price_usd = get_bitcoin_price()

    if bitcoin_price_usd is not None:
        try:
            amount = float(input('Enter the amount of Bitcoin: '))
            total_price_usd = bitcoin_price_usd * amount
            print(f'Total price in USD: {total_price_usd:.2f}')
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Failed to retrieve Bitcoin price.")

if __name__ == "__main__":
    main()
