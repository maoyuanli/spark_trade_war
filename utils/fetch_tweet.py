import tweepy
from tweepy import OAuthHandler, API
from utils.fetch_token import TokenFetcher


class TweetFetcher:
    tf = TokenFetcher('token.json')
    API_KEY = tf.fetch_token('api_key')
    API_SECRET = tf.fetch_token('api_secret')
    ACCESS_TOKEN = tf.fetch_token('access_token')
    ACCESS_SECRET = tf.fetch_token('access_secret')
    auth = OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = API(auth)


class UserTweetsFetcher(TweetFetcher):
    def __init__(self, account_id):
        self.account_id = account_id

    def fetch_user_tweets(self):
        tweets = self.api.user_timeline(id=self.account_id, count=200, tweet_mode='extended')
        tweets_list = []
        for tweet in tweets:
            item = {'created_at': str(tweet.created_at), 'text': tweet.full_text}
            tweets_list.append(item)
        return tweets_list


class SearchTweetsFetcher(TweetFetcher):
    def __init__(self, tweet_src: list, tweet_words: list):
        self.tweet_src = tweet_src
        self.tweet_words = tweet_words

    def fetch_search_tweets(self):
        search_query = self.tweet_query_builder()
        tweets = tweepy.Cursor(self.api.search, q=search_query, lang='en').items(2000)
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
