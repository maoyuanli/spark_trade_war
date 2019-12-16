import tweepy
from tweepy import OAuthHandler, API
from utils.fetch_token import TokenFetcher
import json


class TweetFetcher:
    tf = TokenFetcher('token.json')
    token = tf.fetch_token('quandl_cmhc')
    api_key = tf.fetch_token('api_key')
    api_secret = tf.fetch_token('api_secret')
    access_token = tf.fetch_token('access_token')
    access_secret = tf.fetch_token('access_secret')

    auth = OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)

    def __init__(self, tweet_src: list, tweet_words: list):
        self.tweet_src = tweet_src
        self.tweet_words = tweet_words

    def generate_tweets(self):
        api = API(TweetFetcher.auth)
        search_query = self.tweet_query_builder()
        tweets = tweepy.Cursor(api.search, q=search_query, lang='en').items(2000)
        tweets_json = []
        for tweet in tweets:
            tweets_json.append(tweet._json)
        return tweets_json

    def tweet_query_builder(self):
        from_prefix = 'FROM:'
        or_prefix = ' OR '
        query_from = ''
        for i, s in enumerate(self.tweet_src):
            if i != len(self.tweet_src) - 1:
                query_from = query_from + from_prefix + s + or_prefix
            else:
                query_from = query_from + from_prefix + s
        search_words = ' '.join(self.tweet_words)
        return search_words + ' ' + query_from
