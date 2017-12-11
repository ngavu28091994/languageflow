from sklearn import feature_extraction


class TfidfVectorizer(feature_extraction.text.TfidfVectorizer):
    """
    Convert a collection of raw documents to a matrix of TF-IDF features.
    """
    def __init__(self, *args, **kwargs):
        super(TfidfVectorizer, self).__init__(*args, **kwargs)
