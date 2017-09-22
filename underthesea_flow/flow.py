import numpy
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC, NuSVC, LinearSVC
import matplotlib.pyplot as plt

from underthesea_flow.experiment import Experiment
from underthesea_flow.transformer.tagged import TaggedTransformer
from underthesea_flow.validation.validation import TrainTestSplitValidation


class Flow:
    def __init__(self):
        self.models = []
        self.lc_range = [1]
        self.result = []
        self.validation = TrainTestSplitValidation()
        self.scores = set()

    def data(self, X=None, y=None, sentences=None):
        self.X = X
        self.y = y
        self.sentences = sentences

    def transform(self, transformer):
        if isinstance(transformer, TaggedTransformer):
            self.X, self.y = transformer.transform(self.sentences)
        else:
            self.X = transformer.text2vec(self.X).toarray()
            print("X Shape: ", self.X.shape)

    def add_model(self, model):
        self.models.append(model)

    def add_score(self, score):
        self.scores.add(score)

    def set_learning_curve(self, start, stop, offset):
        self.lc_range = numpy.arange(start, stop, offset)

    def set_validation(self, validation):
        self.validation = validation

    def validation(self):
        for i, model in enumerate(self.models):
            N = [int(i * len(self.Y)) for i in self.lc_range]
            for n in N:
                X = self.X[:n]
                Y = self.Y[:n]
                e = Experiment(X, Y, model.clf, self.validation)
                scores = e.run()

    def visualize(self):
        pass

    def train(self):
        """
        Train dataset with transformer and model
        """
        model = self.models[0]
        model.fit(self.X, self.y)

    def save_model(self, model_name, model_filename):
        model = [model for model in self.models if model.name == model_name][0]
        e = Experiment(self.X, self.Y, model.clf, None)
        e.save(model_filename)

    def test(self, X, y_true, model):
        y_predict = model.predict(X)
        y_true = [item[0] for item in y_true]
