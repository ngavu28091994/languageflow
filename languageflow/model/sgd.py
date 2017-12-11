from sklearn import linear_model



class SGDClassifier(linear_model.SGDClassifier):
    r"""SGDClassifier
    """
    def __init__(self, *args, **kwargs):
        super(SGDClassifier, self).__init__(*args, **kwargs)

    def fit(self, *args, **kwargs):
        """ Fit linear model with Stochastic Gradient Descent

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
