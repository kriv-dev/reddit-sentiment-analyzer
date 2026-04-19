from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyzes sentiment of given text.
    Returns a dict with polarity and label.
    Polarity ranges from -1 (negative) to 1 (positive).
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0.1:
        label = "positive"
    elif polarity < -0.1:
        label = "negative"
    else:
        label = "neutral"
    
    return {
        "polarity": round(polarity, 4),
        "label": label
    }
