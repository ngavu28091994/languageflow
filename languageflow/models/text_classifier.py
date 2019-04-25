from enum import Enum
from os.path import join

import fastText

from languageflow.data import Sentence, Label


class Model:
    pass


class TEXT_CLASSIFIER_ESTIMATOR(Enum):
    FAST_TEXT = "fast_text"


class TextClassifier(Model):

    def __init__(self, estimator: TEXT_CLASSIFIER_ESTIMATOR):
        self.estimator = estimator
        if estimator == TEXT_CLASSIFIER_ESTIMATOR.FAST_TEXT:
            self.ft = None

    @staticmethod
    def load(model_folder):
        model_file = join(model_folder, "model.bin")
        classifier = TextClassifier(estimator=TEXT_CLASSIFIER_ESTIMATOR.FAST_TEXT)
        classifier.ft = fastText.load_model(model_file)
        return classifier

    def predict(self, sentence: Sentence):
        if self.estimator == TEXT_CLASSIFIER_ESTIMATOR.FAST_TEXT:
            values, scores = self.ft.predict(sentence.text)
            labels = []
            for value, score in zip(values, scores):
                value = value.replace("__label__", "")
                label = Label(value, score)
                labels.append(label)
            sentence.add_labels(labels)
