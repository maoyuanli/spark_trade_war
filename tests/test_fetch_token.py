from utils.fetch_token import TokenFetcher


class TestTokenFetcher:

    def test_fetch_token(self):
        tf = TokenFetcher('token.json')
        quandl_key = tf.fetch_token('quandl_key')
        print(quandl_key)
