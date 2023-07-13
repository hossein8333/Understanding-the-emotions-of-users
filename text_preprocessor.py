import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

class TextPreprocessor:
    def __init__(self):
        nltk.download("stopwords")
        nltk.download("punkt")
        nltk.download("wordnet")
        self.stopwords = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()

    def preprocess_text(self, text):
        text = text.lower()
        text = re.sub(r"[^a-zA-Z0-9]", " ", text)
        tokens = word_tokenize(text)
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token not in self.stopwords]
        preprocessed_text = " ".join(tokens)
        return preprocessed_text
