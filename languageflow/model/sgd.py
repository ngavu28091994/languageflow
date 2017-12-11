from sklearn import linear_model


class SGDClassifier(linear_model.SGDClassifier):
    r"""
    Linear classifiers (SVM, logistic regression, a.o.) with SGD training.

    This estimator implements regularized linear models with stochastic gradient descent (SGD) learning: the gradient of the loss is estimated each sample at a time and the model is updated along the way with a decreasing strength schedule (aka learning rate). SGD allows minibatch (online/out-of-core) learning, see the partial_fit method. For best results using the default learning rate schedule, the data should have zero mean and unit variance.

    This implementation works with data represented as dense or sparse arrays of floating point values for the features. The model it fits can be controlled with the loss parameter; by default, it fits a linear support vector machine (SVM).

    The regularizer is a penalty added to the loss function that shrinks model parameters towards the zero vector using either the squared euclidean norm L2 or the absolute norm L1 or a combination of both (Elastic Net). If the parameter update crosses the 0.0 value because of the regularizer, the update is truncated to 0.0 to allow for learning sparse models and achieve online feature selection.
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
