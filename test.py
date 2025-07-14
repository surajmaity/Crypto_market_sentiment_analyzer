COINGECKO_API_URL = "https://api.coingecko.com/api/v3/coins/markets"
import requests


def get_crypto_data(crypto_ids=['bitcoin', 'ethereum', 'solana']):
    """
    Fetches crypto price, 24h change, and volume from CoinGecko.
    """
    params = {
        'vs_currency': 'usd',
        'ids': ','.join(crypto_ids),
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': 'false'
    }
    try:
        response = requests.get(COINGECKO_API_URL, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        print(data)
        return data 
    except requests.exceptions.RequestException as e:
        print(f"Error fetching crypto data: {e}")
        return None


if __name__ == "__main__":
    price_data = get_crypto_data()
    if not price_data:
        print("Could not fetch price data. Exiting.")