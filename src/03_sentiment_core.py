from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class SentimentAnalyzer:
    """
    Module for performing sentiment analysis on text.
    Uses VADER (Valence Aware Dictionary and sEntiment Reasoner).
    """
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def get_sentiment(self, text):
        """
        Calculates sentiment scores and returns a label.
        Returns:
            dict: {
                'compound': score,
                'label': 'Positive'/'Negative'/'Neutral'
            }
        """
        # VADER works best on raw text (with punctuation/caps) but 
        # for modularity we can pass our cleaned text or raw text.
        # Often keeping some context (like 'not good') is better with VADER.
        
        scores = self.analyzer.polarity_scores(text)
        compound = scores['compound']

        if compound >= 0.05:
            label = "Positive"
        elif compound <= -0.05:
            label = "Negative"
        else:
            label = "Neutral"

        return {
            'score': compound,
            'label': label
        }

if __name__ == "__main__":
    analyzer = SentimentAnalyzer()
    samples = [
        "I love this product, it is amazing!",
        "This is the worst thing I have ever bought.",
        "It is an average item, nothing special."
    ]
    for s in samples:
        res = analyzer.get_sentiment(s)
        print(f"Text: {s} | Sentiment: {res['label']} ({res['score']})")
