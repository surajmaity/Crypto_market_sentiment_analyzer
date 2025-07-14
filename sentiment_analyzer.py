from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment_vader(text):
    """
    Analyzes sentiment using VADER. Returns a normalized compound score.
    """
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)
    # VADER's compound score is from -1 to 1. We normalize it to 0-10.
    return (sentiment['compound'] + 1) * 5

def analyze_sentiment_textblob(text):
    """
    Analyzes sentiment using TextBlob. Returns a normalized polarity score.
    """
    blob = TextBlob(text)
    # TextBlob's polarity is from -1 to 1. We normalize it to 0-10.
    return (blob.sentiment.polarity + 1) * 5

def get_combined_sentiment(headlines):
    """
    Calculates a combined sentiment score from a list of headlines.
    """
    if not headlines:
        return 5.0, "Neutral" # Return a neutral score if no news

    vader_scores = []
    textblob_scores = []

    for headline in headlines:
        # Ensure headline is a non-empty string
        if headline and isinstance(headline, str):
            vader_scores.append(analyze_sentiment_vader(headline))
            textblob_scores.append(analyze_sentiment_textblob(headline))

    if not vader_scores: # Check if any valid headlines were processed
        return 5.0, "Neutral"

    # Average the scores from both analyzers for a more robust result
    avg_vader = sum(vader_scores) / len(vader_scores)
    avg_textblob = sum(textblob_scores) / len(textblob_scores)
    final_score = (avg_vader + avg_textblob) / 2

    # Determine sentiment label based on the final score
    if final_score > 7:
        sentiment_label = "Very Bullish"
    elif final_score > 6:
        sentiment_label = "Bullish"
    elif final_score > 4:
        sentiment_label = "Neutral"
    else:
        sentiment_label = "Bearish"

    return final_score, sentiment_label