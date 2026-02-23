import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

class TextCleaner:
    """
    Module for preprocessing and cleaning raw text data.
    """
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def clean_text(self, text):
        """
        Cleans the input text:
        - Converts to lowercase
        - Removes punctuation and special characters
        - Removes stopwords
        - Performs tokenization
        """
        if not isinstance(text, str):
            return ""

        # 1. Lowercase
        text = text.lower()

        # 2. Remove special characters and punctuation
        # Using regex to keep only alphanumeric and spaces
        text = re.sub(r'[^a-zA-Z\s]', '', text)

        # 3. Tokenization
        tokens = word_tokenize(text)

        # 4. Remove stopwords
        filtered_tokens = [w for w in tokens if w not in self.stop_words]

        # Join back into a string or return tokens depending on needs
        # For simple sentiment analysis, a cleaned string is often sufficient
        return " ".join(filtered_tokens)

if __name__ == "__main__":
    cleaner = TextCleaner()
    sample = "I love this product! It's simply the best... 10/10."
    print(f"Original: {sample}")
    print(f"Cleaned: {cleaner.clean_text(sample)}")
