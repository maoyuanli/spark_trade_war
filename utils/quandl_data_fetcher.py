from utils.fetch_token import TokenFetcher
import quandl


class QuandlDataFetcher:
    tf = TokenFetcher('token.json')
    token = tf.fetch_token('quandl_cmhc')

    @classmethod
    def fetch_data(cls, dataset_str):
        df = quandl.get(dataset_str, authtoken= cls.token).reset_index()
        return df



