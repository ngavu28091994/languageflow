from sklearn import linear_model



class SGDClassifier(linear_model.SGDClassifier):
    r"""SGDClassifier
    """
    def __init__(self, *args, **kwargs):
        super(SGDClassifier, self).__init__(*args, **kwargs)

    def fit(self, *args, **kwargs):
        """

        :param X: Training data
        :type X: {array-like, sparse matrix}, shape (n_samples, n_features)
        :param kwargs:
        :return:
        """
        super(SGDClassifier, self).fit(*args, **kwargs)
