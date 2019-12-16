from utils.analyze_sentiment import SentimentAnalyzer


class TestSentimentAnalyzer:
    sa = SentimentAnalyzer()
    ts = 'Congress considers EV tax credit revamp to help Tesla, GM, and used EVs… https://t.co/K1Aph5l1ZU'

    def test_sentilyze(self):
        score = self.sa.sentiment_score(self.ts)
        print(score)

    def test_process_words(self):
        clean_str = self.sa.process_words(self.ts, True)
        print(clean_str)
