from sklearn import linear_model



class SGDClassifier(linear_model.SGDClassifier):
    r"""SGDClassifier
    """
    def __init__(self, *args, **kwargs):
        super(SGDClassifier, self).__init__(*args, **kwargs)

    def fit(self, *args, **kwargs):
        """ Fit linear model with Stochastic Gradient Descent

        :param X: Training data
        :type X: {array-like, sparse matrix}, shape (n_samples, n_features)
        :param kwargs:
        :return:

        Parameters
        ----------
        arg1 : int
            Description of arg1
        arg2 : str
            Description of arg2

        Returns
        -------
        int
            Description of return value

        """
        super(SGDClassifier, self).fit(*args, **kwargs)
