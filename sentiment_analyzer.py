from text_preprocessor import TextPreprocessor
from sentiment_lexicon import SentimentLexicon
from machine_learning_model import MachineLearningModel

class SentimentAnalyzer:
    def __init__(self):
        self.preprocessor = TextPreprocessor()
        self.lexicon = SentimentLexicon()
        self.model = MachineLearningModel()

    def analyze_sentiment(self, text):
        preprocessed_text = self.preprocessor.preprocess_text(text)
        sentiment = self.lexicon.analyze_sentiment(preprocessed_text)
        if sentiment == "confusing":
            sentiment = self.model.predict_sentiment(preprocessed_text)
        return sentiment
