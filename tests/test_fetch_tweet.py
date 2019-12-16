from utils.fetch_tweet import TweetFetcher


class TestTweetFetcher:
    tweet_src = ['marketwatch', 'wsj', 'ft', 'business', 'theeconomist', 'cnbc', 'cnn']
    tweet_words = ['china', 'trade']
    tweetfetcher = TweetFetcher(tweet_src, tweet_words)

    def test_generate_tweets(self):
        tweets = self.tweetfetcher.generate_tweets()
        print(tweets)

    def test_tweet_query_builder(self):
        tweet_src = ['realDonaldTrump']
        tweet_words = ['china', 'trade']
        tweetfetcher = TweetFetcher(tweet_src, tweet_words)
        query = self.tweetfetcher.tweet_query_builder()
        print(query)
