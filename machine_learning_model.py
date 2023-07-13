from typing import Any

class MachineLearningModel:
    def __init__(self):
        self.model = self.load_model("path/to/model.pkl")

    def load_model(self, model_path):
        # Load the trained machine learning model from the specified path
        # Return the loaded model
        pass

    def predict_sentiment(self, text):
        # Use the loaded model to predict the sentiment of the given text
        # Return the sentiment category (positive or negative)
        pass
