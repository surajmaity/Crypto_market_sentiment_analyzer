import os
import requests
from dotenv import load_dotenv

load_dotenv()

# CoinGecko API URL for market data and prices
COINGECKO_API_URL = "https://api.coingecko.com/api/v3/coins/markets"
# NewsAPI URL for fetching news
NEWS_API_URL = "https://newsapi.org/v2/everything"

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
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching crypto data: {e}")
        return None

def get_crypto_news(query, from_date='2025-07-11'):
    """
    Fetches recent news for a specific cryptocurrency from NewsAPI.
    """
    params = {
        'q': query,
        'from': from_date,
        'sortBy': 'relevancy',
        'language': 'en',
        'apiKey': os.getenv('NEWS_API_KEY')
    }
    try:
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()
        # Return only the top 5 articles to avoid rate limits and also relevant content
        return response.json().get('articles', [])[:5]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news for '{query}': {e}")
        return []