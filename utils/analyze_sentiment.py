from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import PorterStemmer
import re
import string


class SentimentAnalyzer:

    def sentiment_score(self, s: str):
        clean_s = (lambda c: self.process_words(c, remove_punc=True))(s)
        analyzer = SentimentIntensityAnalyzer()
        sent_score = (lambda t: analyzer.polarity_scores(t)['compound'] if t is not None else 'Null')(clean_s)
        return sent_score

    @staticmethod
    def process_words(raw, remove_punc=False, stem=False):
        link_pattern = [
            r'(http|https)://[a-zA-Z0-9\./]*\s',
            r'\s+(http|https)://[a-zA-Z0-9\./]*\s',
            r'\s+(http|https)://[a-zA-Z0-9\./]*$',
        ]
        if raw:
            clean = raw.lower().strip()
            for ptn in link_pattern:
                clean = re.sub(ptn, '', clean)
            if remove_punc:
                nopunc = [c for c in clean if c not in string.punctuation]
                raw = ''.join(nopunc)

            stopwords_list = []
            stopwords_list_en = set(stopwords.words('english'))
            stopwords_list_fr = set(stopwords.words('french'))
            stopwords_list.extend(stopwords_list_en)
            stopwords_list.extend(stopwords_list_fr)

            nostop = [w for w in raw.split() if w.lower() not in stopwords_list]
            if stem:
                stemmer = PorterStemmer()
                return ' '.join([stemmer.stem(t) for t in nostop])
            else:
                return ' '.join(nostop)
