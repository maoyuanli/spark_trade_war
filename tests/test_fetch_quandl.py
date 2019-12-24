from utils.fetch_quandl import IndexFetcher
from pprint import pprint


class TestIndexFetcher:
    def test_fetch_return(self):
        index_fetcher = IndexFetcher(dataset_id='NASDAQOMX/XQC', start_date='2019-12-01')
        rslt = index_fetcher.fetch_return()
        pprint(rslt)
