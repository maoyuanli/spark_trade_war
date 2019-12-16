from utils.fetch_token import TokenFetcher
import findspark


class SparkInitializer:
    tf = TokenFetcher('token.json')
    spark_loc = tf.fetch_token('spark_loc')

    @classmethod
    def init_spark(cls):
        return findspark.init(SparkInitializer.spark_loc)
