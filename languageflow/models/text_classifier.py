from os.path import join

import fastText

from languageflow.data import Sentence, Label


class Model:
    pass


class TextClassifier(Model):

    def __init__(self):
        self.ft = None

    @staticmethod
    def load(model_folder):
        model_file = join(model_folder, "model.bin")
        classifier = TextClassifier()
        classifier.ft = fastText.load_model(model_file)
        return classifier

    def predict(self, sentence: Sentence):
        values, scores = self.ft.predict(sentence.text)
        labels = []
        for value, score in zip(values, scores):
            value = value.replace("__label__", "")
            label = Label(value, score)
            labels.append(label)
        sentence.add_labels(labels)
