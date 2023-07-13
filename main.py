from sentiment_analyzer import SentimentAnalyzer

def main():
    text = input("Enter a comment or text: ")
    analyzer = SentimentAnalyzer()
    sentiment = analyzer.analyze_sentiment(text)
    print(f"Sentiment: {sentiment}")

if __name__ == "__main__":
    main()
