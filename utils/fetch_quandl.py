import quandl
from utils.fetch_token import TokenFetcher


class QuandlFetcher:
    tf = TokenFetcher('token.json')
    QUANDL_KEY = tf.fetch_token('quandl_key')


class IndexFetcher(QuandlFetcher):
    def __init__(self, dataset_id, start_date):
        """start_date formart  2019-12-25 """
        self.dataset_id = dataset_id
        self.start_date = start_date
        self.df = quandl.get(dataset=self.dataset_id, api_key=self.QUANDL_KEY, start_date=start_date)

    def fetch_return(self):
        self.df.sort_index(ascending=True, inplace=True)
        nonzero_df = self.df[self.df['Index Value'] != 0]
        change_df = nonzero_df.copy()
        change_df['Change'] = change_df['Index Value'].pct_change()
        nonindex_df = change_df.reset_index()
        return nonindex_df[['Trade Date', 'Index Value', 'Change']]
