from data_collector import get_crypto_data, get_crypto_news
from sentiment_analyzer import get_combined_sentiment
from report_generator import generate_html_report

def main():
    """
    Main function to run the crypto sentiment analysis.
    """
    # Define the cryptocurrencies to analyze
    crypto_config = {
        'bitcoin': {'name': 'Bitcoin', 'query': 'Bitcoin'},
        'ethereum': {'name': 'Ethereum', 'query': 'Ethereum'},
        'solana': {'name': 'Solana', 'query': 'Solana'}
    }
    crypto_ids = list(crypto_config.keys())

    # 1. Fetch Crypto Price Data
    price_data = get_crypto_data(crypto_ids)
    if not price_data:
        print("Could not fetch price data. Exiting.")
        return

    # 2. Process each crypto
    report_data = []
    for data in price_data:
        crypto_id = data['id']
        if crypto_id in crypto_config:
            # Fetch news
            news_articles = get_crypto_news(crypto_config[crypto_id]['query'])
            headlines = [article['title'] for article in news_articles]
            
            # Analyze sentiment
            sentiment_score, sentiment_label = get_combined_sentiment(headlines)

            # Consolidate data
            report_data.append({
                'id': crypto_id,
                'name': data['name'],
                'symbol': data['symbol'],
                'price': data.get('current_price', 0),
                'change': data.get('price_change_percentage_24h', 0),
                'volume': data.get('total_volume', 0),
                'headlines': headlines if headlines else ["No relevant news found in the last 24 hours."],
                'sentiment_score': sentiment_score,
                'sentiment_label': sentiment_label
            })

    # 3. Generate the report
    if report_data:
        generate_html_report(report_data)
    else:
        print("No data was processed to generate a report.")

if __name__ == "__main__":
    main()