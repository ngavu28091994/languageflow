try:
    from sklearn import linear_model
except:
    pass


class SGDClassifier(linear_model.SGDClassifier):
    r"""SGDClassifier
    """
    def __init__(self, *args, **kwargs):
        super(SGDClassifier, self).__init__(*args, **kwargs)
