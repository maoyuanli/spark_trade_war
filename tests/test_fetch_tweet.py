from utils.fetch_tweet import UserTweetsFetcher, SearchTweetsFetcher
from pprint import pprint


class TestUserTweets:
    def test_user_tweets(self):
        usertweets = UserTweetsFetcher('realdonaldtrump')
        rslt = usertweets.fetch_user_tweets()
        pprint(rslt)


class TestSearchTweetsFetcher:
    def test_fetch_search_tweets(self):
        topic = ['china', 'trade']
        media = ['marketwatch', 'wsj', 'ft', 'business', 'theeconomist', 'cnbc', 'cnn']
        searchtweets = SearchTweetsFetcher(media, topic)
        print(searchtweets.fetch_search_tweets())

    def test_tweet_query_builder(self):
        assert False
