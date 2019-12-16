from utils.fetch_tweet import TweetFetcher


class TestTweetFetcher:
    def test_generate_tweets(self):
        tweet_src = ['marketwatch', 'wsj', 'ft', 'business', 'theeconomist', 'cnbc', 'cnn']
        # tweet_src = ['realDonaldTrump']
        # tweet_src = ['realDonaldTrump','POTUS']
        tweet_words = ['china', 'trade']
        tweetfetcher = TweetFetcher(tweet_src, tweet_words)
        tweets = tweetfetcher.generate_tweets()
        print(tweets)

    def test_tweet_query_builder(self):
        tweet_src = ['realDonaldTrump']
        tweet_words = ['china', 'trade']
        tweetfetcher = TweetFetcher(tweet_src, tweet_words)
        query = tweetfetcher.tweet_query_builder()
        print(query)
